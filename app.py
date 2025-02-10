import streamlit as st
import subprocess
from config import FINAL_ART_PATH, PROMPTS, get_word_image_path

st.title("Multilingual Word Art Generator")

word = st.selectbox("Choose a word:", ["beautiful", "angry"])
if st.button("Generate Art"):
    # TODO: Replace with your full pipeline logic
    st.write("Generating... (this may take a few minutes)")
    # subprocess.run(["python", "./components/generate_styled_words.py"])
    # subprocess.run(["python", "./components/generate_background.py"])
    # subprocess.run(["python", "./components/assemble_art.py"])
    st.image(FINAL_ART_PATH)
    st.write(" ")
    st.write("intermediate images created:")
    for lang in PROMPTS.keys():
        st.image(get_word_image_path(lang), width=400, use_container_width="auto", caption=f"{lang}")


# Create radio buttons 
# langs = list(PROMPTS.keys())
# picture = st.radio('Select the intermediate image you want to see: ', tuple(langs))
# if picture:
#     st.success(picture)
#     st.image(get_word_image_path(picture), width=400)



# genre = st.radio(
#     "What's your favorite movie genre",
#     [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
#     captions=[
#         "Laugh out loud.",
#         "Get the popcorn.",
#         "Never stop learning.",
#     ],
# )

# if genre == ":rainbow[Comedy]":
#     st.write("You selected comedy.")
# else:
#     st.write("You didn't select comedy.")

