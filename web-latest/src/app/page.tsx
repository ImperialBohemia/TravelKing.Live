import { posts } from '../../.velite';
import Link from 'next/link';
import { ArrowRight, Clock, User } from 'lucide-react';
import { format } from 'date-fns';

export default function Home() {
  const publishedPosts = posts.filter(p => p.published).sort((a, b) =>
    new Date(b.date).getTime() - new Date(a.date).getTime()
  );

  return (
    <div className="flex flex-col w-full">
      {/* Hero */}
      <section className="relative h-[50vh] flex items-center justify-center border-b border-border bg-[url('https://images.unsplash.com/photo-1544006659-f0b21f04cb1d?q=80&w=1600&auto=format&fit=crop')] bg-cover bg-center">
        <div className="absolute inset-0 bg-black/80"></div>
        <div className="container relative z-10 px-4 text-center">
          <h1 className="text-6xl md:text-9xl mb-4 leading-none">THE <span className="text-primary">INTEL</span> FEED</h1>
          <p className="max-w-xl mx-auto text-muted-foreground uppercase tracking-widest text-sm">Strategic travel briefing for the elite operative.</p>
        </div>
      </section>

      {/* Grid */}
      <section className="container mx-auto px-4 py-24 max-w-7xl">
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {publishedPosts.map((post: any) => (
            <Link
              key={post.slug}
              href={post.permalink}
              className="group flex flex-col glass rounded-2xl overflow-hidden hover:border-primary/40 transition-all duration-500"
            >
              <div className="aspect-video relative overflow-hidden">
                <img
                  src={post.coverImage}
                  alt={post.title}
                  className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
                />
                <div className="absolute top-4 left-4">
                  <span className="bg-primary text-black text-[8px] font-black uppercase px-2 py-1 rounded">
                    {post.category}
                  </span>
                </div>
              </div>

              <div className="p-8 flex flex-col flex-1">
                <div className="flex items-center justify-between text-[8px] uppercase font-bold text-muted-foreground tracking-widest mb-4">
                  <span className="flex items-center gap-1"><Clock size={10} /> {format(new Date(post.date), 'MMM dd, yyyy')}</span>
                  <span className="flex items-center gap-1"><User size={10} /> {post.author}</span>
                </div>

                <h3 className="text-2xl mb-4 group-hover:text-primary transition-colors leading-tight">
                  {post.title}
                </h3>

                <p className="text-muted-foreground text-sm line-clamp-3 mb-8">
                  {post.excerpt}
                </p>

                <div className="mt-auto flex items-center justify-between pt-6 border-t border-border">
                  <span className="text-[10px] uppercase font-black tracking-widest text-primary flex items-center gap-2">
                    Access Intel <ArrowRight size={12} />
                  </span>
                </div>
              </div>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
