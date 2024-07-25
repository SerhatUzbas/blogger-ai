from crewai import Crew
from crew_ai_tutorial.agents import BagAnalysisAgents, PhotoAgents
from crew_ai_tutorial.tasks import BagMarketAnalysisTasks, PhotoTasks

website = "https://madisonavenuecouture.com/products/hermes-birkin-25-rose-extreme-varanus-niloticus-lizard-palladium-hardware?variant=41026202697822"
details = "This Birkin is in Rose Extreme Varanus Niloticus Lizard leather with palladium hardware and has tonal stitching, front strap, two straps with center toggle closure, clochette with lock and two keys and double rolled handles.The interior is lined with Rose Extreme chevre and has one zip pocket with an Hermes engraved zipper pull and an open pocket on the opposite side."
description = "Very expensive handbag with red color."

# website = input("Bag website?\n")
# details = input("Bag details?\n")
# description = input("Bag description?\n")

bag_analysts = BagAnalysisAgents()
media_creators = PhotoAgents()

manager = bag_analysts.manager_agent()
product_analyzer = bag_analysts.product_analyzer_agent()
content_creator = bag_analysts.content_creator_agent()
summarizer = bag_analysts.summarizer_agent()


analysis_tasks = BagMarketAnalysisTasks()
photo_tasks = PhotoTasks()

manage = analysis_tasks.manage(agent=manager)
product_analysis = analysis_tasks.product_analysis(
    product_description=description,
    agent=product_analyzer,
    product_details=details,
    product_website=website,
)
write_post = analysis_tasks.write_blog_post(agent=content_creator, detail=details)
summarize = analysis_tasks.post_summarizer(agent=summarizer)


analyst_crew = Crew(
    manager_agent=manager,
    agents=[product_analyzer, content_creator, summarizer],
    tasks=[product_analysis, write_post, summarize],
    verbose=True,
)

post = analyst_crew.kickoff()

photographer = media_creators.photographer_agent()
quality_assurance_manager = media_creators.quality_agent()

take_photo = photo_tasks.take_photo(
    agent=photographer,
    summary=post,
    product_details=details,
    product_website=website,
)
review = photo_tasks.review_photo(
    agent=quality_assurance_manager, product_details=details, product_website=website
)


photo_crew = Crew(
    agents=[photographer, quality_assurance_manager],
    tasks=[
        take_photo,
        review,
    ],
    verbose=True,
)


photo = photo_crew.kickoff()

print("----post----")
print("----------------------------------------")
print(post)
print("----------------------------------------")
print("photo")
print("----------------------------------------")
print(photo)
