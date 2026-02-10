"use client";

import { motion } from "framer-motion";
import { Shield, Activity, Compass, Star, ChevronRight } from "lucide-react";

const fadeIn = {
  initial: { opacity: 0, y: 20 },
  whileInView: { opacity: 1, y: 0 },
  viewport: { once: true },
  transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] }
};

export const FeaturesSection = () => {
  return (
    <section className="w-full py-24 sm:py-32 relative">
      <div className="container px-4 sm:px-6 max-w-7xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-12 gap-8">
          <motion.div
            className="md:col-span-4 rounded-3xl bg-card border border-white/5 p-10 flex flex-col justify-between group hover:border-primary/50 transition-all"
            variants={fadeIn}
            initial="initial"
            whileInView="whileInView"
          >
            <Shield className="w-12 h-12 text-primary mb-8" />
            <div>
              <h4 className="text-2xl font-bold text-white uppercase italic tracking-tighter mb-4">EU261 Overdrive</h4>
              <p className="text-muted-foreground text-sm leading-relaxed mb-8">
                Instant legal extraction for delayed flights. We bypass standard queues via direct API links to enforcement bodies.
              </p>
              <button className="flex items-center text-[10px] font-black uppercase tracking-widest text-primary group-hover:gap-2 transition-all">
                Learn More <ChevronRight className="w-3 h-3" />
              </button>
            </div>
          </motion.div>

          <motion.div
            className="md:col-span-4 rounded-3xl bg-card border border-white/5 p-10 flex flex-col justify-between group hover:border-primary/50 transition-all"
            variants={fadeIn}
            initial="initial"
            whileInView="whileInView"
          >
            <Activity className="w-12 h-12 text-primary mb-8" />
            <div>
              <h4 className="text-2xl font-bold text-white uppercase italic tracking-tighter mb-4">Market Sniper</h4>
              <p className="text-muted-foreground text-sm leading-relaxed mb-8">
                Real-time error fare detection and high-alpha travel routes analyzed by OMEGA Neural engine.
              </p>
              <button className="flex items-center text-[10px] font-black uppercase tracking-widest text-primary group-hover:gap-2 transition-all">
                View Intel <ChevronRight className="w-3 h-3" />
              </button>
            </div>
          </motion.div>

          <motion.div
            className="md:col-span-4 rounded-3xl bg-card border border-white/5 p-10 flex flex-col justify-between group hover:border-primary/50 transition-all"
            variants={fadeIn}
            initial="initial"
            whileInView="whileInView"
          >
            <Compass className="w-12 h-12 text-primary mb-8" />
            <div>
              <h4 className="text-2xl font-bold text-white uppercase italic tracking-tighter mb-4">Sovereign Travel</h4>
              <p className="text-muted-foreground text-sm leading-relaxed mb-8">
                Diplomatic-grade logistics for individuals who require absolute privacy and optimized routing.
              </p>
              <button className="flex items-center text-[10px] font-black uppercase tracking-widest text-primary group-hover:gap-2 transition-all">
                Access Node <ChevronRight className="w-3 h-3" />
              </button>
            </div>
          </motion.div>

          {/* Large Row */}
          <motion.div
            className="md:col-span-4 rounded-3xl bg-primary/5 border border-primary/20 p-10 flex flex-col gap-6"
            variants={fadeIn}
            initial="initial"
            whileInView="whileInView"
          >
            <Star className="w-10 h-10 text-primary" />
            <h4 className="text-xl font-bold text-white uppercase italic tracking-tighter">Stealth Concierge</h4>
            <p className="text-muted-foreground text-sm">Anonymous booking & personalized security logistics for high-net-worth operations.</p>
          </motion.div>

          <motion.div
            className="md:col-span-8 rounded-3xl bg-linear-to-br from-secondary to-background border border-border p-12 relative overflow-hidden flex items-center justify-center group hover:border-primary/50 transition-all"
            variants={fadeIn}
            initial="initial"
            whileInView="whileInView"
          >
            <div className="absolute top-0 right-0 p-8 text-[8px] font-mono text-primary/30 uppercase tracking-[0.4em]">SYSTEM://OMEGA_DEPLOYED</div>
            <div className="text-center">
              <h4 className="text-4xl md:text-6xl font-black text-white mb-4 italic tracking-tighter group-hover:scale-105 transition-transform duration-700">BEYOND <span className="bg-linear-to-r from-primary to-accent bg-clip-text text-transparent">FIRST CLASS.</span></h4>
              <button className="text-[10px] font-black uppercase tracking-[0.5em] text-primary hover:text-white transition-colors mt-4">Initiate Protocol →</button>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
};
