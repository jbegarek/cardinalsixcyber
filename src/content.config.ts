import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
    schema: z.object({
        title: z.string(),
        description: z.string().max(180),
        publishDate: z.coerce.date(),
        updatedDate: z.coerce.date().optional(),
        author: z.string(),
        lane: z.enum(['practical', 'research']),
        topics: z.array(z.string()).min(1),
        featured: z.boolean().default(false),
        draft: z.boolean().default(false),
        heroStyle: z.string().optional(),
        heroImage: z.string().optional(),
        citations: z.boolean().default(false),
        diagrams: z.boolean().default(false),
        canonicalUrl: z.string().url().optional(),
    }),
});

export const collections = {
    blog,
};
