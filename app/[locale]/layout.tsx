import { ReactNode } from 'react';
import { NextIntlClientProvider } from 'next-intl';
import { notFound } from 'next/navigation';
import HeaderNav from '@/components/HeaderNav';
import Sidebar from '@/components/Sidebar';

export default async function LocaleLayout({
  children,
  params: { locale },
}: {
  children: ReactNode;
  params: { locale: string };
}) {
  let messages;
  try {
    messages = (await import(`../../messages/${locale}.json`)).default;
  } catch (error) {
    notFound();
  }
  return (
    <NextIntlClientProvider locale={locale} messages={messages}>
      <div className="app-container" data-locale={locale}>
        <HeaderNav />
        <div className="content-wrapper">
          <Sidebar />
          <main>{children}</main>
        </div>
      </div>
    </NextIntlClientProvider>
  );
}
