from vertexai.preview.language_models import TextGenerationModel

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


def interview(temperature: float = 0.2):
    """Ideation example with a Large Language Model"""

    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": temperature,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40,
    }

    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
        # prompt = "Give me ten interview questions for the role of program manager.",
        prompt="Summarize this:" + meeting_transcript,
        **parameters,
    )
    print(f"Response from Model: {response.text}")


interview()
