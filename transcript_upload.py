import random
import string
from google.cloud import storage

storage_client = storage.Client()

def generate_random_transcript(length):
    return ' '.join([''.join(random.choices(string.ascii_letters + string.digits + ' ', k=random.randint(3, 10))) for _ in range(length)])

transcript_length = 100

random_transcript = generate_random_transcript(transcript_length)

file_name = 'random_transcript.txt'
with open(file_name, 'w') as file:
    file.write(random_transcript)

bucket_name = 'transcript_poc'
file_path = 'input_transcript' + file_name

bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(file_path)
blob.upload_from_filename(file_name)

print(f"Transcript uploaded to {bucket_name}/{file_path}")
