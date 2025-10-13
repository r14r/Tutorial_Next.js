import type { ComponentType } from "react";
import { DEFAULT_LOCALE, isLocale } from "./i18n";

export type ContentModule = {
  default: ComponentType;
};

type SubchapterConfig = {
  slug: string;
  title: string;
  file: string;
};

type ChapterConfig = {
  slug: string;
  title: string;
  description: string;
  basePath: string;
  subchapters: SubchapterConfig[];
};

export type Subchapter = {
  slug: string;
  i18nKey: string;
  fallbackTitle: string;
  load: (locale?: string) => Promise<ContentModule>;
};

export type Chapter = {
  slug: string;
  i18nKey: string;
  fallbackTitle: string;
  fallbackDescription: string;
  subchapters: Subchapter[];
};

const chapterConfigs: ChapterConfig[] = [
  {
    slug: "day-1",
    title: "Tag 1",
    description: "Einführung in KI & Ollama Grundlagen.",
    basePath: "day-1",
    subchapters: [
      { slug: "overview", file: "content", title: "Inhalt" },
      { slug: "intro-to-ai", file: "1-1", title: "1 — Was ist Künstliche Intelligenz (KI)?" },
      { slug: "ollama-getting-started", file: "1-2", title: "2 — Einstieg in Ollama" },
      { slug: "ollama-cli", file: "1-3", title: "3 — Ollama in der Kommandozeile (CLI)" },
      { slug: "ollama-api-curl", file: "1-4", title: "4 — Ollama API mit der Kommandozeile (cURL)" },
      { slug: "api-python", file: "1-5", title: "5 — Zugriff über die API mit Python (Requests)" },
      { slug: "ollama-sdks", file: "1-6", title: "6 — Nutzung der Ollama SDKs" },
      { slug: "llm-basics", file: "1-7", title: "7 — Grundlagen der Arbeit mit LLMs" },
      { slug: "prompt-basics", file: "1-8", title: "8 — Prompt Engineering Grundlagen" },
    ],
  },
  {
    slug: "day-2",
    title: "Tag 2",
    description: "Arbeiten mit LLMs & Prompt Engineering.",
    basePath: "day-2",
    subchapters: [
      { slug: "overview", file: "content", title: "Inhalt" },
      { slug: "llm-intro", file: "2-1", title: "1 — Einführung in Large Language Models (LLMs)" },
      { slug: "what-is-a-prompt", file: "2-2", title: "2 — Was ist ein Prompt?" },
      { slug: "prompt-roles", file: "2-3", title: "3 — Rollen im Prompting & Prompt Engineering: Grundlagen" },
      { slug: "prompt-principles", file: "2-4", title: "4 — Prompting-Prinzipien" },
      { slug: "prompt-playground", file: "2-5", title: "5 — Prompt-Playground & Prompt-Vergleich (Streamlit-App)" },
      { slug: "temperature-creativity", file: "2-6", title: "6 — Temperatur & Steuerung der Kreativität" },
      { slug: "model-comparison", file: "2-7", title: "7 — Vergleich verschiedener Modelle" },
      { slug: "llm-limitations", file: "2-8", title: "8 — Fehler & Grenzen von LLMs" },
      { slug: "prompt-examples", file: "2-9", title: "9 — Praktische Beispiele für Prompts" },
    ],
  },
  {
    slug: "day-3",
    title: "Tag 3",
    description: "Datenverarbeitung & KI-Anwendungen.",
    basePath: "day-3",
    subchapters: [
      { slug: "overview", file: "content", title: "Inhalt" },
      { slug: "text-analytics", file: "3-1", title: "1 — Einführung in Textanalyse" },
      { slug: "sentiment-analysis", file: "3-2", title: "2 — Sentimentanalyse (Stimmung erkennen)" },
      { slug: "topic-classification", file: "3-3", title: "3 — Themenklassifikation" },
      { slug: "keyword-extraction", file: "3-4", title: "4 — Schlüsselwort-Extraktion" },
      { slug: "ner", file: "3-5", title: "5 — Named Entity Recognition (NER)" },
      { slug: "faq-bot", file: "3-6", title: "6 — FAQ-Bot mit Ollama" },
      { slug: "combined-analytics", file: "3-7", title: "7 — Kombination von Analysen (Sentiment + Keywords + Entities)" },
      { slug: "analytics-dashboard", file: "3-8", title: "8 — Erweiterte Streamlit-App: Analyse-Dashboard" },
    ],
  },
  {
    slug: "day-4",
    title: "Tag 4",
    description: "Fortgeschrittene Anwendungen mit LLMs & Daten.",
    basePath: "day-4",
    subchapters: [
      { slug: "overview", file: "content", title: "Inhalt" },
      { slug: "pandas-integration", file: "4-1", title: "1 — Datenintegration mit Pandas" },
      { slug: "csv-qa", file: "4-2", title: "2 — Q&A über CSV-Dateien" },
      { slug: "ai-dashboards", file: "4-3", title: "3 — KI-Dashboards mit Streamlit" },
      { slug: "deployment", file: "4-4", title: "4 — Deployment" },
      { slug: "multi-source-qa", file: "4-5", title: "5 — Bonus: Q&A über mehrere Datenquellen" },
    ],
  },
];

