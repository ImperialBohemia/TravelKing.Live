"use client";

export default function Hero() {
    return (
        <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
            {/* Dynamic Background */}
            <div
                className="absolute inset-0 z-0 bg-cover bg-center transition-transform duration-[10000ms] hover:scale-110"
                style={{ backgroundImage: "url('/hero-bg.png')" }}
            >
                <div className="absolute inset-0 bg-gradient-to-b from-deep-space/40 via-deep-space/60 to-deep-space"></div>
                <div className="absolute inset-0 bg-gradient-to-r from-deep-space via-transparent to-transparent opacity-80"></div>
            </div>

            {/* Content */}
            <div className="relative z-10 max-w-7xl mx-auto px-6 w-full pt-20">
                <div className="max-w-3xl">
                    <div className="flex items-center gap-4 mb-8">
                        <div className="h-[1px] w-12 bg-gold-bright"></div>
                        <span className="text-gold-bright uppercase tracking-[0.5em] text-[10px] font-bold">Official Industry Leader</span>
                    </div>

                    <h1 className="text-6xl md:text-8xl font-black text-white leading-none font-display mb-8">
                        THE ART OF <br />
                        <span className="text-gradient-gold">SUPREMACY.</span>
                    </h1>

                    <p className="text-xl md:text-2xl text-slate-300 mb-12 leading-relaxed font-light max-w-2xl">
                        Experience travel without boundaries. From neural flight discovery to
                        elite EC No 261/2004 protection, we define the orbit of modern luxury.
                    </p>

                    <div className="flex flex-wrap gap-6">
                        <a href="#search" className="noble-button">
                            Explore Missions
                        </a>
                        <button className="px-8 py-4 rounded-full border border-white/10 hover:border-gold-bright/30 text-white flex items-center gap-3 transition-all backdrop-blur-md">
                            <span className="w-2 h-2 rounded-full bg-gold-bright animate-pulse"></span>
                            Download Dossier
                        </button>
                    </div>
                </div>

                {/* Enterprise Stats Panel */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-8 mt-24 border-t border-white/5 pt-12">
                    {[
                        { label: "Missions Completed", value: "14,820+" },
                        { label: "Recovered Assets", value: "€9.4M" },
                        { label: "Global Presence", value: "192 CTIES" },
                        { label: "Concierge Status", value: "ELITE" }
                    ].map((stat, i) => (
                        <div key={i} className="reveal-up active" style={{ transitionDelay: `${i * 100}ms` }}>
                            <div className="text-2xl font-black text-white mb-1 font-display tracking-tight">{stat.value}</div>
                            <div className="text-[10px] uppercase tracking-widest text-slate-500 font-bold">{stat.label}</div>
                        </div>
                    ))}
                </div>
            </div>

            {/* Scroll indicator */}
            <div className="absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 opacity-30">
                <div className="w-[1px] h-20 bg-gradient-to-b from-gold-bright to-transparent"></div>
                <span className="text-[10px] uppercase tracking-widest text-white rotate-90 mt-8">Scroll</span>
            </div>
        </section>
    );
}
