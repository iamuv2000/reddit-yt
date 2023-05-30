from gtts import gTTS
from moviepy.editor import *


def generateAudio(text, id):
    language = 'en'
    audioClip = gTTS(text=text, lang=language, tld="us" , slow=False)
    audioClip.save(f"./Voiceovers/{id}.mp3")


# Generate clip [Screenshot + TTS + Video Gameplay]
def generateClip(id, text, video_clip):
    generateAudio(text, id)

    audioClip = AudioFileClip(f"./Voiceovers/{id}.mp3")
    image_clip = ImageClip(f"./Screenshots/{id}.png").set_duration(audioClip.duration)

    margin = 20
    w_video, h_video = video_clip.size
    w_img , h_img = image_clip.size

    width_to_set = w_video - margin
    height_to_set = width_to_set * h_img / w_video

    image_clip = image_clip.resize(
        (width_to_set, height_to_set + 70)).set_pos(("center", "center"))
    
    os.remove(f"./Voiceovers/{id}.mp3")
    os.remove(f"./Screenshots/{id}.png")

    return audioClip, image_clip
