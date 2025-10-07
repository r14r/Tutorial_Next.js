import type { Metadata } from "next";
import type { ReactNode } from "react";
import { Inter } from "next/font/google";
import "./globals.css";
import HeaderNav from "@/components/HeaderNav";
import Sidebar from "@/components/Sidebar";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: {
    default: "Next.js Tutorial",
    template: "%s • Next.js Tutorial",
  },
  description:
    "A learning environment with chapters and subchapters rendered from Markdown and MDX.",
};

export default function RootLayout({
  children,
}: {
  children: ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="app-container">
          <HeaderNav />
          <div className="content-wrapper">
            <Sidebar />
            <main>{children}</main>
          </div>
        </div>
      </body>
    </html>
  );
}
