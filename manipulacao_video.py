from moviepy.editor import VideoFileClip
import os
import moviepy.editor as mpe
from moviepy.editor import VideoFileClip, AudioFileClip

def remove_audio_video(video, save):

    # Carregue os vídeos
    video_1 = VideoFileClip(video)


    # Opcional: Remova o áudio do vídeo concatenado
    video_sem_audio = video_1.set_audio(None)

    # Salve o vídeo concatenado sem áudio
    video_sem_audio.write_videofile(f"video_sem_audio/{save}.mp4", codec="libx264")

    
def include_audio_video(video,audio):
  

    # Carregue o vídeo e o áudio
    video = VideoFileClip(video)
    
    musica = AudioFileClip(audio)
    
    musica = musica.set_start(15)

    # Combine o vídeo e o áudio
    video_com_audio = video.set_audio(musica)

    # Salve o vídeo com o novo áudio
    video_com_audio.write_videofile(f"video_final.mp4", codec="libx264", audio_codec="aac")
    
    

    
    
