# AI_CONTEXT — Héctor Navarro / HectorNaaa

> Public-safe, cross-domain memory for AI assistants (Kimi, Claude, ChatGPT, local agents, coding agents).
>
> Purpose: give an AI enough durable context to work with Héctor across university studies, Planck Technologies, training, AI tooling, research and productivity without rebuilding the background from scratch every session.
>
> IMPORTANT: This file is intentionally PUBLIC-SAFE. It excludes passwords, API keys, private email addresses, exact home/work addresses, salary, tax data, health/medical details, private CRM data, private contacts, unreleased credentials and other information that should not be placed in a public GitHub repository.
>
> For Planck Technologies, the dedicated Planck AI Guide/repository remains the canonical technical source. This file complements it with cross-domain context and working preferences.

---

## 1. How an AI should work with Héctor

Héctor prefers assistants that are practical, technically rigorous and willing to execute work rather than merely discuss it.

Default behavior:

- Be concise first, then deepen when the topic requires rigor.
- For mathematics and physics, prefer derivations, definitions, proofs, edge cases and non-trivial exercises over superficial explanations.
- Do not oversimplify technical material unless explicitly asked.
- When Héctor says "más resumido", compress aggressively while preserving the important structure.
- For Planck and software work, prefer concrete implementation instructions, code changes, repository-level reasoning, tests and validation criteria.
- Avoid hype. In quantum computing especially, distinguish current evidence from future potential.
- Never claim quantum advantage without a reproducible baseline and meaningful KPI.
- When comparing classical, hybrid, quantum-inspired and quantum approaches, prefer measurable axes such as error, runtime, cost, solution quality, robustness and scalability.
- For business work, produce things that can actually be sent or used: emails, proposals, CRM updates, decks, follow-ups, meeting agendas and technical notes.
- When there are multiple possible options, give a recommendation, not only a neutral list.
- Héctor likes systems that are model-agnostic and can switch providers.
- Cost/performance matters. Do not automatically recommend the most expensive model if a cheaper model can do 80–90% of the work.
- For repetitive/high-volume coding, prefer cheaper capable agents. Reserve frontier models for architecture, difficult debugging, proofs, research review and high-stakes reasoning.
- If working from files or repositories, inspect the actual source before making claims.
- Do not invent prior decisions. If context is missing, say so.

Communication style:

- Spanish is the default conversational language.
- English is frequently used for technical documents, decks, scientific collaborations and outreach.
- Héctor dislikes unnecessarily verbose corporate language.
- Good format: direct paragraph + compact bullets/table when useful.
- Bad format: generic motivational filler, repeated conclusions, excessive headings, fake certainty.

---

## 2. High-level personal operating profile

Héctor is simultaneously working on:

1. Planck Technologies, a deep-tech startup.
2. University studies in Mathematics and Physics.
3. Combat sports and strength/conditioning.
4. AI tooling and multi-agent systems for personal/startup productivity.
5. Scientific/technical writing and research experiments.
6. Outreach, talks and collaborations related to quantum/hybrid computing.

He often wants one AI stack to cover all of these domains while keeping them logically separated into projects.

Recommended project structure for any AI platform:

- Project: Planck Technologies
- Project: University — Mathematics & Physics
- Project: Training — MMA / Wrestling / BJJ / Strength
- Project: AI / Agents / Plancky
- Project: Research / Papers
- Optional: Personal productivity / hobbies

Do not merge all domains into one giant active context when it is not needed. Use this file as routing memory, then load only the relevant domain context.

---

## 3. Planck Technologies — high-level context

Planck Technologies evolved from a more generic quantum-computing SaaS concept into a platform/SDK for Hybrid Computing Digital Twins.

Core positioning:

- Vertical-agnostic architecture.
- Finance is the first strong commercial/use-case vertical.
- Goal: combine classical computing, HPC/simulation, quantum-inspired methods and quantum hardware where appropriate.
- The product should not look like a visual Qiskit wrapper or a toy quantum interface.
- The user experience should focus on running useful digital-twin workflows rather than exposing low-level algorithms unnecessarily.

Current conceptual UI:

- Dashboard
- Twin Runner
- Presets
- Settings

Core execution philosophy:

- One unified execution abstraction.
- A user should be able to run a problem without manually choosing every low-level backend detail.
- The system may select or fall back between QPU, HPC/classical and simulator paths.
- Hardware should be treated as a backend, not as the entire product.

Relevant technologies and concepts:

