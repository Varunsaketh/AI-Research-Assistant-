import textwrap
from crewai import Task
from agents.analysisAgent import analysis_agent
from tasks.researchTask import research_task

analysis_task = Task(
    agent = analysis_agent,
    description =textwrap.dedent("""
    You are an analysis agent who analyzes the research findings and provides insights and recommendations based on the
    Your TAsks
    1. Analyze the research findings provided by the research agent.
    2. Provide insights and recommendations based on the information gathered.
    3. Ensure that your analysis is thorough and accurate, and that your insights and recommendations are actionable and relevant to the research question.
    4. highlight any potential gaps or limitations in the research findings and suggest areas for further investigation.
    5. highlight most important and relevant information from the research findings that can be used by the writer agent to write the final report.
    
    provide:
    1. A detailed analysis of the research findings, including any patterns, trends, or insights that you have identified.
    2. A list of actionable recommendations based on your analysis, including any potential next steps
    3.trend analysis and future predictions based on the research findings.
    4.actionable conclusions
                                """),
    expected_output = "A report that includes a detailed analysis of the research findings, actionable recommendations, trend analysis and future predictions, and actionable conclusions based on the information gathered by the research agent."
    context = [research_task]
    output_file = "analysis_report.md"
)
print("⚡ZEUS⚡ the analysis task has been initialized and is ready to analyze the research findings at lightning speed! ⚡")