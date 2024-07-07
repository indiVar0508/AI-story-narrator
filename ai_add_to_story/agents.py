import textwrap
import random
from crewai import Agent


class AgentMaker:
    def __init__(
        self,
        humor=0.3,
        age=22,
        reads_books=False,
        sportsman=False,
        career="UnEmployed",
    ) -> None:
        self.humor = humor
        self.age = age
        self.reads_books = reads_books
        self.sportsman = sportsman
        self.career = career

    def agent(self, llm=None):
        return Agent(
            role="Participant to 'Add to Story' game",
            backstory=textwrap.dedent(
                f"""
                Has a career in {self.career} aged {self.age}, having a humor percentage of about {self.humor}.
                {'is a bookworm who loves to read mystery books but enjoys other books as well, ' if self.reads_books is True else 'does not read books much'}
                {f"enjoys playing {random.choice(['Cricket', 'Football', 'Tennis', 'BasketBall'])}" if self.sportsman is True else 'does not play any sports'}
                Enjoys road trip.
                """
            ),
            goal="Extend to ongoing story in 'Add to story' game, by adding 20-30 words keeping the story interesting.",
            llm=llm,
            allow_delegation=False,
            # max_iter=3,
        )
