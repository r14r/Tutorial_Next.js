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

const chapterConfigs = [
  {
    slug: "einfuhrung-in-ki-und-ollama",
    title: "Tag 1 — Einführung in KI & Ollama",
    description: "Tag 1 — Einführung in KI & Ollama Grundlagen.",
    basePath: "1-Einführung-in-KI-und-Ollama",
    subchapters: [
      { slug: "content", title: "Inhalt" },
      { slug: "1-1", title: "1 — Was ist Künstliche Intelligenz (KI)?" },
      { slug: "1-2", title: "2 — Einstieg in Ollama" },
      { slug: "1-3", title: "3 — Ollama in der Kommandozeile (CLI)" },
      { slug: "1-4", title: "4 — Ollama API mit der Kommandozeile (cURL)" },
      { slug: "1-5", title: "5 — Zugriff über die API mit Python (Requests)" },
      { slug: "1-6", title: "6 — Nutzung der Ollama SDKs" },
      { slug: "1-7", title: "7 — Grundlagen der Arbeit mit LLMs" },
      { slug: "1-8", title: "8 — Prompt Engineering Grundlagen" },
    ],
  },
  {
    slug: "arbeiten-mit-llms-und-prompt-engineering",
    title: "Tag 2: Arbeiten mit LLMs & Prompt Engineering",
    description: "Tag 2 — Arbeiten mit LLMs & Prompt Engineering.",
    basePath: "2-Arbeiten-mit-LLMs-und-Prompt-Engineering",
    subchapters: [
      { slug: "content", title: "Inhalt" },
      { slug: "2-1", title: "1 — Einführung in Large Language Models (LLMs)" },
      { slug: "2-2", title: "2 — Was ist ein Prompt?" },
      { slug: "2-3", title: "3 — Rollen im Prompting & Prompt Engineering: Grundlagen" },
      { slug: "2-4", title: "4 — Prompting-Prinzipien" },
      { slug: "2-5", title: "5 — Prompt-Playground & Prompt-Vergleich (Streamlit-App)" },
      { slug: "2-6", title: "6 — Temperatur & Steuerung der Kreativität" },
      { slug: "2-7", title: "7 — Vergleich verschiedener Modelle" },
      { slug: "2-8", title: "8 — Fehler & Grenzen von LLMs" },
      { slug: "2-9", title: "9 — Praktische Beispiele für Prompts" },
    ],
  },
  {
    slug: "datenverarbeitung-und-ki-anwendungen",
    title: "Tag 3: Datenverarbeitung & KI-Anwendungen",
    description: "Tag 3 — Datenverarbeitung & KI-Anwendungen.",
    basePath: "3-Datenverarbeitung-und-KI-Anwendungen",
    subchapters: [
      { slug: "content", title: "Inhalt" },
      { slug: "3-1", title: "1 — Einführung in Textanalyse" },
      { slug: "3-2", title: "2 — Sentimentanalyse (Stimmung erkennen)" },
      { slug: "3-3", title: "3 — Themenklassifikation" },
      { slug: "3-4", title: "4 — Schlüsselwort-Extraktion" },
      { slug: "3-5", title: "5 — Named Entity Recognition (NER)" },
      { slug: "3-6", title: "6 — FAQ-Bot mit Ollama" },
      { slug: "3-7", title: "7 — Kombination von Analysen (Sentiment + Keywords + Entities)" },
      { slug: "3-8", title: "8 — Erweiterte Streamlit-App: Analyse-Dashboard" },
    ],
  },
  {
    slug: "fortgeschrittene-anwendungen-mit-llms-und-daten",
    title: "Tag 4: Fortgeschrittene Anwendungen mit LLMs & Daten",
    description: "Tag 4 — Fortgeschrittene Anwendungen mit LLMs & Daten.",
    basePath: "4-Fortgeschrittene-Anwendungen-mit-LLMs-und-Daten",
    subchapters: [
      { slug: "content", title: "Inhalt" },
      { slug: "4-1", title: "1 — Datenintegration mit Pandas" },
      { slug: "4-2", title: "2 — Q&A über CSV-Dateien" },
      { slug: "4-3", title: "3 — KI-Dashboards mit Streamlit" },
      { slug: "4-4", title: "4 — Deployment" },
      { slug: "4-5", title: "5 — Bonus: Q&A über mehrere Datenquellen" },
    ],
  },
];

export const chapters: Chapter[] = chapterConfigs.map(({ basePath, ...chapter }) => ({
  ...chapter,
  subchapters: chapter.subchapters.map((sub) => ({
    ...sub,
    load: () => import(`@/content/${basePath}/${sub.slug}.md`),
  })),
}));

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
