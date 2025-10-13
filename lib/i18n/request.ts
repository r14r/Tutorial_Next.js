import { getRequestConfig } from 'next-intl/server';
import { DEFAULT_LOCALE, SUPPORTED_LOCALES, type Locale } from '@/lib/i18n';

function resolveLocale(locale?: string): Locale {
  if (locale && SUPPORTED_LOCALES.includes(locale as Locale)) {
    return locale as Locale;
  }
  return DEFAULT_LOCALE;
}

export default getRequestConfig(async ({ locale }) => {
  const targetLocale = resolveLocale(locale);
  const messages = (await import(`../../messages/${targetLocale}.json`)).default;

  return {
    locale: targetLocale,
    messages,
  };
});
