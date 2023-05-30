from jinja2 import Template
from bs4 import BeautifulSoup
import imgkit

def screenshot_reddit_post(id, post):
    with open("./templates/post.html", "r") as file:
        template_content = file.read()

        # Replace the placeholder with the comment body
        html_template = Template(template_content)
        rendered_html = html_template.render(
            post_title=post["title"], author=post["author"], date=post["date"], subreddit=post["subreddit"])
        
        # Create a BeautifulSoup instance to parse the HTML string
        soup = BeautifulSoup(rendered_html, 'html.parser')

        # Find the target node by ID
        target_node = soup.find(id="post")

        # Create a new HTML document containing only the target node
        new_html = str(target_node)

         # Convert the HTML to an image using imgkit
        imgkit.from_string(new_html, f"./Screenshots/{id}.png", css="./templates/post.css", options={
            'format': 'png',
            'crop-w': '450'
        })


def screenshot_reddit_comment(id, comment):
    with open("./templates/comment.html", "r") as file:
        template_content = file.read()

        # print(type(comment_element.decode()))

        # # Replace the placeholder with the comment body
        html_template = Template(template_content)
        rendered_html = html_template.render(
            comment_body=comment["body"], author=comment["author"], date=comment["date"])
    
        # Create a BeautifulSoup instance to parse the HTML string
        soup = BeautifulSoup(rendered_html, 'html.parser')

        # Find the target node by ID
        target_node = soup.find(id="comment")

        # Create a new HTML document containing only the target node
        new_html = str(target_node)

         # Convert the HTML to an image using imgkit
        imgkit.from_string(new_html, f"./Screenshots/{id}.png", css="./templates/comment.css", options={
            'format': 'png',
            'crop-w': '450'
        })
