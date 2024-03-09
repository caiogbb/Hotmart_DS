from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import speech_recognition as sr
import os
from googletrans import Translator
import moviepy.editor as mpe



def split_video(input_file, output_prefix, num_parts):
        clip = VideoFileClip(input_file)
        duration = clip.duration
        part_duration = duration / num_parts

        for i in range(num_parts):
            start_time = i * part_duration
            end_time = (i + 1) * part_duration

            # Extrair o subclip correspondente
            subclip = clip.subclip(start_time, end_time)

            # Salvar o subclip como um novo arquivo
            output_file = f"{output_prefix}_part{i+1}.mp4"
            subclip.write_videofile(output_file)

        clip.close()


def convert_to_mp3(input_file, output_file):
    # Carregar o vídeo usando o MoviePy
    video_clip = VideoFileClip(input_file)
    
    # Extrair o áudio do vídeo
    audio_clip = video_clip.audio
    
    # Salvar o áudio como um arquivo MP3
    audio_clip.write_audiofile(output_file, codec='mp3')
    
    # Fechar os clips para liberar recursos
    audio_clip.close()
    video_clip.close()


def mp3_to_wav(input_file, output_file):
    # Carregar o arquivo MP3
    audio = AudioSegment.from_mp3(input_file)
    
    # Salvar como WAV
    audio.export(output_file, format="wav")

    
def transcribe_audio(audio_file):
    # Inicializar o reconhecedor
    r = sr.Recognizer()
    
    # Abrir o arquivo de áudio
    with sr.AudioFile(audio_file) as source:
        # Ler o áudio do arquivo
        audio_text = r.record(source)
        
        # Reconhecer o áudio usando a API do Google Speech Recognition
        text = r.recognize_google(audio_text, language='pt-BR')
        
        return text
        

def combined_audio(num_parts):
    
    audio_combinado = None

    # Loop sobre os arquivos de áudio
    for i in range(num_parts):
        # Carregue o arquivo de áudio
        audio = AudioSegment.from_wav(f"ia_audio/audio_part{i+1}.wav")

        # Se o áudio combinado ainda não foi inicializado, inicialize-o com o primeiro áudio
        if audio_combinado is None:
            audio_combinado = audio
        else:
            # Adicione o áudio atual ao áudio combinado
            audio_combinado += audio

    # Salve o arquivo combinado
    audio_combinado.export("audio_combinado.wav", format="wav")
    

def geneator_audio(video, time, num_parts):
    
    # Coletar uma sample do video com o tempo que o usuário definir
    
    video_original = mpe.VideoFileClip("case_ai.mp4")
    duracao_corte = time * 60 # 3 minutos em segundos
    video_sample = video_original.subclip(0, duracao_corte)
    video_sample.write_videofile("video_sample.mp4")
    

    # Chamar a função para dividir o vídeo
    input_file = "video_sample.mp4"
    output_prefix = "videos/video"
    split_video(input_file, output_prefix, num_parts)
    
    # tradutor usando recognition 
    translator = Translator()
    
    
    for i in range(num_parts):
        
        # Converter cada parte do vídeo para MP3
        input_file = f"videos/video_part{i+1}.mp4"
        output_file = f"mp3/audio_part{i+1}.mp3"
        convert_to_mp3(input_file, output_file)
        
        # Converter cada parte do vídeo para wav
        input_file = f"mp3/audio_part{i+1}.mp3"
        output_file = f"wav/audio_part{i+1}.wav"
        mp3_to_wav(input_file, output_file)
        
        audio_file = f"wav/audio_part{i+1}.wav"
        text = transcribe_audio(audio_file)

        # Salvar o texto em um arquivo .txt
        with open(f"texto_pt/text_transcription_part{i+1}.txt", "w") as file:
            file.write(text)

        text_en = translator.translate(text).text

          # Salvar o texto em um arquivo .txt
        with open(f"traduzido_en/text_traduzido_part{i+1}.txt", "w") as file:
            file.write(text_en)

    
    
    
    
    

