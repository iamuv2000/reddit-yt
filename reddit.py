# Imports
import praw
import json
import datetime

def convert_timestamp_to_human_readable(timestamp):
    current_time = datetime.datetime.utcnow()
    target_time = datetime.datetime.utcfromtimestamp(timestamp)
    time_difference = current_time - target_time

    # Calculate the time difference in days, hours, and minutes
    days = time_difference.days
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds // 60) % 60

    # Generate the human-readable string
    if days > 0:
        return f"{days} days ago"
    elif hours > 0:
        return f"{hours} hours ago"
    else:
        return f"{minutes} minutes ago"
    

def get_posts(subreddit_name="askreddit", videos_to_generate=3):
    r = praw.Reddit(
        client_id='',
        client_secret='',
        user_agent='u/bot'
    )

    posts_from_subreddit = r.subreddit(subreddit_name).hot(limit=20)

    posts = []

    for post in posts_from_subreddit:

        p = {}

        # Skip if over_18 is true
        if post.over_18:
            continue

        print("Title: " + post.title)

        # Handle comments
        post.comment_sort = "controversial"
        comments = post.comments.list()

        comment_data = []

        for comment in comments:
            # Skip very long comments
            if len(comment.body.split()) > 100:
                continue
                
            # Skip deleted/removed comments
            if (comment.body == "[removed]" or comment.body == "[deleted]"):
                continue
            
            # Comment structure
            c = {}
            c["id"] = comment.id
            c["body"] = comment.body
            c["author"] = comment.author.name
            c["date"] = convert_timestamp_to_human_readable(
                comment.created_utc)

            comment_data.append(c)

            # Limit to 5 comments
            if (len(comment_data) == 10):
                break


        p["id"] = post.id
        p["title"] = post.title
        p["author"] = post.author.name
        p["date"] = convert_timestamp_to_human_readable(
            post.created_utc)
        p["comments"] = comment_data
        p["subreddit"] = subreddit_name
        
        posts.append(p)

        if (len(posts) == videos_to_generate):
            break

    jsonString = json.dumps(posts)
    jsonFile = open("posts.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
    
    return posts
