import type { ComponentType } from "react";

export type ContentModule = {
  default: ComponentType;
};

type Subchapter = {
  slug: string;
  title: string;
  import: () => Promise<ContentModule>;
};

type Chapter = {
  slug: string;
  title: string;
  description: string;
  subchapters: Subchapter[];
};

export const chapters: Chapter[] = [
  {
    slug: "getting-started",
    title: "Getting Started",
    description: "Lay the foundation for your Next.js learning journey.",
    subchapters: [
      {
        slug: "introduction",
        title: "Introduction",
        import: () => import("@/content/getting-started/introduction.mdx"),
      },
      {
        slug: "project-setup",
        title: "Project Setup",
        import: () => import("@/content/getting-started/project-setup.md"),
      },
    ],
  },
  {
    slug: "core-concepts",
    title: "Core Concepts",
    description: "Discover the building blocks that power every application.",
    subchapters: [
      {
        slug: "app-router",
        title: "App Router",
        import: () => import("@/content/core-concepts/app-router.mdx"),
      },
      {
        slug: "data-fetching",
        title: "Data Fetching",
        import: () => import("@/content/core-concepts/data-fetching.md"),
      },
    ],
  },
];

export function getChapterHref(slug: string) {
  const chapter = chapters.find((chapter) => chapter.slug === slug);
  if (!chapter) {
    return "/";
  }
  const firstSubchapter = chapter.subchapters[0];
  return `/${chapter.slug}/${firstSubchapter.slug}`;
}

export function getSubchapter(chapterSlug: string, subchapterSlug: string) {
  const chapter = chapters.find((chapter) => chapter.slug === chapterSlug);
  if (!chapter) {
    return undefined;
  }
  const subchapter = chapter.subchapters.find((entry) => entry.slug === subchapterSlug);
  if (!subchapter) {
    return undefined;
  }
  return { chapter, subchapter } as const;
}

export function flattenSubchapters() {
  return chapters.flatMap((chapter) =>
    chapter.subchapters.map((subchapter) => ({
      chapterSlug: chapter.slug,
      subchapterSlug: subchapter.slug,
    }))
  );
}
