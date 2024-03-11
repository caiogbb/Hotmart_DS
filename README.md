# Fluxograma das atividades desenvolvidas neste Case Técnico


<div align="right">
  <img src="/fluxograma.jpg" alt="Your Logo" width="800">
</div>

## O problema a ser resolvido:

Espera-se que o candidato consiga extrair uma amostra de tamanho 3-5 minutos de um vídeo de curso da Hotmart para extrair a descrição em português traduzi-lá para inglês e gerar uma voz sintética falando em inglês do mesmo vídeo. E ao fim, apresente um vídeo com o áudio gerado pela IA (Inteligência artificial) utilizando linguagem python.

# Descrição de cada etapa do fluxograma:

### Video case: 
Nesta etapa foi carregado o vídeo contendo aproximadamente 35 min de um curso da Hotmart e preparado para ser pre-processado pelo algoritmo em python.

### Pré-processamento: 
Nesta etapa houve um grande desafio, isto é, pode-se extrair uma amostra de vídeo de tamanho 3-5 minutos de maneira simples no python, no entanto, para os próximos passos seria inviável, pos os modelos de transcrição e tradução só permitiam uma quantidade de tempo de 1 minuto e aproxidamente 700 palavras. Neste sentido, optou-se por fragmentar uma amostra de tamanho 3 minutos (essa amostra encontra-se em: `video_sample.mp4`) em 12 partes, desta forma foi possível realizar as próximas etapas.

### Geração da Transcrição: 
Para esta etapa, foi extraido das 12 partes dos vídeos da etapa anterior os áudios dos vídeos e salvos em mp3, para as próximas etapas decidiu-se converter esses audios para arquivos .wav. Para a parte de extração da transcrição foi extraido as 12 partes de transcrição dos áudios utilizando uma `API`da biblioteca do `SpeechRecognition` em `python` e salvas e ao fim do processo foram combinadados para geração de um único arquivo denominado `text_pt.txt`.

### Geração da tradução:
A tradução dos textos quebrados foram realizadas das 12 transcrições geradas da etapa anterior, como a quantidade de palavras era pequena foi possível utilizar o `Translator` da biblioteca `googletrans` do `python`, assim como na etapa anterior ao final foi gerado um único documento combinando as 12 partes, este documento foi chamado de `texto_traduzido.txt`.

### Criação da Voz:
Para a criação da voz foi utilizou-se o auxilio do `HuggingFace` famoso por criar bibliotecas em linguagem python para resolução de divervos probleas de `Text-To-Text`, `Text-to-Speech`, `Speech-To-Text`, dentre outros. A biblioteca utilizada para esta tarefa foi a `transformers` e o modelo considerado foi um apresentado pela Microsoft, que apresenta uma voz feminina para a resolução do teste. É importante ressaltar que pode-se considerar outras vozes também para a execução desta tarefa, assim como a clonagem da voz utilizando os modelos RVC, no entanto, não teve-se tempo suficiente para realizar essa tarefa de clonagem da voz.

### Amostragem final com voz em inglês:
Com a voz criada com o texto que foi traduzido para o ingles, foi realizado ao fim a inclusão desta voz, e optou-se por remover a voz em português e deixar apenas a voz em inglês realizando a fala. Este vídeo final encontra-se em `video_final.mp4`

# Visão geral:

Foi proposto uma metolologia e modelos bem utilizados no mercado no que se refere as novas aplicações atuais, apesar de utilizar modelos open-source, teve-se o desafio de fragamentação para melhorar a qualidade da trancrição-tradução, geração do áudio e video final. É importante ressaltar, que apesar de modernos essas ferramentas open-source apresentam algumas anomalias na execução de algumas partes, como por exemplo, repetição de frase ou pular partes da tradução. Apesar destes contrtempos, o video final apresentou-se um ótimo protótipo para geração de voz para os vídeos presentes nos cursos da Hotmart. Com o tempo necessário e estudo mais profundo, prova-se com os resultados apresentados aqui que essa metodologia apresentada aqui tem potencial para ser melhorada no futuro!


## O que foi entregue neste protótipo

- [x] Códigos executáveis em python para criação da metodologia de Voice-over.
- [x] Arquivo com a transcrição em português do que foi falado na amostra.
- [x] Arquivo com a tradução em inglês do que foi falado na amostra.
- [x] Video com aproximadamente 3 minutos e 16 segundos (contando o não sincronismo com o vídeo original).
- [x] Um README.md contanto sobre a metodologia e como utilizar este códigos em python
      

# Instrução para uso do protótipo


## Pré-Requisitos

- Python instalado na versão 3.8.10 em ubuntu pode-se utilizar o seguinte comando:

```bash
  sudo apt-get update
  sudo apt-get install python3.9
```
- Em seguida, instale as bibliotecas utilizadas neste protótipo com o seguinte comando em CMD:

```bash
pip install -r requirements.txt
```

# Mão na massa

- Em seguida clone o repositório do meu git com o seguinte comando e extrai a pasta:

```bash
git clone https://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@github.com/caiogbb/Appsilon_test.git](https://github.com/caiogbb/Hotmart_DS.git
```

Ao terminar essa etapa, acrecentre qualquer vídeo mp4 (neste caso adicione o vídeo com 35 minutos enviado neste case na pasta) e execute os comandos dentro da pasta no CMD:

```bash
python3 main.py
```
Ao rodar este comando acima todos a pipeline de geração das partes e arquivos similares ao que foi enviado a este repositório do Github será criado (com exceção de modificações na transcrição, tradução e fala que são gerados pela IA e podem variar)


# Conclusão:

O teste proposto teve bastante desafios e oportunidades de inclusão desta pipeline para tradução de vídeos dentro da plataforma da Hotmart! Será proveitoso a aplicação dessa pipeline e sua melhoria! Aproveitem o protótipo.



# Próximos passos do protótipo

-  Criação de um docker para colocar em teste toda pipeline.
-  Estudar outras estruturas de modelos que podem ser utilizados e comparar as performances.
-  Considerar os códigos para geração de clonagem de voz (Segue um documento `next_steps.txt` com um possível códigos em python para solucionar a clonagem de voz usaando a `API` do `TTS` modelo do `HuggingFace`).
- Estudar a possibilidade de incluir versões testes na plataforma para obtenção de feedbeck dos usuários.
- Extensões para outras linguagem além do inglês: Espanhol, Mandarim, Italiano, dentre outras. 
