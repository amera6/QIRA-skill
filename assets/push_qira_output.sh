#!/usr/bin/env bash
#
# push_qira_output.sh — commit a new file into a local qira-assessor repo
# clone's outputs/ folder and push it. Run this from Git Bash on your own
# machine (already authenticated to GitHub) — Claude never runs this or
# handles your git credentials.
#
# Usage:
#   ./push_qira_output.sh /path/to/repo /path/to/new_file.md "commit message"
#
# Example:
#   ./push_qira_output.sh ~/repos/qira-assessor-skill \
#       ~/Downloads/QIRA-QC-2026-07-29-LEGIONELLOSIS-v1.md \
#       "Add Legionnaires/Quebec assessment for review"

set -euo pipefail

REPO_DIR="${1:?Usage: $0 <repo_dir> <file_to_add> <commit_message>}"
SRC_FILE="${2:?Usage: $0 <repo_dir> <file_to_add> <commit_message>}"
COMMIT_MSG="${3:?Usage: $0 <repo_dir> <file_to_add> <commit_message>}"

if [ ! -d "$REPO_DIR/.git" ]; then
  echo "Error: $REPO_DIR does not look like a git repo (no .git folder)." >&2
  exit 1
fi
if [ ! -f "$SRC_FILE" ]; then
  echo "Error: source file $SRC_FILE not found." >&2
  exit 1
fi

cd "$REPO_DIR"
git pull --ff-only

mkdir -p outputs
DEST="outputs/$(basename "$SRC_FILE")"
cp "$SRC_FILE" "$DEST"

git add "$DEST"
git commit -m "$COMMIT_MSG"
git push

echo "Pushed $DEST to $(git remote get-url origin)"
