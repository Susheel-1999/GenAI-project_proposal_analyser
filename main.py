import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import jd_reader_agent, resume_analyzer_agent, web_search_agent, resume_improvement_agent
from tasks import jd_reader_task, resume_analyzer_task, web_search_task, resume_improvement_task

load_dotenv()
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# Create and run the Crew
crew = Crew(
    agents=[jd_reader_agent, resume_analyzer_agent, web_search_agent, resume_improvement_agent],
    tasks=[jd_reader_task, resume_analyzer_task, web_search_task, resume_improvement_task],
    process=Process.sequential
)
result = crew.kickoff()