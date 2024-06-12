import whisper
from pydub import AudioSegment
import os
import torch
import tqdm
from docx import Document
import requests

class AudioTranscriber:
    """
    A class to transcribe large audio files and summarize text using Whisper and LLaMA3 models.

    Attributes:
        device (str): The device to use for model inference ("cuda" for GPU if available, otherwise "cpu").
        model (whisper.Whisper): The Whisper model for transcription.
    """

    def __init__(self, model_name="large-v2", device=None):
        """
        Initializes the AudioTranscriber with the specified model and device.

        Args:
            model_name (str): The name of the Whisper model to load.
            device (str, optional): The device to use for model inference. Defaults to None, which auto-selects "cuda" if available.
        """
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model = whisper.load_model(model_name).to(self.device)
        print(f"Using device: {self.device}")

    def transcribe_large_file(self, audio_path, language="it", chunk_size=10*60*1000):
        """
        Transcribes a large audio file by splitting it into smaller chunks.

        Args:
            audio_path (str): The path to the audio file.
            language (str): The language code for transcription. Defaults to "it" (Italian).
            chunk_size (int): The size of each audio chunk in milliseconds. Defaults to 10 minutes.

        Returns:
            str: The transcribed text of the entire audio file.
        """
        audio = AudioSegment.from_file(audio_path)
        chunks = [audio[i:i+chunk_size] for i in range(0, len(audio), chunk_size)]
        transcription = ""

        for i, chunk in enumerate(tqdm.tqdm(chunks, desc="Transcribing", unit="chunk")):
            chunk_path = f"temp_chunk_{i}.wav"
            chunk.export(chunk_path, format="wav")
            result = self.model.transcribe(chunk_path, language=language)
            transcription += result["text"] + " "
            os.remove(chunk_path)

        return transcription

    @staticmethod
    def save_to_txt(text, filename):
        """
        Saves text to a .txt file.

        Args:
            text (str): The text to save.
            filename (str): The name of the .txt file.
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)

    @staticmethod
    def save_to_docx(text, filename):
        """
        Saves text to a .docx file.

        Args:
            text (str): The text to save.
            filename (str): The name of the .docx file.
        """
        doc = Document()
        doc.add_paragraph(text)
        doc.save(filename)

    @staticmethod
    def summarize_text_llama3(fileToSummarize, system_prompt='Your goal is to summarize the text given to you. It is from a meeting between one or more people. Only output the summary without any additional text. Focus on providing a summary in freeform text with what people said and the action items coming out of it. Summarize the text also using bullet points.'):
        """
        Summarizes the text in a file using the LLaMA3 model via an API.

        Args:
            fileToSummarize (str): The path to the file to summarize.
            system_prompt (str): The prompt to guide the summarization. Defaults to a predefined prompt for meeting summaries.

        Returns:
            str: The summarized text.
        """
        OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"

        # Read the contents of the file to summarize
        with open(fileToSummarize, "r", encoding="utf-8") as file:
            file_content = file.read()

        OLLAMA_PROMPT = f"{system_prompt}: {file_content}"
        OLLAMA_DATA = {
            "model": "llama3",
            "prompt": OLLAMA_PROMPT,
            "stream": False,
            "keep_alive": "1m",
        }
        response = requests.post(OLLAMA_ENDPOINT, json=OLLAMA_DATA)

        response_text = response.json()["response"]

        return response_text
