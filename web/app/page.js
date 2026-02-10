import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import SearchBox from "./components/SearchBox";
import LegalGuide from "./components/LegalGuide";
import Destinations from "./components/Destinations";
import Footer from "./components/Footer";
import CookieBanner from "./components/CookieBanner";

export default function Home() {
  return (
    <main className="min-h-screen bg-deep-space">
      <Navbar />
      <Hero />
      <SearchBox />

      {/* Official Certification Section */}
      <section className="py-20 border-y border-white/5 bg-white/[0.01]">
        <div className="max-w-7xl mx-auto px-6">
          <div className="flex flex-wrap items-center justify-between gap-12 opacity-40 grayscale">
            {/* Logos placeholder using stylish text for enterprise look */}
            {["IATA SYSTEM", "EC 261/2004", "TRAVELPAYOUTS", "OMEGA ENGINE", "SKYNET CONCIERGE"].map((logo) => (
              <span key={logo} className="text-xl font-black tracking-widest text-white/50">{logo}</span>
            ))}
          </div>
        </div>
      </section>

      {/* Services Bento Section */}
      <section id="services" className="py-32 px-6">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-24">
            <h2 className="text-sm font-black text-gold-bright tracking-[0.5em] uppercase mb-4">Elite Intelligence</h2>
            <h3 className="text-5xl font-black text-white font-display uppercase italic">OUR SPECIALIZED <span className="text-gradient-gold">DOMAINS</span></h3>
          </div>

          <div className="grid md:grid-cols-12 gap-6 auto-rows-[300px]">
            <div className="md:col-span-8 glass-pane p-12 flex flex-col justify-end group cursor-pointer hover:glass-pane-gold transition-all">
              <div className="text-gold-bright text-4xl mb-6">✈️</div>
              <h4 className="text-3xl font-black text-white mb-2 uppercase">Neural Flight Search</h4>
              <p className="text-slate-500 max-w-lg">Advanced algorithmic scanning of 800+ airlines to find proprietary pricing unavailable to the general public.</p>
            </div>

            <div className="md:col-span-4 glass-pane p-10 flex flex-col justify-center border-l-gold-bright/20 border-l-2">
              <div className="text-blue-400 text-3xl mb-4">⚖️</div>
              <h4 className="text-xl font-bold text-white mb-2 uppercase">Legal Arsenal</h4>
              <p className="text-slate-500 text-sm italic">"Complete EC No 261/2004 Coverage."</p>
            </div>

            <div className="md:col-span-4 glass-pane p-10 flex flex-col justify-center">
              <div className="text-gold-bright text-3xl mb-4">🛎️</div>
              <h4 className="text-xl font-bold text-white mb-2 uppercase">Stealth Concierge</h4>
              <p className="text-slate-500 text-sm">Anonymous booking & personalized security logistics.</p>
            </div>

            <div className="md:col-span-8 glass-pane p-12 bg-royal-blue/20 relative overflow-hidden flex items-center justify-center">
              <div className="absolute top-0 right-0 p-8 text-[8px] font-mono text-gold-bright/30 uppercase tracking-[0.4em]">SYSTEM://OMEGA_DEPLOYED</div>
              <div className="text-center">
                <h4 className="text-4xl md:text-6xl font-black text-white mb-4 italic tracking-tighter">BEYOND <span className="text-gradient-gold">FIRST CLASS.</span></h4>
                <button className="text-xs font-black uppercase tracking-[0.5em] text-gold-soft hover:text-white transition-colors">Start Mission →</button>
              </div>
            </div>
          </div>
        </div>
      </section>

      <LegalGuide />
      <Destinations />

      {/* Global Command Center (Contact) */}
      <section id="contact" className="py-32 px-6 bg-gradient-to-t from-royal-blue/10 to-transparent">
        <div className="max-w-4xl mx-auto text-center">
          <div className="inline-block p-4 rounded-full bg-gold-bright/5 border border-gold-bright/10 mb-8 animate-float">
            <div className="w-12 h-12 rounded-full bg-gold-bright flex items-center justify-center text-black font-black">
              !
            </div>
          </div>
          <h2 className="text-5xl md:text-7xl font-black text-white mb-8 font-display uppercase tracking-tighter italic">COMMAND YOUR <span className="text-gradient-gold">DOMAIN.</span></h2>
          <p className="text-slate-400 text-xl mb-16 leading-relaxed">
            Our elite handlers are standing by in our global operations center.
            Estimated response time: <span className="text-white font-bold">140 Seconds.</span>
          </p>

          <div className="glass-pane overflow-hidden ring-2 ring-gold-bright/10 p-1">
            <iframe
              src="https://docs.google.com/forms/d/e/1FAIpQLSejJGzQFmdenDKLarechBGV0mI9o7bk62Q3W4TmegHDz1u_5w/viewform?embedded=true"
              width="100%"
              height="800"
              frameBorder="0"
              marginHeight="0"
              marginWidth="0"
              className="grayscale invert opacity-80 transition-all hover:grayscale-0 hover:invert-0 hover:opacity-100"
            >
              Establishing secure link…
            </iframe>
          </div>

          <div className="mt-12 flex items-center justify-center gap-8 opacity-30">
            <div className="h-[1px] w-20 bg-white/20"></div>
            <div className="text-[10px] uppercase font-black tracking-[0.5em] text-white">Encrypted Ops</div>
            <div className="h-[1px] w-20 bg-white/20"></div>
          </div>
        </div>
      </section>

      <Footer />
      <CookieBanner />
    </main>
  );
}
