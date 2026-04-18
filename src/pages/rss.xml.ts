import { getCollection } from 'astro:content';
import type { APIRoute } from 'astro';

export const GET: APIRoute = async () => {
  const posts = await getCollection('blog', ({ data }) => !data.draft);

  const sorted = posts.sort(
    (a, b) =>
      new Date(b.data.publishDate).getTime() -
      new Date(a.data.publishDate).getTime(),
  );

  const base = 'https://cardinalsixcyber.com';

  const items = sorted
    .map((post) => {
      const url = `${base}/blog/${post.id}`;
      const pubDate = new Date(post.data.publishDate).toUTCString();
      const categories = (post.data.topics ?? [])
        .map((t) => `<category>${t}</category>`)
        .join('');
      return `<item><title><![CDATA[${post.data.title}]]></title><link>${url}</link><guid isPermaLink="true">${url}</guid><pubDate>${pubDate}</pubDate><description><![CDATA[${post.data.description}]]></description>${categories}</item>`;
    })
    .join('');

  const xml = `<?xml version="1.0" encoding="UTF-8"?><rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>Cardinal Six Cyber — Blog</title><link>${base}/blog</link><description>Practitioner analysis and practical guidance on CMMC, DFARS, NIST, and federal cybersecurity compliance for defense contractors.</description><language>en-us</language><lastBuildDate>${new Date().toUTCString()}</lastBuildDate><atom:link href="${base}/rss.xml" rel="self" type="application/rss+xml"/>${items}</channel></rss>`;

  return new Response(xml, {
    headers: {
      'Content-Type': 'application/rss+xml; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
