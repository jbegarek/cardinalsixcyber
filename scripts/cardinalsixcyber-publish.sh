#!/usr/bin/env bash
set -euo pipefail

SRC=/home/justin/src/cardinalsixcyber
DEPLOY=/home/justin/deploy/cardinalsixcyber
IMAGE=cardinalsixcyber:local
CONTAINER=cardinalsixcyber
LOG=/home/justin/logs/cardinalsixcyber-publish.log

exec >>"$LOG" 2>&1
echo "===== $(date -Is) publish run starting ====="

cd "$SRC"
git fetch --quiet origin main
LOCAL=$(git rev-parse main)
REMOTE=$(git rev-parse origin/main)
if [ "$LOCAL" = "$REMOTE" ]; then
  echo "no new commits ($LOCAL); rebuilding anyway for date-gated static content"
else
  echo "resetting $LOCAL -> $REMOTE"
fi
git reset --hard origin/main

echo "syncing deployable paths into $DEPLOY"
mkdir -p "$DEPLOY"
for p in src public data nginx; do
  rm -rf "$DEPLOY/$p"
  cp -r "$SRC/$p" "$DEPLOY/$p"
done
for f in astro.config.mjs tsconfig.json package.json package-lock.json Dockerfile compose.yaml .dockerignore; do
  if [ -f "$SRC/$f" ]; then
    cp "$SRC/$f" "$DEPLOY/$f"
  fi
done

cd "$DEPLOY"
echo "building docker image"
docker compose build --no-cache app
docker image inspect "$IMAGE" --format 'built image {{.Id}} created {{.Created}}'
echo "recreating container"
if docker ps -a --format '{{.Names}}' | grep -Fxq "$CONTAINER"; then
  docker rm -f "$CONTAINER"
fi
docker compose up -d --no-deps app

docker ps --filter "name=$CONTAINER" --format "table {{.Names}}\t{{.Status}}\t{{.Image}}"
echo "===== $(date -Is) publish run done (rebuilt) ====="
