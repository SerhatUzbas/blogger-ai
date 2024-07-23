from crewai import Agent

from langchain.agents import load_tools
from langchain.llms import Ollama


class AnalysisAgents:
    def __init__(self):
        self.llm = Ollama(model="llama3")

    def manager_agent():
        return Agent(
            role="Manager",
            goal="Manage the team. Assign the tasks based on other agent's responsibilities. If there is an error and unwanted results, assign it again an finish the job excellent as you can.",
        )

    def product_analyzer_agent(self):
        return Agent(
            role="Lead Product Analyst",
            goal=f"""
                Conduct amazing analysis of the products, in terms of design especially, and
				materials,usage of product, providing in-depth insights to guide
				detailed and attractive blog post.
                """,
            backstory=f"""
                Experienced manager who knows how to things done.
                """,
        )

    def summarizer_agent(self):
        return Agent(
            role="Summarizer",
            goal=f"""
                Summarize the content efficiently as you can.
                """,
        )

    def photographer_agent(self):
        return Agent(
            role="Photographer",
            goal=f"""
            Take a photo of the product.Make them attractive as you can.  
            """,
        )
