"""Render profile activity with the Python standard library and GitHub CLI.

No third-party image service or personal access token is needed in Actions.
Pass a saved GraphQL response as an argument for an offline render.
"""
import calendar
import datetime as dt
import html
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
QUERY = '''query($login:String!) {
  user(login:$login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount color } }
      }
    }
  }
}'''


def render(calendar_data, dark=False, mobile=False):
    weeks = calendar_data['weeks'][-26:] if mobile else calendar_data['weeks']
    if not weeks or not any(w['contributionDays'] for w in weeks):
        raise ValueError('GitHub returned an empty calendar; keeping existing artwork.')
    w, h = (560, 332) if mobile else (960, 306)
    bg, fg, muted, rule = ('#121b2b', '#f1f4ff', '#a9bbd5', '#293950') if dark else ('#eef2ff', '#172340', '#485979', '#c6d1ec')
    colors = ['#26344b', '#4a4cc0', '#7874df', '#f3917b', '#ffbba6'] if dark else ['#dce3f5', '#b6b8f0', '#7c7bd7', '#bf634d', '#883923']
    start = weeks[0]['contributionDays'][0]['date']
    end = weeks[-1]['contributionDays'][-1]['date']
    total = calendar_data['totalContributions']
    label = 'Last 26 weeks shown' if mobile else 'Last 12 months'
    subtitle = f'{total:,} contributions in the last year · 26 weeks shown' if mobile else f'{total:,} GitHub contributions · {label}'
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
           f'<title id="title">GitHub activity: {total} contributions in the last year</title>',
           f'<desc id="desc">{html.escape(label)}: {start} to {end}. Each square is one day; darker or warmer colors indicate more contributions.</desc>',
           f'<rect width="{w}" height="{h}" rx="12" fill="{bg}"/>',
           f'<g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Arial, sans-serif" fill="{fg}">',
           f'<text x="30" y="49" font-size="25" font-weight="700">A year of building.</text>',
           f'<text x="30" y="78" font-size="15" fill="{muted}">{subtitle}</text>']
    cell, step = (14, 19) if mobile else (12, 16)
    left, top = 30, 119
    # A week can straddle two months. One label per column; leave at least
    # three columns between labels so abbreviated month names never collide.
    labels = {0: dt.date.fromisoformat(start).month}
    for x, week in enumerate(weeks):
        for day in week['contributionDays']:
            date = dt.date.fromisoformat(day['date'])
            if date.day == 1:
                labels[x] = date.month
    spaced_labels = []
    for x, month in sorted(labels.items()):
        if spaced_labels and x-spaced_labels[-1][0] < 3:
            spaced_labels.pop()
        spaced_labels.append((x, month))
    for x, month in spaced_labels:
        out.append(f'<text x="{left+x*step}" y="108" font-size="11" fill="{muted}">{calendar.month_abbr[month]}</text>')
    counts = [d['contributionCount'] for week in weeks for d in week['contributionDays']]
    max_count = max(counts) or 1
    for x, week in enumerate(weeks):
        for day in week['contributionDays']:
            date = dt.date.fromisoformat(day['date'])
            y = (date.weekday() + 1) % 7
            n = day['contributionCount']
            level = 0 if n == 0 else min(4, 1 + int(3 * n / max_count))
            out.append(f'<rect x="{left+x*step}" y="{top+y*step}" width="{cell}" height="{cell}" rx="2" fill="{colors[level]}"><title>{date}: {n} contributions</title></rect>')
    y = 277 if mobile else 265
    out.append(f'<text x="30" y="{y}" font-size="12" fill="{muted}">{start} — {end}</text>')
    legend_x = w-185
    out.append(f'<text x="{legend_x-36}" y="{y}" font-size="11" fill="{muted}">Less</text>')
    for i, color in enumerate(colors):
        out.append(f'<rect x="{legend_x+i*16}" y="{y-10}" width="12" height="12" rx="2" fill="{color}"/>')
    out.append(f'<text x="{legend_x+86}" y="{y}" font-size="11" fill="{muted}">More</text>')
    stamp = dt.datetime.now(dt.timezone.utc).strftime('%d %b %Y')
    out.append(f'<text x="30" y="{h-17}" font-size="11" fill="{muted}">Source: GitHub · Updated {stamp} UTC</text></g></svg>')
    return '\n'.join(out)


def main():
    if len(sys.argv) > 1:
        result = json.loads(Path(sys.argv[1]).read_text())
    else:
        login = os.environ.get('PROFILE_LOGIN', 'lolbruhXD')
        response = subprocess.run(['gh', 'api', 'graphql', '-f', f'query={QUERY}', '-f', f'login={login}'], check=True, capture_output=True, text=True)
        result = json.loads(response.stdout)
    if result.get('errors'):
        raise RuntimeError('GitHub GraphQL returned errors; keeping existing artwork.')
    data = result['data']['user']['contributionsCollection']['contributionCalendar']
    outputs = {}
    for dark in (False, True):
        for mobile in (False, True):
            name = 'activity-' + ('mobile-' if mobile else '') + ('dark' if dark else 'light') + '.svg'
            outputs[ROOT / 'assets' / name] = render(data, dark, mobile)
    for path, content in outputs.items():
        temp = path.with_suffix('.tmp')
        temp.write_text(content)
        temp.replace(path)
    print('Rendered four activity variants from GitHub data.')


if __name__ == '__main__':
    main()
