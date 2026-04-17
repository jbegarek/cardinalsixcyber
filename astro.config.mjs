import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
    site: 'https://cardinalsixcyber.com',
    integrations: [sitemap(), mdx()],
    build: {
        format: 'file',
    },
});
