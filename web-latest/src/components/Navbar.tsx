'use client';

import { Menu, X, Plane } from 'lucide-react';
import Link from 'next/link';
import { useState } from 'react';

import ThemeToggle from './ThemeToggle';

export default function MainNavbar() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const handleToggle = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <header className="sticky top-0 z-50 w-full bg-background/85 backdrop-blur-lg border-b border-border shadow-sm">
      <div className="container flex h-16 items-center justify-between px-4 sm:px-6 max-w-full">
        <Link href="/" className="flex items-center space-x-2">
          <Plane className="h-6 w-6 text-primary" />
          <span className="text-xl sm:text-2xl font-bold font-poppins bg-linear-to-r from-primary to-accent bg-clip-text text-transparent italic">
            TRAVELKING
          </span>
          <span className="text-xl sm:text-2xl font-black font-poppins animate-pulse-green italic ml-0.5">
            .LIVE
          </span>
        </Link>

        <nav className="hidden md:flex items-center gap-8">
          <Link
            href="/"
            className="text-sm font-bold uppercase tracking-widest text-foreground hover:text-primary transition-colors duration-200"
          >
            Home
          </Link>
          <Link
            href="/eu261/"
            className="text-sm font-bold uppercase tracking-widest text-foreground hover:text-primary transition-colors duration-200"
          >
            EU261 Guide
          </Link>
          <Link
            href="/privacy-policy/"
            className="text-sm font-bold uppercase tracking-widest text-foreground hover:text-primary transition-colors duration-200"
          >
            Privacy
          </Link>
          <button className="px-6 py-2 rounded-full bg-primary text-primary-foreground text-xs font-bold tracking-widest uppercase hover:scale-105 transition-all">
            Inquire Now
          </button>
          <ThemeToggle />
        </nav>

        <button
          type="button"
          className="md:hidden text-foreground hover:text-primary transition-colors duration-200"
          onClick={handleToggle}
        >
          {mobileMenuOpen ? (
            <X className="h-6 w-6" />
          ) : (
            <Menu className="h-6 w-6" />
          )}
        </button>

        {mobileMenuOpen && (
          <div className="fixed inset-x-0 top-16 z-50 bg-background border-b border-border shadow-lg md:hidden animate-in slide-in-from-top duration-300 max-w-full">
            <div className="container py-6 flex flex-col space-y-4 px-4 sm:px-6 max-w-full">
              <Link
                href="/"
                className="text-sm font-bold uppercase tracking-widest text-foreground hover:text-primary transition-colors duration-200"
                onClick={handleToggle}
              >
                Home
              </Link>
              <Link
                href="/eu261/"
                className="text-sm font-bold uppercase tracking-widest text-foreground hover:text-primary transition-colors duration-200"
                onClick={handleToggle}
              >
                EU261 Guide
              </Link>
              <div className="flex items-center justify-between">
                <button className="px-6 py-2 rounded-full bg-primary text-primary-foreground text-xs font-bold tracking-widest uppercase hover:scale-105 transition-all">
                  Inquire Now
                </button>
                <ThemeToggle />
              </div>
            </div>
          </div>
        )}
      </div>
    </header>
  );
}
