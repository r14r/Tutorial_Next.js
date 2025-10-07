import { redirect } from 'next/navigation';

const DEFAULT_LOCALE = 'de';

export default function IndexPage() {
  redirect(`/${DEFAULT_LOCALE}`);
}
