"use client";

import { useState } from 'react';
import { Button } from '../ui/Button';
import { Plane, Search } from 'lucide-react';

export function FlightSearch() {
  const [origin, setOrigin] = useState('');
  const [destination, setDestination] = useState('');

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    // Redirect to Aviasales affiliate link
    // Fallback to generic link if empty, or try to construct deep link
    // For now, just open the main partner link which tracks cookies
    window.open('https://aviasales.tp.st/495365', '_blank');
  };

  return (
    <div className="w-full max-w-4xl mx-auto -mt-24 relative z-20 px-4">
      <div className="bg-card/90 backdrop-blur-xl border border-border p-6 rounded-2xl shadow-2xl">
        <form onSubmit={handleSearch} className="grid md:grid-cols-[1fr_1fr_auto] gap-4">
          <div className="relative group">
            <Plane className="absolute left-4 top-1/2 -translate-y-1/2 text-muted-foreground group-focus-within:text-primary transition-colors" size={20} />
            <input
              type="text"
              placeholder="Origin (e.g. LON)"
              className="w-full h-14 pl-12 bg-background/50 border border-border rounded-xl focus:border-primary outline-none text-white uppercase font-bold tracking-widest placeholder:text-muted-foreground/50"
              value={origin}
              onChange={(e) => setOrigin(e.target.value.toUpperCase())}
            />
          </div>

          <div className="relative group">
            <Plane className="absolute left-4 top-1/2 -translate-y-1/2 text-muted-foreground group-focus-within:text-primary transition-colors rotate-90" size={20} />
            <input
              type="text"
              placeholder="Destination (e.g. NYC)"
              className="w-full h-14 pl-12 bg-background/50 border border-border rounded-xl focus:border-primary outline-none text-white uppercase font-bold tracking-widest placeholder:text-muted-foreground/50"
              value={destination}
              onChange={(e) => setDestination(e.target.value.toUpperCase())}
            />
          </div>

          <Button size="lg" className="h-14 px-8 text-lg font-black bg-accent text-black hover:bg-accent/90 shadow-[0_0_20px_rgba(0,255,154,0.3)]">
            <Search className="mr-2" size={20} /> SEARCH
          </Button>
        </form>
        <div className="mt-4 flex items-center justify-center gap-2 text-[10px] uppercase tracking-widest text-muted-foreground">
          <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
          Connected to Global Flight Database (Aviasales)
        </div>
      </div>
    </div>
  );
}
