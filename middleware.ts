import createMiddleware from 'next-intl/middleware';
import { DEFAULT_LOCALE, SUPPORTED_LOCALES } from '@/lib/i18n';

export default createMiddleware({
  defaultLocale: DEFAULT_LOCALE,
  locales: SUPPORTED_LOCALES,
  localePrefix: 'always',
});

export const config = {
  matcher: ['/((?!_next|_vercel|.*\..*).*)'],
};