- Qiskit Runtime
- Sampler / Estimator workflows
- OpenQASM 2/3
- IBM quantum hardware
- IonQ
- QAOA
- VQE
- QUBO / Ising formulations
- simulated annealing / tabu-style heuristics
- quantum-inspired methods
- hybrid solvers
- backend recommendation/orchestration
- telemetry and execution history

Finance-first presets discussed:

1. Portfolio / asset allocation
   - risk-return optimization
   - Sharpe-like metrics
   - HPR research connection
   - constraints and rebalancing
   - QUBO/QAOA as experimental alternative, always benchmarked against classical baselines

2. Cross-venue risk / arbitrage
   - latency
   - slippage
   - opportunity selection
   - risk-aware decisions

3. Credit/default-risk micro-portfolio
   - probability of default
   - loss given default
   - constrained allocation / decision problems

Custom digital twins should remain possible so additional verticals can be added without a large architectural refactor.

### Quark compiler

Planck has explored a "Quark compiler" abstraction:

- hardware-agnostic logical optimization layer
- output can be expressed in QASM
- intended to reduce redundant gates / simplify circuits
- especially interesting in variational or dense optimization workflows
- should be optional/toggleable
- do not assume it improves every circuit
- previous experiments did not always show a meaningful advantage, so claims must be evidence-driven

### Product engineering principles

- API key required for execution
- user quotas and rate limits
- visible quota/status in UI/SDK
- ability to delete execution data
- secure user-data handling
- modular/docker-friendly architecture
- avoid breaking public SDK interfaces unnecessarily
- telemetry should be useful for comparing execution paths
- keep future vertical expansion in mind

### Commercial / scientific positioning

Planck should be presented as a hybrid computing/digital-twin platform that can investigate whether a quantum or quantum-inspired component helps a specific bottleneck.

Preferred proof format:

- define problem
- define classical reference
- define hybrid/quantum formulation
- run controlled experiment
- compare KPIs
- state limitations

Never sell "quantum advantage" as already established unless the experiment truly supports it.

Canonical note: for current implementation details, source code, endpoints, schemas and exact product behavior, use the dedicated Planck AI Guide and repositories instead of treating this public cross-domain memory as authoritative.

---

## 4. Planck outreach, talks and educational sessions

Héctor also uses Planck for technical/business talks.

Typical talk structure:

- innovation / computational bottlenecks
- physical intuition and quantum-computing fundamentals
- programming / SDK concepts
- practical use case
- classical baseline
- hybrid/quantum approach
- KPI comparison
- limitations and realistic outlook

Good target audiences:

- business schools
- engineering schools
- finance programs
- entrepreneurship hubs
- university innovation offices
- deep-tech communities
- students/researchers

Talks should be customized to the audience.

Examples:

Finance:
- portfolio optimization via QUBO/QAOA
- opportunity search
- risk/return comparison
- KPIs: return, risk, Sharpe/HPR, runtime, cost, solution quality

Engineering:
- scheduling / resource allocation
- QUBO constraints
- design-space exploration
- KPIs: makespan, cost, utilization, quality

Chemistry/materials:
- reduced Hamiltonian
- exact diagonalization classical baseline
- VQE experimental path
- KPIs: energy error, convergence, depth, runtime, cost

The goal is a professional session, not a generic "what is a qubit" presentation.

---

## 5. Scientific research context — HPR

Héctor has worked on a concept called Holistic Performance Ratio (HPR).

Core idea:

HPR = E[R - R_f] / S(rho)

with a normalized covariance-derived density-like matrix:

rho = C / Tr(C)

and von Neumann-style entropy:

S(rho) = -Tr(rho log rho)

Research interests around HPR:

- compare HPR with Sharpe Ratio
- rolling/time-dependent versions
- covariance structure as information
- pure/mixed/entangled analogies, used carefully
- tensor-product constructions
- mutual information
- asset sets including large US technology equities
- mathematical rigor and publishability
- remove trivial/redundant proofs
- avoid references that do not support claims
- distinguish mathematical analogy from physical quantum interpretation

When reviewing HPR work:

- prioritize correctness over novelty hype
- identify circular or trivial arguments
- check normalization/domain assumptions
- check whether entropy interpretation is meaningful
- recommend simpler, stronger statements when possible
- aim for arXiv-quality exposition

---

## 6. University — Mathematics and Physics

Héctor studies Mathematics and Physics through UNED-style coursework and prefers learning above the minimum exam level.

### Learning philosophy

The ideal explanation should:

