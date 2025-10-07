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
    slug: "einfuhrung-in-ki-und-ollama",
    title: "Tag 1 — Einführung in KI & Ollama",
    description: "Tag 1 — Einführung in KI & Ollama Grundlagen.",
    subchapters: [
      {
        slug: "einheit-1-1",
        title: "1 — Was ist Künstliche Intelligenz (KI)?",
        load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/einheit-1-1.md"),
      },
      {
        slug: "einheit-1-2",
        title: "2 — Einstieg in Ollama",
        load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/einheit-1-2.md"),
      },
      {
        slug: "einheit-1-3",
        title: "3 — Ollama in der Kommandozeile (CLI)",
        load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/einheit-1-3.md"),
      },
      {
        slug: "einheit-1-4",
        title: "4 — Ollama API mit der Kommandozeile (cURL)",
        load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/einheit-1-4.md"),
      },
      {
        slug: "einheit-1-5",
        title: "5 — Zugriff über die API mit Python (Requests)",
        load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/einheit-1-5.md"),
      },
      {
        slug: "einheit-1-6",
        title: "6 — Nutzung der Ollama SDKs",
        load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/einheit-1-6.md"),
      },
      {
        slug: "einheit-1-7",
        title: "7 — Grundlagen der Arbeit mit LLMs",
        load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/einheit-1-7.md"),
      },
      {
        slug: "einheit-1-8",
        title: "8 — Prompt Engineering Grundlagen",
        load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/einheit-1-8.md"),
      },
    ],
  },
  {
    slug: "arbeiten-mit-llms-und-prompt-engineering",
    title: "Tag 2: Arbeiten mit LLMs & Prompt Engineering",
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
    title: "Tag 3: Datenverarbeitung & KI-Anwendungen",
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
    title: "Tag 4: Fortgeschrittene Anwendungen mit LLMs & Daten",
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
