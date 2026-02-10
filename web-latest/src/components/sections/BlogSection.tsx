"use client";

import { motion } from "framer-motion";
import { BookOpen, Clock, User, ArrowRight } from "lucide-react";
import Link from "next/link";

const fadeIn = {
  initial: { opacity: 0, y: 20 },
  whileInView: { opacity: 1, y: 0 },
  viewport: { once: true },
  transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] }
};

const posts = [
  {
    slug: "sovereign-travel-2026",
    title: "Sovereign Travel: The New Global Standard",
    excerpt: "Why the elite are moving away from traditional luxury towards sovereign logistics and automated protection.",
    author: "Stanislav Pasztorek",
    date: "Feb 10, 2026",
    readTime: "6 min",
    category: "Intelligence",
    image: "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&q=80&w=800"
  },
  {
    slug: "eu261-hidden-mechanics",
    title: "EU261: Hidden Mechanics of Compensation",
    excerpt: "How to extract maximum value from flight disruptions using OMEGA's automated legal bridges.",
    author: "OMEGA Handler",
    date: "Feb 08, 2026",
    readTime: "4 min",
    category: "Legal",
    image: "https://images.unsplash.com/photo-1436491865332-7a61a109c0f2?auto=format&fit=crop&q=80&w=800"
  },
  {
    slug: "stealth-concierge-operations",
    title: "Stealth Concierge: Anonymous Logistics",
    excerpt: "Behind the scenes of our 24/7 anonymous booking network for high-stakes travel operations.",
    author: "Jules AI",
    date: "Feb 05, 2026",
    readTime: "8 min",
    category: "Operations",
    image: "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&q=80&w=800"
  }
];

export const BlogSection = () => {
  return (
    <section id="blog" className="w-full py-24 sm:py-32 bg-black relative">
      <div className="container px-4 sm:px-6 max-w-7xl mx-auto">
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-8">
          <div>
            <h2 className="text-sm font-black text-primary tracking-[0.5em] uppercase mb-4">Elite Intel</h2>
            <h3 className="text-4xl sm:text-6xl font-black text-white italic uppercase tracking-tighter">
              THE TRAVEL <span className="opacity-40 text-primary">KNOWLEDGE</span> BASE
            </h3>
          </div>
          <Link href="/blog" className="group flex items-center gap-3 text-xs font-black uppercase tracking-widest text-white border-b-2 border-primary/20 pb-2 hover:border-primary transition-all">
            View All Intelligence <ArrowRight className="w-4 h-4 group-hover:translate-x-2 transition-transform" />
          </Link>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {posts.map((post, idx) => (
            <motion.article
              key={post.slug}
              className="group flex flex-col bg-card border border-white/5 rounded-3xl overflow-hidden hover:border-primary/50 transition-all"
              variants={fadeIn}
              initial="initial"
              whileInView="whileInView"
              transition={{ delay: idx * 0.1 }}
            >
              <div className="aspect-video relative overflow-hidden">
                <img
                  src={post.image}
                  alt={post.title}
                  className="object-cover w-full h-full group-hover:scale-110 transition-transform duration-700"
                />
                <div className="absolute top-4 left-4 bg-primary text-black text-[8px] font-black uppercase tracking-widest px-3 py-1 rounded-full">
                  {post.category}
                </div>
              </div>

              <div className="p-8 flex flex-col flex-1">
                <div className="flex items-center gap-4 text-[10px] font-bold text-muted-foreground uppercase tracking-widest mb-4">
                  <span className="flex items-center gap-1"><Clock className="w-3 h-3" /> {post.readTime}</span>
                  <span className="flex items-center gap-1"><User className="w-3 h-3" /> {post.author}</span>
                </div>

                <h4 className="text-xl font-bold text-white mb-4 group-hover:text-primary transition-colors leading-tight">
                  {post.title}
                </h4>

                <p className="text-muted-foreground text-sm leading-relaxed mb-8 flex-1">
                  {post.excerpt}
                </p>

                <Link
                  href={`/blog/${post.slug}`}
                  className="inline-flex items-center gap-2 text-[10px] font-black uppercase tracking-[0.2em] text-white hover:gap-3 transition-all"
                >
                  Decrypt Post <ArrowRight className="w-3 h-3 text-primary" />
                </Link>
              </div>
            </motion.article>
          ))}
        </div>
      </div>
    </section>
  );
};
