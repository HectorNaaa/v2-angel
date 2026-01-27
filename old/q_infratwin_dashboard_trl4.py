
# Q-InfraTwin TRL4 — Streamlit Dashboard
# Run:
#   python -m pip install -r requirements_dashboard_q_infratwin_trl4.txt
#   streamlit run q_infratwin_dashboard_trl4.py
#
# This dashboard can:
#  - Run a new simulation using the TRL4 hybrid prototype engine
#  - Or load an exported CSV from a previous run
#  - Visualise routing, latency, objective, fallback reasons, and per-twin traces

from __future__ import annotations

import os
import json
import importlib.util
from typing import Optional, Tuple, Dict, Any

import pandas as pd
import streamlit as st

# Optional matplotlib (Streamlit also has native charts)
try:
    import matplotlib.pyplot as plt
    _HAS_MPL = True
except ModuleNotFoundError:
    plt = None
    _HAS_MPL = False


st.set_page_config(page_title="Q-InfraTwin TRL4 Dashboard", layout="wide")

st.title("Q-InfraTwin — TRL4 Hybrid (Quantum–Classical) Dashboard")

st.markdown(
    """
This dashboard is built for the **TRL4 hybrid prototype**:
- **TwinCORE registry + state/history**
- **Hybrid Orchestrator** (rule/bandit routing)
- **Quantum Request Envelope (QRE)** + normalised results
- **Cloud QPU simulation** (queue/noise/cost/failure)
- **Latency governance + fallback**
"""
)

# -----------------------------
# Helpers
# -----------------------------

