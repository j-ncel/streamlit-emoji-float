import streamlit as st
from streamlit_emoji_float import emoji_float

st.set_page_config(page_title="Streamlit Emoji Float Demo", page_icon="🎈", layout="centered")

st.markdown("## streamlit-emoji-float demo 🎈")

emoji_text = st.text_area(
    "Write your emojis here",
    "🎈⭐🤩😍🍔🏀"
)
emojis = list(emoji_text.strip())


st.write("Play with the settings below and press the button to see emojis float.")
col1, col2 = st.columns(2)
with col1:
    count = st.number_input("Number of emojis", min_value=10, max_value=100, value=30, step=5)
    animation_length = st.number_input("Animation Length", min_value=3, value=3, step=1)
with col2:
    min_size = st.number_input("Minimum size", min_value=20, value=50, step=5)
    max_size = st.number_input("Maximum size", min_value=min_size+5, value=100, step=5)


if st.button("Float Emojis"):
    st.session_state["float_trigger"] = st.session_state.get("float_trigger", 0) + 1
    emoji_float(
        emojis=emojis,
        count=count,
        minSize=min_size,
        maxSize=max_size,
        animationLength=animation_length,
        key=f"demo-{st.session_state['float_trigger']}",
    )
