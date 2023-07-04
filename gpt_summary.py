import openai

openai.api_key = "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"

meeting_transcript = """Good morning, everyone. Let's begin the ABC meeting.",
        "I hope everyone had a productive week. Nisha, can you provide your inputs.",
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

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            # "content": f"Assign tasks for developers: {meeting_transcript}",
            # "content": f"Summarize this: {meeting_transcript}",
            # "content": f"Take aways from the meeting: {meeting_transcript}",
            # "content": f"What is the tone of the meeting: {meeting_transcript}",
            # "content": f"can you mask the confidential info: {meeting_transcript}",
            "content": f"get intent of the text: {meeting_transcript}",
        },
    ],
)
page_summary = response["choices"][0]["message"]["content"]

print(page_summary)
