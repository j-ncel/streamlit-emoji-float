const EMOJI_REFERENCE_SIZE = 256;

interface FloatEmojiData {
  emojis: string[];
  minSize: number;
  maxSize: number;
  count: number;
  animationLength: number;
}

function createFloatEmoji(
  emoji: string,
  minSize: number,
  maxSize: number,
  duration: number,
): HTMLElement {
  const element = document.createElement("float-emoji") as HTMLElement;
  const emojiSize =
    minSize + Math.floor(Math.random() * (maxSize - minSize + 1));
  const padding = 20;
  const svgWidth = emojiSize + padding;
  const svgHeight = emojiSize + padding;
  const scaleAdjustment = EMOJI_REFERENCE_SIZE / emojiSize;

  const svgContent = `
    <svg xmlns="http://www.w3.org/2000/svg" 
         width="${svgWidth * scaleAdjustment}" 
         height="${svgHeight * scaleAdjustment}">
      <text x="50%" y="50%" dominant-baseline="central" text-anchor="middle"
        font-size="${EMOJI_REFERENCE_SIZE}px">
        ${emoji}
      </text>
    </svg>
  `;
  const encodedSVG = encodeURIComponent(svgContent);
  const delay = Math.random() * duration;
  const viewportWidth = window.innerWidth;
  const emojiWidth = svgWidth;
  const maxLeft = viewportWidth - emojiWidth;
  const safeLeft = Math.random() * maxLeft;

  Object.assign(element.style, {
    position: "absolute",
    top: "100%",
    left: `${safeLeft}px`,
    width: `${svgWidth}px`,
    height: `${svgHeight}px`,
    fontSize: String(emojiSize),
    lineHeight: "1",
    display: "inline-block",
    minWidth: "1ch",
    animation: `floatUp ${duration}s linear ${delay}s forwards`,
  });

  element.addEventListener("animationend", () => {
    element.remove();
  });

  const content = document.createElement("emoji-content") as HTMLElement;
  Object.assign(content.style, {
    display: "block",
    position: "absolute",
    left: "50%",
    top: "50%",
    width: `${svgWidth * scaleAdjustment}px`,
    height: `${svgHeight * scaleAdjustment}px`,
    transform: `translate(-50%, -50%) scale(${1 / scaleAdjustment})`,
    transformOrigin: "center",
    backgroundImage: `url("data:image/svg+xml,${encodedSVG}")`,
    backgroundSize: "contain",
  });

  element.appendChild(content);
  return element;
}

export function floatEmoji(lines: FloatEmojiData[]): void {
  let container = document.querySelector(
    "float-container",
  ) as HTMLElement | null;

  if (!container) {
    container = document.createElement("float-container") as HTMLElement;

    const styleEl = document.createElement("style");
    styleEl.className = "float-style";
    styleEl.innerHTML = `
      @keyframes floatUp {
        0%   { transform: translateY(0); opacity: 0; }
        10%   { opacity: 1; }
        90%  { opacity: 1; }
        95%  { opacity: 0; }
        100% { transform: translateY(-100vh); opacity: 0; }
      }
    `;
    container.appendChild(styleEl);

    Object.assign(container.style, {
      position: "fixed",
      bottom: "0",
      left: "0",
      width: "100%",
      height: "100%",
      zIndex: "9999",
      pointerEvents: "none",
    });

    document.body.appendChild(container);
  } else {
    container
      .querySelectorAll(":scope > float-emoji")
      .forEach((node) => node.remove());
  }

  lines.forEach((line) => {
    const list = Array.isArray(line.emojis) ? line.emojis : [];
    const total = Math.max(0, Number(line.count) || 0);
    if (list.length === 0 || total === 0) return;

    const duration = line.animationLength;

    const chosen = Array.from({ length: total }, () => {
      const idx = Math.floor(Math.random() * list.length);
      return list[idx];
    });

    const fragment = document.createDocumentFragment();
    chosen.forEach((emoji) => {
      const el = createFloatEmoji(emoji, line.minSize, line.maxSize, duration);
      fragment.appendChild(el);
    });
    container!.appendChild(fragment);
  });
}
