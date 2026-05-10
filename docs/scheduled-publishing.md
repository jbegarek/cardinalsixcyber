# Scheduled Blog Post Publishing

## How it works

The blog index, post pages, and RSS feed filter posts by `publishDate <= now`. A post with a future `publishDate` is not built into the site — its route does not exist, it is hidden from `/blog`, and it is omitted from `/rss.xml`. When the site is rebuilt on or after the post's `publishDate`, the post appears.

This means the publishing schedule is a function of two things:

1. The `publishDate` value in each post's frontmatter.
2. How often the Docker site is rebuilt.

To publish one post per day, the site needs to rebuild at least once per day.

## What is installed on the server

A daily cron on the Docker server (`justin@192.168.0.240`) drives the rebuild. Three pieces are in place:

**Source mirror at `/home/justin/src/cardinalsixcyber`.** A shallow clone of the GitHub repo. The publish script pulls from `origin/main` here.

**Publish script at `/home/justin/bin/cardinalsixcyber-publish.sh`.** Pulls the source clone, exits as a no-op if nothing changed, otherwise syncs `src/`, `public/`, `data/`, `nginx/` and the top-level config files into `/home/justin/deploy/cardinalsixcyber`, runs `docker buildx build --load --no-cache`, and recreates the container with `docker compose up -d --force-recreate --no-build`.

**Cron entry running daily at 09:00 server time.** Logs append to `/home/justin/logs/cardinalsixcyber-publish.log`.

```
0 9 * * * /home/justin/bin/cardinalsixcyber-publish.sh
```

The script is idempotent. If no new commits exist on `origin/main`, it exits without rebuilding.

## Operational checks

Verify the cron is installed:

```
ssh justin@192.168.0.240 'crontab -l | grep cardinal'
```

Tail the publish log:

```
ssh justin@192.168.0.240 'tail -40 ~/logs/cardinalsixcyber-publish.log'
```

Trigger a publish on demand (e.g., to push a scheduled post live early):

```
ssh justin@192.168.0.240 '~/bin/cardinalsixcyber-publish.sh'
```

## Changing a post's publish date

Edit the post's frontmatter:

```
publishDate: 2026-05-15
```

Commit and push. The post will become visible after the next cron run on or after that date, or after a manual publish-script run.

## Checking the schedule

```
grep -h "^publishDate:" src/content/blog/*.md | sort
```

This lists every post's publishDate so you can see the schedule at a glance.

## Workstation deploy script still works

The original `scripts/deploy-docker-server.ps1` SCP-and-rebuild flow remains valid for ad-hoc deploys from the workstation. It and the cron do not conflict — they touch the same `/home/justin/deploy/cardinalsixcyber` working directory and run the same docker build steps, just from different sources (workstation SCP vs. server git clone).

## Changing the rebuild time

Edit the cron entry on the server:

```
ssh justin@192.168.0.240 'crontab -e'
```

The default is 09:00 server time. Adjust the `0 9` fields to suit (e.g., `0 6` for 06:00, or `0 14` for 14:00).
