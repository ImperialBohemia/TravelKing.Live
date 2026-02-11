import { posts } from '../../.velite';
import Link from 'next/link';
import { ArrowRight, Clock, User } from 'lucide-react';
import { format } from 'date-fns';
import { Button } from '../components/ui/Button';
import { Card, CardContent } from '../components/ui/Card';
import { FlightSearch } from '../components/features/FlightSearch';

export default function Home() {
  const publishedPosts = posts.filter(p => p.published).sort((a, b) =>
    new Date(b.date).getTime() - new Date(a.date).getTime()
  );

  return (
    <div className="flex flex-col w-full">
      {/* Hero */}
      <section className="relative h-[80vh] flex flex-col items-center justify-center border-b border-border bg-[url('https://images.unsplash.com/photo-1544006659-f0b21f04cb1d?q=80&w=1600&auto=format&fit=crop')] bg-cover bg-center">
        <div className="absolute inset-0 bg-background/80 backdrop-blur-sm"></div>
        <div className="container relative z-10 px-4 text-center mt-[-10vh]">
          <span className="inline-block py-1 px-3 rounded-full bg-accent/10 border border-accent/20 text-accent text-[10px] font-black uppercase tracking-[0.2em] mb-6 animate-pulse-green">
            System Online: OMEGA v3.0
          </span>
          <h1 className="text-6xl md:text-9xl mb-6 leading-none tracking-tighter text-white">
            THE <span className="text-primary">INTEL</span> FEED
          </h1>
          <p className="max-w-xl mx-auto text-muted-foreground uppercase tracking-widest text-sm mb-12 font-serif">
            Strategic travel briefing for the elite operative. Flight hacks, compensation recovery, and global logistics.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button size="lg" className="font-black h-12 px-8" asChild>
                <Link href="/eu261">Start Compensation Claim</Link>
            </Button>
            <Button variant="outline" size="lg" className="font-black h-12 px-8" asChild>
                <Link href="/about">Access Network</Link>
            </Button>
          </div>
        </div>
      </section>

      {/* Flight Search Widget - Overlapping Hero */}
      <FlightSearch />

      {/* Grid */}
      <section className="container mx-auto px-4 py-24 max-w-7xl">
        <div className="flex items-center justify-between mb-12">
            <h2 className="text-3xl font-black text-white">Latest Intelligence</h2>
            <div className="h-px bg-border flex-1 ml-8 hidden md:block"></div>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {publishedPosts.map((post: any) => (
            <Link
              key={post.slug}
              href={post.permalink}
              className="group flex flex-col h-full"
            >
              <Card className="h-full border-border/50 bg-card/40 hover:border-primary/50 transition-all duration-500 overflow-hidden flex flex-col">
                  <div className="aspect-video relative overflow-hidden">
                    <img
                      src={post.coverImage}
                      alt={post.title}
                      className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 filter grayscale group-hover:grayscale-0"
                    />
                    <div className="absolute top-4 left-4">
                      <span className="bg-primary text-white text-[10px] font-black uppercase tracking-widest px-2 py-1 rounded-sm">
                        {post.category}
                      </span>
                    </div>
                  </div>

                  <CardContent className="p-8 flex flex-col flex-1">
                    <div className="flex items-center justify-between text-[10px] uppercase font-bold text-muted-foreground tracking-widest mb-4 font-mono">
                      <span className="flex items-center gap-2"><Clock size={12} className="text-accent" /> {format(new Date(post.date), 'MMM dd, yyyy')}</span>
                    </div>

                    <h3 className="text-2xl mb-4 group-hover:text-primary transition-colors leading-tight font-black uppercase">
                      {post.title}
                    </h3>

                    <p className="text-muted-foreground text-sm line-clamp-3 mb-8 font-serif leading-relaxed">
                      {post.excerpt}
                    </p>

                    <div className="mt-auto flex items-center justify-between pt-6 border-t border-white/5">
                      <span className="text-[10px] uppercase font-black tracking-widest text-primary flex items-center gap-2 group-hover:translate-x-1 transition-transform">
                        Read Briefing <ArrowRight size={12} />
                      </span>
                    </div>
                  </CardContent>
              </Card>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
