import os
from crewai import Agent,LLM
from crewai_tools import FileWriterTool

_model = os.getenv("WRITER_AGENT_MODEL")
if not _model:
    _model = "groq/llama-3.3-70b-versatile"

llm = LLM(
    model = _model,
    temperature = 0.3
)
writer_agent = Agent(
    role = "You are a writer agent who writes a comprehensive report based on the analysis provided by the analysis agent.",
    goal = "Write a simple and short comprehensive report based on the analysis provided by the analysis agent.",
    backstory = ("You are an expert in writing and communication. "
                "You have a deep understanding of how to structure and present information in a clear and concise manner. "
                "You are skilled at synthesizing complex information and presenting it in a way that is easy to understand and actionable."),
    llm = llm,
    tools = [FileWriterTool()],
    verbose = True
)