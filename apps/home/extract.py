import ffmpeg

def extract_audio(input_file):
    input_webm_file = input_file 
    output_audio_file = "C:/Users/sumit/Summarizer/media/new_audio/output.mp3"  
    ffmpeg.input(input_file).output(output_audio_file, format='mp3').run(overwrite_output=True)
    print("Audio extraction completed successfully.")
