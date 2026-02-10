"use client";

import { motion } from "framer-motion";
import { Zap } from "lucide-react";

const fadeIn = {
  initial: { opacity: 0, y: 20 },
  whileInView: { opacity: 1, y: 0 },
  viewport: { once: true },
  transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] }
};

export const HeroSection = () => {
  return (
    <section className="w-full min-h-[90vh] flex flex-col items-center justify-center relative overflow-hidden bg-black pt-20">
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-primary/10 via-transparent to-transparent opacity-50" />

      {/* Decorative Grid */}
      <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-20 mix-blend-overlay pointer-events-none" />

      <div className="container px-4 sm:px-6 max-w-7xl mx-auto relative z-10">
        <div className="flex flex-col items-center space-y-12 text-center">
          <motion.div
            className="inline-flex items-center rounded-full border border-primary/30 bg-primary/5 px-6 py-2 text-[10px] font-black uppercase tracking-[0.4em] text-primary backdrop-blur-xl"
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.5 }}
          >
            <span className="relative flex h-2 w-2 mr-3">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-primary"></span>
            </span>
            System Status: Omega Active
          </motion.div>

          <div className="space-y-6">
            <motion.h1
              className="text-6xl sm:text-8xl md:text-9xl font-black tracking-tighter italic uppercase text-white leading-[0.85]"
              initial={{ opacity: 0, y: 40 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2, duration: 1, ease: [0.16, 1, 0.3, 1] }}
            >
              Travel <br />
              <span className="bg-linear-to-r from-primary via-accent to-primary bg-clip-text text-transparent animate-gradient-x">Supremacy.</span>
            </motion.h1>

            <motion.p
              className="mx-auto max-w-[800px] text-muted-foreground text-lg sm:text-2xl font-light tracking-tight leading-relaxed"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.5, duration: 1 }}
            >
              The OMEGA Hub for elite flight intelligence, high-stakes compensation recovery,
              and sovereign travel logistics. Powered by Neural OMEGA v4.
            </motion.p>
          </div>

          <motion.div
            className="flex flex-col sm:flex-row gap-6 w-full sm:w-auto"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.8 }}
          >
            <button
              onClick={() => document.getElementById('search')?.scrollIntoView({ behavior: 'smooth' })}
              className="h-16 inline-flex items-center justify-center rounded-full bg-primary px-12 text-xs font-black uppercase tracking-widest text-primary-foreground shadow-2xl shadow-primary/20 hover:bg-accent transition-all duration-300 hover:scale-105 active:scale-95 group"
            >
              Enter Dashboard
              <Zap className="ml-3 h-4 w-4 fill-current group-hover:rotate-12 transition-transform" />
            </button>
            <button className="h-16 inline-flex items-center justify-center rounded-full border border-white/10 bg-white/5 px-12 text-xs font-black uppercase tracking-widest text-white backdrop-blur-xl hover:bg-white/10 transition-all">
              Read Manifesto
            </button>
          </motion.div>
        </div>
      </div>

      {/* Background Elements */}
      <div className="absolute bottom-0 left-0 w-full h-64 bg-linear-to-t from-background to-transparent pointer-events-none" />
    </section>
  );
};
