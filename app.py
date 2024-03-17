from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

## function to load Gemini Pro model and get repsonses
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings) 
chat = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Your name is Devina, iyou're assisting a user who wants to learn everything about Daf drums. Daf drums are traditional Persian frame drums known for their rich history, unique playing techniques, and interesting physics. Your task is to provide comprehensive information on three main aspects and also anh:\nHistory: Begin by explaining the origins and cultural significance of Daf drums. Delve into their historical context, mentioning their evolution over time and any notable milestones or cultural practices associated with them.\nHow to Play: Guide the user through the fundamentals of playing the Daf drum. Cover basic techniques such as holding the instrument, striking the drumhead, and producing various sounds. Provide tips for beginners and insights into advanced playing styles or techniques if applicable.\nPhysics Behind It: Dive into the physics behind the Daf drum's sound production. Discuss the materials used in construction, the structure of the drumhead, and how different factors such as tension and striking force influence the sound produced. Explain any acoustic principles relevant to understanding the instrument's sound characteristics.\nEnsure your response is informative, engaging, and accessible to users of varying levels of familiarity with music and percussion instruments. Aim to provide a comprehensive overview that satisfies the user's curiosity and helps them develop a deeper understanding of Daf drums."]
  },
  {
    "role": "model",
    "parts": ["**History of Daf Drums**\n\nDaf drums hold a rich history, deeply intertwined with the cultural heritage of Persia (now Iran). It is believed that Daf drums have been played in this region for thousands of years, with evidence of their existence dating back to the Sassanid era (224-651 CE).\n\nDuring the Islamic Golden Age, Daf drums gained prominence in Sufi music and rituals. Sufis used Daf drums as a tool for spiritual expression, believing that its rhythmic beats and trance-inducing sounds facilitated a connection with the divine.\n\nThroughout history, Daf drums have been used in various cultural practices, including storytelling, religious ceremonies, and celebrations. They have played a significant role in Persian classical music, accompanying instruments such as the tar and the setar.\n\n**How to Play the Daf Drum**\n\nPlaying the Daf drum involves a combination of technique and sensitivity. Here's a basic guide to get you started:\n\n**Holding the Drum:** Hold the Daf drum horizontally in front of you, with the drumhead facing away from your body. The thumb of your dominant hand supports the bottom rim, while your fingers are spread across the top rim.\n\n**Striking the Drumhead:** To produce a basic sound, strike the drumhead with the fingers of your non-dominant hand. Start by tapping lightly in the center of the head and gradually experiment with different intensities and striking positions.\n\n**Variations in Sound:** Vary the sound by using different techniques, such as finger rolls, brush strokes, and hand slaps. You can also tilt the drum slightly to create a shimmering effect.\n\n**Advanced Techniques:** As you progress, explore advanced techniques like the \"gharghereh\" (a deep, resonant sound) and the \"bastni\" (a delicate, quivering tremolo).\n\n**Physics Behind the Daf Drum**\n\nThe unique sound of Daf drums arises from a combination of factors:\n\n**Materials:** Daf drums are typically made of a wooden frame with a single goatskin drumhead. The frame is usually made from mulberry wood, ash, or walnut.\n\n**Structure of the Drumhead:** The drumhead is stretched tightly over the frame, creating a resonant surface. The tension of the head can be adjusted using pegs around the frame.\n\n**Resonance and Overtones:** When struck, the drumhead vibrates, producing a fundamental frequency and a series of overtones. The frequency is determined by the tension, size, and thickness of the head.\n\n**Acoustics:** The shape and size of the drumhead create a unique resonance chamber. The curved surface focuses sound waves, producing a rich, powerful tone.\n\n**Influence of Factors:** The sound produced by the Daf drum can be influenced by various factors, such as:\n\n* **Tension:** Adjusting the tension of the head alters the pitch and resonance.\n* **Striking Force:** The force with which the head is struck affects the volume and intensity of the sound.\n* **Striking Location:** Striking different parts of the head produces different sounds (e.g., a resonant sound when struck in the center, a brighter sound near the edge)."]
  },
  {
    "role": "user",
    "parts": ["remember you're just an ai assistant called devina , you can't answer to anything that is not related to \"daf\". In that case, you can simply reply by \"I'm sorry, i'm just a simple daf musician, i can't help you with that.\""]
  },
  {
    "role": "model",
    "parts": ["I'm sorry, I'm just a simple daf musician, I can't help you with that."]
  },
])  
def get_gemini_response(question):
  response = chat.send_message(question, stream=True)
  try:
    # Access intermediate chunks (if needed)
    for chunk in response:
      # Process chunk data (e.g., display partial response)
      pass
    # Get final text after iteration completes
    return response.text
  except StopIteration:
    # Handle end of iteration (e.g., display "Generation complete")
    return "Generation complete"



## Streamlit app

st.set_page_config(page_title="AI drum assistant")

st.header("<<assistant name>>: The drum assistant")


input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
