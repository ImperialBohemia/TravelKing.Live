import type { Metadata } from "next";
import { Inter, Poppins } from "next/font/google";
import "./globals.css";
import Script from "next/script";
import Link from "next/link";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });
const poppins = Poppins({
  weight: ["400", "700", "900"],
  subsets: ["latin"],
  variable: "--font-poppins"
});

export const metadata: Metadata = {
  title: "TravelKing.Live | Travel Intelligence & Elite Logistics",
  description: "Advanced flight hacks, safety intel, and elite travel logistics orchestration.",
  robots: "noindex, nofollow", // As per user rules until 'Ready'
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <Script id="monetization" strategy="afterInteractive">
          {`
            (function () {
                var script = document.createElement("script");
                script.async = 1;
                script.src = 'https://emrldtp.cc/NDk1MzY1.js?t=495365';
                document.head.appendChild(script);
            })();
          `}
        </Script>
      </head>
      <body className={`${inter.variable} ${poppins.variable} font-sans min-h-screen flex flex-col`}>
        <a
          href="#main-content"
          className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 bg-primary text-black px-4 py-2 z-[100] font-bold rounded-md"
        >
          Skip to content
        </a>
        <nav className="sticky top-0 z-50 glass h-16 flex items-center px-4 md:px-8 justify-between">
          <Link href="/" className="flex items-center gap-2 hover:opacity-80 transition-opacity" aria-label="TravelKing.Live Home">
            <span className="text-xl font-black italic tracking-tighter">TRAVELKING</span>
            <span className="text-xl font-black text-primary animate-pulse-gold italic">.LIVE</span>
          </Link>
          <div className="hidden md:flex gap-8 text-[10px] font-bold uppercase tracking-widest">
            <Link href="/" className="hover:text-primary transition-colors">Intelligence</Link>
            <Link href="/about" className="hover:text-primary transition-colors">The Network</Link>
            <Link href="/contact" className="hover:text-primary transition-colors">Contact Protocol</Link>
          </div>
        </nav>
        <main id="main-content" className="flex-1">
          {children}
        </main>
        <footer className="py-12 border-t border-border bg-black text-center">
          <p className="text-[10px] uppercase tracking-[0.4em] text-muted-foreground">© 2026 TRAVELKING OPERATIONAL INTELLIGENCE</p>
        </footer>
      </body>
    </html>
  );
}
