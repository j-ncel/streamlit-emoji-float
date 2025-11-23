import streamlit as st
from streamlit_emoji_float import emoji_float

st.set_page_config(page_title="Streamlit Emoji Float Demo", page_icon="🎈", layout="centered")

st.markdown("## streamlit-emoji-float demo 🎈")

emoji_text = st.text_area(
    "Write your emojis here",
    "🎈⭐🤩😍🍔🏀"
)
emojis = list(emoji_text.strip())

with st.container(border=True):
    st.write("Play with the settings below and press the button to see emojis float.")
    cols = st.columns(2)
    with cols[0]:
        count = st.number_input("Number of emojis", min_value=10, max_value=100, value=30, step=5)
        animation_length = st.number_input("Animation Length", min_value=3, value=3, step=1)
    with cols[1]:
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

with st.container(border=True):
    st.write("Installation & Usage")
    st.code("pip install streamlit-emoji-float", language="bash")
    st.code('''
from streamlit_emoji_float import emoji_float

# Usage with default emojis
emoji_float()

# Usage with custom parameters
emoji_float(
    emojis=["🔥", "🚀", "🎉"],
    count=20,
    minSize=50,
    maxSize=100,
    animationLength=5)
    ''', language="python")
    cols = st.columns(3, width=300)

    with cols[0]:
        st.markdown(
            """
            [![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/j-ncel/streamlit-emoji-float)
            """,
            unsafe_allow_html=True
        )

    with cols[1]:
        st.markdown(
            """
            <a href="https://coff.ee/jncel">
                <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" width="150" alt="Buy Me a Coffee">
            </a>
            """,
            unsafe_allow_html=True
        )
    with cols[2]:
        st.markdown(
            """
            <a href="https://share.streamlit.io/user/j-ncel">
                <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width="40" alt="Streamlit">
            </a>
            """,
            unsafe_allow_html=True
        )
