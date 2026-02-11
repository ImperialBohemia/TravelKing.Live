import { posts } from '../../../../.velite';
import { notFound } from 'next/navigation';
import { format } from 'date-fns';
import { ChevronLeft } from 'lucide-react';
import Link from 'next/link';

export function generateStaticParams() {
    return posts.map((post) => ({
        slug: post.slug,
    }));
}

export default async function BlogPost({ params }: { params: Promise<{ slug: string }> }) {
    const { slug } = await params;
    const post = posts.find((p: any) => p.slug === slug);

    if (!post) {
        notFound();
    }

    return (
        <div className="min-h-screen py-24">
            <div className="container mx-auto px-4 max-w-4xl">
                <Link
                    href="/"
                    className="flex items-center gap-2 text-xs font-black uppercase tracking-widest text-muted-foreground hover:text-primary mb-12 transition-colors"
                >
                    <ChevronLeft size={14} /> Back to Intelligence Feed
                </Link>

                <header className="mb-16">
                    <span className="text-primary text-[10px] font-black uppercase tracking-[0.3em] mb-4 block">
                        {post.category} {"// INTEL_REPORT"}
                    </span>
                    <h1 className="text-4xl md:text-7xl mb-8 leading-tight">{post.title}</h1>

                    <div className="flex items-center gap-8 py-8 border-y border-border">
                        <div className="flex flex-col gap-1">
                            <span className="text-muted-foreground text-[8px] font-bold uppercase tracking-widest">Author</span>
                            <span className="text-xs font-black uppercase tracking-wider">{post.author}</span>
                        </div>
                        <div className="flex flex-col gap-1 text-right ml-auto">
                            <span className="text-muted-foreground text-[8px] font-bold uppercase tracking-widest">Authored Date</span>
                            <span className="text-xs font-black uppercase tracking-wider">{format(new Date(post.date), 'MMMM dd, yyyy')}</span>
                        </div>
                    </div>
                </header>

                <div className="aspect-video mb-16 rounded-3xl overflow-hidden border border-border">
                    <img
                        src={post.coverImage}
                        alt={post.title}
                        className="w-full h-full object-cover"
                    />
                </div>

                <article className="prose prose-invert prose-primary max-w-none prose-headings:italic prose-headings:uppercase prose-headings:font-black">
                    <div dangerouslySetInnerHTML={{ __html: post.content }} />
                </article>

                <footer className="mt-24 pt-12 border-t border-border flex justify-between items-center">
                    <div className="text-[10px] text-muted-foreground font-bold uppercase tracking-[0.2em]">
                        END OF INTELLIGENCE BRIEF
                    </div>
                    <Link href="/" className="text-xs font-black text-primary uppercase tracking-widest hover:text-white transition-colors">
                        Return to Front
                    </Link>
                </footer>
            </div>
        </div>
    );
}
