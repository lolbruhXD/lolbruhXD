"""Build original light/dark SVG artwork for a GitHub-native profile."""
from pathlib import Path
import math

ROOT = Path(__file__).resolve().parents[1]
PALETTES = {
    'light': dict(field='#e8edff', ink='#172b78', muted='#3c5093', mesh='#4b68b7', signal='#af4936', panel='#f9fbff', bright='#fff7e9'),
    'dark': dict(field='#101b36', ink='#f2f5ff', muted='#b2c8ef', mesh='#80a9ef', signal='#ffab90', panel='#18284b', bright='#f2f5ff'),
}
PROJECTS = [
    ('autograd', 'Autograd from scratch', 'AUTOGRAD / LEARNING SYSTEMS', 'Automatic differentiation learning implementation'),
    ('orbit', 'OpenOrbit', 'OPENORBIT / PRODUCT', 'Developer project sharing platform'),
    ('holo', 'Holo-Vex', 'HOLO-VEX / INTERACTION', 'Hand tracked holographic visual effects'),
    ('vision', 'FacPosCheck', 'FACPOSCHECK / VISION', 'Experimental real-time vision pipeline'),
]


def start(w, h, title, desc, fill):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
            f'<title id="title">{title}</title><desc id="desc">{desc}</desc>',
            f'<rect width="{w}" height="{h}" rx="14" fill="{fill}"/>']


def orbital_mesh(cx, cy, radius, p):
    def project(x, y, z):
        a, b = .55, -.48
        x, z = x * math.cos(a) + z * math.sin(a), -x * math.sin(a) + z * math.cos(a)
        y, z = y * math.cos(b) - z * math.sin(b), y * math.sin(b) + z * math.cos(b)
        return cx + radius * x, cy + radius * y
    def path(points):
        return ' '.join(('M' if i == 0 else 'L') + f'{x:.1f},{y:.1f}' for i, (x, y) in enumerate(points))
    result = [f'<g fill="none" stroke="{p["mesh"]}" stroke-width="1" opacity="0.66">']
    for j in range(16):
        theta = 2 * math.pi * j / 16
        pts = []
        for k in range(81):
            phi = 2 * math.pi * k / 80
            pinch = .77 + .23 * math.cos(phi * 2)
            pts.append(project(math.cos(theta)*math.cos(phi)*pinch, math.sin(phi), math.sin(theta)*math.cos(phi)*pinch))
        result.append(f'<path d="{path(pts)}"/>')
    for j in range(1, 16):
        phi = -math.pi/2 + math.pi*j/16
        pts = []
        for k in range(81):
            theta = 2*math.pi*k/80
            pinch = .77+.23*math.cos(phi*2)
            pts.append(project(math.cos(theta)*math.cos(phi)*pinch, math.sin(phi), math.sin(theta)*math.cos(phi)*pinch))
        result.append(f'<path d="{path(pts)}"/>')
    result.append('</g>')
    pts = [project(1.12*math.cos(a), .27*math.sin(a*2), 1.12*math.sin(a)) for a in (i/124*math.pi*3 for i in range(125))]
    orbit = path(pts)
    result += [f'<path d="{orbit}" fill="none" stroke="{p["signal"]}" stroke-width="3.2"/>',
               f'<path class="signal" d="{orbit}" pathLength="100" fill="none" stroke="{p["bright"]}" stroke-width="4" stroke-linecap="round" stroke-dasharray="4 96"/>']
    return '\n'.join(result)


def hero(theme, mobile=False):
    p = PALETTES[theme]
    w, h = (560, 490) if mobile else (960, 408)
    s = start(w, h, 'Abisanka Bhattacharjee', 'From first principles to production systems. Original orbital wire sculpture.', p['field'])
    s += ['<style>.signal{animation:travel 4.5s ease-in-out 1}@keyframes travel{from{stroke-dashoffset:100}to{stroke-dashoffset:0}}@media(prefers-reduced-motion:reduce){.signal{animation:none}}</style>',
          f'<path d="M0 {h-9}H{w}" stroke="{p["signal"]}" stroke-width="18"/>',
          f'<g font-family="Trebuchet MS, Segoe UI, Arial, sans-serif" fill="{p["ink"]}">']
    if mobile:
        s += ['<text x="30" y="78" font-size="60" font-weight="700" letter-spacing="-2">Abisanka</text>',
              '<text x="30" y="134" font-size="49" font-weight="700" letter-spacing="-1.7">Bhattacharjee.</text>',
              '<text x="30" y="210" font-size="30" font-weight="700">From first principles</text>',
              '<text x="30" y="248" font-size="30" font-weight="700">to production systems.</text>',
              '<text x="30" y="341" font-size="20">AI engineering.</text>',
              '<text x="30" y="370" font-size="20">Machine learning.</text>',
              '<text x="30" y="399" font-size="20">Real-time vision.</text>',
              f'<text x="30" y="453" font-size="16" font-weight="700" fill="{p["muted"]}">@lolbruhXD</text>',
              '</g>', orbital_mesh(399, 374, 94, p)]
    else:
        s += ['<text x="44" y="100" font-size="79" font-weight="700" letter-spacing="-2.5">Abisanka</text>',
              '<text x="44" y="170" font-size="65" font-weight="700" letter-spacing="-2">Bhattacharjee.</text>',
              '<text x="46" y="260" font-size="34" font-weight="700">From first principles</text>',
              '<text x="46" y="304" font-size="34" font-weight="700">to production systems.</text>',
              f'<text x="46" y="363" font-size="17" fill="{p["muted"]}">AI engineering · Machine learning · Real-time vision</text>',
              f'<text x="902" y="363" text-anchor="end" font-size="16" font-weight="700" fill="{p["muted"]}">@lolbruhXD</text>',
              '</g>', orbital_mesh(763, 179, 128, p)]
    return '\n'.join(s) + '</svg>'


