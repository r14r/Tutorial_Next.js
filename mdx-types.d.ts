declare module 'mdx/types' {
  import type { ComponentType } from 'react';
  export type MDXComponents = {
    [key: string]: ComponentType<any>;
  };
}
