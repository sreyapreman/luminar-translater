from pydub import AudioSegment

def split_audio(video_path, audio_path):
    video = AudioSegment.from_file(video_path, format='mp4')
    audio = video.export(audio_path, format='mp3')
audio_file = "C:/Users/sreya/OneDrive/Desktop/luminarapp/LuminarTranslatorApp/videos/audio.mp3"

# Example usage
video_file = "C:/Users/sreya/OneDrive/Desktop/luminarapp/LuminarTranslatorApp/videos/samplevideooo.mp4"

split_audio(video_file, audio_file)
