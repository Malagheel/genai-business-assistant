#  GenAI Business Assistant

A GenAI-powered assistant that helps translate high-level business problems into structured solution specifications — built to showcase AI product thinking for business analyst and tech strategy roles.

---

##  Features

- **LLM-Powered Reasoning**: Uses OpenRouter's API to generate technical and strategic specs.
- **Business Use Case Translator**: Takes vague goals and returns architecture, data needs, tools, and timelines.
- **Streamlit Web App**: User-friendly interface for live demos and non-technical users.
- **Modular Codebase**: Easy to extend with new prompts, data sources, or deployment backends.

---

## 📸 Screenshot

![screenshot](./assets/demo.png)

---

##  Tech Stack

- `Python 3.11+`
- `Streamlit` for UI
- `OpenRouter + LLM` (Mistral 7B Instruct)
- `dotenv` for secure API key loading

---

##  Example Input

> We want to use AI to reduce customer service wait times.

##  Output Includes:

- Business Requirements Summary
- Suggested GenAI Use Cases
- Required Data
- Technical Architecture Overview
- Implementation Timeline
- Tools & Technologies

---

##  Local Setup

```bash
git clone https://github.com/your-username/genai-business-assistant.git
cd genai-business-assistant
pip install -r requirements.txt
python -m streamlit run web/streamlit_app.py

##  Contact

Built by [Matthew D. Alagheel](https://github.com/Malagheel).  
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/matthewdalagheel/).
