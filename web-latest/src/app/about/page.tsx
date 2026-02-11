import { Button } from '../../components/ui/Button';
import Link from 'next/link';
import { Shield, Globe, Cpu, Users } from 'lucide-react';

export const metadata = {
  title: "The OMEGA Network | TravelKing",
  description: "About the OMEGA Intelligence Hub and TravelKing operations. The mission to democratize elite travel logistics.",
};

export default function AboutPage() {
  return (
    <div className="container mx-auto px-4 py-24 max-w-4xl">
      {/* Header */}
      <div className="text-center mb-24">
        <span className="text-primary text-xs font-black uppercase tracking-[0.3em] mb-4 block">
            System Identity
        </span>
        <h1 className="text-5xl md:text-8xl mb-12 leading-none tracking-tighter text-white font-sans">
          THE <span className="text-accent">OMEGA</span> HUB
        </h1>
        <p className="text-xl font-serif text-muted-foreground leading-relaxed mb-12 max-w-2xl mx-auto">
            TravelKing.Live is not a blog. It is a decentralized intelligence node designed to maximize traveler leverage against corporate airlines and global logistical friction.
        </p>
      </div>

      {/* Manifesto */}
      <div className="prose prose-invert prose-lg max-w-none mb-24 prose-headings:font-sans prose-headings:uppercase prose-headings:font-black prose-p:font-serif prose-p:text-muted-foreground">
        <h2>The Operational Mandate</h2>
        <p>
            The modern travel landscape is hostile. Airlines algorithmically overbook flights to maximize yield. Dynamic pricing engines exploit your search history. Complex legal frameworks hide your rights behind bureaucracy.
        </p>
        <p>
            The <strong>OMEGA Intelligence Hub</strong> was activated to level the playing field. We believe that elite travel logistics—the kind reserved for diplomats and billionaires—should be accessible to the informed operative.
        </p>
        <p>
            We do not provide "travel inspiration." We provide <strong>actionable intelligence</strong>. We analyze regulations, dissect airline contracts of carriage, and monitor global safety vectors to ensure your mission success.
        </p>
      </div>

      {/* Core Values */}
      <div className="grid md:grid-cols-2 gap-8 mb-24">
          <div className="bg-card/40 p-8 border border-border rounded-xl hover:border-primary/50 transition-colors">
              <Shield className="text-accent mb-6" size={32} />
              <h3 className="text-2xl font-black uppercase mb-4 text-white font-sans">Sovereignty</h3>
              <p className="font-serif text-muted-foreground leading-relaxed">
                  The traveler must remain sovereign. We equip you with the legal knowledge (EC 261, Montreal Convention) to enforce your rights against corporate entities.
              </p>
          </div>
          <div className="bg-card/40 p-8 border border-border rounded-xl hover:border-primary/50 transition-colors">
              <Cpu className="text-primary mb-6" size={32} />
              <h3 className="text-2xl font-black uppercase mb-4 text-white font-sans">Automation</h3>
              <p className="font-serif text-muted-foreground leading-relaxed">
                  We reject manual inefficiency. We leverage algorithmic tools to predict delays, automate compensation claims, and find error fares before they are corrected.
              </p>
          </div>
          <div className="bg-card/40 p-8 border border-border rounded-xl hover:border-primary/50 transition-colors">
              <Globe className="text-white mb-6" size={32} />
              <h3 className="text-2xl font-black uppercase mb-4 text-white font-sans">Global Reach</h3>
              <p className="font-serif text-muted-foreground leading-relaxed">
                  Our intelligence network spans all major aviation hubs. From the strict regulations of the EU to the wild west of deregulated markets, we have a protocol.
              </p>
          </div>
          <div className="bg-card/40 p-8 border border-border rounded-xl hover:border-primary/50 transition-colors">
              <Users className="text-accent mb-6" size={32} />
              <h3 className="text-2xl font-black uppercase mb-4 text-white font-sans">The Collective</h3>
              <p className="font-serif text-muted-foreground leading-relaxed">
                  Information shared is power multiplied. The OMEGA network thrives on the shared data of thousands of operatives reporting ground conditions in real-time.
              </p>
          </div>
      </div>

      {/* Operator Data */}
      <div className="border-t border-border pt-12 text-center">
          <p className="font-mono text-xs uppercase tracking-widest text-muted-foreground mb-4">
              Authorized by Imperial Bohemia
          </p>
          <p className="font-mono text-xs uppercase tracking-widest text-muted-foreground mb-8">
              System Architecture: Next.js 16 / Tailwind / OMEGA AI v3.0
          </p>
          <Button size="lg" className="font-black" asChild>
              <Link href="/contact">Establish Contact</Link>
          </Button>
      </div>
    </div>
  );
}
