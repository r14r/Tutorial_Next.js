import type { ReactNode } from 'react';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export default function RootLayout({
	children,
	params,
}: {
	children: ReactNode;
	params: { locale?: string };
}) {
	const lang = params?.locale ?? 'en';

	return (
		<html lang={lang} suppressHydrationWarning>
			<body className={inter.className}>{children}</body>
		</html>
	);
}
