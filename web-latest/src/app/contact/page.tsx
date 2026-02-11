import { Button } from '../../components/ui/Button';
import { Card, CardContent } from '../../components/ui/Card';

export const metadata = {
  title: "Contact Protocol | TravelKing",
  description: "Secure communication channels.",
};

export default function ContactPage() {
  return (
    <div className="container mx-auto px-4 py-24 max-w-3xl">
      <header className="mb-16">
        <h1 className="text-4xl md:text-6xl mb-6 font-black uppercase text-white">Contact Protocol</h1>
        <p className="text-muted-foreground font-serif text-lg">
            Direct secure line to OMEGA Operations.
        </p>
      </header>

      <Card>
          <CardContent className="p-8">
            <form className="space-y-6">
                <div className="grid md:grid-cols-2 gap-6">
                    <div className="space-y-2">
                        <label className="text-xs font-black uppercase tracking-widest text-muted-foreground">Codename</label>
                        <input className="w-full bg-background/50 border border-border rounded-md p-3 text-white focus:border-primary outline-none transition-colors" placeholder="Name" />
                    </div>
                    <div className="space-y-2">
                        <label className="text-xs font-black uppercase tracking-widest text-muted-foreground">Frequency</label>
                        <input className="w-full bg-background/50 border border-border rounded-md p-3 text-white focus:border-primary outline-none transition-colors" placeholder="Email" />
                    </div>
                </div>
                <div className="space-y-2">
                    <label className="text-xs font-black uppercase tracking-widest text-muted-foreground">Briefing</label>
                    <textarea className="w-full bg-background/50 border border-border rounded-md p-3 text-white h-32 focus:border-primary outline-none transition-colors" placeholder="Message content..." />
                </div>
                <Button className="w-full font-black text-lg bg-primary hover:bg-primary/90">
                    Transmit
                </Button>
            </form>
          </CardContent>
      </Card>

      <div className="mt-12 text-center">
          <p className="text-sm font-mono text-muted-foreground">
              Direct Uplink: <a href="mailto:ops@travelking.live" className="text-primary hover:text-white">ops@travelking.live</a>
          </p>
      </div>
    </div>
  );
}
