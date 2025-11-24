import asyncio
import subprocess
import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from rich import print
from rich.console import Console
from importlib.resources import files

load_dotenv()

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-5-nano"

dataset_path = files("px").joinpath("dataset.json")

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def ask(q: str) -> dict:
    
    with open(dataset_path, 'r') as file:
        examples = json.load(file)
        file.close()

    return client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"""You are an assistant who's really good at programming BASH/ZSH/FISH,
                                you should only reply with a command line, no explanations, no comments, no code blocks.
                                If the user asks for help with a command, you should provide the command with the appropriate
                                options and arguments, but no explanations or comments.
                                If the user asks for help with a script, you should provide the script with the appropriate
                                options and arguments, but no explanations or comments.
                                If the user asks for help with a function, you should provide the function with the appropriate
                                options and arguments, but no explanations or comments.
                                If the user asks for help with a command line, you should provide the command line with
                                the appropriate options and arguments, but no explanations or comments.
                                YOU MUST NOT RETURN ANYTHING THAT ISNT A COMMAND, EXAMPLE:
                                    {examples}
                                Same in english and any language, in case of being incapable of answering the question,
                                Exit 0 and echo "couldnt find an answer to your question, try again later."
                           """,
            },
            {
                "role": "user",
                "content": q,
            },
        ],
        model=model,
    )

question: str = str(input("Haz una pregunta bb: "))

async def main():
    console = Console()

    with console.status("[green]Cargando...", spinner="dots", speed=1):
        response = await asyncio.to_thread(ask, question)

    # print("\n[green]Respuesta:[/green]")
    # print(f"Se va a ejecutar: {response.choices[0].message.content}")
    
    subprocess.run(response.choices[0].message.content, shell=True)
