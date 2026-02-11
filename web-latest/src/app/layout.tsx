import type { Metadata } from "next";
import { Oswald, Azeret_Mono } from "next/font/google";
import "./globals.css";
import Script from "next/script";
import { Header } from "../components/layout/Header";
import { Footer } from "../components/layout/Footer";

const oswald = Oswald({
  subsets: ["latin"],
  variable: "--font-oswald",
  display: "swap",
});

const azeret = Azeret_Mono({
  subsets: ["latin"],
  variable: "--font-azeret",
  display: "swap",
});

export const metadata: Metadata = {
  title: "TravelKing.Live | Elite Flight Intelligence",
  description: "The autonomous authority for flight compensation and travel logistics. Powered by OMEGA.",
  openGraph: {
    title: "TravelKing.Live | Elite Flight Intelligence",
    description: "The autonomous authority for flight compensation and travel logistics.",
    url: "https://www.travelking.live",
    siteName: "TravelKing",
    locale: "en_US",
    type: "website",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
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
        <Script id="google-analytics" strategy="afterInteractive" src="https://www.googletagmanager.com/gtag/js?id=G-CENSTCTLCW" />
        <Script id="ga-setup" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-CENSTCTLCW');
          `}
        </Script>
      </head>
      <body className={`${oswald.variable} ${azeret.variable} font-sans min-h-screen flex flex-col bg-background text-foreground antialiased`}>
        <Header />
        <main className="flex-1 w-full">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  );
}
