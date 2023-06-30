from google.cloud import language_v1
from google.cloud import storage
import openai

client = language_v1.LanguageServiceClient()
storage_client = storage.Client()
openai.api_key = ''
bucket_name = 'transcript_poc'
file_name = 'input_transcriptrandom_transcript.txt'

bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(file_name)
text = blob.download_as_text()


document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
response = client.analyze_syntax(request={'document': document})
sentences = [token.text.content for token in response.sentences]

summary = ' '.join(sentences)  
prompt = summary  
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=100  
)
summary = response.choices[0].text.strip()


print("Generated Summary:")
print(summary)
