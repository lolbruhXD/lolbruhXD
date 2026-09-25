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
    weeks = calendar_data['weeks'][-18:] if mobile else calendar_data['weeks']
    if not weeks or not any(w['contributionDays'] for w in weeks):
        raise ValueError('GitHub returned an empty calendar; keeping existing artwork.')
    w, h = (390, 355) if mobile else (960, 320)
    bg, fg, muted = ('#101b36', '#f2f5ff', '#b2c8ef') if dark else ('#e8edff', '#172b78', '#3c5093')
    colors = (['#324668', '#6c91ef', '#acc3ff', '#ffab90', '#f97865'] if dark
              else ['#b3c3eb', '#5477df', '#2446bf', '#d9684e', '#a93d2b'])
    start = weeks[0]['contributionDays'][0]['date']
    end = weeks[-1]['contributionDays'][-1]['date']
    total = calendar_data['totalContributions']
    label = 'Latest 18 weeks shown' if mobile else 'Last 12 months shown'
    subtitle = f'{total:,} contributions in the last year · 18 weeks shown' if mobile else f'{total:,} contributions in the last year'
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
           f'<title id="title">GitHub activity: {total} contributions in the last year</title>',
           f'<desc id="desc">{html.escape(label)}: {start} to {end}. Each square is one day; darker or warmer colors indicate more contributions.</desc>',
           f'<rect width="{w}" height="{h}" rx="12" fill="{bg}"/>',
           f'<g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Arial, sans-serif" fill="{fg}">',
           f'<text x="{24 if mobile else 30}" y="{43 if mobile else 53}" font-size="{24 if mobile else 28}" font-weight="700">A year of building.</text>',
           f'<text x="{24 if mobile else 30}" y="{74 if mobile else 85}" font-size="{13 if mobile else 17}" fill="{muted}">{subtitle}</text>']
    cell, step = (16, 19) if mobile else (15, 17)
    left, top = (24, 111) if mobile else (30, 133)
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
        if spaced_labels and x-spaced_labels[-1][0] < (2 if mobile else 3):
            spaced_labels.pop()
        spaced_labels.append((x, month))
    for x, month in spaced_labels:
        out.append(f'<text x="{left+x*step}" y="{101 if mobile else 120}" font-size="{11 if mobile else 13}" fill="{muted}">{calendar.month_abbr[month]}</text>')
    counts = [d['contributionCount'] for week in weeks for d in week['contributionDays']]
    max_count = max(counts) or 1
    for x, week in enumerate(weeks):
        for day in week['contributionDays']:
            date = dt.date.fromisoformat(day['date'])
            y = (date.weekday() + 1) % 7
            n = day['contributionCount']
            level = 0 if n == 0 else 1 if n == 1 else 2 if n == 2 else 3 if n <= 4 else 4
            out.append(f'<rect x="{left+x*step}" y="{top+y*step}" width="{cell}" height="{cell}" rx="3" fill="{colors[level]}"><title>{date}: {n} contributions</title></rect>')
    y = 282 if mobile else 283
    out.append(f'<text x="{left}" y="{y}" font-size="{12 if mobile else 13}" fill="{muted}">{start} — {end}</text>')
    legend_y = 311 if mobile else y
    legend_x = w-(175 if mobile else 185)
    out.append(f'<text x="{legend_x-40}" y="{legend_y}" font-size="12" fill="{muted}">Less</text>')
    for i, color in enumerate(colors):
        out.append(f'<rect x="{legend_x+i*17}" y="{legend_y-11}" width="13" height="13" rx="2" fill="{color}"/>')
    out.append(f'<text x="{legend_x+91}" y="{legend_y}" font-size="12" fill="{muted}">More</text>')
    stamp = dt.datetime.now(dt.timezone.utc).strftime('%d %b %Y')
    out.append(f'<text x="{left}" y="{h-17}" font-size="11" fill="{muted}">Source: GitHub · Updated {stamp} UTC</text></g></svg>')
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