1. State definitions rigorously.
2. Explain intuition.
3. Derive results rather than only state formulas.
4. Show how concepts connect to linear algebra, analysis, geometry, probability and physics.
5. Include subtle cases/counterexamples.
6. Give intermediate exercises.
7. Give harder exercises.
8. Solve representative examples step by step.
9. Then compress into an exam-oriented summary if requested.

Héctor often asks for:
- "sin saltos"
- step-by-step numerical derivations
- proofs
- examples that are harder than typical exams

### Areas studied/discussed

Mathematical language / foundations:

1. logic
2. sets
3. relations and mappings
4. internal operations and algebraic structures
5. natural numbers and integers
6. rational and real numbers
7. complex numbers

Other mathematics:

- algebra
- analysis of one variable
- graph theory
- discrete mathematics
- linear algebra
- algebraic structures
- supremum axiom / completeness of R
- rings and related structures
- mathematical language and proof techniques

Physics:

- mathematical analysis for physics
- methods
- vibrations and waves
- circuits/electronics
- mechanics
- quantum mechanics concepts
- Heisenberg uncertainty principle
- Lagrangian mechanics
- path-integral connections
- computational physics

### Preferred explanation depth

For ordinary course questions, the assistant should aim slightly above the course level.

Example:

Instead of saying "an uncertainty relation follows because measurements disturb the system", derive the Robertson uncertainty relation from operator variance and Cauchy-Schwarz, and then connect it to canonical commutation relations.

Instead of only defining a ring, explain:
- underlying abelian group under addition
- associative multiplication
- distributivity
- unity/no-unity convention
- commutative/noncommutative examples
- zero divisors
- relation to fields and integral domains

### Study organization

Héctor prefers:

- weekday theory/notes and conceptual study
- weekend problem solving when possible
- using commute/dead time for oral review and short explanations
- consolidating afternoons in one location when possible
- structured blocks instead of constantly changing environments

For study planning, prioritize consistency and reduce context switching.

---

## 7. Training — combat sports and strength

Héctor trains combat sports and strength work.

Relevant disciplines:

- wrestling
- Brazilian Jiu-Jitsu / no-gi grappling
- MMA
- strength training
- running/cardio as secondary conditioning

Training interests:

- explosiveness
- strength
- speed
- agility
- aggressive forward pressure when tactically appropriate
- escaping compromised positions efficiently
- movement quality
- transferable athleticism

He is interested in:

- wrestling mechanics
- grappling transitions
- MMA-specific conditioning
- force production
- how animals move/attack/defend as inspiration for movement concepts
- legal/technical questions about grappling positions
- efficient weekly scheduling around work/study/startup obligations

### How an AI should help with training

Prefer practical programming:

- exercise selection
- sets/reps/RPE
- weekly split
- fatigue management
- progression
- sport-specific transfer
- conditioning placement

Avoid pseudoscience.

If discussing injury/medical symptoms, switch from performance coaching to conservative health guidance and recommend qualified care when appropriate.

### Scheduling philosophy

Training should coexist with study and Planck.

Useful pattern:

- several fixed weekday training evenings
- study beforehand
- strength integrated where logistics are easiest
- weekend blocks can absorb some university problem-solving or strength work
- minimize unnecessary travel and location switching

---

## 8. AI / local models / Plancky

One major ongoing project is "Plancky": a multi-agent AI setup for Planck and personal workflows.

### Goal

Create a system of specialized agents such as:

- Plancky/tech
- Plancky/marketing
- Plancky/research
- Plancky/email-CRM
- Plancky/reviewer

with:

- shared persistent memory
- specialized skills
- common startup context
- parallel execution
- GitHub integration
- warnings when agents disagree
- readable Markdown memory
- simple terminal UX
- model-provider independence

### Desired architecture

A strong pattern is:

orchestrator
→ specialist workers
→ reviewer
→ frontier fallback only when necessary

Example:

Tech lead / orchestrator
- delegates implementation

Backend worker
- endpoints, services, data

Frontend worker
- UI

SDK worker
- Python SDK/public API

Test worker
- tests, regression checks

Research worker
- papers/docs

Reviewer
- verifies integration and conflicts

Frontier reviewer
- used only for architecture, difficult reasoning or high-risk changes

### Model philosophy

Héctor is interested in:

- Kimi
- Qwen
- DeepSeek
- GLM
- MiniMax
- Claude
- GPT
- local models via Ollama

The goal is not loyalty to one provider.

Preferred routing:

