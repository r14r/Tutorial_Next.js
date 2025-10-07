import createMDX from '@next/mdx';

const withMDX = createMDX({
  extension: /\.mdx?$/,
});


const nextConfig = withMDX({
  experimental: {
    mdxRs: true,
  },
  pageExtensions: ['ts', 'tsx', 'md', 'mdx'],
  i18n: {
    locales: ['de', 'en', 'mr'],
    defaultLocale: 'de',
  },
});

export default nextConfig;
