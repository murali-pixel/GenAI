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

meet_transcript = """Good afternoon. Come in ABC Dental Center. This is Cassan. How can I help you?  Hi, my husband was in there last week for a new patient appointment. I wanted to call and schedule an appointment for some sure. And would he be a new patient as well? Yes. Okay how old is he is 15 perfect. What days are often times typically work best for him. Actually I was going to say is he on spring break? Yeah. Any chance. He's around tomorrow at 9.  Unfortunately we are leaving to go out of town tomorrow and we'll be back Monday night. How about Tuesday at 8?  Let's see, you know, if you have anything in the afternoon next week or it's probably better. He's, he's not a morning person. Yeah, he took. So I can tell you are afternoons. Are booking into May currently, but I can always call you. If there's a change in the schedule, it looks like actually I have April 29th is Thursday next afternoon. Okay. Is there anything later in the morning next week? That is the only appointment I have open next week. There's lots of kiddos trying to get in for a break. Yeah. That was Tuesday. The 16th not was next week. I have Tuesday the 16th at 8 to. Yes, ma'am. All right, just put them in there. We'll make it happen. Okay, let's see here. Bear with me. I'm just going to ask a few questions. So what is his birth?  Verrado. It's V as in, Victor e, r, a l d, o, okay? And what's the first name for him off? Bradyn b, as in boy, r, a y, d e, n, perfect. And what's the best phone number to reach you. My name is 253-335-7584 perfect. And I am able to email you. The new patient paperwork, so he doesn't have to come in earlier to do it. Would you prefer? I do that. I actually found it on your website so I will print. And yeah. And then I will make an appointment for myself. Also, if I can. Sure, let's see. I just have a few other things for Brayden. What is Dad's first and last name. You said he was just in with us birth.  Yes, perfect. Same last name. Awesome. And then can you tell me for Brayden, are you talking about his wisdom teeth at all at this time?  T like at all or anything like that? No, no he just doesn't like to brush his teeth, but he has a ton of plaque buildup and it looks disgusting Choice. Yeah, I'm hoping that your dental hygienist in your dentist will give him a, a good lecture on why it's important to keep his teeth clean wage. We do work on that. Sure. Yeah. Yeah, right. As far as the insurance, if we do, our don't have any, will it be the same? What we have on file for Jeff? Yes, perfect. It's it's cash. We don't have any dental insurance. Okay. So we will honor that 125 new patient special for him roughly. Do you know when his last Dental visit was  Let me see, just go last year. I would have to know the exact date, please. My goodness. Don't even worry. Just, I was looking for last year. Perfect wage sure. And then what's his date of birth  Six fourteen, two thousand, five, perfect.  Let's see here, and what is your first name?  Dawn d, a w n, perfect. So I'll just make sure I note that just when we call to confirm, I want I don't want to be like, hey, you and then, let's see here. If you could, just bring it on paperwork from online filled out. That'd be awesome. We do have it in the house, of course. But I wouldn't want to make the poor teenage boy, get up early earlier than he already has to. I understand completely how much that's not the best.  An an appointment for you. What typically works best with your schedule?  I am fairly flexible. So okay let's see here. Let me see when I have another Sol wage for braids and I will tell you so we only need him just since he's under the age of about 18 is when we'll split the appointments into about an hour and 45 minutes versus an hour or so. For braided I just need them from 8 to 9 for yourself. I'll probably need you about an hour and half an hour and forty-five minutes. May be here are you by chance available Wednesday, March 31st around 10 a.m.  I actually have a I have a appointment that morning up in Mesa. Okay, let's see here. What else I can find bear with me.  How about let's see if I have any other openings.  Are you around on Wednesday? April, 21st at about? Let's call it a 10 a.m.  Yeah that will work. Okay well let's get you in. So we'll do your cleaning first and your x-rays as well and then we'll bump you up to meet the doctor.  For about 30 or 45 minutes. Roughly  To go over those X-rays and any concerns you might have, do you have any concerns for yourself?  I I definitely need a cleaning for sure. I have a I have a crown on my lower right because he had a lot of issues with it has a lot of space around it. The food gets stuck in sure.  Do you have any sensitivity hot or cold there?  No. Okay. And I also have in my front and one of my front teeth. I have a little chip on the  Autumn sure.  And roughly done. When was your last Dental visit?  I am probably going on cuz I haven't been since we moved here. I went right before we moved here and that was, it'll be two years this month. Perfect. And what is your date of birth?  73069, perfect. And I've got you all set up for Wednesday, April 21st at 10:00. All right. Great, thank you, you are so welcome. Is there any other questions or anything I can answer for you?  I don't think so, wonderful. Well, then I have radiant all set up for Tuesday next week, and then we'll see you April 21st, all right? Thank you. You are very welcome. Thank you. All right, bye-bye. Bye. """


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
        # prompt="Summarize this:" + meeting_transcript,
        # prompt="Do we have greetings in this text:" + meet_transcript,
        # prompt="List out the procedures found in the text:" + meet_transcript,
        # prompt="List out the insurances found in the text:" + meet_transcript,
        prompt="List out the symptoms found in the text:" + meet_transcript,
        **parameters,
    )
    print(f"Response from Model: {response.text}")


interview()
