import { defineConfig, s } from 'velite';

export default defineConfig({
    root: 'content',
    output: {
        data: '.velite',
        assets: 'public/static',
        base: '/static/',
        name: '[name]-[hash].[ext]',
        clean: true
    },
    collections: {
        posts: {
            name: 'Post',
            pattern: 'posts/**/*.md',
            schema: s
                .object({
                    title: s.string().max(99),
                    slug: s.slug('posts'),
                    date: s.isodate(),
                    excerpt: s.string().max(200),
                    coverImage: s.string(),
                    category: s.string(),
                    author: s.string(),
                    published: s.boolean().default(true),
                    content: s.markdown()
                })
                .transform((data) => ({ ...data, permalink: `/blog/${data.slug}` }))
        }
    }
});
