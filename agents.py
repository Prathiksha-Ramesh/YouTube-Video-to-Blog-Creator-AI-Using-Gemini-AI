from crewai import Agent
from tools import tool

from dotenv import load_dotenv
load_env()

import os
os.environ['OPEN_API_KEY']='NA'   #os.getenv('OPEN_API_KEY')
os.environ['OPENAI_MODEL_NAME']='gpt-4-0125-preview'

#create a senior blog content resercher:
blog_researcher=Agent(
    role='Blog Researcher from youtube videos',
    goal='get the relevant video content for the topic{topic} from yt channel',
    verbose=True,
    memory=True,
    backstory=(
        "expert in understanding the videos in AI data science,machine learning and gen ai and providing suggestions"
    ),
    tools=[tool],
    llm=llm,
    allow_dellegations=True
    
)
#create the blog writer agent:

blog_writer=Agent(
    role='writer',
    goal='narrate compelling tech stories about the video {topic} from yt channel',
    verbose=True,
    backstory=(
        'with a flair for simplyfing complex topics, you craft'
        "engaging narratives that captivate and educate, bringing new"
        'discoveries to light in an accessible manner'

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)