@st.cache_resource
def load_engine_module(engine_path: str):
    """Dynamically load the prototype engine as a module."""
    spec = importlib.util.spec_from_file_location("q_infratwin_engine", engine_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load engine module from: {engine_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_simulation(engine, steps: int, twins: int, policy: str, seed: int):
    core, df = engine.run_sim(steps=steps, twins=twins, policy=policy, seed=seed)
    return core, df


def kpis(df: pd.DataFrame) -> Dict[str, Any]:
    out = {}
    out["steps"] = int(len(df))
    out["twins"] = int(df["twin_id"].nunique()) if "twin_id" in df else 0
    out["quantum_rate"] = float((df["route"] == "QUANTUM").mean()) if "route" in df else 0.0
    out["fallback_rate"] = float((df["route"] == "FALLBACK_CLASSICAL").mean()) if "route" in df else 0.0
    out["sla_breach_rate"] = float(df["latency_breach"].mean()) if "latency_breach" in df else 0.0
    out["mean_latency_ms"] = float(df["exec_ms"].mean()) if "exec_ms" in df else float("nan")
    out["p95_latency_ms"] = float(df["exec_ms"].quantile(0.95)) if "exec_ms" in df else float("nan")
    out["mean_objective"] = float(df["objective_value"].mean()) if "objective_value" in df else float("nan")
    out["mean_confidence"] = float(df["confidence"].mean()) if "confidence" in df else float("nan")
    if "qpu_queue_ms" in df and df["qpu_queue_ms"].notna().any():
        out["mean_queue_ms"] = float(df["qpu_queue_ms"].dropna().mean())
    else:
        out["mean_queue_ms"] = float("nan")
    return out


def safe_parse_json(s: Optional[str]) -> Optional[dict]:
    if s is None or (isinstance(s, float) and pd.isna(s)):
        return None
    try:
        return json.loads(s)
    except Exception:
        return None


# -----------------------------
# Sidebar controls
# -----------------------------

with st.sidebar:
    st.header("Mode")
    mode = st.radio("Choose data source", ["Run simulation", "Load CSV"], index=0)

    st.header("Engine")
    default_engine_path = os.path.abspath("q_infratwin_trl4_hybrid_prototype_v1_1.py")
    engine_path = st.text_input("Prototype engine path", value=default_engine_path)

    if mode == "Run simulation":
        st.header("Simulation parameters")
        steps = st.slider("Steps", min_value=50, max_value=2000, value=300, step=50)
        twins = st.slider("Twins", min_value=1, max_value=20, value=5, step=1)
        policy = st.selectbox("Routing policy", ["rule", "bandit"], index=1)
        seed = st.number_input("Seed", min_value=1, max_value=1_000_000, value=42, step=1)
        run_btn = st.button("Run", use_container_width=True)
    else:
        uploaded = st.file_uploader("Upload exported CSV", type=["csv"])
        run_btn = False

# -----------------------------
# Data load/run
# -----------------------------

df: Optional[pd.DataFrame] = None
core = None

if mode == "Run simulation":
    if run_btn:
        try:
            engine = load_engine_module(engine_path)
        except Exception as e:
            st.error(f"Failed to load engine module: {e}")
            st.stop()

        with st.spinner("Running simulation..."):
            core, df = run_simulation(engine, steps=int(steps), twins=int(twins), policy=str(policy), seed=int(seed))
        st.success("Simulation completed.")
elif mode == "Load CSV":
    if uploaded is not None:
        df = pd.read_csv(uploaded)
        st.success("CSV loaded.")

if df is None:
    st.info("Select parameters and click **Run**, or upload a CSV.")
    st.stop()

# -----------------------------
# KPI strip
# -----------------------------

m = kpis(df)
c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.metric("Steps", f'{m["steps"]}')
c2.metric("Twins", f'{m["twins"]}')
c3.metric("Quantum rate", f'{m["quantum_rate"]*100:.1f}%')
c4.metric("Fallback rate", f'{m["fallback_rate"]*100:.1f}%')
c5.metric("SLA breach", f'{m["sla_breach_rate"]*100:.1f}%')
c6.metric("p95 latency", f'{m["p95_latency_ms"]:.0f} ms')

c7, c8, c9, c10, c11, c12 = st.columns(6)
c7.metric("Mean latency", f'{m["mean_latency_ms"]:.0f} ms')
c8.metric("Mean objective", f'{m["mean_objective"]:.3f}')
c9.metric("Mean confidence", f'{m["mean_confidence"]:.2f}')
c10.metric("Mean QPU queue", "—" if pd.isna(m["mean_queue_ms"]) else f'{m["mean_queue_ms"]:.0f} ms')
c11.metric("Policy", str(df["policy"].iloc[0]) if "policy" in df else "—")
c12.metric("Data rows", str(len(df)))

st.divider()

# -----------------------------
# Charts
# -----------------------------

left, right = st.columns([2, 1])

with left:
    st.subheader("Objective & latency over time")

    chart_df = df.copy()
    chart_df["step"] = range(1, len(chart_df) + 1)

    st.line_chart(chart_df.set_index("step")[["objective_value"]], height=220)
    st.line_chart(chart_df.set_index("step")[["exec_ms"]], height=220)

with right:
    st.subheader("Routing distribution")
    st.bar_chart(df["route"].value_counts())

    st.subheader("Fallback reasons (top)")
    if "fallback_reasons" in df:
        # fallback_reasons is a list in JSONL but in CSV it's stored as a string repr; handle both.
        reasons = []
        for x in df["fallback_reasons"].fillna(""):
            if isinstance(x, str) and x.startswith("["):
                try:
                    reasons.extend(json.loads(x.replace("'", '"')))
                except Exception:
                    # fallback: split rough
                    reasons.extend([r.strip() for r in x.strip("[]").split(",") if r.strip()])
            elif isinstance(x, list):
                reasons.extend(x)
        if reasons:
            rs = pd.Series(reasons).value_counts().head(10)
            st.bar_chart(rs)
        else:
            st.caption("No fallback reasons recorded in this run.")
    else:
        st.caption("No fallback_reasons column present.")

st.divider()

# -----------------------------
# Drill-down: per twin
# -----------------------------
st.subheader("Per-twin drill-down")

twin_ids = sorted(df["twin_id"].unique().tolist()) if "twin_id" in df else []
sel = st.selectbox("Select twin_id", twin_ids, index=0 if twin_ids else None)

if sel:
    dft = df[df["twin_id"] == sel].copy()
    dft["step"] = range(1, len(dft) + 1)
    a1, a2 = st.columns(2)
    with a1:
        st.line_chart(dft.set_index("step")[["objective_value"]], height=220)
        st.line_chart(dft.set_index("step")[["exec_ms"]], height=220)
    with a2:
        st.bar_chart(dft["route"].value_counts())
        if "qpu_queue_ms" in dft and dft["qpu_queue_ms"].notna().any():
            st.line_chart(dft.set_index("step")[["qpu_queue_ms"]], height=220)

st.divider()

# -----------------------------
# Inspect QRE / Result payloads
# -----------------------------
st.subheader("Inspect QRE / Quantum Result (audit)")

cols = ["step_id", "ts", "twin_id", "route", "exec_ms", "qpu_queue_ms", "noise_proxy", "cost_eur", "latency_breach"]
st.dataframe(df[cols].tail(50), use_container_width=True, height=260)

row_idx = st.number_input("Pick a row index (0-based)", min_value=0, max_value=max(0, len(df) - 1), value=max(0, len(df) - 1), step=1)
row = df.iloc[int(row_idx)]

qre_obj = safe_parse_json(row.get("qre_json", None))
res_obj = safe_parse_json(row.get("result_json", None))

b1, b2 = st.columns(2)
with b1:
    st.markdown("**QRE (Quantum Request Envelope)**")
    if qre_obj:
        st.json(qre_obj)
    else:
        st.caption("No QRE recorded for this step (likely classical route).")

with b2:
    st.markdown("**Quantum Result (normalised)**")
    if res_obj:
        st.json(res_obj)
    else:
        st.caption("No quantum result recorded for this step.")

st.divider()

# -----------------------------
# Export current dataframe
# -----------------------------
st.subheader("Export")

csv_bytes = df.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", data=csv_bytes, file_name="q_infratwin_run.csv", mime="text/csv", use_container_width=True)

st.caption("Tip: run with --export in the engine script to persist CSV/JSONL on disk.")