def project_icon(key, title, label, desc, theme):
    p = PALETTES[theme]
    s = start(320, 174, title, desc + '. Click through for project details.', p['panel'])
    icon_transform = ' transform="translate(34 14) scale(.8)"' if key == 'holo' else ''
    s += [f'<path d="M0 172H320" stroke="{p["signal"]}" stroke-width="4"/>',
          f'<g{icon_transform} fill="none" stroke="{p["ink"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">']
    if key == 'autograd':
        s += ['<path d="M48 48L112 87M48 125L112 87M112 87L184 47M112 87L184 126M184 47L258 87M184 126L258 87"/>',
              '<circle cx="48" cy="48" r="12"/><circle cx="48" cy="125" r="12"/><circle cx="112" cy="87" r="14"/>',
              '<circle cx="184" cy="47" r="12"/><circle cx="184" cy="126" r="12"/><circle cx="258" cy="87" r="17"/>',
              f'<path d="M258 70V104M241 87H275" stroke="{p["signal"]}"/>']
    elif key == 'orbit':
        s += ['<ellipse cx="160" cy="86" rx="100" ry="43" transform="rotate(-18 160 86)"/>',
              '<ellipse cx="160" cy="86" rx="100" ry="43" transform="rotate(18 160 86)"/>',
              '<rect x="120" y="49" width="80" height="73" rx="7"/>',
              '<path d="M134 65H186M134 78H175M134 91H181M134 104H159"/>',
              f'<circle cx="244" cy="50" r="11" fill="{p["signal"]}" stroke="none"/>']
    elif key == 'holo':
        s += ['<path d="M103 142V99L92 89Q85 80 93 73Q101 67 108 76L124 91V43Q124 31 134 31Q144 31 144 43V76V31Q144 21 154 21Q164 21 164 31V74V37Q164 27 174 27Q184 27 184 37V78V51Q184 41 194 41Q204 41 204 51V104Q201 131 182 143"/>',
              '<path d="M103 142H182"/><circle cx="153" cy="94" r="21"/>',
              '<path d="M50 87H68M241 87H259M160 9V20M160 151V163"/>',
              f'<circle cx="153" cy="94" r="8" fill="{p["signal"]}" stroke="none"/>']
    else:
        s += ['<path d="M86 37H73V51M234 37H247V51M73 123V137H86M247 123V137H234"/>',
              '<ellipse cx="160" cy="75" rx="32" ry="38"/>',
              '<path d="M105 149Q118 111 140 112M215 149Q202 111 180 112M116 160H204"/>',
              f'<circle cx="145" cy="71" r="3" fill="{p["signal"]}" stroke="none"/>',
              f'<circle cx="175" cy="71" r="3" fill="{p["signal"]}" stroke="none"/>',
              f'<path d="M145 94Q160 104 175 94" stroke="{p["signal"]}"/>']
    s += ['</g>', f'<text x="20" y="29" font-size="14" font-family="Trebuchet MS, Segoe UI, Arial, sans-serif" font-weight="700" fill="{p["muted"]}">{label}</text>', '</svg>']
    return '\n'.join(s)


def footer(theme):
    p = PALETTES[theme]
    s = start(960, 100, 'Understand deeply. Build deliberately.', 'Contact Abisanka Bhattacharjee to collaborate.', p['field'])
    s += [f'<path d="M36 50H118M96 30L118 50L96 70" stroke="{p["signal"]}" stroke-width="3" fill="none"/>',
          f'<text x="148" y="60" fill="{p["ink"]}" font-size="28" font-weight="700" font-family="Trebuchet MS, Segoe UI, Arial, sans-serif">Understand deeply. Build deliberately.</text></svg>']
    return '\n'.join(s)


def main():
    assets = ROOT / 'assets'
    assets.mkdir(exist_ok=True)
    for theme in PALETTES:
        (assets / f'hero-{theme}.svg').write_text(hero(theme))
        (assets / f'hero-mobile-{theme}.svg').write_text(hero(theme, mobile=True))
        (assets / f'footer-{theme}.svg').write_text(footer(theme))
        for key, title, label, desc in PROJECTS:
            (assets / f'project-{key}-{theme}.svg').write_text(project_icon(key, title, label, desc, theme))
    for old in ['hero.svg', 'hero-mobile.svg', 'work.svg', 'footer.svg']:
        (assets / old).unlink(missing_ok=True)
    print('Built 14 theme-aware original SVG illustrations.')


if __name__ == '__main__':
    main()
