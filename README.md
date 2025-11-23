# streamlit-emoji-float

`streamlit-emoji-float` is a fun custom Streamlit component that animates emojis, making them float on your Streamlit app.

<a href="https://share.streamlit.io/user/j-ncel" style="text-decoration:none;">
    <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width="40" alt="Streamlit">
    <h3 style="display:inline; margin-left:4px;">Try the live demo on Streamlit Cloud</h3>
</a>

---

![Demo GIF](https://github.com/j-ncel/streamlit-emoji-float/blob/main/sample/emoji-float-sample.gif?raw=true)

## Installation

```bash
pip install streamlit-emoji-float
```

## Usage

```python
from streamlit_emoji_float import emoji_float

# Usage with default emojis
emoji_float()

# Usage with custom parameters
emoji_float(
    emojis=["🔥", "🚀", "🎉"],
    count=20,
    minSize=50,
    maxSize=100,
    animationLength=5
)
```

`emojis:` List of emoji characters to animate (default: ["⭐", "😊", "🎈"])  
`count:` Number of emojis to spawn (default: 50)  
`minSize:` Minimum size in pixels (default: 50)  
`maxSize:` Maximum size in pixels (default: 100)  
`animationLength:` Duration of floating animation (default: 3)  
`key:` Streamlit component key for uniqueness

<a href="https://coff.ee/jncel">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" width="100" height="" alt="Buy Me a Coffee">
</a>
