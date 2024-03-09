from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
from datasets import load_dataset
import sentencepiece as spm
import librosa
import os

def combined_text_pt(num_parts):
    
    text_combinado = None

    # Loop sobre os arquivos de áudio
    for i in range(num_parts):
        # Carregue o arquivo de áudio
        
        with open(f"texto_pt/text_transcription_part{i+1}.txt", "r") as file:
            text = file.read()
        # Se o áudio combinado ainda não foi inicializado, inicialize-o com o primeiro áudio
        if text_combinado is None:
            text_combinado = text
        else:
            # Adicione o áudio atual ao áudio combinado
            text_combinado += text + " "

    # Salve o arquivo combinado
    with open(f"texto_pt.txt", "w") as file:
            file.write(text_combinado)

def combined_text_en(num_parts):
    
    text_combinado = None

    # Loop sobre os arquivos de áudio
    for i in range(num_parts):
        # Carregue o arquivo de áudio
        
        with open(f"traduzido_en/text_traduzido_part{i+1}.txt", "r") as file:
            text = file.read()
        # Se o áudio combinado ainda não foi inicializado, inicialize-o com o primeiro áudio
        if text_combinado is None:
            text_combinado = text
        else:
            # Adicione o áudio atual ao áudio combinado
            text_combinado += text + " "

    # Salve o arquivo combinado
    with open(f"texto_traduzido.txt", "w") as file:
            file.write(text_combinado)

def model_generate_voice(num_parts):

    processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
    model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
    vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
    
    
    for i in range(num_parts):
        
        with open(f"traduzido_en/text_traduzido_part{i+1}.txt", "r") as file:
            text_en = file.read()    
    

        inputs = processor(text=text_en, return_tensors="pt")

        # load xvector containing speaker's voice characteristics from a dataset
        embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
        speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

        speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

        sf.write(f"ia_audio/audio_part{i+1}.wav", speech.numpy(), samplerate=16000)
        
        
