// app/layout.tsx
import { Inter, Poppins } from 'next/font/google';
import { Toaster } from 'react-hot-toast';

import MainFooter from '@/components/Footer';
import MainNavbar from '@/components/Navbar';
import { QueryProvider } from '@/providers/query';
import { ThemeProvider } from '@/providers/theme';
import '@/styles/globals.css';
import type { ChildrenProps } from '@/types';

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
  adjustFontFallback: false,
});

const poppins = Poppins({
  weight: ['400', '500', '600', '700'],
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-poppins',
});

export const metadata = {
  title: 'TravelKing.Live | Premium Flight Deals & Travel Assistance',
  description:
    'Find the cheapest flights, get expert EU261 compensation guidance, and discover luxury travel deals. AI-powered travel concierge for smart travelers.',
  keywords: [
    'cheap flights',
    'flight deals',
    'EU261 compensation',
    'flight delay compensation',
    'travel assistant',
    'private jet',
    'luxury travel',
    'flight search',
    'TravelKing',
  ],
  authors: [{ name: 'TravelKing' }],
  robots: 'noindex, nofollow',
  openGraph: {
    title: 'TravelKing.Live | Premium Flight Deals & Travel Assistance',
    description:
      'AI-powered travel concierge. Find cheapest flights, get flight compensation, discover luxury deals.',
    url: 'https://travelking.live',
    siteName: 'TravelKing.Live',
    type: 'website',
    locale: 'en_GB',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'TravelKing.Live | Premium Travel',
    description:
      'AI-powered travel concierge. Flights, compensation, luxury deals.',
  },
  other: {
    'theme-color': '#0a0e1a',
  },
};

export default function RootLayout({ children }: ChildrenProps) {
  return (
    <html lang="en" suppressHydrationWarning className="overflow-x-hidden">
      <body
        className={`${inter.variable} ${poppins.variable} font-sans antialiased overflow-x-hidden`}
      >
        <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
          <QueryProvider>
            <div className="flex min-h-screen bg-background w-full overflow-x-hidden">
              <div className="flex-1 flex flex-col w-full">
                <MainNavbar />
                <main className="flex-1 w-full overflow-x-hidden">
                  {children}
                </main>
                <MainFooter />
              </div>
            </div>
            <Toaster
              position="bottom-right"
              toastOptions={{
                className: 'bg-card text-foreground border-border',
                duration: 3000,
              }}
            />
          </QueryProvider>
        </ThemeProvider>
      </body>
    </html>
  );
}
