import { Button } from '../../components/ui/Button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/Card';
import { ArrowRight, CheckCircle, XCircle } from 'lucide-react';
import Link from 'next/link';

export const metadata = {
  title: "EU261 Compensation | TravelKing",
  description: "Claim up to €600 for delayed or cancelled flights. The definitive guide to passenger rights.",
};

export default function EU261Page() {
  return (
    <div className="container mx-auto px-4 py-24 max-w-5xl">
      <header className="mb-24 text-center">
        <span className="text-accent text-xs font-black uppercase tracking-[0.3em] mb-4 block">
          Legal Protocol
        </span>
        <h1 className="text-5xl md:text-8xl mb-8 leading-none tracking-tighter text-white">
          DON'T LET THEM <br/><span className="text-primary">KEEP YOUR MONEY</span>
        </h1>
        <p className="max-w-2xl mx-auto text-muted-foreground text-lg font-serif mb-12">
          If your flight was delayed 3+ hours, cancelled, or overbooked, you are legally entitled to up to €600 in cash compensation. Not vouchers. Cash.
        </p>
        <Button size="lg" className="font-black text-lg h-14 px-10 bg-accent text-black hover:bg-accent/90" asChild>
            <Link href="https://www.airhelp.com/en/?utm_source=travelking" target="_blank">
                Check Eligibility Now <ArrowRight className="ml-2" />
            </Link>
        </Button>
      </header>

      <section className="grid md:grid-cols-3 gap-8 mb-24">
        <Card className="bg-card/40 border-primary/20">
            <CardHeader>
                <CardTitle className="text-4xl text-white mb-2">€250</CardTitle>
                <span className="text-xs font-mono uppercase text-muted-foreground">Short Haul</span>
            </CardHeader>
            <CardContent>
                <p className="font-serif text-sm">Flights under 1,500km (e.g., London to Paris).</p>
            </CardContent>
        </Card>
        <Card className="bg-card/40 border-primary/20 scale-105 border-primary shadow-[0_0_30px_-10px_rgba(0,63,250,0.3)]">
            <CardHeader>
                <CardTitle className="text-4xl text-white mb-2">€400</CardTitle>
                <span className="text-xs font-mono uppercase text-muted-foreground">Medium Haul</span>
            </CardHeader>
            <CardContent>
                <p className="font-serif text-sm">Flights 1,500km - 3,500km (e.g., London to Athens).</p>
            </CardContent>
        </Card>
        <Card className="bg-card/40 border-primary/20">
            <CardHeader>
                <CardTitle className="text-4xl text-white mb-2">€600</CardTitle>
                <span className="text-xs font-mono uppercase text-muted-foreground">Long Haul</span>
            </CardHeader>
            <CardContent>
                <p className="font-serif text-sm">Flights over 3,500km (e.g., London to New York).</p>
            </CardContent>
        </Card>
      </section>

      <section className="mb-24">
          <h2 className="text-3xl font-black mb-12 uppercase">The "Extraordinary" Lie</h2>
          <div className="grid md:grid-cols-2 gap-12">
              <div>
                  <h3 className="text-xl font-bold mb-6 flex items-center gap-3 text-red-500">
                      <XCircle /> Airline Excuses (NOT Valid)
                  </h3>
                  <ul className="space-y-4 font-serif text-muted-foreground">
                      <li>"Technical Difficulties" (Their problem, not yours)</li>
                      <li>"Operational Reasons" (Staff scheduling issues)</li>
                      <li>"Late Incoming Aircraft" (Poor planning)</li>
                  </ul>
              </div>
              <div>
                  <h3 className="text-xl font-bold mb-6 flex items-center gap-3 text-accent">
                      <CheckCircle /> Valid Reasons
                  </h3>
                  <ul className="space-y-4 font-serif text-muted-foreground">
                      <li>Actual Extreme Weather (Airport closed)</li>
                      <li>Air Traffic Control Strikes (Not airline staff)</li>
                      <li>Security Risks / Political Instability</li>
                  </ul>
              </div>
          </div>
      </section>

      <section className="text-center bg-primary/10 rounded-3xl p-12 border border-primary/20">
          <h2 className="text-2xl font-black mb-6 uppercase">Automate Your Claim</h2>
          <p className="max-w-2xl mx-auto font-serif text-muted-foreground mb-8">
              Don't fight their legal team alone. Use a specialist service that only gets paid if you win.
          </p>
          <Button size="lg" className="font-black" asChild>
            <Link href="https://www.airhelp.com/en/?utm_source=travelking" target="_blank">
                Launch Claim Process
            </Link>
          </Button>
      </section>
    </div>
  );
}
