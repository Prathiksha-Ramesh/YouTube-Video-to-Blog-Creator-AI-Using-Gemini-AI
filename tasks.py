from crewai import tasks
from tools import tool
from agents import blog_researcher,blog_writer

## research task:

research_task=Task(
    description=(
        'Identify the video {topic}'
        'get detailed information about the video from the channel'
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content'
    tools=[tool],
    agent=blog_researcher
)

#writer task

writer_task=Task(
    description=(
        'get the info from the youtube channel on the topic{topic}'
        
    ),
    expected_output='summarize the info from the youtube channel video on the topic {topic} and create the content for the blog '
    tools=[tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new_blog_post.md'
)