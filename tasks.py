from crewai import Task
from agents import jd_reader_agent, resume_analyzer_agent, web_search_agent, resume_improvement_agent

jd_reader_task = Task(
    description=(
        "Analyze the job description and Understand it."
    ),
    expected_output="A simple summary of the job description.",
    agent=jd_reader_agent
)

resume_analyzer_task = Task(
    description=(
        "Analyze the candidate's resume and Understand it."
    ),
    expected_output="A summary of the candidate's resume with key takeaways.",
    agent=resume_analyzer_agent
)

web_search_task = Task(
    description=(
        "Research the latest techniques and trends relevant to the domain mentioned in the job description."
    ),
    expected_output="A brief report on the latest industry trends and resume optimization tips.",
    agent=web_search_agent
)

resume_improvement_task = Task(
    description=(
        "Analyze the candidate's resume against the job description and industry trends. "
        "Identify strengths and weaknesses, and provide targeted improvement suggestions "
        "to enhance alignment with the job requirements."
    ),
    expected_output=(
        "A list highlighting strengths and weaknesses in the current resume, along with "
        "specific recommendations for improvement based on the job description."
    ),
    agent=resume_improvement_agent,
    output_file="improvements.md"
)