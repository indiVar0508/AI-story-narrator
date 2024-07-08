# Ai Story generator

A small project doing a PoC trying to generate a Ai Story narator by deploying 5 [CrewAI](https://www.crewai.com/) agents to build story
by playing "Add to Story" game, Once the story is generated the text is sent to [D-iD](https://www.d-id.com/) application to generate a
Clip narating the story internally leveraging [ElevenLabs](https://elevenlabs.io/) to use for voide audio.

## Setup

To install project in your local you can use poetry or any virtual environment manager of your choice,
I used `poetry` and assume that you have poetry installed

```sh
poetry install
```

Update .env.example for keys for your specific account, In this project for LLM to for CrewAI agents [Google](https://ai.google.dev/aistudio?authuser=1)'s
Gemini-1.0-pro was used but you can use any model of your choice or even ollama deployed locally(refer crewAI's ollama connection section)
Similarly for ElevenLabs and D-ID api key you can generate from your specific account

## Execution

Once your setup is complete you can run the Crew with following command

```sh
poetry run python crew.py
```

## Result

Here is a Demo run result, Story that was generated

```txt
It was his 20th birthday. He was a software engineer and still at his desk. All he wanted to do was go home and
read some Agatha Christie. The last eighty hours had been a blur for him. He'd been on a roll. He'd been coding
all weekend, and he was still only halfway through the project. He knew he needed to take a break, but he
couldn't bring himself to stop. He was so close to finishing, and he didn't want to lose his momentum. As the
sun began to set, casting a warm glow over the desk, he finally reached the end of the code. A sense of
accomplishment washed over him as he hit the compile button. The computer whirred to life, and moments later,
the program ran flawlessly. He couldn't help but smile as he leaned back in his chair, exhausted but satisfied.
His mind raced with possibilities as he contemplated his next project. The world of coding was vast and
ever-evolving, and he couldn't wait to dive deeper into its depths. As the sun dipped below the horizon,
casting hues of gold and crimson across the sky, Ethan's thoughts drifted back to the tales he'd heard during
the road trip. The stories had ignited a spark within him, a yearning to unravel the mysteries of the universe
through the power of code. He knew that his journey was just beginning, and he couldn't wait to see where it
would lead him.
```

Video generated : https://youtu.be/D4QJvdOtZA8
