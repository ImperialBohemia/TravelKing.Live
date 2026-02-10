"use client";

import { useState, useEffect } from "react";

export default function Navbar() {
    const [scrolled, setScrolled] = useState(false);

    useEffect(() => {
        const handleScroll = () => setScrolled(window.scrollY > 20);
        window.addEventListener("scroll", handleScroll);
        return () => window.removeEventListener("scroll", handleScroll);
    }, []);

    return (
        <nav
            className={`fixed top-0 left-0 right-0 z-50 transition-all duration-500 ${scrolled
                    ? "bg-slate-900/80 backdrop-blur-xl border-b border-white/5 py-4"
                    : "bg-transparent py-6"
                }`}
        >
            <div className="max-w-7xl mx-auto px-6 flex justify-between items-center">
                <div className="flex items-center gap-2">
                    <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-yellow-400 to-amber-600 flex items-center justify-center font-bold text-slate-900 text-sm">
                        TK
                    </div>
                    <span className="text-2xl font-black tracking-tight font-display text-white">
                        TRAVELKING<span className="text-gradient-gold">.LIVE</span>
                    </span>
                </div>

                <div className="hidden md:flex items-center gap-8 text-sm font-medium text-slate-300">
                    <a href="#search" className="hover:text-amber-400 transition-colors">Flights</a>
                    <a href="#services" className="hover:text-amber-400 transition-colors">Services</a>
                    <a href="#compensation" className="hover:text-amber-400 transition-colors">EU261 Guide</a>
                    <a href="#contact" className="hover:text-amber-400 transition-colors">Support</a>
                </div>

                <a href="#contact" className="btn-gold hidden sm:flex">
                    Concierge Support
                </a>
            </div>
        </nav>
    );
}
