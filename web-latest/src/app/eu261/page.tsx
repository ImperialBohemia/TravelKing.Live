'use client';

import { motion } from 'framer-motion';
import { ShieldAlert, FileText, CheckCircle } from 'lucide-react';

export default function EU261Page() {
    const fadeIn = {
        initial: { opacity: 0, y: 20 },
        animate: { opacity: 1, y: 0, transition: { duration: 0.6 } },
    };

    return (
        <div className="flex flex-col items-center w-full min-h-screen bg-background pt-32 pb-24">
            <div className="container px-4 sm:px-6 max-w-4xl mx-auto">
                <motion.div {...fadeIn} className="text-center mb-16">
                    <ShieldAlert className="w-16 h-16 text-primary mx-auto mb-6" />
                    <h1 className="text-4xl sm:text-6xl font-black italic uppercase tracking-tighter text-white">
                        EC No 261/2004 <span className="bg-linear-to-r from-primary to-accent bg-clip-text text-transparent">Compliance</span>
                    </h1>
                    <p className="text-muted-foreground mt-6 text-xl font-light">
                        Your rights as a passenger are protected by European law.
                        We ensure you receive the maximum compensation you are entitled to.
                    </p>
                </motion.div>

                <div className="grid gap-12 text-white/80 leading-relaxed">
                    <motion.section {...fadeIn} transition={{ delay: 0.1 }}>
                        <h2 className="text-2xl font-bold text-primary uppercase flex items-center gap-3 mb-4">
                            <FileText className="w-6 h-6" /> Overview
                        </h2>
                        <p>
                            Regulation (EC) No 261/2004 establishes common rules on compensation and assistance to passengers
                            in the event of denied boarding and of cancellation or long delay of flights.
                        </p>
                    </motion.section>

                    <motion.section {...fadeIn} transition={{ delay: 0.2 }}>
                        <h2 className="text-2xl font-bold text-primary uppercase flex items-center gap-3 mb-4">
                            <CheckCircle className="w-6 h-6" /> Eligibility
                        </h2>
                        <ul className="list-disc pl-6 space-y-4 font-light">
                            <li>Flights departing from an airport located in an EU Member State.</li>
                            <li>Flights arriving in an EU Member State from a third country if the carrier is an EU airline.</li>
                            <li>Conditions: You must have a confirmed reservation and have checked in on time.</li>
                        </ul>
                    </motion.section>

                    <motion.section {...fadeIn} transition={{ delay: 0.3 }} className="p-8 rounded-3xl border border-border bg-white/5">
                        <h2 className="text-2xl font-bold text-white uppercase mb-4 tracking-tight italic">Compensation Levels</h2>
                        <div className="grid sm:grid-cols-3 gap-6">
                            <div className="p-4 border border-white/10 rounded-xl">
                                <div className="text-2xl font-black text-primary">€250</div>
                                <div className="text-[10px] uppercase opacity-50 font-bold">Short distance (&lt;1500km)</div>
                            </div>
                            <div className="p-4 border border-white/10 rounded-xl">
                                <div className="text-2xl font-black text-primary">€400</div>
                                <div className="text-[10px] uppercase opacity-50 font-bold">Medium distance (1500-3500km)</div>
                            </div>
                            <div className="p-4 border border-white/10 rounded-xl">
                                <div className="text-2xl font-black text-primary">€600</div>
                                <div className="text-[10px] uppercase opacity-50 font-bold">Long distance (&gt;3500km)</div>
                            </div>
                        </div>
                    </motion.section>
                </div>
            </div>
        </div>
    );
}
