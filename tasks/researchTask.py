import textwrap
from crewai import Task
from agents.searchAgent import research_agent

research_task = Task(
    agent=research_agent,
    description=textwrap.dedent("""

conduct comprehensive search on the web to gather accurate and relevant information on topic : {topic}.
    1. gather the information from the current year
    2. search for the most recent and relevant information
    3. gather the information for multiple sources to ensure the accuracy and reliability of the information
    4. organize the findings in a structured format
        
provide the summary with
    1.Key findings
    2.Sources used
    3.importanat statistics and data
    4.recent develpopments related to the topic
    5.expert opinions and analysis

                                """)
    expected_output = "A structured summary of the research findings with key insights, sources, statistics, recent developments, and expert opinions."
    output_file = "research_summary.md"

)