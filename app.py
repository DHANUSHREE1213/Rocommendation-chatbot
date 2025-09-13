import streamlit as st
import pandas as pd
import random

# Load dataset
df = pd.read_csv(r"C:\Users\Dhanushree\Downloads\kollywood_expanded.csv")

# Streamlit UI
st.set_page_config(page_title="Kollywood Recommender", page_icon="🎬")
st.title("🎬  Movie & TV Show Chatbot")

# Chat history
if "history" not in st.session_state:
    st.session_state["history"] = []

# User input
user_input = st.chat_input("🎥 Lights, camera, action! Ready to discover your next favorite film?")



def get_recommendation(user_text):
    user_text = user_text.lower()

    # Mood based
    if "funny" in user_text or "comedy" in user_text or "light" in user_text:
        recs = df[df["genre"].str.contains("Comedy", case=False)]
    elif "thriller" in user_text:
        recs = df[df["genre"].str.contains("Thriller", case=False)]
    elif "love" in user_text or "love" in user_text:
        recs = df[df["genre"].str.contains("love", case=False)]
    elif "emotional" in user_text:
        recs = df[df["mood"].str.contains("Emotional", case=False)]
    elif "kamal" in user_text:
        recs = df[df["lead_actors"].str.contains("Kamal Haasan", case=False)]
    elif "vijay sethupathi" in user_text:
        recs = df[df["lead_actors"].str.contains("Vijay Sethupathi", case=False)]
    else:
        recs = df

    if len(recs) == 0:
        return "Hmm 🤔 I couldn't find a match. Want me to suggest a random gem?"
    else:
        choice = recs.sample(1).iloc[0]
        return f"I think you’ll enjoy **{choice['title']} ({choice['year']})** 🎥\n\n" \
               f"📝 Genre: {choice['genre']}\n" \
               f"🎭 Mood: {choice['mood']}\n" \
               f"⭐ Cast: {choice['lead_actors']}\n" \
               f"📺 Available on: {choice['platform']}"


# Chatbot flow
if user_input:
    st.session_state["history"].append({"role": "user", "content": user_input})
    response = get_recommendation(user_input)
    st.session_state["history"].append({"role": "assistant", "content": response})

# Display chat history
for chat in st.session_state["history"]:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])
