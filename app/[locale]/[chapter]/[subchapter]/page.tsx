import { notFound } from "next/navigation";
import { flattenSubchapters, getSubchapter } from "@/lib/chapters";
import { SUPPORTED_LOCALES } from "@/lib/i18n";

export function generateStaticParams() {
  return SUPPORTED_LOCALES.flatMap((locale) =>
    flattenSubchapters().map(({ chapterSlug, subchapterSlug }) => ({
      locale,
      chapter: chapterSlug,
      subchapter: subchapterSlug,
    }))
  );
}

type PageProps = {
  params: {
    locale: string;
    chapter: string;
    subchapter: string;
  };
};

export async function generateMetadata({ params }: PageProps) {
  const result = getSubchapter(params.chapter, params.subchapter);
  if (!result) {
    return {};
  }

  return {
    title: `${result.subchapter.title} — ${result.chapter.title}`,
    description: result.chapter.description,
  };
}

export default async function SubchapterPage({ params }: PageProps) {
  const result = getSubchapter(params.chapter, params.subchapter);
  if (!result) {
    notFound();
  }

  const { subchapter } = result;
  const Content = (await subchapter.load()).default;

  return (
    <article>
      <Content />
    </article>
  );
}
