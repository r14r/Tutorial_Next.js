import createMDX from '@next/mdx';
import createNextIntlPlugin from 'next-intl/plugin';

const withMDX = createMDX({
  extension: /.mdx?$/,
});

const withNextIntl = createNextIntlPlugin('./next-intl.config.mjs');

const nextConfig = withNextIntl(
  withMDX({
    experimental: {
      mdxRs: true,
    },
    pageExtensions: ['ts', 'tsx', 'md', 'mdx'],
  })
);

export default nextConfig;
