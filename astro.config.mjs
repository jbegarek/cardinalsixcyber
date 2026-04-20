import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
    site: 'https://cardinalsixcyber.com',
    integrations: [
        sitemap({
            filter: (page) =>
                !page.includes('/404') &&
                !page.endsWith('/_astro/') &&
                !page.includes('/backup/'),
        }),
        mdx(),
    ],
    build: {
        format: 'file',
    },
});
