"use client";

import { Activity, MapPin, Zap, ArrowRight, Crosshair } from 'lucide-react';
import { Button } from '../ui/Button';
import Link from 'next/link';

export function LiveIntelWidget() {
  return (
    <div className="w-full max-w-sm bg-white rounded-none shadow-2xl overflow-hidden border-4 border-black relative z-20 mx-auto lg:mx-0 transform hover:-translate-y-1 transition-transform duration-300 group/widget">
      {/* Header */}
      <div className="p-8 text-center border-b border-gray-100">
        <div className="w-16 h-16 bg-black flex items-center justify-center mx-auto mb-6 group-hover/widget:bg-[#003FFA] transition-colors duration-500">
            <Activity className="text-[#00FF9A] animate-pulse" size={32} />
        </div>
        <h3 className="text-black font-black uppercase tracking-[0.3em] text-sm mb-2 font-sans">
          Live Update
        </h3>
        <p className="text-gray-500 text-[10px] font-mono uppercase tracking-widest">
          Real-Time Exploration v3.0
        </p>
      </div>

      {/* Sector */}
      <div className="p-8 border-b border-gray-100 text-center">
        <span className="text-gray-400 text-[10px] font-black uppercase tracking-[0.2em] mb-4 block">
            Current Sector
        </span>
        <div className="border border-gray-200 p-4 flex items-center justify-between group cursor-pointer hover:border-black transition-colors bg-gray-50 hover:bg-white">
            <span className="font-black uppercase tracking-widest text-lg text-black">Global</span>
            <MapPin size={16} className="text-gray-400 group-hover:text-[#003FFA]" />
        </div>
      </div>

      {/* Status */}
      <div className="p-8 text-center">
        <span className="text-[#003FFA] text-[10px] font-black uppercase tracking-[0.2em] mb-2 block">
            System Status
        </span>
        <h2 className="text-5xl font-black uppercase tracking-tighter italic font-sans mb-8 text-black">
            ACTIVE
        </h2>

        <p className="font-serif italic text-gray-600 mb-8 text-sm">
            "Flight compensation algorithms operating at peak efficiency. Refunds processing normally."
        </p>

        {/* Black Box */}
        <div className="bg-black text-white p-6 text-center mb-8 relative overflow-hidden group">
            <div className="absolute inset-0 bg-[#00FF9A] opacity-0 group-hover:opacity-10 transition-opacity"></div>
            <Crosshair className="text-[#003FFA] mx-auto mb-2 animate-spin-slow" size={24} />
            <span className="text-[#003FFA] text-[10px] font-black uppercase tracking-[0.3em] mb-2 block">
                Expert Tip
            </span>
            <p className="font-black uppercase tracking-wide text-sm">
                Always photograph your boarding pass immediately.
            </p>
        </div>

        {/* Actions */}
        <div className="space-y-3">
            <Button variant="outline" className="w-full border-gray-200 text-gray-500 hover:text-black hover:border-black h-12 text-[10px] tracking-[0.2em] font-black bg-transparent" asChild>
                <Link href="/about">JOIN THE NETWORK</Link>
            </Button>
            <Button className="w-full bg-[#E50914] hover:bg-[#b2070f] text-white h-14 font-black uppercase tracking-[0.2em] text-sm group flex items-center justify-center gap-2" asChild>
                <Link href="/eu261">
                    ACTIVATE <Zap className="group-hover:text-[#00FF9A] transition-colors" size={16} fill="currentColor" />
                </Link>
            </Button>
        </div>
      </div>
    </div>
  );
}
