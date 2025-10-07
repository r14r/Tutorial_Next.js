declare module '*.mdx' {
  import type { ComponentType } from 'react';
  const MDXComponent: ComponentType<any>;
  export default MDXComponent;
}

declare module '*.md' {
  import type { ComponentType } from 'react';
  const MarkdownComponent: ComponentType<any>;
  export default MarkdownComponent;
}