cheap/high-volume model:
- repetitive coding
- tests
- documentation
- mechanical refactors
- simple frontend
- data cleanup

frontier model:
- architecture
- difficult debugging
- mathematical proof
- scientific review
- security-critical reasoning
- ambiguous product decisions

### Local hardware context

Personal hardware discussed:

- NVIDIA GTX 1060 class GPU with 6 GB VRAM
- 16 GB RAM

This means:

- small/medium quantized local models are feasible
- very large frontier open-weight models are not realistically equivalent to cloud frontier models on this hardware
- local inference is useful for privacy/offline/light tasks
- cloud inference remains better for heavy reasoning/coding

### Ollama / local setup

Ollama has been used/planned on Windows.

Prior model exploration included:

- small Qwen models
- larger quantized Qwen-family models
- approximately 8–9B-class GGUF/Q4 models

Plancky should not be hardcoded to a single local model.

### Repository / filesystem idea

A Plancky repository has been envisioned with:

- memory/
- skills/
- agents/
- instructions/
- scripts/
- shared Markdown context

Each agent should load:

1. shared memory
2. domain-specific instructions
3. current task context
4. relevant repo files only

Do not push the entire memory into every prompt if retrieval can select the needed parts.

---

## 9. Kimi-specific intended workflow

Kimi is being evaluated as a possible replacement for more expensive AI/coding subscriptions.

Desired use:

- Kimi web/mobile for general chat and studying
- Kimi Projects for domain separation
- Kimi Code Desktop for codebase work
- Kimi Code CLI for terminal workflows
- Kimi Code VS Code extension for editor workflows
- potentially Kimi API-compatible access through third-party coding clients
- multi-agent workflows for Planck

Suggested projects:

### Project: Planck Technologies
Load:
- Planck AI Guide
- product docs
- relevant architecture docs
- this file only when cross-domain context matters

### Project: Carrera
Load:
- subject notes
- syllabus
- exercise sheets
- this file's study-preference section

### Project: Entrenos
Load:
- training plan
- weekly availability
- exercise log
- this file's training section

### Project: AI / Plancky
Load:
- Plancky repo
- agent definitions
- provider configs
- benchmarks
- this file's AI/tooling section

### Project: Research
Load:
- HPR paper
- notebooks
- references
- peer-review notes

Kimi should treat this file as durable context, not as a replacement for the latest source files.

---

## 10. Coding-agent operating rules

When an agent is allowed to modify repositories:

1. Inspect the repository first.
2. Identify the public API/behavior that must remain stable.
3. Make a plan for non-trivial changes.
4. Use small coherent commits/patches.
5. Run tests.
6. Report failures instead of hiding them.
7. Do not rewrite unrelated files.
8. Avoid massive dependency additions unless justified.
9. Respect existing style.
10. Do not fabricate success if tests were not run.

For Planck specifically:

- preserve unified execution concepts
- avoid reintroducing obsolete duplicated endpoints
- keep backend abstraction clean
- keep finance-first presets extensible to other verticals
- preserve classical baselines
- avoid quantum hype in docs
- surface quotas/errors clearly
- think about user isolation/security

---

## 11. Research-agent operating rules

For papers, scientific claims and technical comparisons:

- distinguish source-backed claim vs inference
- cite primary/official sources where possible
- do not use benchmark marketing as proof of real-world superiority
- check experimental setup
- compare against strong classical baselines
- avoid cherry-picking
- quantify uncertainty
- separate "promising" from "demonstrated"
- explicitly state assumptions

When comparing AI models:

- compare quality and total useful work, not only benchmark scores
- include context-window behavior
- agent reliability
- CLI integration
- rate limits
- price
- concurrency
- tool use
- privacy/data handling
- ecosystem friction

---

## 12. Business / product decision style

Héctor tends to prefer decisions framed as:

- What would you choose?
- Why?
- What is the cheapest viable option?
- Where is the bottleneck?
- What should be tested for one month before committing?

A good answer often includes:

- default recommendation
- cheaper fallback
- condition for upgrading
- concrete experiment/KPI

Example for AI subscriptions:

Do not say:
"Claude is better but Kimi is cheaper."

Say:
"Use Kimi as the default worker for one month. Track how often you need a frontier fallback. If >20–30% of meaningful tasks require Claude/GPT rework, upgrade. If <10%, keep the cheaper stack."

---

## 13. Productivity / weekly organization

Important recurring idea:

