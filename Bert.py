# Importing the transformers library with version 2.2.0
import transformers
from transformers import BertTokenizer, BertModel

# Importing the bert-extractive-summarizer library
from summarizer import Summarizer

import time

body = """Extreme heat is choking continents around the world, with record-setting temperatures expected Tuesday in the United States and several European nations.
Around 63 million people in the U.S. are under heat alerts from Southern California to Miami. A punishing heat wave in southern Europe is also nearing its peak, fueling widespread triple-digit temperatures across Spain, Italy and Greece. Meanwhile, China and other parts of Asia have been baking for weeks on end.
These punishing heat waves, many persisting for long stretches of time, are expected to become a fixture of a warming world. Studies have shown that climate change is making extreme heat events more frequent, more intense and longer lasting.
In the U.S., more heat records are expected to fall this week. Phoenix is on track Tuesday to set a record for the most consecutive days at or above 110 degrees F. The previous record of 18 days was set in 1974, according to the National Weather Service. The city hit 116 F on Monday, which also tied a daily high temperature record set in 2005, according to the Phoenix office of the weather service.
The weekslong heat wave is putting a strain on some hospitals in the area, as patients seek treatment for dehydration, heat exhaustion and other heat-related illnesses.
“It’s kind of the post-Covid problems where we still have nursing shortages, and we still have ancillary staff shortages,” said Dr. Kara Geren, an emergency medicine physician at Valleywise Health in Phoenix. “So, you have fewer staff to focus on emergency patients, and that is definitely putting a strain on the system.”
Geren said she expects her hospital will remain busy in the coming days.
“Temperatures are going to stay up, and people still have to do what they have to do, so I don’t really think anything is going to change in the near future,” she said.

There’s little relief on the horizon for the Southwest. Stifling heat is expected to continue baking the region through the week and will also expand across much of the southern portion of the country.
“Record breaking heat is expected in the Four Corners states, Texas to the Lower Mississippi Valley, and South Florida each day,” the National Weather Service said in its short-range forecast, adding that daily low temperatures will also stay elevated, “allowing for minimal relief from the heat overnight.”
Temperatures in the triple digits are expected across much of Texas. The city of El Paso, nestled against the Mexican border, has sweltered under more than a month straight of temperatures above 100 F and is expected to notch its 33rd day on Tuesday.
In Europe, potential record-breaking high temperatures are expected this week.
Twenty cities in Italy are under red alert heat warnings, and temperatures in some parts of the country could reach 115 to 118 F. Widespread heat alerts are in effect in Spain, where temperatures of 110 F or higher are expected in the Balearic Islands, off the country's east coast.
The heat is exacerbating wildfires on the Continent. Several blazes that broke out near Athens forced thousands of evacuations on Monday, reported The Associated Press."""

def summarize_with_latency():
    # TODO developer - customize the summarizer as needed
    bert_model = Summarizer()

    # Start measuring the time
    start_time = time.time()

    bert_summary = ''.join(bert_model(body, min_length=60))

    # End measuring the time
    end_time = time.time()

    print("BERT Summary:")
    print(bert_summary)

    # Calculate the latency
    latency = end_time - start_time
    print("Latency (seconds):", latency)


summarize_with_latency()
