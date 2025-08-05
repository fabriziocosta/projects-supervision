import requests
import os
from collections import defaultdict
from datetime import datetime

REPO = "fabriziocosta/projects-supervision"
LABEL_PREFIX = "project:"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

MAX_ALLOWED = {
    "smartplan-ai": 3,
    "game-level": 3,
    "docuclass-ai": 3,
}
DEFAULT_MAX = 3

def fetch_issues():
    issues = []
    url = f"https://api.github.com/repos/{REPO}/issues?state=all&per_page=100"
    while url:
        r = requests.get(url, headers=HEADERS)
        r.raise_for_status()
        issues += r.json()
        url = r.links.get("next", {}).get("url")
    return issues

def count_by_project(issues):
    counts = defaultdict(int)
    for issue in issues:
        if 'pull_request' in issue:
            continue
        for label in issue['labels']:
            if label['name'].startswith(LABEL_PREFIX):
                project = label['name'][len(LABEL_PREFIX):]
                counts[project] += 1
    return counts

def update_status_md(counts):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    with open("status.md", "w") as f:
        f.write("# 📊 Project Interest Status\n\n")
        f.write(f"Last updated: **{timestamp}**\n\n")
        f.write("| Project | Interested Students | Max Allowed |\n")
        f.write("|---------|---------------------|-------------|\n")
        for project, count in sorted(counts.items()):
            max_allowed = MAX_ALLOWED.get(project, DEFAULT_MAX)
            f.write(f"| {project} | {count} | {max_allowed} |\n")

if __name__ == "__main__":
    issues = fetch_issues()
    counts = count_by_project(issues)
    update_status_md(counts)
