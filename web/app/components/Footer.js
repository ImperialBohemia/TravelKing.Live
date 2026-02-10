export default function Footer() {
    return (
        <footer className="bg-black py-20 px-6 border-t border-white/5">
            <div className="max-w-7xl mx-auto">
                <div className="grid md:grid-cols-4 gap-12 mb-16">
                    <div className="col-span-2">
                        <div className="flex items-center gap-2 mb-6">
                            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-yellow-400 to-amber-600 flex items-center justify-center font-bold text-black text-xs">
                                TK
                            </div>
                            <span className="text-xl font-black tracking-tight font-display text-white italic">
                                TRAVELKING<span className="text-gradient-gold">.LIVE</span>
                            </span>
                        </div>
                        <p className="text-slate-500 text-sm leading-relaxed max-w-sm mb-8">
                            The supreme travel orchestration engine for the modern elite.
                            Autonomous search, legal supremacy, and luxury destination management.
                        </p>
                        <div className="flex gap-4">
                            <div className="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-white/10 transition-colors cursor-pointer border border-white/5">
                                <span className="text-xs text-slate-400 font-bold">FB</span>
                            </div>
                            <div className="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-white/10 transition-colors cursor-pointer border border-white/5">
                                <span className="text-xs text-slate-400 font-bold">X</span>
                            </div>
                            <div className="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-white/10 transition-colors cursor-pointer border border-white/5">
                                <span className="text-xs text-slate-400 font-bold">LI</span>
                            </div>
                        </div>
                    </div>

                    <div>
                        <h4 className="text-white font-bold mb-6 uppercase tracking-widest text-xs">Navigation</h4>
                        <ul className="space-y-4 text-slate-500 text-sm">
                            <li><a href="#" className="hover:text-amber-400 transition-colors">Flight Search</a></li>
                            <li><a href="#" className="hover:text-amber-400 transition-colors">Private Rescue</a></li>
                            <li><a href="#" className="hover:text-amber-400 transition-colors">EU261 Guidelines</a></li>
                            <li><a href="#" className="hover:text-amber-400 transition-colors">Luxury Concierge</a></li>
                        </ul>
                    </div>

                    <div>
                        <h4 className="text-white font-bold mb-6 uppercase tracking-widest text-xs">Operations</h4>
                        <ul className="space-y-4 text-slate-500 text-sm">
                            <li><a href="#" className="hover:text-amber-400 transition-colors">Claim Tracker</a></li>
                            <li><a href="#" className="hover:text-amber-400 transition-colors">Support Center</a></li>
                            <li><a href="#" className="hover:text-amber-400 transition-colors">Partner Program</a></li>
                            <li><a href="#" className="hover:text-amber-400 transition-colors">Omega Status</a></li>
                        </ul>
                    </div>
                </div>

                <div className="border-t border-white/5 pt-10 flex flex-col md:flex-row justify-between items-center gap-6">
                    <p className="text-slate-600 text-xs">
                        © 2026 TRAVELKING.LIVE — ENTERPRISE OMEGA ECOLOGY. ALL RIGHTS RESERVED.
                    </p>
                    <div className="flex gap-8 text-xs text-slate-600 font-medium">
                        <span className="hover:text-slate-400 transition-colors cursor-pointer">PRIVACY POLICY</span>
                        <span className="hover:text-slate-400 transition-colors cursor-pointer">TERMS OF SERVICE</span>
                        <span className="hover:text-slate-400 transition-colors cursor-pointer">EU261 COMPLIANCE</span>
                    </div>
                </div>
            </div>
        </footer>
    );
}
