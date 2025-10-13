import { notFound } from "next/navigation";
import { getTranslations } from "next-intl/server";
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

  const t = await getTranslations({ locale: params.locale });
  const subchapterTitle = t(result.subchapter.i18nKey, {
    defaultMessage: result.subchapter.fallbackTitle,
  });
  const chapterTitle = t(`${result.chapter.i18nKey}.title`, {
    defaultMessage: result.chapter.fallbackTitle,
  });
  const description = t(`${result.chapter.i18nKey}.description`, {
    defaultMessage: result.chapter.fallbackDescription,
  });

  return {
    title: `${subchapterTitle} — ${chapterTitle}`,
    description,
  };
}

export default async function SubchapterPage({ params }: PageProps) {
  const result = getSubchapter(params.chapter, params.subchapter);
  if (!result) {
    notFound();
  }

  const { subchapter } = result;
  const Content = (await subchapter.load(params.locale)).default;

  return (
    <article>
      <Content />
    </article>
  );
}
