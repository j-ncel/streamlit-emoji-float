import { Component, ComponentArgs } from "@streamlit/component-v2-lib";
import { StrictMode } from "react";
import { createRoot, Root } from "react-dom/client";

import EmojiFloat from "./EmojiFloat";

const reactRoots: WeakMap<ComponentArgs["parentElement"], Root> = new WeakMap();

const EmojiFloatRoot: Component<any, any> = (args) => {
  const { data, parentElement } = args;
  const rootElement = parentElement.querySelector(".react-root");

  if (!rootElement) {
    throw new Error("Unexpected: React root element not found");
  }

  let reactRoot = reactRoots.get(parentElement);
  if (!reactRoot) {
    reactRoot = createRoot(rootElement);
    reactRoots.set(parentElement, reactRoot);
  }

  const { emojis, count } = data;

  reactRoot.render(
    <StrictMode>
      <EmojiFloat emojis={emojis} count={count} />
    </StrictMode>,
  );

  return () => {
    const reactRoot = reactRoots.get(parentElement);
    if (reactRoot) {
      reactRoot.unmount();
      reactRoots.delete(parentElement);
    }
  };
};

export default EmojiFloatRoot;
