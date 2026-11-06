#!/usr/bin/env python3
"""Generate a meaningful, animated engineering constellation from real public GitHub metadata.

Only the repository's public language and last-push date are shown. The connectors
represent shared engineering disciplines, not repository or runtime dependencies.
No API secrets or private data are added to the artwork.
"""

from datetime import datetime, timezone
from html import escape
from pathlib import Path
import json
import os
import random
from urllib.request import Request, urlopen

OWNER = "HuLaxx"
PROJECTS = [
    {
        "name": "Sentinance",
        "number": "01",
        "domain": "AGENTIC MARKET INTELLIGENCE",
        "specialty": "LANGGRAPH  /  FORECASTING",
        "x": 54, "y": 129, "color": "#72e9f2",
    },
    {
        "name": "GraphGuard",
        "number": "02",
        "domain": "GRAPH + EXPLAINABLE ML",
        "specialty": "NEO4J  /  XGBOOST",
        "x": 669, "y": 129, "color": "#bd9cfb",
    },
    {
        "name": "FleetFlow",
        "number": "03",
        "domain": "REAL-TIME OPTIMIZATION",
        "specialty": "OR-TOOLS  /  STREAMING",
        "x": 54, "y": 362, "color": "#74e6be",
    },
    {
        "name": "Shiftify",
        "number": "04",
        "domain": "PRIVACY-FIRST WEB PRODUCT",
        "specialty": "NEXT.JS  /  TYPESCRIPT",
        "x": 669, "y": 362, "color": "#f7bd8b",
    },
]


def load_public_repo(name):
    url = "https://api.github.com/repos/{}/{}".format(OWNER, name)
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "HuLaxx-profile-constellation",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    with urlopen(Request(url, headers=headers), timeout=20) as response:
        value = json.load(response)
    if value.get("full_name", "").lower() != (OWNER + "/" + name).lower():
        raise ValueError("Unexpected repository API response for " + name)
    pushed_at = value.get("pushed_at")
    if pushed_at:
        parsed = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
        last_push = parsed.strftime("%d %b %Y").upper()
    else:
        last_push = "NOT REPORTED"
    return {
        "language": value.get("language") or "UNSPECIFIED",
        "last_push": last_push,
    }


def node_markup(project, metadata):
    x, y = project["x"], project["y"]
    color = project["color"]
    name = escape(project["name"])
    index = escape(project["number"])
    domain = escape(project["domain"])
    specialty = escape(project["specialty"])
    language = escape(metadata["language"].upper())
    pushed = escape(metadata["last_push"])
    pulse_delay = float(project["number"]) * 0.5
    return f"""
    <g transform="translate({x},{y})">
      <rect width="397" height="151" rx="17" fill="#111e35" stroke="{color}" stroke-opacity=".48" stroke-width="1.5"/>
      <rect width="5" height="151" rx="2.5" fill="{color}" opacity=".82"/>
      <rect x="19" y="17" width="28" height="25" rx="6" fill="{color}" fill-opacity=".16"/>
      <text x="33" y="34" fill="{color}" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">{index}</text>
      <text x="59" y="37" fill="#f4f7ff" font-family="Arial,Helvetica,sans-serif" font-size="23" font-weight="bold" letter-spacing=".3">{name}</text>
      <circle cx="367" cy="29" r="5" fill="{color}">
        <animate attributeName="opacity" values=".3;1;.3" dur="3.5s" begin="{pulse_delay}s" repeatCount="indefinite"/>
      </circle>
      <text x="19" y="65" fill="#acbdd7" font-family="monospace" font-size="12">{domain}</text>
      <text x="19" y="87" fill="{color}" font-family="monospace" font-size="11" letter-spacing=".4">{specialty}</text>
      <path d="M19 103H378" fill="none" stroke="#718baa" stroke-opacity=".3"/>
      <text x="19" y="126" fill="#8da6c5" font-family="monospace" font-size="10">PRIMARY LANGUAGE</text>
      <text x="19" y="143" fill="#d7e9ff" font-family="monospace" font-size="12">{language}</text>
      <text x="201" y="126" fill="#8da6c5" font-family="monospace" font-size="10">LAST CODE PUSH</text>
      <text x="201" y="143" fill="#d7e9ff" font-family="monospace" font-size="12">{pushed}</text>
    </g>
    """


