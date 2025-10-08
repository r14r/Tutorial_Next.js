"use client";

import { useRouter, usePathname } from 'next/navigation';
import { DEFAULT_LOCALE, SUPPORTED_LOCALES, isLocale, type Locale } from '@/lib/i18n';

const LANGUAGE_META: Record<Locale, { label: string; flag: string }> = {
  de: { label: 'Deutsch', flag: '🇩🇪' },
  en: { label: 'English', flag: '🇺🇸' },
  mr: { label: 'मराठी', flag: '🇮🇳' },
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

  const handleLocaleSelection = (nextLocale: Locale) => {
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
    <div className="language-switcher" role="group" aria-label="Sprachauswahl">
      {SUPPORTED_LOCALES.map((locale) => {
        const { label, flag } = LANGUAGE_META[locale];
        const isActive = locale === currentLocale;

        return (
          <button
            key={locale}
            type="button"
            onClick={() => handleLocaleSelection(locale)}
            aria-pressed={isActive}
            aria-label={label}
            title={label}
            className="language-switcher__button"
          >
            <span aria-hidden="true" role="img">
              {flag}
            </span>
          </button>
        );
      })}
    </div>
  );
}
