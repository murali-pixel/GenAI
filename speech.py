import os
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import storage

import ffmpy
from config import *
from vertexai.preview.language_models import TextGenerationModel
import openai

openai.api_key = "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"


storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)


def clean_and_convert_media(file_name, name_and_ext):
    output_command = ""
    if name_and_ext[-1] in VIDEO_EXTENSIONS:
        output_command = "-f flac -ac 1 -ar 48000 -vn -y"
    elif name_and_ext[-1] in AUDIO_EXTENSIONS:
        output_command = "-ac 1 -ar 48000 -y"
    else:
        # process as video if extension is empty
        output_command = "-f flac -ac 1 -ar 48000 -vn -y"

    fname = os.path.join(ROOT_PATH, file_name)
    nfname = os.path.join(ROOT_PATH, name_and_ext[0] + ".flac")
    try:
        ###TODO: Replace the executable path in your system
        ff = ffmpy.FFmpeg(
            executable=r"/Users/muralikrishnakancheti/Downloads/ffmpeg-6.0",
            inputs={fname: None},
            outputs={nfname: output_command},
        )
    except Exception as e:
        print("ffmpy: ", e)

    try:
        # convert media
        ff.run()
    except Exception as e:
        print(e)
        return False
    finally:
        if os.path.exists(fname):
            os.remove(fname)

    return True


def extract_transcripts(video_path):
    client = speech.SpeechClient()

    config = speech.RecognitionConfig(
        # encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        # sample_rate_hertz=16000,
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
    blob = bucket.blob("transcripts/" + file_name)

    blob.upload_from_string(
        "\n".join(transcripts).encode("utf-8"), content_type="text/plain; charset=utf-8"
    )


def process_media(video_or_audio_file):
    download_blob(video_or_audio_file)
    name_and_ext = video_or_audio_file.split(".")
    if clean_and_convert_media(video_or_audio_file, name_and_ext):
        blob_name = upload_flac_to_gcs(name_and_ext[0])
        transcripts = extract_transcripts("gs://" + BUCKET_NAME + "/" + blob_name)
        print("Transcript for the given file: ", transcripts)
        extract_summary_using_gen_ai_gcp(" ".join(transcripts))
        extract_summary_using_chat_gpt(transcripts)
        save_transcripts(transcripts, BUCKET_NAME, name_and_ext[0] + ".txt")
        print("Transcript file for the given file generated successfully")


def upload_flac_to_gcs(file_name):
    blob = bucket.blob("cleaned_audio/" + file_name + ".flac")
    flac_file = os.path.join(ROOT_PATH, file_name + ".flac")
    blob.upload_from_filename(flac_file)
    print("uploaded cleaned flac file to gcs for media " + file_name)
    os.remove(flac_file)
    return blob.name


def download_blob(video_or_audio_file):
    blob = bucket.blob("media/" + video_or_audio_file)
    blob.download_to_filename(video_or_audio_file)


def extract_summary_using_gen_ai_gcp(meeting_transcript):
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40,
    }

    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
        prompt="Summarize this:" + meeting_transcript,
        **parameters,
    )
    print(f"Response from Model(GCP): {response.text}")
    return response.text


def extract_summary_using_chat_gpt(meeting_transcript):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Summarize this: {meeting_transcript}",
            },
        ],
    )

    page_summary = response["choices"][0]["message"]["content"]
    print("Response from CHAT GPT:", page_summary)
    return page_summary


if __name__ == "__main__":
    video_or_audio_file = "test3.mp4"
    process_media(video_or_audio_file)
