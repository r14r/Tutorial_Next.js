"use client";

import { useRouter, usePathname } from 'next/navigation';
import { DEFAULT_LOCALE, SUPPORTED_LOCALES, isLocale, type Locale } from '@/lib/i18n';

const LANGUAGE_LABELS: Record<Locale, string> = {
  de: 'Deutsch',
  en: 'English',
  mr: 'मराठी',
};

function getCurrentLocale(pathname: string): Locale {
  const segments = pathname.split('/').filter(Boolean);
  const maybeLocale = segments[0];
  if (isLocale(maybeLocale)) {
    return maybeLocale;
  }
  return DEFAULT_LOCALE;
}

export default function LanguageSwitcher() {
  const router = useRouter();
  const pathname = usePathname();
  const currentLocale = getCurrentLocale(pathname);

  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const nextLocale = event.target.value as Locale;

    if (nextLocale === currentLocale) {
      return;
    }

    const segments = pathname.split('/').filter(Boolean);

    if (isLocale(segments[0])) {
      segments[0] = nextLocale;
    } else {
      segments.unshift(nextLocale);
    }

    router.push(`/${segments.join('/')}`);
  };

  return (
    <select onChange={handleChange} value={currentLocale}>
      {SUPPORTED_LOCALES.map((locale) => (
        <option key={locale} value={locale}>
          {LANGUAGE_LABELS[locale]}
        </option>
      ))}
    </select>
  );
}
