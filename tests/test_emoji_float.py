import pytest
import streamlit_emoji_float


@pytest.fixture(autouse=True)
def fake_out(monkeypatch):
    def dummy_out(**kwargs):
        return kwargs
    monkeypatch.setattr(streamlit_emoji_float, "_get_out", lambda: dummy_out)


def test_default_emojis():
    result = streamlit_emoji_float.emoji_float()
    assert isinstance(result, list)
    assert result == ["⭐", "😊", "🎈"]


def test_custom_emojis():
    emojis = ["🔥", "🚀"]
    result = streamlit_emoji_float.emoji_float(
        emojis=emojis,
        count=10,
        minSize=30,
        maxSize=60,
        animationLength=5,
        key="test"
    )
    assert result == emojis


def test_size_range():
    emojis = ["✨"]
    result = streamlit_emoji_float.emoji_float(
        emojis=emojis,
        minSize=20,
        maxSize=100
    )
    assert result == emojis


def test_animation_length():
    emojis = ["🎉"]
    result = streamlit_emoji_float.emoji_float(
        emojis=emojis,
        animationLength=3
    )
    assert result == emojis
