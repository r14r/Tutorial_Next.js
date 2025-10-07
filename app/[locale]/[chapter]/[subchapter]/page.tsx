import { notFound } from "next/navigation";
import { flattenSubchapters, getSubchapter } from "@/lib/chapters";
import { useTranslations } from 'next-intl';

export function generateStaticParams() {
  return flattenSubchapters();
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

  // Example: useTranslations for i18n
  // const t = useTranslations();
  // <h1>{t('contentTitle')}</h1>

  return (
    <article>
      <Content />
    </article>
  );
}