- Planck should have a protected daily block.
- University study needs recurring weekday blocks.
- Weekend time can be used for heavier exercises/problem sets.
- Training should be scheduled around these fixed anchors.
- Commute/dead time can be used for oral review or light planning.
- Prefer fewer locations and less context switching.

The assistant should optimize for sustainable throughput, not maximum theoretical hours.

When making a weekly plan:
- include travel/logistics
- include buffer
- protect the highest-priority fixed blocks
- do not schedule every minute
- separate deep work from low-cognitive tasks

---

## 14. Creative / presentation preferences

For Planck decks and marketing:

Visual identity previously discussed:

- serif/Lora-like typography
- beige/cream
- dark gray
- turquoise/green accent around #578e7e

Avoid obvious AI-generated presentation clichés:

- "Slide 1" labels
- decorative highlight bars above every title
- excessive cards/chips
- repetitive section tags
- generic robot/quantum stock imagery
- huge blocks of hype text

Prefer:
- clean editorial layouts
- technical diagrams
- simple charts
- restrained branding
- real problem → method → KPI structure
- credible language

---

## 15. Preferred technical depth by domain

### Mathematics
High rigor. Proofs and definitions matter.

### Physics
Derivations plus physical interpretation.

### Software
Repository-aware implementation and testing.

### Quantum computing
Realistic, experimental, baseline-driven.

### Finance
Quantitative but skeptical of overfitting and unsupported return claims.

### Training
Practical programming and sport transfer.

### AI tooling
Cost/quality/throughput trade-offs; model-agnostic architecture.

### Business outreach
Short, credible, personalized, clear next step.

---

## 16. Topics that have come up but should NOT automatically be pulled into every session

These may exist in historical conversations but should be retrieved only when relevant:

- personal vehicle troubleshooting
- personal investing/leverage ideas
- detailed outreach lead lists
- individual university contacts
- exact calendar logistics
- airsoft DIY ideas
- subscription comparisons
- one-off travel plans

Do not pollute a mathematics session with startup or training context unless it materially helps.

---

## 17. Public-memory privacy rules

Because this repository is public, never add the following to this file without explicit review:

- passwords
- API keys/tokens
- private repository secrets
- bank/account numbers
- exact home address
- exact workplace address
- personal phone numbers
- private third-party contact details
- salary/tax records
- medical/health records
- private CRM exports
- confidential contracts
- unpublished customer data
- unreleased proprietary algorithms/source code

If a future AI wants to update this memory, it should create a proposed patch and clearly mark potentially sensitive additions.

---

## 18. How to update this memory

Recommended workflow:

- Update only durable facts/preferences.
- Do not add every temporary appointment or short-lived task.
- Date major architectural changes.
- Keep exact implementation details in their canonical repositories.
- Keep course-specific notes in the Carrera project/repo.
- Keep training logs in a training-specific file/repo.
- Keep this file as a routing layer.

Suggested supplemental files if this grows further:

- AI_CONTEXT/PLANCK_PUBLIC.md
- AI_CONTEXT/CAREER.md
- AI_CONTEXT/TRAINING.md
- AI_CONTEXT/AI_TOOLING.md
- AI_CONTEXT/RESEARCH.md
- AI_CONTEXT/WORKING_STYLE.md

---

## 19. Compact routing summary for an AI

If the task is about Planck:
- use Planck AI Guide + current repository
- use this file for strategic/history context
- prioritize hybrid-computing digital twins and finance-first extensibility

If the task is about university:
- load Carrera materials
- teach rigorously
- include derivations/exercises
- compress only on request

If the task is about training:
- use practical sport/strength programming
- respect weekly logistics
- avoid pseudoscience

If the task is about AI/Plancky:
- prefer model-agnostic multi-agent design
- cheap workers + strong reviewer
- optimize cost and concurrency
- preserve shared memory in Markdown

If the task is about research:
- verify claims
- prefer primary sources
- benchmark against classical methods
- prioritize correctness

---

## 20. Current meta-goal

The broader goal is to create an AI operating environment where Héctor can move between:

- building Planck
- studying Mathematics/Physics
- training
- research
- outreach
- personal tooling

without re-explaining months of context, while still keeping each project sufficiently isolated that irrelevant context does not degrade performance.

The ideal system is:

- persistent
- searchable
- modular
- provider-agnostic
- cheap enough for high-volume use
- capable of parallel agents
- able to escalate hard tasks to frontier models
- transparent about what it changed
- safe with repositories and personal data

This file is the public cross-domain starting point for that system.

---

Last major context consolidation: November 2026.
