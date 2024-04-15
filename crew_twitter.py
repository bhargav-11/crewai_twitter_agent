import os
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import click

load_dotenv()

from tools import TweeterTweetsOpinionsFinder

from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["SERPER_API_KEY"] = SERPER_API_KEY

# Rest of the code

search_tool = SerperDevTool(SERPER_API_KEY=SERPER_API_KEY)
scrape_tool = ScrapeWebsiteTool()
tweets_opinion_tool = TweeterTweetsOpinionsFinder()

llm = ChatOpenAI(model_name="gpt-4-turbo-preview", temperature=0.3)

# Define your agents with roles and goals
web_agent = Agent(
    role="Web search analyst",
    goal="Read the provided web article content and summarise it",
    backstory=""" You are a web search analyst with expertise in extracting key insights from online articles.
  Your role is to read the content from provided URL using scrape_tool and summarize the content by extracting key points.
  Once you are done you pass the article summary to 'Senior Research Analyst' to do further research.
  """,
    verbose=True,
    allow_delegation=True,
    tools=[scrape_tool],
    llm=llm,
)

# Define your agents with roles and goals
researcher = Agent(
    role="Senior Research Analyst",
    goal="Do research of provided article gather insights",
    backstory="""You need to do online research on provided article information and gather key insights from your research. then you pass the article and key insights to 'Senior tweets creator' to create tweets.""",
    verbose=True,
    allow_delegation=True,
    tools=[search_tool],
    llm=llm,
)

# Define your agents with roles and goals
tweet_opinions = Agent(
    role="Twitter Opinions Analyst",
    goal="Fetch opinions from twitter based on the article and key insights",
    backstory="""You need to find opinions from twitter based on the article and key insights. You need to use 'tweets_opinion_tool' tool to fetch tweets opinions. then you pass the article, key insights and opinions to 'Senior tweets creator' to create tweets.""",
    verbose=True,
    allow_delegation=True,
    tools=[tweets_opinion_tool],
    llm=llm,
)

# Define your agents with roles and goals
tweety = Agent(
    role="Senior tweets creator",
    goal="Create 4-5 tweers replies using provided article and key insights",
    backstory="""You are a helpful AI assistant that can create tweets based on the provided article and key insights. You create 4-5 uniquely tailored twwets""",
    verbose=True,
    allow_delegation=True,
    llm=llm,
)


# Initialize the CLI application with click
@click.command()
@click.option(
    "--url",
    prompt="Enter the URL of the article",
    help="The URL of the article to process.",
)
def run_crew(url):
    if not url:
        return "Please provide a valid URL."

    scrape_task = Task(
        description="analyze the article {} and extract the key insights and generate sample tweets.".format(
            url
        ),
        expected_output="A summary of the article.",
        agent=web_agent,
        next_task="research_task",  # Linking to the next task
    )

    research_task = Task(
        description="Analyze the summary and do research gather insights about the article",
        expected_output="summary of article and Key insights from the research.",
        agent=researcher,
        next_task="tweeter_opinions_task",  # Linking to the final task
    )

    tweeter_opinions_task = Task(
        description="Find tweets opinions based on the article and key insights.",
        expected_output="summary of article, Key insights and tweets opinions.",
        agent=tweet_opinions,
        next_task="tweet_creation_task",  # Linking to the final task
    )

    tweet_creation_task = Task(
        description="Create 4-5 tweets based on the article content, insights and tweets opinions.",
        expected_output="4-5 uniquely tailored tweets.",
        agent=tweety,
    )

    # Update your crew configuration
    crew = Crew(
        agents=[web_agent, researcher, tweet_opinions, tweety],
        tasks=[scrape_task, research_task, tweeter_opinions_task, tweet_creation_task],
        verbose=2,
    )

    # Get your crew to work!
    result = crew.kickoff()

    print("######################")
    print(result)


if __name__ == "__main__":
    run_crew()
