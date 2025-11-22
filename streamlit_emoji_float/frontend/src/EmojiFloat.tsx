import { FC, ReactElement, useMemo } from "react";

export type EmojiFloatProps = {
  emojis?: Array<string>;
  count?: number;
};

const EmojiFloat: FC<EmojiFloatProps> = ({
  emojis = ["⭐", "😊", "🎈"],
  count = 10,
}): ReactElement => {
  const randomEmojis = useMemo(
    () =>
      Array.from(
        { length: count },
        () => emojis[Math.floor(Math.random() * emojis.length)],
      ),
    [count, emojis],
  );

  return (
    <div>
      {randomEmojis.map((emoji, i) => (
        <span
          key={i}
          style={{
            display: "inline-block",
            margin: "0 4px",
          }}
        >
          {emoji}
        </span>
      ))}
    </div>
  );
};

export default EmojiFloat;
