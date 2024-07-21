import os
from textwrap import dedent
from crewai import Agent

# from tools.browser_tools import BrowserTools
# from tools.search_tools import SearchTools
from langchain.agents import load_tools
from langchain.llms import Ollama


class AnalysisAgents:
    def __init__(self):
        self.llm = Ollama(model="llama3")

    def product_analyzer_agent(self):
        return Agent(
            role="Lead Product Analyst",
            goal=f"""
                Conduct amazing analysis of the products, in terms of design especially, and
				materials,usage of product, providing in-depth insights to guide
				detailed and attractive blog post.
                """,
        )

    def summarizer_agent(self):
        return Agent(
            role="Summarizer",
            goal=f"""
                Summarize the content
                """,
        )
