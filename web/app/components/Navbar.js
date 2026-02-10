"use client";

import { useState, useEffect } from "react";

export default function Navbar() {
    const [isScrolled, setIsScrolled] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            setIsScrolled(window.scrollY > 50);
        };
        window.addEventListener("scroll", handleScroll);
        return () => window.removeEventListener("scroll", handleScroll);
    }, []);

    return (
        <nav
            className={`fixed top-0 left-0 right-0 z-50 transition-all duration-700 ${isScrolled ? "py-4 bg-deep-space/80 backdrop-blur-xl border-b border-white/5" : "py-8 bg-transparent"
                }`}
        >
            <div className="max-w-7xl mx-auto px-6 flex items-center justify-between">
                <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-gold-soft to-gold-bright flex items-center justify-center font-black text-black shadow-lg shadow-gold-bright/20">
                        TK
                    </div>
                    <span className="text-2xl font-black tracking-tighter text-white font-display">
                        TRAVEL<span className="text-gold-bright">KING</span>
                        <span className="text-[10px] uppercase tracking-[0.3em] block -mt-1 opacity-50">Private Concierge</span>
                    </span>
                </div>

                <div className="hidden md:flex items-center gap-10">
                    {["Flights", "Services", "EU261 Guide", "Support"].map((item) => (
                        <a
                            key={item}
                            href={`#${item.toLowerCase().split(' ')[0]}`}
                            className="text-sm font-medium uppercase tracking-widest text-slate-400 hover:text-gold-bright transition-colors"
                        >
                            {item}
                        </a>
                    ))}
                    <button className="px-6 py-2 rounded-full border border-gold-bright/30 text-gold-bright hover:bg-gold-bright hover:text-black transition-all text-xs font-bold tracking-widest uppercase">
                        Inquire Now
                    </button>
                </div>

                <div className="md:hidden text-white text-2xl">
                    <span className="cursor-pointer">☰</span>
                </div>
            </div>
        </nav>
    );
}
