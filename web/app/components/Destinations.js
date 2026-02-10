"use client";

const destinations = [
    {
        title: "PRIVATE ISLANDS",
        desc: "Discrete sanctuaries in French Polynesia and Maldives.",
        tag: "Exclusive",
        img: "https://images.unsplash.com/photo-1548574505-5e239809ee19?q=80&w=2000"
    },
    {
        title: "ALPINE ESTATES",
        desc: "Luxury chalets with private helipads in Courchevel.",
        tag: "Summit",
        img: "https://images.unsplash.com/photo-1517043583535-44a115a31bb2?q=80&w=2000"
    },
    {
        title: "METROPOLIS OPS",
        desc: "Penthouse command centers in Dubai and NYC.",
        tag: "Urban",
        img: "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?q=80&w=2000"
    }
];

export default function Destinations() {
    return (
        <section className="py-32 px-6 section-noble">
            <div className="max-w-7xl mx-auto">
                <div className="flex flex-col md:flex-row items-end justify-between mb-20 gap-8">
                    <div className="max-w-xl">
                        <h2 className="text-sm font-black text-gold-bright tracking-[0.5em] uppercase mb-4">World Network</h2>
                        <h3 className="text-4xl md:text-5xl font-black text-white font-display uppercase tracking-tight">CURATED <span className="text-gradient-silver">TOP-TIER</span> DESTINATIONS</h3>
                    </div>
                    <div className="text-slate-500 text-sm italic font-light border-l border-white/10 pl-8 hidden md:block">
                        "We don't go where others go. <br /> We define the destination."
                    </div>
                </div>

                <div className="grid md:grid-cols-3 gap-8">
                    {destinations.map((dest, i) => (
                        <div key={i} className="group relative h-[600px] rounded-3xl overflow-hidden glass-pane border-white/5 cursor-pointer">
                            <div
                                className="absolute inset-0 bg-cover bg-center transition-transform duration-1000 group-hover:scale-110"
                                style={{ backgroundImage: `url('${dest.img}')` }}
                            >
                                <div className="absolute inset-0 bg-gradient-to-t from-deep-space via-deep-space/20 to-transparent"></div>
                            </div>

                            <div className="absolute top-6 left-6">
                                <span className="px-4 py-1 rounded-full bg-white/10 backdrop-blur-md text-[10px] font-black uppercase tracking-widest text-white border border-white/10">
                                    {dest.tag}
                                </span>
                            </div>

                            <div className="absolute bottom-10 left-10 right-10">
                                <h4 className="text-3xl font-black text-white mb-4 font-display group-hover:text-gold-bright transition-colors uppercase">{dest.title}</h4>
                                <p className="text-slate-400 text-sm leading-relaxed mb-6 transform opacity-0 translate-y-4 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-500">
                                    {dest.desc}
                                </p>
                                <div className="w-12 h-1 bg-gold-bright/30 transition-all group-hover:w-full duration-500"></div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
}
