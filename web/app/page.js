import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import SearchBox from "./components/SearchBox";
import LegalGuide from "./components/LegalGuide";
import Destinations from "./components/Destinations";
import Footer from "./components/Footer";

export default function Home() {
  return (
    <main className="min-h-screen">
      <Navbar />
      <Hero />
      <SearchBox />

      <section id="services" className="py-32 px-6 bg-slate-900/30">
        <div className="max-w-7xl mx-auto text-center mb-20">
          <h2 className="text-4xl font-black text-white mb-6 font-display">UNIFIED TRAVEL <span className="text-gradient-gold">INTELLIGENCE</span></h2>
          <div className="h-1 w-20 bg-amber-400 mx-auto mb-8"></div>
          <p className="text-slate-400 max-w-2xl mx-auto text-lg leading-relaxed">
            One platform, every solution. We leverage neural search and EU regulatory direct-links
            to protect your journey and optimize your travel investment.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          <div className="glass-card p-10">
            <div className="w-12 h-12 rounded-xl bg-amber-400/10 flex items-center justify-center mb-8 border border-amber-400/20">
              <span className="text-xl">✈️</span>
            </div>
            <h3 className="text-2xl font-bold text-white mb-4">Neural Search</h3>
            <p className="text-slate-400 leading-relaxed">Cross-referencing 800+ airlines in real-time to find the absolute floor for premium and business ticketing.</p>
          </div>

          <div className="glass-card p-10 border-amber-400/20 shadow-[0_0_50px_rgba(212,175,55,0.05)]">
            <div className="w-12 h-12 rounded-xl bg-blue-500/10 flex items-center justify-center mb-8 border border-blue-500/20">
              <span className="text-xl">⚖️</span>
            </div>
            <h3 className="text-2xl font-bold text-white mb-4">Legal Supremacy</h3>
            <p className="text-slate-400 leading-relaxed">Automated EC No 261/2004 monitoring. We detect disruptions before you do and prepare your claim package instantly.</p>
          </div>

          <div className="glass-card p-10">
            <div className="w-12 h-12 rounded-xl bg-purple-500/10 flex items-center justify-center mb-8 border border-purple-500/20">
              <span className="text-xl">🛎️</span>
            </div>
            <h3 className="text-2xl font-bold text-white mb-4">Private Network</h3>
            <p className="text-slate-400 leading-relaxed">Exclusive access to 'Empty Leg' private jet repositioning and last-minute luxury villa inventory worldwide.</p>
          </div>
        </div>
      </section>

      <LegalGuide />
      <Destinations />

      {/* Contact Section with Lead Integration */}
      <section id="contact" className="py-32 px-6 section-gradient">
        <div className="max-w-3xl mx-auto text-center">
          <h2 className="text-4xl md:text-5xl font-black text-white mb-8 leading-tight font-display">
            COMMAND YOUR <br />
            <span className="text-gradient-gold">NEXT MISSION.</span>
          </h2>
          <p className="text-slate-400 mb-12 text-lg">
            Our Elite Concierge is standing by. Submit your requirements and let our
            OMEGA engine handle the complexities of your travel.
          </p>

          {/* We use the user's existing Google Form but styled within our container */}
          <div className="glass-card overflow-hidden ring-1 ring-white/10 p-1">
            <iframe
              src="https://docs.google.com/forms/d/e/1FAIpQLSejJGzQFmdenDKLarechBGV0mI9o7bk62Q3W4TmegHDz1u_5w/viewform?embedded=true"
              width="100%"
              height="800"
              frameBorder="0"
              marginHeight="0"
              marginWidth="0"
              className="grayscale invert opacity-90 transition-all hover:grayscale-0 hover:invert-0 hover:opacity-100"
            >
              Loading…
            </iframe>
          </div>

          <div className="mt-12 text-slate-500 text-sm font-medium tracking-widest uppercase">
            Encrypted • Anonymous • Priority
          </div>
        </div>
      </section>

      <Footer />
    </main>
  );
}
