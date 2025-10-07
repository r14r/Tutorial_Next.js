"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { chapters } from "@/lib/chapters";

export default function Sidebar() {
  const pathname = usePathname();
  const [_, chapterSlug, subchapterSlug] = pathname.split("/");
  const currentChapter = chapters.find((chapter) => chapter.slug === chapterSlug);

  if (!currentChapter) {
    return null;
  }

  return (
    <aside className="sidebar" aria-label="Subchapter navigation">
      <h2>{currentChapter.title}</h2>
      {currentChapter.subchapters.map((subchapter) => {
        const href = `/${currentChapter.slug}/${subchapter.slug}`;
        const isActive = subchapter.slug === subchapterSlug;
        return (
          <Link key={subchapter.slug} href={href} className={isActive ? "active" : undefined}>
            {subchapter.title}
          </Link>
        );
      })}
    </aside>
  );
}
