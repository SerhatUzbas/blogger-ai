from textwrap import dedent
import requests
from bs4 import BeautifulSoup
import os
from crewai import Agent, Task
from crewai_tools import tool
from langchain.llms import Ollama


class BrowserTools:

    @tool("Scrape website content")
    def scrape_and_summarize_website(url: str) -> str:
        """Useful to scrape and summarize a website content, just pass a string with
        only the full url, no need for a final slash `/`, eg: https://google.com or https://clearbit.com/about-us
        """

        response = requests.get(url)
        if response.status_code != 200:
            return f"Error: Unable to access the website (status code: {response.status_code})"

        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all("p")
        content = "\n\n".join([p.get_text() for p in paragraphs])

        # Split content into chunks of 8000 characters
        content_chunks = [content[i : i + 8000] for i in range(0, len(content), 8000)]
        summaries = []

        for chunk in content_chunks:
            agent = Agent(
                role="Principal Researcher",
                goal="Do amazing researches and summaries based on the content you are working with",
                backstory="You're a Principal Researcher at a big company and you need to do a research about a given topic.",
                llm=Ollama(model="llama3"),
                allow_delegation=False,
            )
            task = Task(
                agent=agent,
                description=f"Analyze and make a LONG summary of the content below, make sure to include ALL relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}",
                expected_output=dedent(
                    """\
                Detailed analysis of the product.
                """
                ),
            )
            summary = task.execute()
            summaries.append(summary)

        combined_summary = "\n\n".join(summaries)
        return f"\nScraped Content: {combined_summary}\n"