def render(projects, signals):
    randomizer = random.Random(91021)
    stars = []
    for index in range(115):
        x = round(randomizer.uniform(16, 1104), 1)
        y = round(randomizer.uniform(75, 520), 1)
        radius = round(randomizer.uniform(0.5, 1.5), 1)
        alpha = round(randomizer.uniform(0.12, 0.55), 2)
        stars.append(
            f'<circle cx="{x}" cy="{y}" r="{radius}" fill="#b4d6ff" opacity="{alpha}"/>'
        )
    node_svg = "\n".join(node_markup(p, signals[p["name"]]) for p in projects)
    synced = datetime.now(timezone.utc).strftime("%d %b %Y %H:%M UTC").upper()
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1120 560" width="1120" height="560" role="img" aria-labelledby="title subtitle">
  <title id="title">HuLaX Living Project Constellation</title>
  <desc id="subtitle">Four real GitHub projects connected by shared engineering disciplines. Project language and last pushed dates refresh daily from GitHub.</desc>
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#071021"/><stop offset=".55" stop-color="#10182d"/><stop offset="1" stop-color="#0b1b2e"/>
    </linearGradient>
    <linearGradient id="connections" x1="0" x2="1">
      <stop stop-color="#7eecde"/><stop offset=".55" stop-color="#b59afe"/><stop offset="1" stop-color="#ffca94"/>
    </linearGradient>
    <radialGradient id="aura">
      <stop stop-color="#737dff" stop-opacity=".25"/><stop offset="1" stop-color="#737dff" stop-opacity="0"/>
    </radialGradient>
    <pattern id="matrix" width="35" height="35" patternUnits="userSpaceOnUse">
      <path d="M35 0H0V35" fill="none" stroke="#7bb6d9" stroke-opacity=".08" stroke-width=".7"/>
    </pattern>
    <clipPath id="bounds"><rect width="1120" height="560" rx="22"/></clipPath>
  </defs>
  <g clip-path="url(#bounds)">
    <rect width="1120" height="560" fill="url(#sky)"/>
    <rect width="1120" height="560" fill="url(#matrix)"/>
    <circle cx="560" cy="302" r="250" fill="url(#aura)">
      <animate attributeName="r" values="228;272;228" dur="10s" repeatCount="indefinite"/>
    </circle>
    <g>{"".join(stars)}</g>
    <path d="M0 68H1120" stroke="#536988" stroke-opacity=".38"/>
    <text x="43" y="28" fill="#a7c4e4" font-family="monospace" font-size="12" letter-spacing="2">HULAX LABS  /  LIVING PROJECT CONSTELLATION</text>
    <text x="43" y="49" fill="#81dfd4" font-family="monospace" font-size="11" letter-spacing=".9">REPO SIGNALS ARE REAL · LINKS OPEN THE FULL CASE STUDIES</text>
    <text x="1074" y="43" fill="#82e7d7" text-anchor="end" font-family="monospace" font-size="12">04 PROJECTS</text>
    <g fill="none" stroke="url(#connections)" stroke-opacity=".65" stroke-width="2">
      <path id="p1" d="M478 264Q460 215 451 193" stroke-dasharray="6 11">
        <animate attributeName="stroke-dashoffset" values="0;-85" dur="9s" repeatCount="indefinite"/>
      </path>
      <path id="p2" d="M640 264Q652 212 669 193" stroke-dasharray="6 11">
        <animate attributeName="stroke-dashoffset" values="0;85" dur="9s" repeatCount="indefinite"/>
      </path>
      <path id="p3" d="M478 332Q465 392 451 427" stroke-dasharray="6 11">
        <animate attributeName="stroke-dashoffset" values="0;85" dur="9s" repeatCount="indefinite"/>
      </path>
      <path id="p4" d="M640 332Q657 392 669 427" stroke-dasharray="6 11">
        <animate attributeName="stroke-dashoffset" values="0;-85" dur="9s" repeatCount="indefinite"/>
      </path>
    </g>
    <circle cx="560" cy="300" r="83" fill="#0b2339" stroke="#76dfdc" stroke-opacity=".7"/>
    <circle cx="560" cy="300" r="97" fill="none" stroke="#9ac8f9" stroke-opacity=".36" stroke-width="1.3" stroke-dasharray="4 10">
      <animateTransform attributeName="transform" type="rotate" from="0 560 300" to="360 560 300" dur="50s" repeatCount="indefinite"/>
    </circle>
    <g font-family="Arial,Helvetica,sans-serif" text-anchor="middle">
      <text x="560" y="281" fill="#a3eadd" font-family="monospace" font-size="11" letter-spacing="1">SHARED CORE</text>
      <text x="560" y="308" fill="#f3fbff" font-size="27" font-weight="bold">HULAX</text>
      <text x="560" y="330" fill="#abc0dc" font-size="12">ENGINEERING</text>
    </g>
    {node_svg}
    <path d="M35 524H1083" stroke="#6883a2" stroke-opacity=".48"/>
    <text x="43" y="543" fill="#8ed5cf" font-family="monospace" font-size="11" letter-spacing=".7">SHARED SKILLS, NOT SOFTWARE DEPENDENCIES</text>
    <text x="1075" y="543" fill="#a5bbd7" text-anchor="end" font-family="monospace" font-size="10">SYNCED {escape(synced)}</text>
  </g>
</svg>
"""


def main():
    signals = {item["name"]: load_public_repo(item["name"]) for item in PROJECTS}
    art = render(PROJECTS, signals)
    output = Path("dist/project-constellation.svg")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(art, encoding="utf-8")
    print(f"Created {output} from GitHub public repository signals")


if __name__ == "__main__":
    main()
