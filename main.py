# Imports
from reddit import get_posts
from screenshot import *
from moviepy.editor import VideoFileClip, CompositeAudioClip, CompositeVideoClip
from video_generation import generateClip


def main():
    posts = get_posts(videos_to_generate=100)

    index = 0

    for post in posts:
        screenshot_reddit_post(post["id"], post)

        # Post data
        id = post['id']
        text = post["title"]

        # Store audio and image clips
        audio_clips =[]
        image_clips = []

        video_clip = VideoFileClip("./subway.mp4")
        audio_clip, image_clip = generateClip(id, text, video_clip)

        audio_clips.append(audio_clip)
        image_clips.append(image_clip)

        end_time = audio_clip.duration

        for comment in post["comments"]:
            screenshot_reddit_comment(comment["id"], comment)
            audio_clip, image_clip = generateClip(comment["id"], comment["body"], video_clip)

            # If duration exceeds video's duration, don't append
            if video_clip.duration < (end_time + audio_clip.duration + 0.75):
                continue
            
            audio_clips.append(audio_clip.set_start(end_time))
            image_clips.append(image_clip.set_start(
                end_time).set_duration(audio_clip.duration + 0.75))
            
            end_time = end_time + audio_clip.duration + 0.75
        
        video_clip = video_clip.subclip(0, end_time)

        audio_final = CompositeAudioClip(
            [*audio_clips])
        video_clip.audio = audio_final

        final_video_file = CompositeVideoClip(
            [video_clip, *image_clips])
        
        final_video_file.write_videofile("./Output/output"+str(index)+".mp4",
                              audio_codec='aac', fps=60, threads=4)
        index = index + 1
        
main()





