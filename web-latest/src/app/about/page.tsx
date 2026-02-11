import { Button } from '../../components/ui/Button';
import Link from 'next/link';

export const metadata = {
  title: "The Network | TravelKing",
  description: "About the OMEGA Intelligence Hub and TravelKing operations.",
};

export default function AboutPage() {
  return (
    <div className="container mx-auto px-4 py-24 max-w-4xl text-center">
      <span className="text-primary text-xs font-black uppercase tracking-[0.3em] mb-4 block">
          System Identity
      </span>
      <h1 className="text-5xl md:text-8xl mb-12 leading-none tracking-tighter text-white">
        THE <span className="text-accent">OMEGA</span> HUB
      </h1>

      <p className="text-xl font-serif text-muted-foreground leading-relaxed mb-12 max-w-2xl mx-auto">
        TravelKing.Live is not a travel blog. It is an autonomous intelligence node designed to maximize traveler leverage against corporate airlines.
      </p>

      <div className="grid md:grid-cols-2 gap-8 text-left mb-24">
          <div className="bg-card/40 p-8 border border-border rounded-xl">
              <h3 className="text-2xl font-black uppercase mb-4 text-white">Mission</h3>
              <p className="font-serif text-muted-foreground">To democratize elite travel logistics and ensure no passenger leaves money on the table.</p>
          </div>
          <div className="bg-card/40 p-8 border border-border rounded-xl">
              <h3 className="text-2xl font-black uppercase mb-4 text-white">Operator</h3>
              <p className="font-serif text-muted-foreground">Authorized by Imperial Bohemia. Powered by OMEGA AI (v3.0) and Google Enterprise Infrastructure.</p>
          </div>
      </div>

      <Button size="lg" className="font-black" asChild>
          <Link href="/contact">Establish Contact</Link>
      </Button>
    </div>
  );
}
