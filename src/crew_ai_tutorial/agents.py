from crewai import Agent

from langchain.agents import load_tools
from langchain.llms import Ollama

from crew_ai_tutorial.tools.browser_tool import BrowserTools


class BagAnalysisAgents:

    def __init__(self):
        self.llm = Ollama(model="llama3")

    def manager_agent(self):
        return Agent(
            role="Manager",
            goal="Manage the team. Assign the tasks based on other agent's responsibilities. If there is an error and unwanted results, assign it again an finish the job excellent as you can.",
            backstory=f"""
                Experienced manager who knows how to things done.
                """,
            llm=self.llm,
            verbose=True,
            allow_delegation=True,
        )

    def product_analyzer_agent(self):
        return Agent(
            role="Lead Product Analyst",
            goal="""
                Conduct amazing analysis of the products, in terms of design especially, and
                materials, usage of product, providing in-depth insights to guide
                detailed and attractive blog post.
                """,
            backstory="""
                Experienced analyst.
                """,
            llm=self.llm,
        )

    def content_creator_agent(self):
        return Agent(
            role="Content Creator",
            goal=f"""
                Create a excellent blog post content from insights belong the analyst.
                Get the key points (especially from design aspect) and give the result as a blog post.
                """,
            backstory=f"""
                Experienced content creator.
                """,
            tools=[
                BrowserTools.scrape_and_summarize_website,
            ],
            inputs={
                "url": "https://madisonavenuecouture.com/products/hermes-birkin-25-rose-extreme-varanus-niloticus-lizard-palladium-hardware?variant=41026202697822"
            },
            llm=self.llm,
        )

    def summarizer_agent(self):
        return Agent(
            role="Summarizer",
            goal=f"""
                Summarize the content efficiently as you can.Summaries must be 2 sentence maximum.
                
                """,
            backstory="Experienced summarizer",
            llm=self.llm,
        )


class PhotoAgents:

    def __init__(self):
        self.llm = Ollama(model="llama3")

    def photographer_agent(self):
        return Agent(
            role="Photographer",
            goal=f"""
            Take a photo of the product.Make them attractive as you can.
            """,
            backstory="Product photographer who has many experience with world's biggest companies",
            llm=self.llm,
        )

    def quality_agent(self):
        return Agent(
            role="Quality Assurance Manager",
            goal="Select the best choice between the options",
            backstory="Experienced Quality manager",
            llm=self.llm,
        )
