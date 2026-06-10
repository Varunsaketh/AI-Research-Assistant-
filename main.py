from dotenv import load_dotenv

load_dotenv()

from crewai.llms import cache as crewai_cache


def _strip_cache_breakpoint(message):
    if isinstance(message, dict):
        message.pop("cache_breakpoint", None)
    return message


crewai_cache.mark_cache_breakpoint = _strip_cache_breakpoint

from crew import research_crew

def run(topic : str):
    result = research_crew.kickoff(inputs={"topic": topic})

    print("⚡ZEUS⚡ has completed the research task.")
    print(result)
          


if __name__ == "__main__":
    print("hello I am ⚡ZEUS⚡ the research agent i can do everything in the speed of ⚡")
    topic = input("Enter the research topic: ")
    run(topic)