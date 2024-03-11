# Fluxograma das atividades desevolvidas neste Case Técnico


<div align="right">
  <img src="/fluxograma.jpg" alt="Your Logo" width="800">
</div>

## O problema a ser resolvido:

Espera-se que o candidato consiga extrair uma amostra de tamanho 3-5 minutos de um vídeo de curso da Hotmart para extrair a descrição em português traduzi-lá para inglês e gerar uma voz sintética falando em inglês do mesmo vídeo. E ao fim, apresente um vídeo com o áudio gerado pela IA (Inteligência artificial)

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
Para a criação da voz foi utilizado o auxilio do `HuggingFace` famoso por criar bibliotecas em linguagem python para resolução de divervos probleas de `Text-To-Text`, `Text-to-Speech`, `Speech-To-Text`, dentre outros. A biblioteca utilizada para esta tarefa foi a `transformers` e o modelo considerado foi um apresentado pela Microsoft, que apresenta uma voz feminina para a resolução do teste. É importante ressaltar que pode-se considerar outras vozes também para a execução desta tarefa, assim como a clonagem da voz utilizando os modelos RVC, no entanto, não teve-se tempo suficiente para realizar essa tarefa de clonagem da voz.

### Amostragem final com voz em inglês:
Com a voz criada com o texto que foi traduzido para o ingles, foi realizado ao fim a inclusão desta voz, e optou-se por remover a voz em português e deixar apenas a voz em inglês realizando a fala. Este vídeo final encontra-se em `video_final.mp4`

# Visão geral:

Foi proposto uma metolologia e modelos bem utilizados no mercado no que se refere as novas aplicações atuais, apesar de utilizar modelos open-source, teve-se o desafio de fragamentação para melhorar a qualidade da trancrição-tradução, geração do áudio e video final. É importante ressaltar, que apesar de modernos essas ferramentas open-source apresentam algumas anomalias na execução de algumas partes, como por exemplo, repetição de frase ou pular partes da tradução. Apesar destes contrtempos, o video final apresentou-se um ótimo protótipo para geração de voz para os vídeos presentes nos cursos da Hotmart. Com o tempo necessário e estudo mais profundo, prova-se com os resultados apresentados aqui que essa metodologia apresentada aqui tem potencial para ser melhorada no futuro!


**

## Business and Technical requirements (Main task)

- [x] Presented an application capable of searching for species by their vernacular name and scientific name.
- [x] Presented the count of species that were observed
- [x] Included a visualization of a timeline when selected species were observed
- [x] Implemented the App using shinyModules
- [x] Unit tests have been added for the most important functions and cover edge cases
- [x] Deploy the BioApp to shinyapps.io (see, https://gx1jfd-caio-balieiro.shinyapps.io/BioApp/)
      
## Extra - Beautiful UI and Infrastructure skill skill

- [x] Beautiful UI Skill was made available using the help of the `fresh` library, available on `CRAN`
      

# Instructions for New Developers

If you are a new developer contributing to this project, follow these steps to set up your development environment:

### Prerequisites

- R installed on your machine. You can download it from [CRAN](https://cran.r-project.org/).

-  Download RStudio: Visit the [RStudio download page](https://www.rstudio.com/products/rstudio/download/).
   - Choose the appropriate version for your operating system (Windows, macOS, or Linux).
   - Download and run the installer.

### Clone the Repository

```bash
git clone https://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@github.com/caiogbb/Appsilon_test.git
```

# Application infrastructure

## ETL process

The data corresponding to this application contains information from the entire planet Earth, which corresponds to 22GB. Processing this data on a local machine is impractical.

Therefore, to process this dataset `Spark` was used, the codes with the application in R are found in `ETL`. In summary, the data is being loaded with the help of the `sparklyr` package, after loading the data considering some jobs, a filter was carried out to select only species located in Poland. After this process, the filtered dataset was saved in CSV to be consumed by the App, resulting in a size of approximately 25MB.

## Main Functions

The core functionality of the app is driven by two main functions defined in the `example.R` script:

#### `mapa_function`

The `mapa_function` is responsible for constructing a map of species based on latitude and longitude information. It utilizes the `leaflet` library to create interactive and visually appealing maps.

#### `time_series_function`

The `time_series_function` is used to generate time series plots of species observation events over time. It relies on the plotly library to create dynamic and interactive time series graphs.

## Shiny Modules

To facilitate the creation of the application, modularization of the application was considered, with the aim of fixing future bugs more quickly

#### `filterModuleUI` and `filterModule`

The `filterModuleUI` and 'filterModule' are responsible for creating buttons and interacting data with the application, generating eventReactive and action buttons to make viewing more pleasant with just a few clicks on the screen.

#### `mapModuleUI`, `mapModule`, `timeSeriesModuleUI` and `timeSeriesModule`

The `mapModuleUI`, `mapModule`, `timeSeriesModuleUI` and `timeSeriesModule` are responsible for making the app's buttons come to life, making the user consider viewing the species' location map and the time series of events presented for those species

#### `speciesCountModuleUI` and`speciesCountModule`

The `speciesCountModuleUI`, `speciesCountModule` are responsible for calculating the number of observations that a given species was presented in the dataset

## Unit test

A unit test was performed to investigate whether the `mapa_function` and `time_series_function` functions are working correctly. This test can be found in `tests/unit_test.R`

# Comments about `app.R`

- It presents a structure considering the Shinydashboard, however, with the help of the fresh package, the entire Beautiful UI was modified to an interface different from the standard presented by Shinydashboard.

- The main page does not remain blank for users, it was considered including a description together with an instruction on how the application should be used, and the explanation will be maintained during the use of the app to facilitate learning.

- Remember the application is deployed in the AWS cloud, that is, it is in production, any change in the `app.R` and `examples.R` and `example-Module.R` codes directly affects the deployment of the Model.

- If you have any questions about the model's infrastructure, please contact me via my personal email: cbalieiro39@gmail.com




