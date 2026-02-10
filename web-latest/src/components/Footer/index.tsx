'use client';

import Link from 'next/link';
import { Suspense } from 'react';
import { getCurrentYear } from '@/lib/date';

function CurrentYear() {
  const currentYear = getCurrentYear();
  return <>{currentYear}</>;
}

export default function MainFooter() {

  return (
    <footer className="w-full py-12 bg-card border-t border-white/5">
      <div className="container px-4 md:px-6 flex flex-col md:flex-row items-center justify-between gap-8 max-w-7xl mx-auto">
        <div className="flex flex-col items-center md:items-start gap-2">
          <span className="text-xl font-black text-white italic tracking-tighter">
            TRAVELKING
          </span>
          <span className="text-[10px] uppercase tracking-widest text-muted-foreground font-bold">
            © <Suspense fallback="2026"><CurrentYear /></Suspense> OMEGA OPERATIONAL GROUP.
          </span>
        </div>
        <nav className="flex flex-wrap justify-center gap-8 uppercase text-[10px] font-black tracking-widest">
          <Link
            href="/eu261/"
            className="text-muted-foreground hover:text-primary transition-colors"
          >
            EU261 Compliance
          </Link>
          <Link
            href="/privacy-policy/"
            className="text-muted-foreground hover:text-primary transition-colors"
          >
            Privacy Protocol
          </Link>
          <Link
            href="mailto:concierge@travelking.live"
            className="text-muted-foreground hover:text-primary transition-colors"
          >
            Encryption Key
          </Link>
        </nav>
      </div>
    </footer>
  );
}
