# Neuro-Symbolic Scientific Claim Auditor
### *Grounding Information Retrieval in Physical Reality*

## 🌟 Research Vision
In the era of Large Language Models (LLMs), information retrieval systems often prioritize linguistic fluency over factual and physical accuracy. This project proposes a **Neuro-Symbolic** framework designed for **Responsible Advice-Giving**. By anchoring neural extraction (SciBERT) to a symbolic knowledge base of physical constants, this auditor identifies and "vetoes" scientific hallucinations that violate the laws of physics.



## 🛠️ Technical Implementation
This pipeline processes unstructured scientific reports (PDFs) and audits quantitative claims against established domain constraints (e.g., the **Shockley-Queisser limit** in photovoltaics).

* **Neural Layer:** Utilizes **SciBERT** (Fine-tuned for scientific vocabulary) for Named Entity Recognition (NER) to identify technical metrics within complex text.
* **Symbolic Layer:** A structured Knowledge Base (CSV) containing theoretical efficiency limits for 10 distinct solar technologies.
* **Audit Logic:** A Python-based verification engine that cross-references extracted claims with the symbolic KB to flag data as `VALID` or `IMPOSSIBLE`.



## 📊 Evaluation & Robustness
As a researcher with a background in **Biostatistics (MSc, Distinction, 4.00/4.00 CGPA)**, I have designed this system to handle real-world "noise." The auditor is tested against:
* **Linguistic Variance:** Handling percentages expressed as symbols (%) or text ("percent").
* **Stochastic Stress-Testing:** Evaluation using randomized "noisy" research papers to measure the system's precision in flagging physically impossible data.



## 📂 Project Structure
```text
├── data/
│   └── advanced_physics_kb.csv   # The "Truth Anchor" (Physical Limits)
├── reports/
│   └── Research_...pdf           # Sample scientific documents
├── src/
│   └── auditor_logic.py          # Neuro-symbolic verification engine
├── main.py                       # System entry point & visualization
└── requirements.txt              # Dependency management

## 🚀 Getting Started
1. Install dependencies:
pip install -r requirements.txt
2. Run the Audit:
python main.py
