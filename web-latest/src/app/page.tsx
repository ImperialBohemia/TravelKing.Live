import { posts } from '../../.velite';
import Link from 'next/link';
import { ArrowRight, Clock } from 'lucide-react';
import { format } from 'date-fns';
import { Button } from '../components/ui/Button';
import { Card, CardContent } from '../components/ui/Card';
import { LiveIntelWidget } from '../components/features/LiveIntelWidget';

export default function Home() {
  const publishedPosts = posts.filter(p => p.published).sort((a, b) =>
    new Date(b.date).getTime() - new Date(a.date).getTime()
  );

  return (
    <div className="flex flex-col w-full">
      {/* Hero */}
      <section className="relative min-h-screen flex items-center border-b border-border bg-[url('https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=2021&auto=format&fit=crop')] bg-cover bg-center">
        <div className="absolute inset-0 bg-background/60 backdrop-blur-sm"></div>

        <div className="container relative z-10 px-4 py-24 grid lg:grid-cols-2 gap-12 items-center">
            {/* Left Content */}
            <div className="text-center lg:text-left">
                <span className="inline-block py-1 px-3 rounded-full bg-[#00FF9A]/10 border border-[#00FF9A]/20 text-[#00FF9A] text-[10px] font-black uppercase tracking-[0.2em] mb-6 animate-pulse-green">
                    System Online: OMEGA v3.0
                </span>
                <h1 className="text-6xl md:text-8xl xl:text-9xl mb-6 leading-[0.85] tracking-tighter text-white font-sans">
                    TRAVEL<br/>
                    <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#003FFA] to-[#00FF9A]">INTELLIGENCE</span><br/>
                    AGENCY
                </h1>
                <p className="max-w-xl mx-auto lg:mx-0 text-muted-foreground uppercase tracking-widest text-sm mb-12 font-serif leading-relaxed">
                    We deploy autonomous algorithms to recover flight compensation and optimize global logistics for the elite traveler.
                </p>
                <div className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
                    <Button size="lg" className="font-black h-14 px-10 text-lg bg-[#003FFA] hover:bg-[#002ccb]" asChild>
                        <Link href="/eu261">Start Claim Protocol</Link>
                    </Button>
                </div>
            </div>

            {/* Right Widget */}
            <div className="flex justify-center lg:justify-end">
                <LiveIntelWidget />
            </div>
        </div>
      </section>

      {/* Grid */}
      <section className="container mx-auto px-4 py-24 max-w-7xl">
        <div className="flex items-center justify-between mb-12">
            <h2 className="text-3xl font-black text-white uppercase tracking-tighter">Latest Intelligence</h2>
            <div className="h-px bg-border flex-1 ml-8 hidden md:block opacity-30"></div>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {publishedPosts.map((post: any) => (
            <Link
              key={post.slug}
              href={post.permalink}
              className="group flex flex-col h-full"
            >
              <Card className="h-full border-border/30 bg-card/40 hover:border-[#003FFA]/50 transition-all duration-500 overflow-hidden flex flex-col hover:shadow-[0_0_30px_-10px_rgba(0,63,250,0.3)]">
                  <div className="aspect-video relative overflow-hidden">
                    <img
                      src={post.coverImage}
                      alt={post.title}
                      className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 filter grayscale group-hover:grayscale-0"
                    />
                    <div className="absolute top-4 left-4">
                      <span className="bg-[#003FFA] text-white text-[10px] font-black uppercase tracking-widest px-2 py-1">
                        {post.category}
                      </span>
                    </div>
                  </div>

                  <CardContent className="p-8 flex flex-col flex-1">
                    <div className="flex items-center justify-between text-[10px] uppercase font-bold text-muted-foreground tracking-widest mb-4 font-mono">
                      <span className="flex items-center gap-2"><Clock size={12} className="text-[#00FF9A]" /> {format(new Date(post.date), 'MMM dd, yyyy')}</span>
                    </div>

                    <h3 className="text-2xl mb-4 group-hover:text-[#003FFA] transition-colors leading-[0.9] font-black uppercase tracking-tight">
                      {post.title}
                    </h3>

                    <p className="text-muted-foreground text-sm line-clamp-3 mb-8 font-serif leading-relaxed">
                      {post.excerpt}
                    </p>

                    <div className="mt-auto flex items-center justify-between pt-6 border-t border-white/5">
                      <span className="text-[10px] uppercase font-black tracking-widest text-[#00FF9A] flex items-center gap-2 group-hover:translate-x-1 transition-transform">
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
