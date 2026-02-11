import { Button } from '../../components/ui/Button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/Card';
import { ArrowRight, CheckCircle, XCircle, AlertTriangle, Scale, Clock, Banknote, Plane } from 'lucide-react';
import Link from 'next/link';

export const metadata = {
  title: "EU261 Compensation Guide 2026 | TravelKing",
  description: "The definitive guide to claiming up to €600 for delayed, cancelled, or overbooked flights. Master your passenger rights against airlines.",
};

export default function EU261Page() {
  return (
    <div className="container mx-auto px-4 py-24 max-w-5xl">
      {/* Hero Header */}
      <header className="mb-24 text-center">
        <span className="inline-block py-1 px-3 rounded-full bg-accent/10 border border-accent/20 text-accent text-[10px] font-black uppercase tracking-[0.2em] mb-6 animate-pulse-green">
          Regulation EC 261/2004
        </span>
        <h1 className="text-5xl md:text-8xl mb-8 leading-none tracking-tighter text-white font-sans">
          PASSENGER RIGHTS <br/><span className="text-primary">MANIFESTO</span>
        </h1>
        <p className="max-w-3xl mx-auto text-muted-foreground text-lg md:text-xl font-serif mb-12 leading-relaxed">
          The airlines are banking on your ignorance. Regulation EC 261/2004 is the most powerful consumer protection law in aviation history.
          If your flight was delayed, cancelled, or overbooked, they legally owe you up to <span className="text-white font-bold">€600 in cash</span>.
          Not vouchers. Not miles. Cold, hard cash.
        </p>
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button size="lg" className="font-black text-lg h-14 px-10 bg-accent text-black hover:bg-accent/90 shadow-[0_0_20px_rgba(0,255,154,0.3)]" asChild>
                <Link href="https://www.airhelp.com/en/?utm_source=travelking" target="_blank">
                    Check Eligibility Instantly <ArrowRight className="ml-2" />
                </Link>
            </Button>
            <Button variant="outline" size="lg" className="font-black text-lg h-14 px-10" asChild>
                <Link href="#process">
                    Read The Protocol
                </Link>
            </Button>
        </div>
      </header>

      {/* Compensation Tiers */}
      <section className="grid md:grid-cols-3 gap-8 mb-24">
        <Card className="bg-card/40 border-primary/20 hover:border-accent transition-colors duration-300">
            <CardHeader>
                <div className="w-12 h-12 bg-primary/20 rounded-lg flex items-center justify-center mb-4">
                    <Plane className="text-primary" size={24} />
                </div>
                <CardTitle className="text-5xl text-white mb-2 font-black">€250</CardTitle>
                <span className="text-xs font-mono uppercase text-muted-foreground tracking-widest">Type 1: Short Haul</span>
            </CardHeader>
            <CardContent>
                <p className="font-serif text-sm text-muted-foreground leading-relaxed">
                    For all flights covering a distance of up to <strong>1,500 kilometers</strong>.
                    <br/><br/>
                    <em>Example: London (LHR) to Paris (CDG).</em>
                </p>
            </CardContent>
        </Card>

        <Card className="bg-card/40 border-primary/20 scale-105 border-primary shadow-[0_0_30px_-10px_rgba(0,63,250,0.3)] relative z-10">
            <div className="absolute top-0 right-0 bg-accent text-black text-[10px] font-black uppercase px-2 py-1 tracking-widest">Most Common</div>
            <CardHeader>
                 <div className="w-12 h-12 bg-primary/20 rounded-lg flex items-center justify-center mb-4">
                    <Plane className="text-primary" size={24} />
                </div>
                <CardTitle className="text-5xl text-white mb-2 font-black">€400</CardTitle>
                <span className="text-xs font-mono uppercase text-muted-foreground tracking-widest">Type 2: Medium Haul</span>
            </CardHeader>
            <CardContent>
                <p className="font-serif text-sm text-muted-foreground leading-relaxed">
                    For all intra-Community flights of more than 1,500 km and for all other flights between <strong>1,500 and 3,500 kilometers</strong>.
                    <br/><br/>
                    <em>Example: Manchester (MAN) to Tenerife (TFS).</em>
                </p>
            </CardContent>
        </Card>

        <Card className="bg-card/40 border-primary/20 hover:border-accent transition-colors duration-300">
            <CardHeader>
                 <div className="w-12 h-12 bg-primary/20 rounded-lg flex items-center justify-center mb-4">
                    <Plane className="text-primary" size={24} />
                </div>
                <CardTitle className="text-5xl text-white mb-2 font-black">€600</CardTitle>
                <span className="text-xs font-mono uppercase text-muted-foreground tracking-widest">Type 3: Long Haul</span>
            </CardHeader>
            <CardContent>
                <p className="font-serif text-sm text-muted-foreground leading-relaxed">
                    For all other flights exceeding <strong>3,500 kilometers</strong>.
                    <br/><br/>
                    <em>Example: London (LHR) to New York (JFK).</em>
                </p>
            </CardContent>
        </Card>
      </section>

      {/* Deep Dive Content */}
      <div className="grid lg:grid-cols-[2fr_1fr] gap-12">
        <article className="prose prose-invert prose-lg max-w-none prose-headings:font-sans prose-headings:uppercase prose-headings:font-black prose-p:font-serif prose-p:text-muted-foreground prose-li:font-serif prose-strong:text-white">

            <h2 id="process" className="text-3xl text-white flex items-center gap-3">
                <Scale className="text-accent" /> The Legal Framework
            </h2>
            <p>
                Regulation (EC) No 261/2004 is a regulation establishing common rules on compensation and assistance to passengers in the event of denied boarding and of cancellation or long delay of flights. It applies to:
            </p>
            <ul>
                <li>Passengers departing from an airport located in the territory of a Member State.</li>
                <li>Passengers departing from an airport located in a third country to an airport situated in the territory of a Member State, if the operating air carrier is a Community carrier.</li>
            </ul>

            <h3 className="text-white mt-12 mb-6">Critical: The "Extraordinary Circumstances" Lie</h3>
            <p>
                Airlines employ a standard operating procedure of denying valid claims by citing "Extraordinary Circumstances" (Article 5(3)). You must learn to distinguish truth from fiction.
            </p>

            <div className="grid md:grid-cols-2 gap-6 not-prose my-8">
                <div className="bg-red-500/10 border border-red-500/20 p-6 rounded-xl">
                    <h4 className="text-red-500 font-black uppercase flex items-center gap-2 mb-4">
                        <XCircle size={18} /> Invalid Excuses
                    </h4>
                    <ul className="text-sm font-serif space-y-2 text-red-200/80 list-disc pl-4">
                        <li>"Technical Issues" or "Mechanical Failure" (Inherently the airline's responsibility)</li>
                        <li>"Crew Sickness" or Staffing Issues</li>
                        <li>"Operational Reasons" (Vague internal logistics)</li>
                        <li>"Late Incoming Aircraft" (Poor scheduling)</li>
                    </ul>
                </div>
                <div className="bg-green-500/10 border border-green-500/20 p-6 rounded-xl">
                    <h4 className="text-accent font-black uppercase flex items-center gap-2 mb-4">
                        <CheckCircle size={18} /> Valid Reasons
                    </h4>
                    <ul className="text-sm font-serif space-y-2 text-green-200/80 list-disc pl-4">
                        <li>Actual Extreme Weather (Airport closed, unsafe to fly)</li>
                        <li>Air Traffic Control (ATC) Strikes or Restrictions</li>
                        <li>Political Instability or Security Risks</li>
                        <li>Bird Strikes (Deemed extraordinary by courts)</li>
                    </ul>
                </div>
            </div>

            <h3 className="text-white mt-12">The Right to Care (Article 9)</h3>
            <p>
                Regardless of the reason for the delay (even if it IS extraordinary), the airline must provide you with care if the delay exceeds certain thresholds (2-4 hours depending on distance).
            </p>
            <ul>
                <li><strong>Meals and Refreshments:</strong> In reasonable relation to the waiting time.</li>
                <li><strong>Communication:</strong> Two telephone calls, telex or fax messages, or emails.</li>
                <li><strong>Accommodation:</strong> Hotel stay if an overnight stay becomes necessary, plus transport to/from the hotel.</li>
            </ul>
            <p>
                <strong>Pro Tip:</strong> If the airline refuses to provide vouchers, buy reasonable food/hotel yourself and <strong>KEEP THE RECEIPTS</strong>. They are legally required to reimburse you.
            </p>

            <h3 className="text-white mt-12">Step-by-Step Claim Protocol</h3>
            <ol>
                <li><strong>Secure Evidence:</strong> Photograph boarding passes, delay boards, and any communications.</li>
                <li><strong>Demand Reason:</strong> Ask ground staff for the specific reason for the delay in writing.</li>
                <li><strong>Do Not Sign Waivers:</strong> Never sign a document that waives your rights to further compensation in exchange for a sandwich voucher.</li>
                <li><strong>Execute Claim:</strong> You can file manually with the airline (expect 3-6 months of silence/rejection) or use an automated legal service.</li>
            </ol>

        </article>

        {/* Sidebar */}
        <aside className="space-y-8">
            <div className="bg-card border border-border p-6 rounded-xl sticky top-24">
                <h3 className="text-lg font-black uppercase mb-4 text-white flex items-center gap-2">
                    <AlertTriangle className="text-accent" size={18} /> Status Check
                </h3>
                <p className="text-sm text-muted-foreground font-serif mb-6">
                    Compensation rights expire. The statute of limitations varies by country (e.g., 6 years in the UK, 3 years in Germany).
                </p>
                <div className="space-y-4">
                    <div className="flex items-center justify-between text-xs uppercase font-bold text-muted-foreground border-b border-white/10 pb-2">
                        <span>UK / Ireland</span>
                        <span className="text-white">6 Years</span>
                    </div>
                    <div className="flex items-center justify-between text-xs uppercase font-bold text-muted-foreground border-b border-white/10 pb-2">
                        <span>Germany</span>
                        <span className="text-white">3 Years</span>
                    </div>
                    <div className="flex items-center justify-between text-xs uppercase font-bold text-muted-foreground border-b border-white/10 pb-2">
                        <span>France / Spain</span>
                        <span className="text-white">5 Years</span>
                    </div>
                    <div className="flex items-center justify-between text-xs uppercase font-bold text-muted-foreground border-b border-white/10 pb-2">
                        <span>Italy</span>
                        <span className="text-white">2 Years</span>
                    </div>
                </div>

                <div className="mt-8">
                     <Button className="w-full font-black bg-primary hover:bg-primary/90" asChild>
                        <Link href="https://www.airhelp.com/en/?utm_source=travelking" target="_blank">
                            Check Flight Database
                        </Link>
                    </Button>
                </div>
            </div>

            <div className="bg-card border border-border p-6 rounded-xl">
                 <h3 className="text-lg font-black uppercase mb-4 text-white flex items-center gap-2">
                    <Banknote className="text-accent" size={18} /> Refund vs Compensation
                </h3>
                <p className="text-sm text-muted-foreground font-serif mb-4">
                    They are NOT the same.
                </p>
                <ul className="text-sm font-serif space-y-3 text-muted-foreground list-disc pl-4">
                    <li><strong>Refund:</strong> Getting your ticket money back because the flight was cancelled and you didn't fly.</li>
                    <li><strong>Compensation:</strong> Payment for the <em>inconvenience</em> of the delay/cancellation (up to €600).</li>
                </ul>
                <p className="text-sm font-bold text-white mt-4 font-serif">
                    You can often claim BOTH.
                </p>
            </div>
        </aside>
      </div>

      {/* CTA Footer */}
      <section className="mt-24 text-center bg-primary/5 rounded-3xl p-12 border border-primary/10">
          <h2 className="text-3xl font-black mb-6 uppercase text-white">Don't Leave Money on the Table</h2>
          <p className="max-w-2xl mx-auto font-serif text-muted-foreground mb-8 text-lg">
              The airlines count on you giving up. Automated services take a success fee (usually 35%), but they have the legal teams to force the airlines to pay. No win, no fee.
          </p>
          <Button size="lg" className="font-black h-16 px-12 text-xl" asChild>
            <Link href="https://www.airhelp.com/en/?utm_source=travelking" target="_blank">
                Launch Legal Claim Now
            </Link>
          </Button>
      </section>
    </div>
  );
}
