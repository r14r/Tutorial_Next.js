"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useTranslations } from "next-intl";
import { chapters } from "@/lib/chapters";
import { DEFAULT_LOCALE, isLocale, type Locale } from "@/lib/i18n";

export default function Sidebar() {
  const pathname = usePathname();
  const segments = pathname.split("/").filter(Boolean);
  const maybeLocale = segments[0];
  const hasLocale = isLocale(maybeLocale);
  const locale: Locale = hasLocale ? maybeLocale : DEFAULT_LOCALE;
  const chapterSlug = segments[hasLocale ? 1 : 0];
  const subchapterSlug = segments[hasLocale ? 2 : 1];
  const t = useTranslations();

  if (!chapterSlug) {
    return null;
  }

  const currentChapter = chapters.find((chapter) => chapter.slug === chapterSlug);

  if (!currentChapter) {
    return null;
  }

  return (
    <aside className="sidebar" aria-label="Subchapter navigation">
      <h2>
        {t(`${currentChapter.i18nKey}.description`, {
          defaultMessage: currentChapter.fallbackDescription,
        })}
      </h2>
      {currentChapter.subchapters.map((subchapter) => {
        const href = `/${locale}/${currentChapter.slug}/${subchapter.slug}`;
        const isActive = subchapter.slug === subchapterSlug;
        return (
          <Link key={subchapter.slug} href={href} className={isActive ? "active" : undefined}>
            {t(subchapter.i18nKey, {
              defaultMessage: subchapter.fallbackTitle,
            })}
          </Link>
        );
      })}
    </aside>
  );
}
