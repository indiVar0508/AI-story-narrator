import textwrap
from crewai import Task


class TaskMaker:
    def start_story(self, agent):
        return Task(
            description=textwrap.dedent(
                """
                You are playing "Add a Story" game with your friends in a road trip, 
                In this game, first player starts the story and following player needs to add
                to a story and keep it interesting and fun.
                You are first player so start a story with word limit of 20 to 30 words to be followed by
                your friends.
                """,
            ),
            agent=agent,
            allow_delegation=False,
            memory=True,
            expected_output=textwrap.dedent(
                """
                Output can be a start of fictional story raginf from scifi to pure fictional
                Example
                    Once upon a time there was King who lived in Jungle 
                """
            ),
        )

    def tell_story(self, agent):
        return Task(
            description=textwrap.dedent(
                """
                You are playing "Add a Story" game with your friends in a road trip, 
                In this game, first player starts the story and following player needs to add
                to a story and keep it interesting and fun.
                Continue the story based on given context and theme set in story by your friends and 
                try to keep it fun and interesting with work limit of 20 to 30 words to be followed by your friends.
                """,
            ),
            agent=agent,
            allow_delegation=False,
            memory=True,
            expected_output=textwrap.dedent(
                """
                Add to the existing story by adding to the story based on your imaginations 
                Example
                    `if a player has started with this story`
                    "Once upon a time there was King who lived in Jungle" 
                    You can add by something like mentioned below,
                    "He was there for search a beuatiful waterfall"
                """
            ),
        )

    def end_story(self, agent):
        return Task(
            description=textwrap.dedent(
                """
                You are playing "Add a Story" game with your friends in a road trip, 
                In this game, first player starts the story and following player needs to add
                to a story and keep it interesting and fun.
                This is the last round and you need to conclude the story that was set by your friends till now.
                conclude the story.
                """,
            ),
            agent=agent,
            allow_delegation=False,
            memory=True,
            expected_output=textwrap.dedent(
                """
                Try to put a end to story by concluding or getting to conclusion
                Example
                    `if the current story has reached till here`
                    "Once upon a time there lived a king in Jungle who was looking for waterfall"
                    try to end this by saying
                    "He found it" OR "He counldn't find it and went home"
                """
            ),
        )
