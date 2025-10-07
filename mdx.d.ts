import type { MDXContentProps } from "mdx/types";

declare module "*.mdx" {
  let MDXComponent: (props: MDXContentProps) => JSX.Element;
  export default MDXComponent;
}

declare module "*.md" {
  const content: string;
  export default content;
}
