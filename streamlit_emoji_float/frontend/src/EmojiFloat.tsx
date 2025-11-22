import { FC, ReactElement, useEffect } from "react";
import { floatEmoji } from "./floatEmoji";

export type EmojiFloatProps = {
  emojis?: string[];
  count?: number;
  minSize?: number;
  maxSize?: number;
  animationLength?: number;
};

const EmojiFloat: FC<EmojiFloatProps> = ({
  emojis = ["🎈", "⭐", "😊"],
  count = 24,
  minSize = 50,
  maxSize = 100,
  animationLength = 5,
}): ReactElement => {
  useEffect(() => {
    floatEmoji([{ emojis, count, minSize, maxSize, animationLength }]);
  }, [emojis, count, minSize, maxSize, animationLength]);

  return <div />;
};

export default EmojiFloat;
