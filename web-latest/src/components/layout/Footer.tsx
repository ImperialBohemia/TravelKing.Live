import Link from "next/link";

export function Footer() {
  return (
    <footer className="w-full border-t border-border bg-black py-12 md:py-24 lg:py-32">
      <div className="container px-4 md:px-6">
        <div className="grid gap-8 sm:grid-cols-2 md:grid-cols-4">
          <div className="flex flex-col gap-2">
            <div className="flex items-center gap-2">
               <span className="text-lg font-black italic tracking-tighter text-white font-sans">
                TRAVELKING<span className="text-primary">.LIVE</span>
              </span>
            </div>
            <p className="text-xs text-muted-foreground font-serif leading-relaxed">
              Autonomous flight intelligence and compensation recovery systems.
              Operated by OMEGA for Imperial Bohemia.
            </p>
          </div>

          <div className="flex flex-col gap-2">
            <h3 className="text-sm font-bold uppercase tracking-widest text-primary font-sans">Intelligence</h3>
            <Link href="/eu261" className="text-xs hover:text-white transition-colors">EU261 Guide</Link>
            <Link href="/blog" className="text-xs hover:text-white transition-colors">Intel Feed</Link>
          </div>

          <div className="flex flex-col gap-2">
            <h3 className="text-sm font-bold uppercase tracking-widest text-primary font-sans">Legal</h3>
            <Link href="/privacy-policy" className="text-xs hover:text-white transition-colors">Privacy Protocol</Link>
            <Link href="/terms" className="text-xs hover:text-white transition-colors">Terms of Engagement</Link>
          </div>

          <div className="flex flex-col gap-2">
            <h3 className="text-sm font-bold uppercase tracking-widest text-primary font-sans">Network</h3>
            <Link href="https://twitter.com/TravelKingLive" className="text-xs hover:text-white transition-colors">X (Twitter)</Link>
            <Link href="https://bsky.app/profile/travelking.live" className="text-xs hover:text-white transition-colors">Bluesky</Link>
          </div>
        </div>

        <div className="mt-12 flex flex-col gap-4 sm:flex-row justify-between items-center border-t border-border pt-8">
          <p className="text-[10px] uppercase tracking-[0.2em] text-muted-foreground font-mono">
            © 2026 TRAVELKING.LIVE | SYSTEM ACTIVE
          </p>
        </div>
      </div>
    </footer>
  );
}
