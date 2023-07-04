import requests
import openai
from transformers import pipeline
from google.cloud import storage

storage_client = storage.Client()

openai.api_key = "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"

bucket_name = "transcript_poc"
file_path = "input_transcriptrandom_transcript.txt"

bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(file_path)
meeting_transcript = blob.download_as_text()

summarizer = pipeline("summarization")

summary = summarizer(
    meeting_transcript, max_length=150, min_length=30, do_sample=False
)[0]["summary_text"]


chatgpt_response = openai.Completion.create(
    engine="text-davinci-003",  # Choose the appropriate ChatGPT or GenAI model
    prompt=summary,  # Use the generated summary as the prompt
    max_tokens=50,  # Adjust the max tokens as per your requirements
)

chatgpt_answer = chatgpt_response.choices[0].text.strip()


meeting_transcript = """Good morning, everyone. Let's begin the meeting.",
        "I hope everyone had a productive week.",
        "Absolutely, I made some progress on the project we discussed last time.",
        "That's great to hear. I'm looking forward to your update.",
        "I've completed the initial research and compiled a list of potential solutions.",
        "Excellent work. I appreciate your thoroughness.",
        "Have you considered the budget implications of the proposed solutions?",
        "Yes, I've taken the budget into account and identified cost-effective options.",
        "I have a few suggestions regarding implementation. Can we discuss those?",
        "Certainly, let's hear your ideas.",
        "I believe incorporating agile methodologies would streamline the development process and improve collaboration.",
        "I agree, agile practices have proven to be effective in similar projects.",
        "Thank you, everyone, for your valuable inputs. Let's summarize the action items and assign responsibilities.",
        "Meeting adjourned."""
conversation_history = [meeting_transcript]
api_key = "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"

while True:
    response = requests.post(
        "https://api.openai.com/v1/playground/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "text-davinci-003",  # Choose the appropriate GenAI model
            "prompt": "\n".join(
                conversation_history
            ),  # Use the conversation history as the prompt
            "max_tokens": 50,  # Adjust the max tokens as per your requirements
        },
    )

    response_json = response.json()
    if "choices" in response_json:
        genai_answer = response_json["choices"][0]["text"].strip()
    else:
        genai_answer = response_json["error"]

    print("GenAI Response:", genai_answer)
