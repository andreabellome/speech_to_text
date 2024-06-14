# Import required libraries
from audioTranscriber import AudioTranscriber

# Initialize the transcriber
transcriber = AudioTranscriber( model_name="large-v2" )

# Transcribe the large audio file
result = transcriber.transcribe_large_file("audio1.m4a")

# Save the transcription to a text file
filename1 = 'transcription_model_large_v2.txt'
transcriber.save_to_txt(result, filename1)

# Print the transcription
print( result )

# summarize the result
resultTextSummary = transcriber.summarize_text_llama3( filename1 )

# print the text summary
print(resultTextSummary)

# Save the transcription to a text file
filename3 = 'transcription_model_large_summary.txt'
transcriber.save_to_txt(resultTextSummary, filename3)
