"use client";

import { useState } from "react";
import Link from "next/link";
import { Menu, X } from "lucide-react";
import { Button } from "../ui/Button";

export function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => setIsMenuOpen(!isMenuOpen);

  return (
    <header className="sticky top-0 z-50 w-full border-b border-border bg-background/80 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-16 items-center justify-between">
        <Link href="/" className="flex items-center space-x-2">
          <span className="text-xl font-black italic tracking-tighter font-sans">
            TRAVELKING<span className="text-accent animate-pulse-green">.LIVE</span>
          </span>
        </Link>

        {/* Desktop Nav */}
        <nav className="hidden md:flex items-center gap-6 text-sm font-medium uppercase tracking-widest font-sans">
          <Link href="/eu261" className="hover:text-primary transition-colors">Compensation</Link>
          <Link href="/about" className="hover:text-primary transition-colors">Intel Network</Link>
          <Link href="/contact" className="hover:text-primary transition-colors">Contact</Link>
          <Button variant="accent" size="sm" asChild>
            <Link href="https://aviasales.tp.st/495365" target="_blank">Book Flights</Link>
          </Button>
        </nav>

        {/* Mobile Menu Button */}
        <button
          className="md:hidden p-2 text-foreground hover:text-primary transition-colors"
          onClick={toggleMenu}
          aria-label="Toggle menu"
        >
          {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      {/* Mobile Nav Overlay */}
      {isMenuOpen && (
        <div className="md:hidden fixed inset-0 top-16 z-50 bg-background/95 backdrop-blur-3xl border-t border-border p-6 flex flex-col gap-6 animate-in slide-in-from-top-5">
          <nav className="flex flex-col gap-6 text-lg font-black uppercase tracking-widest font-sans text-center">
            <Link href="/" onClick={toggleMenu} className="hover:text-accent transition-colors">Intelligence Feed</Link>
            <Link href="/eu261" onClick={toggleMenu} className="hover:text-accent transition-colors">EU261 Compensation</Link>
            <Link href="/about" onClick={toggleMenu} className="hover:text-accent transition-colors">The Network</Link>
            <Link href="/contact" onClick={toggleMenu} className="hover:text-accent transition-colors">Contact Protocol</Link>
            <Link href="/privacy-policy" onClick={toggleMenu} className="text-sm text-muted-foreground hover:text-white">Privacy</Link>
            <Link href="/terms" onClick={toggleMenu} className="text-sm text-muted-foreground hover:text-white">Terms</Link>
          </nav>
          <div className="mt-auto">
             <Button variant="accent" size="lg" className="w-full" asChild>
                <Link href="https://aviasales.tp.st/495365" target="_blank" onClick={toggleMenu}>
                  Access Flight Systems
                </Link>
             </Button>
          </div>
        </div>
      )}
    </header>
  );
}
