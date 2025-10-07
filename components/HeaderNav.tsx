"use client";


import Link from "next/link";
import { usePathname } from "next/navigation";
import { chapters, getChapterHref } from "@/lib/chapters";
import LanguageSwitcher from "./LanguageSwitcher";

export default function HeaderNav() {
  const pathname = usePathname();

  return (
    <header className="header">
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <nav aria-label="Chapter navigation">
          {chapters.map((chapter) => {
            const href = getChapterHref(chapter.slug);
            const isActive = pathname.startsWith(`/${chapter.slug}`);
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
