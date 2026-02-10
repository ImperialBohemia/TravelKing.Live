export default function Hero() {
    return (
        <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
            {/* Background Video/Image Placeholder */}
            <div
                className="absolute inset-0 bg-cover bg-center scale-105 transition-transform duration-[10000ms] ease-out"
                style={{
                    backgroundImage: "url('https://images.unsplash.com/photo-1540339832862-4ec701633513?auto=format&fit=crop&q=80&w=2560')",
                    animation: "zoom-out-slow 20s infinite alternate"
                }}
            />
            <div className="hero-overlay" />

            <div className="relative z-10 max-w-7xl mx-auto px-6 text-center">
                <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/5 border border-white/10 backdrop-blur-md mb-8 animate-fade-in">
                    <span className="w-2 h-2 rounded-full bg-amber-400 animate-pulse" />
                    <span className="text-xs font-bold tracking-widest text-amber-200 uppercase">Premium Travel Concierge</span>
                </div>

                <h1 className="text-5xl md:text-8xl font-black text-white mb-6 tracking-tight leading-[0.9] font-display">
                    REDEFINE YOUR <br />
                    <span className="text-gradient-gold">HORIZON.</span>
                </h1>

                <p className="max-w-2xl mx-auto text-lg md:text-xl text-slate-300 mb-10 font-light leading-relaxed">
                    Elite flight solutions, expert EU261 compensation rescue, and access to the world's
                    most exclusive destinations. Where logic meets luxury.
                </p>

                <div className="flex flex-col sm:flex-row gap-4 justify-center">
                    <a href="#search" className="btn-gold">
                        Explore Flight Deals
                    </a>
                    <a href="#compensation" className="btn-outline">
                        EU261 Rescue Guide
                    </a>
                </div>

                <div className="mt-20 grid grid-cols-2 md:grid-cols-4 gap-8 max-w-4xl mx-auto border-t border-white/10 pt-10">
                    <div className="text-center">
                        <div className="stat-number text-white">4k+</div>
                        <div className="text-xs uppercase tracking-widest text-slate-400 mt-2">Private Rescue Jets</div>
                    </div>
                    <div className="text-center">
                        <div className="stat-number text-white">100%</div>
                        <div className="text-xs uppercase tracking-widest text-slate-400 mt-2">Success Rate</div>
                    </div>
                    <div className="text-center">
                        <div className="stat-number text-white">24/7</div>
                        <div className="text-xs uppercase tracking-widest text-slate-400 mt-2">Elite Concierge</div>
                    </div>
                    <div className="text-center">
                        <div className="stat-number text-white">€600</div>
                        <div className="text-xs uppercase tracking-widest text-slate-400 mt-2">Max EU261 Claim</div>
                    </div>
                </div>
            </div>
        </section>
    );
}
