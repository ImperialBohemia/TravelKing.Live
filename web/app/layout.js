import "./globals.css";

export const metadata = {
  title: "TravelKing.Live | Premium Flight Deals & Travel Assistance",
  description:
    "Find the cheapest flights, get expert EU261 compensation guidance, and discover luxury travel deals. AI-powered travel concierge for smart travelers.",
  keywords: [
    "cheap flights",
    "flight deals",
    "EU261 compensation",
    "flight delay compensation",
    "travel assistant",
    "private jet",
    "luxury travel",
    "flight search",
    "TravelKing",
  ],
  authors: [{ name: "TravelKing" }],
  robots: "noindex, nofollow",
  openGraph: {
    title: "TravelKing.Live | Premium Flight Deals & Travel Assistance",
    description:
      "AI-powered travel concierge. Find cheapest flights, get flight compensation, discover luxury deals.",
    url: "https://travelking.live",
    siteName: "TravelKing.Live",
    type: "website",
    locale: "en_GB",
  },
  twitter: {
    card: "summary_large_image",
    title: "TravelKing.Live | Premium Travel",
    description:
      "AI-powered travel concierge. Flights, compensation, luxury deals.",
  },
  other: {
    "theme-color": "#0a0e1a",
  },
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin="anonymous"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@300;400;600;700;800;900&display=swap"
          rel="stylesheet"
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
