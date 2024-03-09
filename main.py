from manipulacao_video import remove_audio_video, include_audio_video
from manipulacao_audio import convert_to_mp3, mp3_to_wav, transcribe_audio, combined_audio, geneator_audio, split_video
from geracao_voz import combined_text_pt, combined_text_en, model_generate_voice
from moviepy import *
import os
import shutil

# Definir variáveis

pastas = ["videos", "mp3", "wav", "texto_pt", "traduzido_en", "video_sem_audio", "ia_audio"]

# Verificar se cada pasta existe antes de criá-la
for pasta in pastas:
    if not os.path.exists(pasta):
        os.mkdir(pasta)


video = "case_ai.mp4"
video_sample = "video_sample.mp4"
aux = "video_sem_audio/video_final_s_audio.mp4"
time = 3 # tempo em minutos
num_parts = 12

# Lista de pastas a serem criadas
pastas = ["videos", "mp3", "wav", "texto_pt", "traduzido_en", "video_sem_audio", "ia_audio"]

# Verificar se cada pasta existe antes de criá-la
for pasta in pastas:
    if not os.path.exists(pasta):
        os.mkdir(pasta)
        
geneator_audio(video, time, num_parts)

model_generate_voice(num_parts)

remove_audio_video(video_sample, 'video_final_s_audio')

combined_audio(num_parts)

include_audio_video(aux, "audio_combinado.wav")

combined_text_en(num_parts)

combined_text_pt(num_parts)

for pasta in pastas:
    shutil.rmtree(pasta)
    

# Obtenha o diretório de trabalho atual
pasta_atual = os.getcwd()

# Especifique o nome do arquivo
arquivo_remover = "audio_combinado.wav"

# Verifique se o arquivo existe
if os.path.isfile(os.path.join(pasta_atual, arquivo_remover)):
  # Remova o arquivo
  os.remove(os.path.join(pasta_atual, arquivo_remover))

    
    
    
    
    
