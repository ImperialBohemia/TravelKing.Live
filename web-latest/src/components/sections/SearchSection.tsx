"use client";

import { motion } from "framer-motion";
import { Search, Plane, MapPin, Calendar, ArrowRight } from "lucide-react";

const fadeIn = {
  initial: { opacity: 0, y: 20 },
  whileInView: { opacity: 1, y: 0 },
  viewport: { once: true },
  transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] }
};

export const SearchSection = () => {
  return (
    <section id="search" className="w-full py-24 sm:py-32 bg-background relative">
      <div className="container px-4 sm:px-6 max-w-7xl mx-auto">
        <motion.div
          className="bg-card border border-white/5 rounded-[3rem] p-8 sm:p-16 shadow-3xl relative overflow-hidden"
          variants={fadeIn}
          initial="initial"
          whileInView="whileInView"
        >
          <div className="absolute top-0 right-0 p-12 opacity-5 pointer-events-none">
            <Plane className="w-64 h-64 -rotate-12" />
          </div>

          <div className="relative z-10">
            <h2 className="text-sm font-black text-primary tracking-[0.5em] uppercase mb-8">Neural Search</h2>
            <h3 className="text-4xl sm:text-6xl font-black text-white italic uppercase tracking-tighter mb-12">
              SCAN GLOBAL <span className="opacity-40">INVENTORY</span>
            </h3>

            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              <div className="bg-black/40 border border-white/10 rounded-2xl p-6 hover:border-primary/50 transition-colors">
                <label className="text-[10px] font-bold text-primary uppercase tracking-widest mb-3 block">Origin</label>
                <div className="flex items-center text-white">
                  <MapPin className="w-5 h-5 mr-3 text-muted-foreground" />
                  <input type="text" placeholder="PRG / London" className="bg-transparent border-none outline-hidden text-xl font-bold w-full placeholder:text-white/20" />
                </div>
              </div>
              <div className="bg-black/40 border border-white/10 rounded-2xl p-6 hover:border-primary/50 transition-colors">
                <label className="text-[10px] font-bold text-primary uppercase tracking-widest mb-3 block">Destination</label>
                <div className="flex items-center text-white">
                  <MapPin className="w-5 h-5 mr-3 text-muted-foreground" />
                  <input type="text" placeholder="Anywhere" className="bg-transparent border-none outline-hidden text-xl font-bold w-full placeholder:text-white/20" />
                </div>
              </div>
              <div className="bg-black/40 border border-white/10 rounded-2xl p-6 hover:border-primary/50 transition-colors">
                <label className="text-[10px] font-bold text-primary uppercase tracking-widest mb-3 block">Window</label>
                <div className="flex items-center text-white">
                  <Calendar className="w-5 h-5 mr-3 text-muted-foreground" />
                  <input type="text" placeholder="Next 30 Days" className="bg-transparent border-none outline-hidden text-xl font-bold w-full placeholder:text-white/20" />
                </div>
              </div>
              <button className="bg-primary hover:bg-accent text-black rounded-2xl flex items-center justify-center transition-all group h-full py-8 md:py-0">
                <span className="text-sm font-black uppercase tracking-widest mr-3">Launch Scan</span>
                <Search className="w-5 h-5 group-hover:scale-110 transition-transform" />
              </button>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};
