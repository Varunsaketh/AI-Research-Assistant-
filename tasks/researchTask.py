import textwrap
from crewai import Task
from agents.searchAgent import research_agent

research_task = Task(
    agent=research_agent,
    description=textwrap.dedent("""

conduct comprehensive search on the web to gather accurate and relevant information on topic : {topic}.
    1. gather the information from the current year 2026 to ensure the information is up to date
    2. search for the most recent and relevant information
    3. gather the information for multiple sources to ensure the accuracy and reliability of the information
    4. organize the findings in a structured format
        
provide the summary with
    1.Key findings
    2.important statistics and data
    3.recent developments related to the topic
    4. keep it simple and short

                                """),
    expected_output = "A structured summary of the research findings with key insights, sources, statistics, recent developments, and expert opinions.",
    output_file = "research_summary.md"

)
print("⚡ZEUS⚡ the research task has been defined and is ready to be executed at lightning speed! ⚡")