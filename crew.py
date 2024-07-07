import os
import time
import random
import requests
import json
import urllib.request
from ai_add_to_story.tasks import TaskMaker
from ai_add_to_story.agents import AgentMaker
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Crew, Process
from dotenv import load_dotenv


NUMBER_OF_PLAYERS = 5
HUMOR_PERCENTAGE = [10, 20, 50, 30, 70, 99, 90]
AGE = [20, 25, 21, 19, 35, 33, 40, 24]
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro", temperature=0.9)

# Create Agents #
# Player who is going to start the game
player_who_starts = AgentMaker(
    humor=random.choice(HUMOR_PERCENTAGE),
    age=random.choice(AGE),
    reads_books=random.choice([True, False]),
    career=random.choice(
        ["Software Engineer", "Doctor", "Lawyer", "UnEmployed", "Student", "Youtuber"]
    ),
    sportsman=random.choice([True, False]),
).agent(llm=llm)

# Player who is going to end the game
player_who_ends = AgentMaker(
    humor=random.choice(HUMOR_PERCENTAGE),
    age=random.choice(AGE),
    reads_books=random.choice([True, False]),
    career=random.choice(
        ["Software Engineer", "Doctor", "Lawyer", "UnEmployed", "Student", "Youtuber"]
    ),
    sportsman=random.choice([True, False]),
).agent(llm=llm)

remaining_players = [
    AgentMaker(
        humor=random.choice(HUMOR_PERCENTAGE),
        age=random.choice(AGE),
        reads_books=random.choice([True, False]),
        career=random.choice(
            [
                "Software Engineer",
                "Doctor",
                "Lawyer",
                "UnEmployed",
                "Student",
                "Youtuber",
            ]
        ),
        sportsman=random.choice([True, False]),
    ).agent(llm=llm)
    for _ in range(NUMBER_OF_PLAYERS - 2)
]

# Create tasks #
start_story = TaskMaker().start_story(agent=player_who_starts)
end_story = TaskMaker().end_story(agent=player_who_ends)
tell_story = [TaskMaker().tell_story(agent) for agent in remaining_players]

# Setup Crew #
crew = Crew(
    agents=[player_who_starts, *remaining_players, player_who_ends],
    tasks=[start_story, *tell_story, end_story],
    process=Process.sequential,
    verbose=1,
    memory=True,
    embedder={
        "provider": "google",
        "config": {
            "model": "models/embedding-001",
            "task_type": "retrieval_document",
            "title": "Embeddings for Embedchain",
        },
    },
    full_output=True,
)

if __name__ == "__main__":
    result = crew.kickoff()
    # Get the Story
    story = ""
    for i in result["tasks_outputs"]:
        story += i.exported_output + " "
    # story = """As the sun dipped below the horizon, casting an ethereal glow over the rugged landscape, our intrepid travelers embarked on a road trip that would forever etch itself into their memories. As the miles melted away, the conversation flowed effortlessly among us, each voice adding a distinct thread to the tapestry of our adventure. Laughter mingled with the hum of the engine, creating a soundtrack that celebrated the bonds we shared. As the road unfurled before us, like a blank canvas waiting to be filled with our collective experiences, we wove words together, creating a vibrant and ever-changing narrative. The humor that weaved through our stories lightened our hearts, while the shared love of literature deepened our connection, proving that even on the open road, the written word had the power to unite us. As the miles turned into memories, our words painted a rich tapestry of laughter and camaraderie. The absence of books and sports only served to amplify the power of our imaginations, making each twist and turn of the story a testament to the limitless possibilities of the human spirit. As the wheels of our adventure ground to a halt, we stood at the cusp of a new chapter, our story forever etched in the annals of memory. The absence of books and sports had been a catalyst for our creative spirits, igniting a fire that would burn brightly for years to come."""
    print("Story that is generated")
    print(story)
    # Make the AI generated Video
    url = "https://api.d-id.com/talks"

    payload = {
        "script": {
            "type": "text",
            "subtitles": "false",
            "input": story,
            "provider": {
                "type": "elevenlabs",
                "voice_id": "pNInz6obpgDQGcFmaJgB",
            },
        },
        # Giga Chad!!
        "source_url": "https://pbs.twimg.com/profile_images/1752515582665068544/3UsnVSp5_400x400.jpg",
        "config": {"fluent": "false", "pad_audio": "0.0"},
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Basic {os.getenv('D_ID_API_KEY')}",
        "x-api-key-external": json.dumps(
            {"elevenlabs": os.getenv("ELEVEN_LABS_API_KEY")}
        ),
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    task_id = json.loads(response.text)["id"]
    print("Got task ID : ", task_id)
    # Wait for 10 seconds for video to get prep
    print("Waiting for video to be generated...")
    time.sleep(30)
    response = requests.get(f"{url}/{task_id}", headers=headers)
    result_url = json.loads(response.text)["result_url"]
    urllib.request.urlretrieve(result_url, "video.mp4")
    print("Story saved successfully")
