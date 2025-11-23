import streamlit as st

_out = None


def _get_out():
    global _out
    if _out is None:
        _out = st.components.v2.component(
            "streamlit-emoji-float.streamlit_emoji_float",
            js="index-*.js",
            html='<div class="react-root"></div>',
        )
    return _out


def emoji_float(
        emojis: list[str] = ["⭐", "😊", "🎈"],
        count: int = 50,
        minSize: int = 50,
        maxSize: int = 100,
        animationLength: int = 3,
        key=None) -> list[str]:
    """
    Display floating emojis in a Streamlit app.

    Parameters
    ----------
    emojis : list[str], optional
        List of emoji characters to float. Default: ["⭐", "😊", "🎈"].
    count : int, optional
        Number of emojis to spawn. Default: 50.
    minSize : int, optional
        Minimum size (px) of an emoji. Default: 50.
    maxSize : int, optional
        Maximum size (px) of an emoji. Default: 100.
    animationLength : int, optional
        Duration (seconds) of the float animation. Default: 3.
    key : str, optional
        Streamlit component key for uniqueness.

    Returns
    -------
    list[str]
        The list of emojis used.
    """
    out = _get_out()
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
