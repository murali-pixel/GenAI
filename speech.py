
import os
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import storage

def extract_transcripts(video_path):
    client = speech.SpeechClient()

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    audio = speech.RecognitionAudio(uri=video_path)

    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result()

    transcripts = []
    for result in response.results:
        transcripts.append(result.alternatives[0].transcript)

    return transcripts

def save_transcripts(transcripts, bucket_name, file_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    blob.upload_from_string('\n'.join(transcripts).encode('utf-8'), content_type='text/plain; charset=utf-8')

    

def main():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'murali-pde-f3ac279e4a26.json'

    video_path = 'gs://transcript_download/test.mp4'

    transcripts = extract_transcripts(video_path)

    bucket_name = 'transcript_download'
    file_name = 'transcripts.txt'

    save_transcripts(transcripts, bucket_name, file_name)

if __name__ == '__main__':
    main()