function isModuleNotFoundError(error: unknown) {
  if (!(error instanceof Error)) {
    return false;
  }

  const message = error.message || "";
  const code = (error as NodeJS.ErrnoException).code;

  return message.includes("Cannot find module") || message.includes("Module not found") || code === "MODULE_NOT_FOUND";
}

async function loadContentModule(basePath: string, file: string, locale?: string) {
  const attempted = new Set<string>();
  const candidates: string[] = [];

  const pushCandidate = (value: string) => {
    if (!attempted.has(value)) {
      attempted.add(value);
      candidates.push(value);
    }
  };

  const normalizedBase = `${basePath}/${file}`;

  if (locale && isLocale(locale)) {
    pushCandidate(`${locale}/${normalizedBase}`);
    pushCandidate(`${normalizedBase}.${locale}`);
  }

  if (!locale || locale !== DEFAULT_LOCALE) {
    pushCandidate(`${DEFAULT_LOCALE}/${normalizedBase}`);
    pushCandidate(`${normalizedBase}.${DEFAULT_LOCALE}`);
  }

  pushCandidate(normalizedBase);

  for (const candidate of candidates) {
    try {
      return await import(`@/content/${candidate}.md`);
    } catch (error) {
      if (!isModuleNotFoundError(error)) {
        throw error;
      }
    }
  }

  throw new Error(`Unable to load content for ${basePath}/${file}`);
}

export const chapters: Chapter[] = chapterConfigs.map(({ basePath, ...chapter }) => {
  const chapterI18nKey = `chapters.${chapter.slug}`;
  return {
    slug: chapter.slug,
    i18nKey: chapterI18nKey,
    fallbackTitle: chapter.title,
    fallbackDescription: chapter.description,
    subchapters: chapter.subchapters.map((sub) => ({
      slug: sub.slug,
      i18nKey: `${chapterI18nKey}.subchapters.${sub.slug}`,
      fallbackTitle: sub.title,
      load: (locale?: string) => loadContentModule(basePath, sub.file, locale),
    })),
  };
});

export function getChapterHref(slug: string, locale?: string) {
  const chapter = chapters.find((chapter) => chapter.slug === slug);
  if (!chapter) {
    if (locale && isLocale(locale)) {
      return `/${locale}`;
    }
    return "/";
  }
  const firstSubchapter = chapter.subchapters[0];
  const basePath = `/${chapter.slug}/${firstSubchapter.slug}`;
  if (locale && isLocale(locale)) {
    return `/${locale}${basePath}`;
  }
  return basePath;
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
