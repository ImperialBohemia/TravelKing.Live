'use client';

import { motion } from 'framer-motion';

export default function PrivacyPage() {
    return (
        <div className="flex flex-col items-center w-full min-h-screen bg-background pt-32 pb-24">
            <div className="container px-4 sm:px-6 max-w-4xl mx-auto">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="mb-16"
                >
                    <h1 className="text-4xl font-black italic uppercase tracking-tighter text-white">
                        Privacy <span className="bg-linear-to-r from-primary to-accent bg-clip-text text-transparent">Policy</span>
                    </h1>
                    <p className="text-muted-foreground mt-4 font-mono text-xs uppercase tracking-[0.2em]">Effective: February 2026</p>
                </motion.div>

                <div className="space-y-12 text-white/70 leading-relaxed font-light">
                    <section>
                        <h2 className="text-xl font-bold text-white uppercase mb-4 tracking-widest">1. Data Collection</h2>
                        <p>
                            TravelKing.Live collects only the necessary information required for travel coordination and
                            flight compensation claims. This includes contact details and travel itineraries.
                        </p>
                    </section>

                    <section>
                        <h2 className="text-xl font-bold text-white uppercase mb-4 tracking-widest">2. Usage of Information</h2>
                        <p>
                            Your data is used exclusively to facilitate your travel missions and to recover assets
                            from airlines under EU regulation 261/2004. We do not sell data to third-party entities.
                        </p>
                    </section>

                    <section>
                        <div className="p-8 border border-border rounded-2xl bg-white/5 italic">
                            "Privacy is the ultimate luxury. We operate with stealth and discretion."
                        </div>
                    </section>
                </div>
            </div>
        </div>
    );
}
