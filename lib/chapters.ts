import type { ComponentType } from "react";

export type ContentModule = {
  default: ComponentType;
};

type Subchapter = {
  slug: string;
  title: string;
  load: () => Promise<ContentModule>;
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
        load: () => import("@/content/getting-started/introduction.mdx"),
      },
      {
        slug: "project-setup",
        title: "Project Setup",
        load: () => import("@/content/getting-started/project-setup.md"),
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
        load: () => import("@/content/core-concepts/app-router.mdx"),
      },
      {
        slug: "data-fetching",
        title: "Data Fetching",
        load: () => import("@/content/core-concepts/data-fetching.md"),
      },
    ],
  },
  {
    slug: "einfuhrung-in-ki-und-ollama",
    title: "Tag 1", // Einführung in KI & Ollama",
    description: "Tag 1 — Einführung in KI & Ollama Grundlagen.",
    subchapters: [
      {
        slug: "course-day1",
        title: "Tag 1: Einführung in KI & Ollama",
        load: () => import("@/content/1-Einführung-in-KI-und-Ollama/content.md"),
      },
    ],
  },
  {
    slug: "arbeiten-mit-llms-und-prompt-engineering",
    title: "Tag 2", // Arbeiten mit LLMs & Prompt Engineering",
    description: "Tag 2 — Arbeiten mit LLMs & Prompt Engineering.",
    subchapters: [
      {
        slug: "course-day2",
        title: "Tag 2: Arbeiten mit LLMs & Prompt Engineering",
        load: () => import("@/content/2-Arbeiten-mit-LLMs-und-Prompt-Engineering/content.md"),
      },
    ],
  },
  {
    slug: "datenverarbeitung-und-ki-anwendungen",
    title: "Tag 3", // Datenverarbeitung & KI-Anwendungen",
    description: "Tag 3 — Datenverarbeitung & KI-Anwendungen.",
    subchapters: [
      {
        slug: "course-day3",
        title: "Tag 3: Datenverarbeitung & KI-Anwendungen",
        load: () => import("@/content/3-Datenverarbeitung-und-KI-Anwendungen/content.md"),
      },
    ],
  },
  {
    slug: "fortgeschrittene-anwendungen-mit-llms-und-daten",
    title: "Tag 4", // Fortgeschrittene Anwendungen mit LLMs & Daten",
    description: "Tag 4 — Fortgeschrittene Anwendungen mit LLMs & Daten.",
    subchapters: [
      {
        slug: "course-day4",
        title: "Tag 4: Fortgeschrittene Anwendungen mit LLMs & Daten",
        load: () => import("@/content/4-Fortgeschrittene-Anwendungen-mit-LLMs-und-Daten/content.md"),
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
