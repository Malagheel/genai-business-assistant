#  GenAI Business Assistant

Transform business problems into structured technical solution specifications using Generative AI.

---

##  Overview

The **GenAI Business Assistant** is a Streamlit-powered application that helps you convert natural language business challenges into detailed, AI-driven solution blueprints.

Whether you're a product owner, business analyst, or technical stakeholder, this tool allows you to:

-  Quickly define AI-powered product opportunities
-  Automatically generate high-level technical documentation
-  Understand the necessary data, architecture, and tooling

---

##  Example Input


---
## We want to use AI to reduce customer service wait times.

##  Output Includes

- **Business Requirements Summary**
- **Suggested Generative AI Use Cases**
- **Required Data**
- **Technical Architecture Overview**
- **Implementation Timeline**
- **Tools & Technologies**

---

##  Local Setup

To run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/Malagheel/genai-business-assistant.git
cd genai-business-assistant
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3. Launch the App
```
python -m streamlit run web/streamlit_app.py
```
Then open your browser and go to:
 http://localhost:8501

## Example Output Preview
--- AI Assistant Output ---

**Business Requirements Summary:**
1. Develop an AI-powered customer service solution to handle inquiries and reduce wait times.
2. The solution should prioritize accurate and efficient handling of issues.
3. The system must learn from past interactions to improve over time.
4. Integration with existing platforms is required.
5. The system must be scalable and support monitoring/analytics.

**Suggested Generative AI Use Case(s):**
1. Chatbot Integration
2. Predictive Analytics
3. Intelligent Routing

**Required Data:**
- Historical customer service interactions
- Customer satisfaction scores
- Agent performance data
- Product/service metadata

**Technical Architecture Overview:**
1. Data Collection and Storage
2. AI Model Training and Prediction
3. Integration Layer with existing systems
4. Monitoring and Feedback Loops

**Implementation Timeline (basic):**
- 2–4 weeks for data preparation
- 4–6 weeks for model development
- 2–4 weeks for integration and testing

**Tools and Technologies:**
- PostgreSQL, MongoDB, AWS S3
- TensorFlow, PyTorch, Scikit-learn
- REST APIs, Webhooks
- Docker, Kubernetes, Prometheus, Grafana
- Power BI, Tableau, Looker
## 🛠 Tech Stack

- **Frontend:** Streamlit  
- **Language:** Python 3.11+  
- **LLM API:** OpenAI GPT (via `openai` Python SDK)  
- **Hosting:** Localhost / Streamlit Cloud  
- **Monitoring:** Prometheus, Grafana  

---

##  Screenshot

![App Screenshot](assets/demo-screenshot.png)

---

##  Author

**Matthew D. Alagheel**  
- GitHub: [@Malagheel](https://github.com/Malagheel)  
- LinkedIn: [Matthew Dalagheel](https://www.linkedin.com/in/matthewdalagheel/)  
- Email: [MatthewDalagheel@outlook.com](mailto:MatthewDalagheel@outlook.com)  



