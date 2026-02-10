"use client";

import { motion } from "framer-motion";

const fadeIn = {
  initial: { opacity: 0, y: 20 },
  whileInView: { opacity: 1, y: 0 },
  viewport: { once: true },
  transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] }
};

export const PricingSection = () => {
  return (
    <section className="w-full py-24 bg-card border-y border-white/5">
      <div className="container px-4 sm:px-6 max-w-7xl mx-auto">
        <div className="grid md:grid-cols-3 gap-8">
          {/* Initiate */}
          <div className="p-8 border border-white/10 rounded-2xl bg-black/50 hover:border-primary/30 transition-all">
            <h4 className="text-xl font-bold text-white uppercase tracking-widest mb-4">Initiate</h4>
            <div className="text-3xl font-black text-primary mb-6">€0 <span className="text-sm font-medium text-muted-foreground">/ month</span></div>
            <ul className="space-y-4 text-sm text-muted-foreground mb-8">
              <li className="flex items-center gap-2"><div className="w-1.5 h-1.5 bg-primary rounded-full"></div>Standard Flight Search</li>
              <li className="flex items-center gap-2"><div className="w-1.5 h-1.5 bg-primary rounded-full"></div>Basic EU261 Guide</li>
              <li className="flex items-center gap-2"><div className="w-1.5 h-1.5 bg-primary rounded-full"></div>Email Support</li>
            </ul>
            <button className="w-full py-3 border border-white/20 rounded-full text-xs font-bold uppercase tracking-widest hover:bg-white hover:text-black transition-colors">Select</button>
          </div>

          {/* Sovereign */}
          <div className="p-8 border border-primary/50 rounded-2xl bg-primary/5 relative hover:scale-105 transition-all duration-300">
            <div className="absolute top-0 right-0 bg-primary text-black text-[10px] font-bold px-3 py-1 uppercase tracking-widest rounded-bl-xl">Most Requested</div>
            <h4 className="text-xl font-bold text-white uppercase tracking-widest mb-4">Sovereign</h4>
            <div className="text-3xl font-black text-primary mb-6">€49 <span className="text-sm font-medium text-muted-foreground">/ month</span></div>
            <ul className="space-y-4 text-sm text-muted-foreground mb-8">
              <li className="flex items-center gap-2"><div className="w-1.5 h-1.5 bg-primary rounded-full"></div>Neural Flight Engine (Priority)</li>
              <li className="flex items-center gap-2"><div className="w-1.5 h-1.5 bg-primary rounded-full"></div>Auto-Claim EU261 Bot</li>
              <li className="flex items-center gap-2"><div className="w-1.5 h-1.5 bg-primary rounded-full"></div>24/7 Concierge Chat</li>
              <li className="flex items-center gap-2"><div className="w-1.5 h-1.5 bg-primary rounded-full"></div>Hidden City Ticketing</li>
            </ul>
            <button className="w-full py-3 bg-primary rounded-full text-black text-xs font-bold uppercase tracking-widest hover:bg-accent transition-colors shadow-lg shadow-primary/20">Apply for Access</button>
          </div>

          {/* Omega */}
          <div className="p-8 border border-white/10 rounded-2xl bg-black/50 hover:border-primary/30 transition-all">
            <h4 className="text-xl font-bold text-white uppercase tracking-widest mb-4">Omega</h4>
            <div className="text-3xl font-black text-primary mb-6">Invite Only</div>
            <ul className="space-y-4 text-sm text-muted-foreground mb-8">
              <li className="flex items-center gap-2"><div className="w-1.5 h-1.5 bg-primary rounded-full"></div>Private Jet Logistics</li>
              <li className="flex items-center gap-2"><div className="w-1.5 h-1.5 bg-primary rounded-full"></div>Diplomatic Security</li>
              <li className="flex items-center gap-2"><div className="w-1.5 h-1.5 bg-primary rounded-full"></div>Off-Market Hotel Suites</li>
              <li className="flex items-center gap-2"><div className="w-1.5 h-1.5 bg-primary rounded-full"></div>Dedicated Handler Team</li>
            </ul>
            <button className="w-full py-3 border border-white/20 rounded-full text-xs font-bold uppercase tracking-widest hover:bg-white hover:text-black transition-colors">Contact Encoders</button>
          </div>
        </div>
      </div>
    </section>
  );
};
