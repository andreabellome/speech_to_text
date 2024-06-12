# Speech-to-text using Artificial Intelligence

This repository contains a simple speech-to-text script using [OpenAI whisper](https://github.com/openai/whisper) models that can run locally.

## Installation

To work with the repository, one can simply clone it in the local machine:

```bash
git clone "https://github.com/andreabellome/speech_to_text"
```

If one wants to specify a specific target directory (should be empty):

```bash
git clone "https://github.com/andreabellome/speech_to_text" /path/to/your/target/directory
```

where `/path/to/your/target/directory` should be replaced with the desired local taregt directory.

The requirements are listed below:

- The toolbox requires [Python](https://www.python.org/downloads/) version 3.10 or above.

- The tool requires [ffmpeg](https://ffmpeg.org/), that can be downloaded using [chocolatey](https://chocolatey.org/) using administrator shell ```choco install ffmpeg```.

- One should run in a terminal ```pip install -r requirements.txt``` to install all the required libraries specified in the file [requirements.txt](requirements.txt).

- To run medium and large [whisper](https://github.com/openai/whisper) models, one should have at least 2 GB on the hard disk. Please check the documentation.

- (Optional) To run the model on the local GPU, if available, you need to install [CUDA](https://developer.nvidia.com/cuda-downloads). Use the script joudiciously.

- (Optional) To integrate [ollama](https://ollama.com/) models to do other operations on the text (e.g., summarize, ask information,...) one could also install [ollama llama3](https://ollama.com/). To integrate ollama, before starting the script run ```ollama serve```. Please check [audioTranscriber](audioTranscriber.py) to see how ollama can be integrated.

## License

The work is under license [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc/4.0/), that is an Attribution Non-Commercial license. One can find the specifics in the [LICENSE](/LICENSE) file.

Only invited developers can contribute to the repository.

## Usage

A Python class is defined [audioTranscriber](audioTranscriber.py) that allows to transcribe files and save them either to .txt or .docx files (if not present, these are automatically created). Please, check the [audioTranscriber](audioTranscriber.py) class that should be self-explanatory.

A [main](main.py) file is used with the following lines:

```python
# Import required libraries
from audioTranscriber import AudioTranscriber

# Initialize the transcriber
transcriber = AudioTranscriber( model_name="large-v2" )
```

The ```model_name``` is important. Please check [whisper](https://github.com/openai/whisper). Other options can be ```small``` or ```medium```.

Then, one can start the transcription of an audio file and save it to a .txt:

```python
# Transcribe the large audio file
result = transcriber.transcribe_large_file("audio1.m4a")

# Save the transcription to a text file
filename1 = 'transcription.txt'
transcriber.save_to_txt(result, filename1)
```

Happy coding!
