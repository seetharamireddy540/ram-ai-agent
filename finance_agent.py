
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

# Load environment variables from .env file
load_dotenv()

print("Hello World")

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
health_agent = Agent(
    name="Health Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    role= "You are a health expert. You are an expert in medical research and analysis. You are able to analyze medical research papers and provide insights. You are also able to provide medical advice based on the latest research. You are also able to provide medical advice based on the symptoms provided by the user. You are also able to provide medical advice based on the medical history provided by the user. You are also able to provide medical advice based on the medical tests provided by the user. Answer if the questions is health related otherwise simply say that you don't know",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
agent_team = Agent(
    team=[health_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent.print_response("How is NVDIA stock performing.", stream=True)
