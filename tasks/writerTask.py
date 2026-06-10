import textwrap
from crewai import Task
from agents.writerAgent import writer_agent
from tasks.analysisTask import analysis_task

write_task = Task(
    agent = writer_agent,
    description = textwrap.dedent("""
    You are a writer agent who writes a comprehensive report based on the analysis provided by the analysis agent.
    Your Tasks
    1. Write a comprehensive report based on the analysis provided by the analysis agent.
    2. Ensure that your report is well-structured, clear, and concise, and that it effectively communicates the insights and recommendations provided by the analysis agent.
    3. apply tables , graphs and charts to present complicated information 
    4. Ensure that your report is actionable and relevant to the research question, and that it provides clear next steps for further investigation or action.
    output:
    1. A comprehensive report that includes a clear and concise summary of the analysis provided by the analysis agent, as well as any relevant insights, recommendations, and next steps for further investigation or action.
    2. A well-structured and visually appealing report that effectively communicates the information provided by the analysis agent, and that is easy to understand and actionable for the intended audience.
    3. keep it simple and short
                                """),
    expected_output = "A comprehensive report that includes a clear and concise summary of the analysis provided by the analysis agent",
    context = [analysis_task],
    output_file = "final_report.md"
)
print("⚡ZEUS⚡ the writer task has been initialized and is ready to write the final report at lightning speed! ⚡")