import { defineConfig } from 'next-intl';

export default defineConfig({
  defaultLocale: 'de',
  locales: ['de', 'en', 'mr'],
  localePrefix: 'always',
  messagesDir: './messages'
});
