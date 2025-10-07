import { redirect } from "next/navigation";
import { chapters, getChapterHref } from "@/lib/chapters";

export default function HomePage() {
  if (chapters.length === 0) {
    return null;
  }

  redirect(getChapterHref(chapters[0].slug));
}
