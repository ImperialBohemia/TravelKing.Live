export default function LegalGuide() {
    const steps = [
        {
            title: "Know Your Rights (EU261)",
            desc: "If your flight departs from the EU or is with an EU airline, you are entitled to up to €600 compensation for delays over 3 hours.",
            color: "border-amber-400"
        },
        {
            title: "Secure Verification",
            desc: "Capture photos of departure boards, save your boarding pass, and request written confirmation of the delay reason from airline staff.",
            color: "border-blue-500"
        },
        {
            title: "The Right to Care",
            desc: "Airlines must provide food, drinks, and hotel accommodation for significant delays. Retain all receipts for reimbursement.",
            color: "border-purple-500"
        },
        {
            title: "Next-Gen Migration",
            desc: "Commercial airlines can take days to rebook. Our network offers private aviation 'rescue' solutions during massive disruptions.",
            color: "border-platinum"
        }
    ];

    return (
        <section id="compensation" className="section-dark py-32 px-6">
            <div className="max-w-7xl mx-auto">
                <div className="grid lg:grid-cols-2 gap-20 items-center">
                    <div>
                        <h2 className="text-4xl md:text-5xl font-black text-white mb-6 leading-tight font-display">
                            FLIGHT DISRUPTED? <br />
                            <span className="text-gradient-gold">WE COMMAND THE RECOVERY.</span>
                        </h2>
                        <hr className="gold-divider" />
                        <p className="text-slate-400 text-lg mb-8 leading-relaxed max-w-xl">
                            TravelKing.Live provides the technical and legal leverage you need.
                            From EU261 compliance monitoring to instant private charter rescue,
                            we ensure you are never stranded.
                        </p>
                        <div className="space-y-4">
                            <div className="flex items-start gap-4">
                                <div className="w-6 h-6 rounded-full bg-amber-400/10 border border-amber-400/30 flex items-center justify-center flex-shrink-0 mt-1">
                                    <span className="w-1.5 h-1.5 rounded-full bg-amber-400" />
                                </div>
                                <p className="text-slate-300 font-medium">Global EU261 Jurisdiction Network</p>
                            </div>
                            <div className="flex items-start gap-4">
                                <div className="w-6 h-6 rounded-full bg-amber-400/10 border border-amber-400/30 flex items-center justify-center flex-shrink-0 mt-1">
                                    <span className="w-1.5 h-1.5 rounded-full bg-amber-400" />
                                </div>
                                <p className="text-slate-300 font-medium">Instant Verification Engines</p>
                            </div>
                        </div>
                    </div>

                    <div className="grid sm:grid-cols-2 gap-6">
                        {steps.map((step, idx) => (
                            <div key={idx} className={`glass-card p-6 border-l-4 ${step.color}`}>
                                <h3 className="text-white font-bold text-lg mb-2">{step.title}</h3>
                                <p className="text-slate-400 text-sm leading-relaxed">{step.desc}</p>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </section>
    );
}
