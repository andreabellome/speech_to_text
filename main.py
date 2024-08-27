# Import required libraries
from audioTranscriber import AudioTranscriber

# Initialize the transcriber
transcriber = AudioTranscriber(model_name="large-v2")

# Transcribe the large audio file
result = transcriber.transcribe_large_file("cyber_evol_sal_27_08_2024.m4a")

# Save the transcription to a text file
filename1 = "transcription_model_large_v2.txt"
transcriber.save_to_txt(result, filename1)

# Print the transcription
print(result)

# try to summarize the text extracted from the model using llama
try:

    # summarize the result
    resultTextSummary = transcriber.summarize_text_llama3(filename1)

    # print the text summary
    print(resultTextSummary)

    # Save the transcription to a text file
    filename3 = "transcription_cyber_evol_sal_27_08_2024.txt"
    transcriber.save_to_txt(resultTextSummary, filename3)

except:

    # print the exception raised
    print(
        "Something went wrong with llama model. Please verify the installation and running."
    )
