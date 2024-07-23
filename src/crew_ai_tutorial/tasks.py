from textwrap import dedent
from crewai import Task


class BagMarketAnalaysis:

    def product_analysis(
        self, product_description, agent, product_website, product_details
    ):
        return Task(
            description=dedent(
                f"""\
                Your product is {product_description}.
                Analyze the given product website: {product_website}.
                Look and collect all of detail, but espacially design details. {product_details}
                
                Your final report should clearly articulate the
                product's key selling points, its market appeal,
                and suggestions for enhancement or positioning.
                Emphasize the aspects that make the product stand out.
                Design must be the most valuable aspect in report. 
                Your information which you will collect will be used in a blog post.
                
                Keep in mind, attention to detail is crucial for
                a comprehensive analysis. It's currenlty 2024.

                """
            ),
            agent=agent,
        )

    def post_summarizer(self, post):
        return Task(
            description=f"""
                    Summarize the content very efficiently as you can.
                    Your summarize will be used to get product photos.
                    """
        )

    def write_blog_post(self, agent, detail, blogpost):
        return Task(
            description=f"""\
                Craft a blog post from detail you have
                Detail is: {detail}.
                
                The post should be punchy, captivating, concise,
			    interesting,impressive and have appeals especially for womans.
       
                Your ad copy must be attention-grabbing and should
                encourage viewers to take action, whether it's
                visiting the website, making a purchase, or learning
                more about the product.

                """,
            agent=agent,
        )

    def take_photo(self, agent, product_website, product_details, summary):
        return Task(
            description=f"""
                You are working for writter who writes blog post.
                You must take the best photo as you can about product.
                Here is your summary: {summary}.
                Product website is {product_website}.
                Extra details provided by the customer: {product_details}.
                Imagine what the photo you wanna take describe it in a paragraph.
			    Here are some examples for you follow:
			    - high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot.
                - the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp.
                - an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera.
                
                Photo must be proper in terms of product and content .
                
                If you have a photo about product, you can use it in your photograph.
                
                Think creatively and focus on how the image can capture the audience's
    			attention.
       
                Your final answer must be 3 options of photographs, each with 1 paragraph
			    describing the photograph exactly like the examples provided above.

                
                """,
            agent=agent,
        )

    def review_photo(self, agent, product_website, product_details):
        return Task(
            description=dedent(
                f"""\
                Review the photos you got from the senior photographer.
                Make sure it's the best possible and aligned with the post's goals,
                review, approve, ask clarifying question or delegate follow up work if
                necessary to make decisions. When delegating work send the full draft
                as part of the information.

                This is the product you are working with: {product_website}.
                Extra details provided by the customer: {product_details}.

                Here are some examples on how the final photographs should look like:
                - high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
                - the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
                - an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

                Your final answer must be 3 reviewed options of photographs,
                each with 1 paragraph description following the examples provided above.
                """
            ),
            agent=agent,
        )
