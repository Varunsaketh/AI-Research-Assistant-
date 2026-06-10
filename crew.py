from crewai import Crew
from tasks.researchTask import research_task
from agents.analysisAgent import analysis_agent
from agents.writerAgent import writer_agent
from agents.searchAgent import research_agent
from tasks.analysisTask import analysis_task
from tasks.writerTask import write_task

research_crew = Crew(
    agents = [research_agent,
              analysis_agent,
              writer_agent
              ],
    tasks = [research_task
             ,analysis_task
             ,write_task
             ],
    verbose = True
)
print("⚡ZEUS⚡ the research crew has been assembled")