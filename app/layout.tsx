import type { ReactNode } from 'react';
import { Inter } from 'next/font/google';
import './globals.css';
import { DEFAULT_LOCALE, isLocale } from '@/lib/i18n';

const inter = Inter({ subsets: ['latin'] });

export default function RootLayout({
	children,
	params,
}: {
	children: ReactNode;
	params: { locale?: string };
}) {
	const langParam = params?.locale;
	const lang = isLocale(langParam) ? langParam : DEFAULT_LOCALE;

	return (
		<html lang={lang} suppressHydrationWarning>
			<body className={inter.className}>{children}</body>
		</html>
	);
}
