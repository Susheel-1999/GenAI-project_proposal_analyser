# GenAI- Resume Analyser
Analyzes a candidate's resume against a job description and industry trends using four agents. It will identifies strengths, weaknesses in the candidate’s resume and provides specific improvements to enhance job alignment.

# Steps to run Streamlit app:
1. Create a openai API or use an existing one, visit: https://platform.openai.com/settings/organization/api-keys
2. Create a serper API or use an existing one, visit: https://serper.dev/api-key
3. Create a new environment: <br>
```conda create -p genai python==3.10 -y```
4. Activate the environment: <br>
```conda activate genai```
5. Install the requirements: <br>
```pip install -r requirements.txt```
6. Place the job_description.pdf and candidate_resume.txt in data folder
7. Run main.py: <br>
```python main.py```

# About Techniques:
CrewAI is a cutting-edge framework for orchestrating autonomous AI agents.
### **Agents**
We use four specialized agents to analyze and improve the resume:
1. **JD Analyzer** – Extracts key skills and qualifications from the job description.
2. **Resume Analyzer** – Assesses the candidate’s experience and alignment with the job.
3. **Industry Researcher** – Fetches the latest job market trends.
4. **Improvement Advisor** – Suggests targeted resume enhancements.

### **Tasks**
Each agent is assigned a specific task to perform:
- Understanding the job description.
- Analyzing the candidate’s resume.
- Researching current industry trends.
- Providing resume improvement suggestions.

### **Tools**
We utilize **four tools** to support this process:
- **Three inbuilt tools**:
  - **WebsiteSearchTool** – Searches the web for relevant industry information.
  - **SerperDevTool** – Retrieves job market trends and relevant insights.
  - **TXTSearchTool** – Extracts key details from text-based documents.
- **One LangChain tool**:
  - **RetrievalQA** – Performs advanced document retrieval and question-answering.

# Reference:
crewai - https://docs.crewai.com/quickstart
<br>langchain - https://python.langchain.com/docs/introduction/
