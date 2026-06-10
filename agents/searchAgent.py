import os
from crewai import Agent , LLM
from crewai.tools import SerperDevTool

llm = LLM(
    model = os.getenv("SEARCH_AGENT_MODEL"),
    temperature = 0.3
)

research_agent = Agent(
    role = "You are a research assistant who gathers the information from the web ",
    goal = "Gather the most accurate and relevant information from the web and answer the question",
    backstory = ("You are an expert in web research and information gathering. "
                "You have access to the latest tools and techniques to find the most accurate and relevant information from the web."
                "You are efficient and thorough in your research "
                "ensuring that you provide the best possible answers to the questions asked."),
    llm = llm,
    tools = [SerperDevTool()]
    verbose = True
)


