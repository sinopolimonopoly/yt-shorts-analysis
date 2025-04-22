import speech_recognition as sr
import os

def transcribe_audio(audio_path, output_transcript_path="data/transcripts/"):

    os.makedirs(output_transcript_path, exist_ok=True)

    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)

        transcript_filename = os.path.basename(audio_path).replace(".wav", ".txt")
        transcript_path = os.path.join(output_transcript_path, transcript_filename)

        with open(transcript_path, 'w') as file:
            file.write(text)

        return text

    except sr.UnknownValueError:
        print("Could not recognize the audio")
    
    except sr.RequestError as e:
        print(f"API unavailable: {e}")

if __name__ == "__main__":
    audio_path = input("Enter the path to the audio file")
    transcript = transcribe_audio(audio_path)
    print(f"Transcript:\n{transcript}")


