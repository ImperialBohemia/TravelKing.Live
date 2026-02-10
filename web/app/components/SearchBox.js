"use client";

import { useState } from "react";

export default function SearchBox() {
    const [from, setFrom] = useState("");
    const [to, setTo] = useState("");

    const handleSearch = () => {
        if (!from || !to) return;
        const url = `https://www.jetradar.com/flights/?origin=${from}&destination=${to}&origin_name=${from}&destination_name=${to}&marker=532822&locale=en`;
        window.open(url, "_blank");
    };

    return (
        <section id="search" className="py-20 px-6 -mt-20 relative z-20">
            <div className="max-w-5xl mx-auto glass-pane p-1 shadow-2xl rounded-3xl">
                <div className="bg-deep-space/60 rounded-[calc(1.5rem-2px)] p-8 md:p-12 relative overflow-hidden">
                    {/* Subtle decoration */}
                    <div className="absolute top-0 right-0 w-64 h-64 bg-gold-bright/5 blur-3xl rounded-full -mr-32 -mt-32"></div>

                    <div className="flex flex-col md:flex-row items-end gap-6 relative z-10">
                        <div className="flex-1 w-full group">
                            <label className="block text-[10px] uppercase font-black tracking-[0.2em] text-gold-soft mb-3 ml-1">Origin Port</label>
                            <input
                                type="text"
                                placeholder="City or Airport (e.g. PRG)"
                                className="w-full bg-white/5 border border-white/10 px-6 py-5 rounded-2xl text-white focus:outline-none focus:border-gold-bright transition-all placeholder:text-slate-600 font-display text-lg"
                                value={from}
                                onChange={(e) => setFrom(e.target.value.toUpperCase())}
                            />
                        </div>

                        <div className="flex items-center justify-center h-16 w-16 mb-2 hidden md:flex">
                            <span className="text-2xl opacity-20 group-hover:opacity-100 transition-opacity">⇌</span>
                        </div>

                        <div className="flex-1 w-full">
                            <label className="block text-[10px] uppercase font-black tracking-[0.2em] text-gold-soft mb-3 ml-1">Destination Target</label>
                            <input
                                type="text"
                                placeholder="Target Destination (e.g. DXB)"
                                className="w-full bg-white/5 border border-white/10 px-6 py-5 rounded-2xl text-white focus:outline-none focus:border-gold-bright transition-all placeholder:text-slate-600 font-display text-lg"
                                value={to}
                                onChange={(e) => setTo(e.target.value.toUpperCase())}
                            />
                        </div>

                        <button
                            onClick={handleSearch}
                            className="w-full md:w-auto noble-button !rounded-2xl h-[68px] mb-[2px] min-w-[180px]"
                        >
                            Analyze Flights
                        </button>
                    </div>

                    <div className="mt-8 flex items-center gap-6 text-[10px] font-bold text-slate-500 tracking-widest uppercase opacity-60">
                        <div className="flex items-center gap-2">
                            <span className="w-1 h-1 rounded-full bg-green-500"></span>
                            Live Market Feed
                        </div>
                        <div className="flex items-center gap-2">
                            <span className="w-1 h-1 rounded-full bg-gold-bright"></span>
                            Neural Pricing Active
                        </div>
                        <div className="ml-auto hidden sm:block">
                            Provider Node: 532822
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}
