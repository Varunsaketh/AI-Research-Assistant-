from dotenv import load_dotenv
from crew import research_crew

load_dotenv()

def run(topic : str):
    result = research_crew.kickoff(inputs={"topic": topic})

    print("⚡ZEUS⚡ has completed the research task.")
    print(result)
          


if __name__ == "__main__":
    print("hello I am ⚡ZEUS⚡ the research agent i can do everything in the speed of ⚡")
    topic = input("Enter the research topic: ")
    run(topic)