"use client";

import { motion } from "framer-motion";
import { Globe, Award } from "lucide-react";

const fadeIn = {
  initial: { opacity: 0, y: 20 },
  whileInView: { opacity: 1, y: 0 },
  viewport: { once: true },
  transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] }
};

export const MapSection = () => {
  return (
    <section className="w-full py-24 sm:py-32 relative overflow-hidden">
      <div className="container px-4 sm:px-6 max-w-7xl mx-auto flex flex-col items-center">
        <motion.div
          className="w-full flex flex-col md:flex-row items-center justify-between gap-12"
          variants={fadeIn}
          initial="initial"
          whileInView="whileInView"
        >
          <div className="max-w-xl">
            <h2 className="text-sm font-black text-primary tracking-[0.5em] uppercase mb-4">World Network</h2>
            <h3 className="text-4xl sm:text-5xl font-black text-white italic uppercase tracking-tighter">GLOBAL <span className="opacity-50">OPERATIONAL</span> INTELLIGENCE</h3>
            <p className="text-muted-foreground mt-8 text-lg font-light leading-relaxed">
              Our network spans 14 global data centers and 192 major travel hubs. We operate in real-time,
              cross-referencing localized pricing nodes to ensure the absolute floor for premium and business ticketing.
            </p>
            <div className="mt-12 grid grid-cols-3 gap-6">
              <div className="flex flex-col gap-1">
                <span className="text-white font-bold text-2xl">24/7</span>
                <span className="text-muted-foreground text-[8px] uppercase tracking-widest">Active Monitoring</span>
              </div>
              <div className="flex flex-col gap-1">
                <span className="text-white font-bold text-2xl">100%</span>
                <span className="text-muted-foreground text-[8px] uppercase tracking-widest">Client Privacy</span>
              </div>
              <div className="flex flex-col gap-1">
                <span className="text-white font-bold text-2xl">1ms</span>
                <span className="text-muted-foreground text-[8px] uppercase tracking-widest">Sync Latency</span>
              </div>
            </div>
          </div>
          <div className="relative group">
            <div className="absolute -inset-1 rounded-full bg-linear-to-r from-primary to-accent opacity-20 blur-2xl group-hover:opacity-40 transition-opacity"></div>
            <Globe className="w-64 h-64 md:w-96 md:h-96 text-primary/20 relative animate-pulse" />
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center gap-2">
              <Award className="w-12 h-12 text-primary" />
              <span className="text-white font-black text-xl italic tracking-[0.2em]">TK_OMEGA</span>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};
