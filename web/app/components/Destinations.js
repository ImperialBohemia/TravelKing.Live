export default function Destinations() {
    const items = [
        { name: "Dubai", category: "Ultra Luxury", img: "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&q=80&w=800" },
        { name: "Maldives", category: "Serene Private", img: "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?auto=format&fit=crop&q=80&w=800" },
        { name: "St. Moritz", category: "Alpine Elite", img: "https://images.unsplash.com/photo-1502014822147-1aedfb0676e0?auto=format&fit=crop&q=80&w=800" },
        { name: "Monaco", category: "Riviera Grand", img: "https://images.unsplash.com/photo-1559121225-4c96207671f2?auto=format&fit=crop&q=80&w=800" }
    ];

    return (
        <section className="py-32 px-6">
            <div className="max-w-7xl mx-auto">
                <div className="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
                    <div>
                        <h2 className="text-4xl font-black text-white mb-4 font-display">THE ULTIMATE <span className="text-gradient-gold">BUCKET LIST</span></h2>
                        <p className="text-slate-500 max-w-lg">Vetted by the world's most discerning travelers. Discover destinations that define elite status.</p>
                    </div>
                    <a href="#" className="btn-outline">View Global Map</a>
                </div>

                <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-8">
                    {items.map((item, idx) => (
                        <div key={idx} className="group relative overflow-hidden rounded-2xl h-[450px] cursor-pointer">
                            <img
                                src={item.img}
                                className="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
                                alt={item.name}
                            />
                            <div className="absolute inset-0 bg-gradient-to-t from-black via-black/20 to-transparent opacity-80 group-hover:opacity-100 transition-opacity" />
                            <div className="absolute bottom-0 left-0 p-8">
                                <div className="text-xs uppercase tracking-[0.2em] text-amber-400 font-bold mb-2">{item.category}</div>
                                <h3 className="text-2xl font-black text-white font-display tracking-tight">{item.name}</h3>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
}
