"use client";

import { useState } from "react";

export default function SearchBox() {
    const [form, setForm] = useState({
        origin: "",
        destination: "",
        date: ""
    });

    const handleSearch = (e) => {
        e.preventDefault();
        // In a real app, this would trigger our TravelpayoutsConnector
        // For now, redirect to our affiliate search engine
        const dateStr = form.date.replace(/-/g, "");
        const url = `https://www.aviasales.com/search/${form.origin}${dateStr}${form.destination}1?marker=11089`;
        window.open(url, "_blank");
    };

    return (
        <section id="search" className="py-24 px-6 relative">
            <div className="max-w-6xl mx-auto">
                <div className="glass-card p-8 md:p-12 glow-gold">
                    <div className="flex flex-col md:flex-row md:items-end gap-6">
                        <div className="flex-1">
                            <label className="block text-xs uppercase tracking-widest text-slate-400 mb-3 font-bold">Origin</label>
                            <input
                                type="text"
                                placeholder="From (e.g. PRG)"
                                className="input-dark"
                                value={form.origin}
                                onChange={(e) => setForm({ ...form, origin: e.target.value.toUpperCase() })}
                            />
                        </div>
                        <div className="flex-1">
                            <label className="block text-xs uppercase tracking-widest text-slate-400 mb-3 font-bold">Destination</label>
                            <input
                                type="text"
                                placeholder="To (e.g. DXB)"
                                className="input-dark"
                                value={form.destination}
                                onChange={(e) => setForm({ ...form, destination: e.target.value.toUpperCase() })}
                            />
                        </div>
                        <div className="flex-1">
                            <label className="block text-xs uppercase tracking-widest text-slate-400 mb-3 font-bold">Travel Date</label>
                            <input
                                type="date"
                                className="input-dark"
                                value={form.date}
                                onChange={(e) => setForm({ ...form, date: e.target.value })}
                            />
                        </div>
                        <button
                            onClick={handleSearch}
                            className="btn-gold w-full md:w-auto px-10 h-[52px]"
                        >
                            Search Excellence
                        </button>
                    </div>

                    <div className="mt-8 flex flex-wrap gap-6 text-sm text-slate-400 items-center border-t border-white/5 pt-8">
                        <span className="flex items-center gap-2">
                            <span className="w-1.5 h-1.5 rounded-full bg-green-500" />
                            Live Pricing
                        </span>
                        <span className="flex items-center gap-2">
                            <span className="w-1.5 h-1.5 rounded-full bg-blue-500" />
                            Direct Carrier Deals
                        </span>
                        <span className="flex items-center gap-2">
                            <span className="w-1.5 h-1.5 rounded-full bg-purple-500" />
                            Business & First Class Priority
                        </span>
                    </div>
                </div>
            </div>
        </section>
    );
}
