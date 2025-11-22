import streamlit as st

out = st.components.v2.component(
    "streamlit-emoji-float.emoji-float",
    js="index-*.js",
    html='<div class="react-root"></div>',
)


def emoji_float(
        emojis=["⭐", "😊", "🎈"],
        count=50,
        minSize=50,
        maxSize=100,
        animationLength=3,
        key=None):

    out(key=key,
        data={
            "emojis": emojis,
            "count": count,
            "minSize": minSize,
            "maxSize": maxSize,
            "animationLength": animationLength,
        },
        )
    return emojis
