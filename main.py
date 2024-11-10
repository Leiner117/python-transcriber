import os
import whisper

audio_file_path = 'docu21.mp3'
print(os.path.exists(audio_file_path))
model = whisper.load_model("base")
def transcribe_audio(audio_path):
    try:
        # Verificar si el archivo de audio existe
        if not os.path.exists(audio_path):
            print(f"Archivo de audio no encontrado: {audio_path}")
            return ''

        # Transcribir el audio
        result = model.transcribe(audio_path, fp16=False)
        text = result['text']

        print(f"Audio transcrito: {audio_path}")
        print(f"Texto: {text}")
        return text
    except Exception as e:
        print(f"Error al transcribir el audio {audio_path}: {e}")
        return ''
transcription = transcribe_audio(audio_file_path)
if transcription:
    text_file_path = os.path.splitext(audio_file_path)[0] + '_transcription.txt'

    with open(text_file_path, 'w') as file:
        file.write(transcription)

    print(f"Transcripción guardada en: {text_file_path}")
else:
    print("No se pudo transcribir el audio.")
    