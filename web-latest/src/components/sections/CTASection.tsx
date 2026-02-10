"use client";

import { motion } from "framer-motion";
import { Zap } from "lucide-react";
import Link from "next/link";

const fadeIn = {
  initial: { opacity: 0, y: 20 },
  whileInView: { opacity: 1, y: 0 },
  viewport: { once: true },
  transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] }
};

export const CTASection = () => {
  return (
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
  );
};
