'use client';

import { useState } from 'react';
import { motion } from 'framer-motion';
import { ArrowRight, Plane, ShieldCheck, Globe, Star, Award, Zap } from 'lucide-react';
import Link from 'next/link';
import toast from 'react-hot-toast';

export default function Home() {
  const [flightNo, setFlightNo] = useState('');
  const [email, setEmail] = useState('');
  const [wantsNews, setWantsNews] = useState(true);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!flightNo || !email) {
      toast.error('Please enter both Flight No. and Email.');
      return;
    }
    setLoading(true);
    try {
      const response = await fetch('/submit_lead.php', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ flightNo, email, wantsNews }),
      });
      const data = await response.json();
      if (data.status === 'success') {
        toast.success('Tactical analysis dispatched. Redirecting to recommended service...');
        setFlightNo('');
        setEmail('');
        if (data.redirect) {
          setTimeout(() => {
            window.location.href = data.redirect;
          }, 2000);
        }
      } else {
        toast.error('Connection error. Please try again.');
      }
    } catch (error) {
      toast.error('Transmission failed.');
    } finally {
      setLoading(false);
    }
  };
  const fadeIn = {
    initial: { opacity: 0, y: 30 },
    whileInView: { opacity: 1, y: 0 },
    viewport: { once: true },
    transition: { duration: 0.8, ease: "easeOut" }
  };

  const staggerContainer = {
    initial: { opacity: 0 },
    whileInView: { opacity: 1 },
    viewport: { once: true },
    transition: { staggerChildren: 0.2 }
  };

  return (
    <div className="flex flex-col items-center w-full overflow-hidden bg-background text-foreground">
      {/* Hero Section */}
      <motion.section
        className="relative w-full min-h-[90vh] flex items-center justify-center overflow-hidden"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
      >
        {/* Elite Background with Parallax effect simulation */}
        <div
          className="absolute inset-0 z-0 bg-cover bg-center"
          style={{ backgroundImage: "url('/hero-bg.png')" }}
        >
          <div className="absolute inset-0 bg-linear-to-b from-black/60 via-black/40 to-background"></div>
          <div className="absolute inset-0 bg-linear-to-r from-background via-transparent to-transparent opacity-90"></div>
        </div>

        <div className="container relative z-10 px-4 sm:px-6 max-w-7xl mx-auto pt-20">
          <motion.div
            className="flex flex-col items-start space-y-8 text-left"
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
          >
            <div className="flex items-center gap-4">
              <div className="h-[1px] w-12 bg-primary"></div>
              <span className="text-primary uppercase tracking-[0.5em] text-[10px] font-bold">Official Industry Leader</span>
            </div>

            <h1 className="text-5xl sm:text-7xl md:text-8xl lg:text-9xl font-black leading-none font-poppins tracking-tighter uppercase italic pr-4">
              FLIGHT <br />
              <span className="bg-linear-to-r from-primary via-accent to-primary bg-clip-text text-transparent italic pr-2">DISRUPTED?</span>
            </h1>

            <p className="max-w-[700px] text-muted-foreground text-lg sm:text-xl font-light leading-relaxed">
              Don't let airlines keep your money. Our flight analysis is <span className="text-white font-bold">100% FREE</span>. Receive an <span className="text-white font-bold">instant email response</span> identifying the absolute best recovery service for your specific disruption to ensure you get the <span className="text-white font-bold">maximum payout</span>.
            </p>

            <div className="flex flex-col w-full max-w-md bg-card/50 backdrop-blur-md border border-white/10 p-6 rounded-2xl gap-4 mt-8">
              <div className="flex flex-col gap-2">
                <label className="text-xs uppercase font-bold text-muted-foreground tracking-widest">Flight Number (e.g. BA123)</label>
                <input
                  type="text"
                  placeholder="Flight No."
                  className="w-full bg-black/50 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-primary transition-colors uppercase font-mono"
                  value={flightNo}
                  onChange={(e) => setFlightNo(e.target.value)}
                />
              </div>
              <div className="flex flex-col gap-2">
                <label className="text-xs uppercase font-bold text-muted-foreground tracking-widest">Email Address</label>
                <input
                  type="email"
                  placeholder="Your Email"
                  className="w-full bg-black/50 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-primary transition-colors"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
              <div className="flex items-center gap-3 py-2 cursor-pointer group" onClick={() => setWantsNews(!wantsNews)}>
                <div
                  className={`w-10 h-5 rounded-full relative transition-colors duration-300 ${wantsNews ? 'bg-primary' : 'bg-white/10'}`}
                >
                  <div className={`absolute top-0.5 w-4 h-4 rounded-full bg-white transition-all duration-300 ${wantsNews ? 'left-5.5' : 'left-0.5'}`}></div>
                </div>
                <span className="text-[10px] uppercase font-bold text-muted-foreground tracking-widest group-hover:text-white transition-colors max-w-[300px] leading-tight">
                  {wantsNews
                    ? "Activate Long-Run Intelligence: Get Latest News, Safety Tips & Travel Warnings"
                    : "One-time tactical email only. No future marketing protocol."}
                </span>
              </div>
              <button
                onClick={handleSubmit}
                disabled={loading}
                className="w-full h-14 rounded-full bg-primary text-black font-black uppercase tracking-widest hover:bg-accent transition-all hover:scale-105 shadow-xl shadow-primary/20 flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {loading ? 'TRANSMITTING...' : 'START PROTOCOL'} <Zap className="w-4 h-4 fill-current" />
              </button>
              <p className="text-[10px] text-center text-muted-foreground uppercase tracking-wider">
                100% FREE ANALYSIS. MAXIMUM PAYOUT GUARANTEED. RESPONSE TIME: <span className="text-white font-bold">INSTANT</span>.
              </p>
            </div>
          </motion.div>

          {/* Enterprise Stats */}
          <motion.div
            className="grid grid-cols-2 md:grid-cols-4 gap-8 mt-24 border-t border-white/5 pt-12"
            variants={staggerContainer}
            initial="initial"
            whileInView="whileInView"
          >
            {[
              { label: "Missions Completed", value: "15,240+" },
              { label: "Recovered Assets", value: "€9.8M" },
              { label: "Global Presence", value: "192 CTIES" },
              { label: "Concierge Status", value: "ELITE" }
            ].map((stat, i) => (
              <motion.div key={i} variants={fadeIn}>
                <div className="text-2xl font-black text-white mb-1 tracking-tight">{stat.value}</div>
                <div className="text-[10px] uppercase tracking-widest text-muted-foreground font-bold">{stat.label}</div>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </motion.section>

      {/* Certification Section */}
      <section className="w-full py-16 border-y border-white/5 bg-white/[0.01]">
        <div className="container px-4 sm:px-6 max-w-7xl mx-auto">
          <div className="flex flex-wrap items-center justify-center gap-12 sm:gap-20 opacity-30">
            {["IATA SYSTEM", "EC 261/2004", "TRAVELPAYOUTS", "OMEGA ENGINE", "SKYNET CONCIERGE"].map((logo) => (
              <span key={logo} className="text-lg font-black tracking-[0.3em] text-white italic">{logo}</span>
            ))}
          </div>
        </div>
      </section>

      {/* Live Deals Ticker */}
      <section className="w-full py-8 bg-black border-y border-white/5 overflow-hidden">
        <div className="container px-4 sm:px-6 max-w-7xl mx-auto">
          <div className="flex items-center gap-8 animate-scroll whitespace-nowrap">
            {/* Duplicated for smooth scrolling loop */}
            {[...Array(2)].map((_, i) => (
              <div key={i} className="flex gap-12">
                {[
                  { route: "LHR -> JFK", price: "€450", class: "BUSINESS" },
                  { route: "DXB -> LHR", price: "€320", class: "FIRST" },
                  { route: "CDG -> TYO", price: "€680", class: "BUSINESS" },
                  { route: "MUC -> BKK", price: "€510", class: "BUSINESS" },
                  { route: "ZRH -> LAX", price: "€890", class: "FIRST" },
                  { route: "FRA -> SIN", price: "€550", class: "BUSINESS" },
                ].map((deal, j) => (
                  <div key={j} className="flex items-center gap-3">
                    <Plane className="w-4 h-4 text-primary" />
                    <span className="text-white font-mono text-xs tracking-widest">{deal.route}</span>
                    <span className="text-primary font-bold text-xs">{deal.price}</span>
                    <span className="text-[10px] bg-white/10 px-2 py-0.5 rounded text-muted-foreground">{deal.class}</span>
                  </div>
                ))}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section id="services" className="w-full py-24 sm:py-32 bg-card">
        <div className="container px-4 sm:px-6 max-w-7xl mx-auto">
          <motion.div
            className="flex flex-col items-center justify-center space-y-6 text-center mb-20"
            variants={fadeIn}
            initial="initial"
            whileInView="whileInView"
          >
            <h2 className="text-primary uppercase tracking-[0.5em] text-xs font-bold">Elite Intelligence</h2>
            <h3 className="text-4xl sm:text-5xl md:text-6xl font-black tracking-tighter italic uppercase text-white">
              OUR SPECIALIZED <span className="bg-linear-to-r from-primary to-accent bg-clip-text text-transparent">DOMAINS</span>
            </h3>
          </motion.div>

          <div className="grid md:grid-cols-12 gap-6 auto-rows-[300px]">
            <motion.div
              className="md:col-span-8 group relative overflow-hidden rounded-3xl border border-border bg-linear-to-br from-white/5 to-transparent p-12 flex flex-col justify-end hover:border-primary/50 transition-all duration-500"
              variants={fadeIn}
              initial="initial"
              whileInView="whileInView"
            >
              <Plane className="w-12 h-12 text-primary mb-8 group-hover:scale-110 transition-transform" />
              <h4 className="text-3xl font-black text-white mb-4 uppercase italic">Neural Flight Search</h4>
              <p className="text-muted-foreground max-w-lg">Advanced algorithmic scanning of 800+ airlines to find proprietary pricing unavailable to the general public.</p>
            </motion.div>

            <motion.div
              className="md:col-span-4 rounded-3xl border border-border bg-linear-to-bl from-white/5 to-transparent p-10 flex flex-col justify-center gap-4 hover:border-primary/50 transition-all duration-500"
              variants={fadeIn}
              initial="initial"
              whileInView="whileInView"
            >
              <ShieldCheck className="w-10 h-10 text-blue-400" />
              <h4 className="text-xl font-bold text-white uppercase italic tracking-tighter">Legal Arsenal</h4>
              <p className="text-muted-foreground text-sm leading-relaxed italic border-l-2 border-primary pl-4">"Complete EC No 261/2004 Coverage & Strategic Recovery."</p>
            </motion.div>

            <motion.div
              className="md:col-span-4 rounded-3xl border border-border bg-linear-to-tr from-white/5 to-transparent p-10 flex flex-col justify-center gap-4 hover:border-primary/50 transition-all duration-500"
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

      {/* World Map Section */}
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

      {/* Membership Tiers */}
      <section className="w-full py-24 bg-card border-y border-white/5">
        <div className="container px-4 sm:px-6 max-w-7xl mx-auto">
          <div className="grid md:grid-cols-3 gap-8">
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

      {/* CTA Section */}
      <motion.section
        className="w-full py-24 sm:py-32 bg-linear-to-br from-black to-secondary"
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        viewport={{ once: true }}
        transition={{ duration: 1 }}
      >
        <div className="container px-4 sm:px-6 max-w-7xl mx-auto">
          <motion.div
            className="flex flex-col items-center space-y-10 text-center"
            variants={fadeIn}
            initial="initial"
            whileInView="whileInView"
          >
            <h2 className="text-5xl sm:text-7xl md:text-8xl font-black tracking-tighter italic uppercase text-white leading-tight">
              COMMAND YOUR <br />
              <span className="bg-linear-to-r from-primary to-accent bg-clip-text text-transparent italic">DOMAIN.</span>
            </h2>
            <p className="mx-auto max-w-[700px] text-muted-foreground text-lg sm:text-xl font-light">
              Our elite handlers are standing by in our global operations center.
              Estimated response time: <span className="text-white font-bold">140 Seconds.</span>
            </p>
            <Link
              href="#search"
              className="inline-flex h-16 items-center justify-center rounded-full bg-primary px-12 text-xs font-black uppercase tracking-widest text-primary-foreground shadow-2xl hover:bg-accent transition-all duration-300 hover:scale-105"
            >
              Initiate Contact Protocol
              <Zap className="ml-3 h-4 w-4 fill-current" />
            </Link>
          </motion.div>
        </div>
      </motion.section>
    </div>
  );
}
