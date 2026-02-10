"use client";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

export default function EU261() {
    return (
        <main className="min-h-screen bg-black text-slate-300">
            <Navbar />
            <section className="py-32 px-6 max-w-4xl mx-auto">
                <h1 className="text-4xl font-bold text-white mb-8 text-gradient-gold">EU261 Compliance Guide</h1>
                <div className="prose prose-invert prose-lg max-w-none">
                    <p className="mb-6 text-xl text-white">
                        Regulation (EC) No 261/2004 establishes common rules on compensation and assistance to passengers in the event of denied boarding and of cancellation or long delay of flights.
                    </p>

                    <div className="grid md:grid-cols-2 gap-8 my-12">
                        <div className="glass-card p-8 border-l-4 border-amber-400">
                            <h3 className="text-xl font-bold text-white mb-2">Compensation Amounts</h3>
                            <ul className="list-disc list-inside space-y-2 text-slate-400">
                                <li><strong className="text-white">€250</strong> for flights ≤ 1,500 km</li>
                                <li><strong className="text-white">€400</strong> for EU flights &gt; 1,500 km or non-EU 1,500-3,500 km</li>
                                <li><strong className="text-white">€600</strong> for all other flights &gt; 3,500 km</li>
                            </ul>
                        </div>
                        <div className="glass-card p-8 border-l-4 border-blue-500">
                            <h3 className="text-xl font-bold text-white mb-2">Your Rights</h3>
                            <ul className="list-disc list-inside space-y-2 text-slate-400">
                                <li>Right to reimbursement or re-routing</li>
                                <li>Right to care (food, hotel, calls)</li>
                                <li>Right to compensation (unless extraordinary circumstances)</li>
                            </ul>
                        </div>
                    </div>

                    <h2 className="text-2xl font-bold text-white mt-8 mb-4">How to Claim</h2>
                    <p className="mb-4">
                        If your flight was delayed by more than 3 hours or cancelled less than 14 days before departure, you may be eligible. TravelKing.Live assists you in filing these claims with legal precision.
                    </p>
                    <p className="mb-4">
                        Contact our concierge immediately via the <a href="/#contact" className="text-amber-400 hover:underline">Support Form</a> to initiate a claim review.
                    </p>
                </div>
            </section>
            <Footer />
        </main>
    );
}
