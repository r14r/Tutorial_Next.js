import { notFound } from "next/navigation";
import { flattenSubchapters, getSubchapter } from "@/lib/chapters";

export function generateStaticParams() {
  return flattenSubchapters();
}

type PageProps = {
  params: {
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
  const Content = (await subchapter.import()).default;

  return (
    <article>
      <Content />
    </article>
  );
}
