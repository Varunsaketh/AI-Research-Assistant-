import os
from crewai import Agent,LLM
from crewai_tools import (SerperDevTool,ScrapeWebsiteTool)

_model = os.getenv("SEARCH_AGENT_MODEL")
if not _model:
    _model = "groq/llama-3.3-70b-versatile"

llm = LLM(
    model = _model,
    temperature = 0.3
)

research_agent = Agent(
    role = "You are a research assistant who gathers the latest information of current year 2026 from the web  ",
    goal = "keep it simple and short , Gather the most accurate and relevant information in 2026 from the web and answer the question",
    backstory = ("You are an expert in web research and information gathering. "
                "You have access to the latest tools and techniques to find the most accurate and relevant information from the web."
                "You are efficient and thorough in your research "
                "ensuring that you provide the best possible answers to the questions asked."),
    llm = llm,
    tools = [SerperDevTool(), ScrapeWebsiteTool()],
    verbose = True
)
print("⚡ZEUS⚡ the research agent has been initialized and is ready to gather information at lightning speed! ⚡")
