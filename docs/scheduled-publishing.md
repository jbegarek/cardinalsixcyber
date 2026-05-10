# Scheduled Blog Post Publishing

## How it works

The blog index, post pages, and RSS feed filter posts by `publishDate <= now`. A post with a future `publishDate` is not built into the site — its route does not exist, it is hidden from `/blog`, and it is omitted from `/rss.xml`. When the site is rebuilt on or after the post's `publishDate`, the post appears.

This means the publishing schedule is a function of two things:

1. The `publishDate` value in each post's frontmatter.
2. How often the Docker site is rebuilt.

To publish one post per day, the site needs to rebuild at least once per day.

## Daily rebuild via server-side cron (recommended)

The Docker server lives at `justin@192.168.0.240` on the LAN. The simplest scheduler is a server-side cron entry.

SSH to the server and add this line to your crontab (`crontab -e`):

```
0 9 * * * cd /home/justin/deploy/cardinalsixcyber && git pull --quiet && docker compose build --quiet && docker compose up -d >/dev/null 2>&1
```

This runs every day at 09:00 server time:

- `git pull` — fetches new commits (including any new scheduled posts).
- `docker compose build` — rebuilds the image so the new post is baked into the static site.
- `docker compose up -d` — recreates the container so the new build serves traffic.

To check it is set up:

```
crontab -l
```

To watch it run:

```
journalctl -u cron --since "today"
```

## Alternative: GitHub Actions

A GitHub Actions workflow cannot reach `192.168.0.240` directly because that is a LAN address. If you want GitHub Actions to drive the rebuild, you would need either:

- A self-hosted GitHub runner on the LAN.
- A VPN/Tailscale path from GitHub-hosted runners to the server.
- The server exposed via a public ingress with SSH.

None of these is recommended unless you have an independent reason to use them. Server-side cron is simpler and avoids credentials in GitHub secrets.

## Changing a post's publish date

Edit the post's frontmatter:

```
publishDate: 2026-05-15
```

Commit. The post will become visible after the next rebuild that occurs on or after that date.

## Checking what is scheduled

```
grep -h "^publishDate:" src/content/blog/*.md | sort
```

This lists every post's publishDate so you can see the schedule at a glance.

## Manually publishing a scheduled post early

Run the deploy script from your workstation:

```
pwsh scripts/deploy-docker-server.ps1
```

Any post whose `publishDate` is on or before the day you run the script will be built. The next scheduled cron run on the server is harmless — it will pull, build, and recreate again with the same content.
