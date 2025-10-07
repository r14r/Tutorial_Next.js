"use client";


import Link from "next/link";
import { usePathname } from "next/navigation";
import { chapters, getChapterHref } from "@/lib/chapters";
import LanguageSwitcher from "./LanguageSwitcher";
import { DEFAULT_LOCALE, isLocale, type Locale } from "@/lib/i18n";

export default function HeaderNav() {
  const pathname = usePathname();
  const segments = pathname.split("/").filter(Boolean);
  const maybeLocale = segments[0];
  const locale: Locale = isLocale(maybeLocale) ? maybeLocale : DEFAULT_LOCALE;
  const pathWithoutLocale = isLocale(maybeLocale)
    ? `/${segments.slice(1).join("/")}`
    : pathname;

  return (
    <header className="header">
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <nav aria-label="Chapter navigation">
          {chapters.map((chapter) => {
            const href = getChapterHref(chapter.slug, locale);
            const isActive = pathWithoutLocale.startsWith(`/${chapter.slug}`);
            return (
              <Link
                key={chapter.slug}
                href={href}
                className={isActive ? "active" : undefined}
              >
                {chapter.title}
              </Link>
            );
          })}
        </nav>
        <LanguageSwitcher />
      </div>
    </header>
  );
}
