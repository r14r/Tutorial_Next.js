import { defineConfig } from 'next-intl';
import { DEFAULT_LOCALE, SUPPORTED_LOCALES } from './lib/i18n';

export default defineConfig({
  defaultLocale: DEFAULT_LOCALE,
  locales: SUPPORTED_LOCALES,
  localePrefix: 'always',
  messagesDir: './messages',
});
