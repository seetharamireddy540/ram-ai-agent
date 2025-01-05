
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq


# Load environment variables from .env file
load_dotenv()

print("Hello World")

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)

agent.print_response(
    "What is the capital of France?"
)