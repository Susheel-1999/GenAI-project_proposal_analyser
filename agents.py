from crewai import Agent
from tools import jd_reader_tool, resume_analyzer_tool, web_search_tool, serper_search_tool
from utils import llm

# Job Description Reading Agent
jd_reader_agent = Agent(
    role="Job Description Reader",
    goal="Understand the job description",
    verbose=True,
    memory=True,
    backstory="You are an AI assistant that helps candidates understand job descriptions.",
    llm=llm,
    allow_delegation=False,
    tools=[jd_reader_tool]
)

# Candidate Resume Analyzer Agent
resume_analyzer_agent = Agent(
    role="Candidate Resume Analyzer",
    goal="Understand key details from the resume.",
    verbose=True,
    memory=True,
    backstory="You are an expert in analyzing resumes and identifying key skills, experiences, and qualifications.",
    llm=llm,
    allow_delegation=False,
    tools=[resume_analyzer_tool]
)

# Web Search Agent
web_search_agent = Agent(
    role="Job Market Researcher",
    goal="Find the latest knowledge trends for the domain mentioned in the job description.",
    verbose=True,
    memory=True,
    backstory=(
        "You specialize in researching job market trends. "
        "Your goal is to find the latest knowledge trends and resume optimization techniques for the given job domain."
    ),
    llm=llm,
    allow_delegation=False,
    tools=[web_search_tool, serper_search_tool]
)

# Resume Improvement Agent
resume_improvement_agent = Agent(
    role="Resume Improvement Specialist",
    goal="Analyze the candidate's resume against the job description and industry trends. Identify strengths and weaknesses, and provide targeted improvement suggestions.",
    verbose=True,
    memory=True,
    backstory="You are a resume expert who tailors resumes to better fit job descriptions.",
    llm=llm,
    allow_delegation=False,
    output_formatter="text",
)