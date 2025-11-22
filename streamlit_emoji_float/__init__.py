import streamlit as st

out = st.components.v2.component(
    "streamlit-emoji-float.emoji-float",
    js="index-*.js",
    html='<div class="react-root"></div>',
)


def emoji_float(emojis=["⭐", "😊", "🎈"], count=10, key=None):
    component_value = out(
        key=key,
        data={
            "emojis": emojis,
            "count": count,
        },
    )
    return component_value
