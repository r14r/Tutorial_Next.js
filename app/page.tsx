import { debug } from '@/lib/debug';
import { redirect } from 'next/navigation';
import { DEFAULT_LOCALE } from '@/lib/i18n';

export default function IndexPage() {
  debug('Redirecting to default locale...');
  redirect(`/${DEFAULT_LOCALE}`);
}
