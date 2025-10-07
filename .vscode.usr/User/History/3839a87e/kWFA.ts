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
  { slug: "1-1", title: "1 — Was ist Künstliche Intelligenz (KI)?", load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/1-1.md") },
  { slug: "1-2", title: "2 — Einstieg in Ollama", load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/1-2.md") },
  { slug: "1-3", title: "3 — Ollama in der Kommandozeile (CLI)", load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/1-3.md") },
  { slug: "1-4", title: "4 — Ollama API mit der Kommandozeile (cURL)", load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/1-4.md") },
  { slug: "1-5", title: "5 — Zugriff über die API mit Python (Requests)", load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/1-5.md") },
  { slug: "1-6", title: "6 — Nutzung der Ollama SDKs", load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/1-6.md") },
  { slug: "1-7", title: "7 — Grundlagen der Arbeit mit LLMs", load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/1-7.md") },
  { slug: "1-8", title: "8 — Prompt Engineering Grundlagen", load: () => import("@/content/1-Einführung-in-KI-und-Ollama/units/1-8.md") },
    ],
  },
  {
    slug: "arbeiten-mit-llms-und-prompt-engineering",
    title: "Tag 2: Arbeiten mit LLMs & Prompt Engineering",
    description: "Tag 2 — Arbeiten mit LLMs & Prompt Engineering.",
    subchapters: [
  { slug: "2-1", title: "1 — Einführung in Large Language Models (LLMs)", load: () => import("@/content/2-Arbeiten-mit-LLMs-und-Prompt-Engineering/units/2-1.md") },
  { slug: "2-2", title: "2 — Was ist ein Prompt?", load: () => import("@/content/2-Arbeiten-mit-LLMs-und-Prompt-Engineering/units/2-2.md") },
  { slug: "2-3", title: "3 — Rollen im Prompting & Prompt Engineering: Grundlagen", load: () => import("@/content/2-Arbeiten-mit-LLMs-und-Prompt-Engineering/units/2-3.md") },
  { slug: "2-4", title: "4 — Prompting-Prinzipien", load: () => import("@/content/2-Arbeiten-mit-LLMs-und-Prompt-Engineering/units/2-4.md") },
  { slug: "2-5", title: "5 — Prompt-Playground & Prompt-Vergleich (Streamlit-App)", load: () => import("@/content/2-Arbeiten-mit-LLMs-und-Prompt-Engineering/units/2-5.md") },
  { slug: "2-6", title: "6 — Temperatur & Steuerung der Kreativität", load: () => import("@/content/2-Arbeiten-mit-LLMs-und-Prompt-Engineering/units/2-6.md") },
  { slug: "2-7", title: "7 — Vergleich verschiedener Modelle", load: () => import("@/content/2-Arbeiten-mit-LLMs-und-Prompt-Engineering/units/2-7.md") },
  { slug: "2-8", title: "8 — Fehler & Grenzen von LLMs", load: () => import("@/content/2-Arbeiten-mit-LLMs-und-Prompt-Engineering/units/2-8.md") },
  { slug: "2-9", title: "9 — Praktische Beispiele für Prompts", load: () => import("@/content/2-Arbeiten-mit-LLMs-und-Prompt-Engineering/units/2-9.md") },
    ],
  },
  {
    slug: "datenverarbeitung-und-ki-anwendungen",
    title: "Tag 3: Datenverarbeitung & KI-Anwendungen",
    description: "Tag 3 — Datenverarbeitung & KI-Anwendungen.",
    subchapters: [
  { slug: "3-1", title: "1 — Einführung in Textanalyse", load: () => import("@/content/3-Datenverarbeitung-und-KI-Anwendungen/units/3-1.md") },
  { slug: "3-2", title: "2 — Sentimentanalyse (Stimmung erkennen)", load: () => import("@/content/3-Datenverarbeitung-und-KI-Anwendungen/units/3-2.md") },
  { slug: "3-3", title: "3 — Themenklassifikation", load: () => import("@/content/3-Datenverarbeitung-und-KI-Anwendungen/units/3-3.md") },
  { slug: "3-4", title: "4 — Schlüsselwort-Extraktion", load: () => import("@/content/3-Datenverarbeitung-und-KI-Anwendungen/units/3-4.md") },
  { slug: "3-5", title: "5 — Named Entity Recognition (NER)", load: () => import("@/content/3-Datenverarbeitung-und-KI-Anwendungen/units/3-5.md") },
  { slug: "3-6", title: "6 — FAQ-Bot mit Ollama", load: () => import("@/content/3-Datenverarbeitung-und-KI-Anwendungen/units/3-6.md") },
  { slug: "3-7", title: "7 — Kombination von Analysen (Sentiment + Keywords + Entities)", load: () => import("@/content/3-Datenverarbeitung-und-KI-Anwendungen/units/3-7.md") },
  { slug: "3-8", title: "8 — Erweiterte Streamlit-App: Analyse-Dashboard", load: () => import("@/content/3-Datenverarbeitung-und-KI-Anwendungen/units/3-8.md") },
    ],
  },
  {
    slug: "fortgeschrittene-anwendungen-mit-llms-und-daten",
    title: "Tag 4: Fortgeschrittene Anwendungen mit LLMs & Daten",
    description: "Tag 4 — Fortgeschrittene Anwendungen mit LLMs & Daten.",
    subchapters: [
  { slug: "4-1", title: "1 — Datenintegration mit Pandas", load: () => import("@/content/4-Fortgeschrittene-Anwendungen-mit-LLMs-und-Daten/units/4-1.md") },
  { slug: "4-2", title: "2 — Q&A über CSV-Dateien", load: () => import("@/content/4-Fortgeschrittene-Anwendungen-mit-LLMs-und-Daten/units/4-2.md") },
  { slug: "4-3", title: "3 — KI-Dashboards mit Streamlit", load: () => import("@/content/4-Fortgeschrittene-Anwendungen-mit-LLMs-und-Daten/units/4-3.md") },
  { slug: "4-4", title: "4 — Deployment", load: () => import("@/content/4-Fortgeschrittene-Anwendungen-mit-LLMs-und-Daten/units/4-4.md") },
  { slug: "4-5", title: "5 — Bonus: Q&A über mehrere Datenquellen", load: () => import("@/content/4-Fortgeschrittene-Anwendungen-mit-LLMs-und-Daten/units/4-5.md") },
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
