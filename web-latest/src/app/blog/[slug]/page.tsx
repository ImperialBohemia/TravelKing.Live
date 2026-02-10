import { Metadata } from "next";
import { notFound } from "next/navigation";
import Link from "next/link";
import { ArrowLeft, Clock, User, Calendar } from "lucide-react";

// Mock post data for SSR simulation
const posts: Record<string, any> = {
  "sovereign-travel-2026": {
    title: "Sovereign Travel: The New Global Standard",
    content: "Sovereign travel is not just about luxury; it's about the absolute control over one's movement. In 2026, the global elite are moving towards decentralized travel infrastructure...",
    author: "Stanislav Pasztorek",
    date: "2026-02-10",
    category: "Intelligence",
    readTime: "6 min"
  },
  "eu261-hidden-mechanics": {
    title: "EU261: Hidden Mechanics of Compensation",
    content: "The legal framework of EU261 provides significant protection, but the hidden mechanics of extraction require deep API integration with airline logistics...",
    author: "OMEGA Handler",
    date: "2026-02-08",
    category: "Legal",
    readTime: "4 min"
  }
};

export async function generateMetadata({ params }: { params: { slug: string } }): Promise<Metadata> {
  const post = posts[params.slug];
  if (!post) return { title: "Post Not Found" };

  return {
    title: `${post.title} | TravelKing OMEGA`,
    description: `Elite travel intelligence: ${post.title}`,
    openGraph: {
      title: post.title,
      description: post.content.substring(0, 160),
      type: "article",
    }
  };
}

export default function BlogPost({ params }: { params: { slug: string } }) {
  const post = posts[params.slug];
  if (!post) notFound();

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": post.title,
    "author": { "@type": "Person", "name": post.author },
    "datePublished": post.date,
    "articleBody": post.content
  };

  return (
    <article className="w-full bg-black min-h-screen pt-32 pb-24">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />

      <div className="container px-4 sm:px-6 max-w-4xl mx-auto">
        <Link href="/#blog" className="inline-flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-primary mb-12 hover:gap-3 transition-all">
          <ArrowLeft className="w-3 h-3" /> Back to Intelligence
        </Link>

        <header className="mb-16">
          <div className="flex items-center gap-4 text-[10px] font-bold text-primary uppercase tracking-[0.3em] mb-6">
            <span className="bg-primary/10 px-3 py-1 rounded-full">{post.category}</span>
            <span className="flex items-center gap-1"><Clock className="w-3 h-3" /> {post.readTime}</span>
          </div>

          <h1 className="text-4xl sm:text-6xl md:text-7xl font-black text-white italic uppercase tracking-tighter leading-[0.9] mb-8">
            {post.title}
          </h1>

          <div className="flex items-center gap-6 border-y border-white/5 py-6 text-muted-foreground text-xs uppercase font-bold tracking-widest">
            <span className="flex items-center gap-2"><User className="w-4 h-4 text-primary" /> {post.author}</span>
            <span className="flex items-center gap-2"><Calendar className="w-4 h-4 text-primary" /> {post.date}</span>
          </div>
        </header>

        <div className="prose prose-invert prose-primary max-w-none text-muted-foreground text-lg leading-relaxed font-light">
          <p className="first-letter:text-7xl first-letter:font-black first-letter:text-primary first-letter:mr-3 first-letter:float-left first-letter:italic">
            {post.content}
          </p>
        </div>
      </div>
    </article>
  );
}
