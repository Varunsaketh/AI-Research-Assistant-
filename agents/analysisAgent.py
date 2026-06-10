import os
from crewai_tools import FileReadTool,DirectoryReadTool
from crewai import Agent,LLM

_model = os.getenv("ANALYSIS_AGENT_MODEL")
if not _model:
    _model = "groq/llama-3.3-70b-versatile"

llm = LLM(
    model = _model,
    temperature = 0.3
)
analysis_agent = Agent(
    role = "You are an analysis agent who analyzes the research findings and provides insights and recommendations based on the information gathered.",
    goal = "Analyze the research findings and provide insights and recommendations based on the information gathered keep it simple and short.",
    backstory = ("You are an expert in data analysis and interpretation. "
                "You have a deep understanding of various analytical techniques and methodologies. "
                "You are skilled at interpreting complex data and providing actionable insights and recommendations based on your analysis."),
    llm = llm,
    tools = [FileReadTool(), DirectoryReadTool()],
    verbose = True
)
print("⚡ZEUS⚡ the analysis agent has been initialized and is ready to analyze the research findings at lightning speed! ⚡")