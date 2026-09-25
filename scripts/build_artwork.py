"""Build original, self-contained vector artwork. No external assets or fonts."""
from pathlib import Path
import math

ROOT = Path(__file__).resolve().parents[1]


def orbital_mesh(cx, cy, radius):
    parts = ['<g fill="none" stroke="#a4baff" stroke-width="0.8" opacity="0.65">']
    def project(x, y, z):
        a = .55
        x, z = x*math.cos(a)+z*math.sin(a), -x*math.sin(a)+z*math.cos(a)
        b = -.48
        y, z = y*math.cos(b)-z*math.sin(b), y*math.sin(b)+z*math.cos(b)
        return cx+radius*x, cy+radius*y
    for j in range(17):
        theta = 2*math.pi*j/17
        coords=[]
        for k in range(101):
            phi=2*math.pi*k/100
            x=math.cos(theta)*math.cos(phi)
            y=math.sin(phi)
            z=math.sin(theta)*math.cos(phi)
            # A sculpted surface, not a data or model-performance plot.
            pinch=0.77+0.23*math.cos(phi*2)
            coords.append(project(x*pinch, y, z*pinch))
        parts.append('<path d="'+' '.join(('M' if i==0 else 'L')+f'{x:.2f},{y:.2f}' for i,(x,y) in enumerate(coords))+'"/>')
    for j in range(1,17):
        phi=-math.pi/2+math.pi*j/17
        coords=[]
        for k in range(101):
            theta=2*math.pi*k/100
            pinch=.77+.23*math.cos(phi*2)
            coords.append(project(math.cos(theta)*math.cos(phi)*pinch,math.sin(phi),math.sin(theta)*math.cos(phi)*pinch))
        parts.append('<path d="'+' '.join(('M' if i==0 else 'L')+f'{x:.2f},{y:.2f}' for i,(x,y) in enumerate(coords))+'"/>')
    parts.append('</g>')
    coords=[]
    for i in range(160):
        a=i/159*math.pi*3
        r=1.12
        coords.append(project(r*math.cos(a), .27*math.sin(a*2), r*math.sin(a)))
    path=' '.join(('M' if i==0 else 'L')+f'{x:.2f},{y:.2f}' for i,(x,y) in enumerate(coords))
    parts.append(f'<path d="{path}" fill="none" stroke="#ffac95" stroke-width="3"/>')
    parts.append(f'<path class="signal" d="{path}" pathLength="100" fill="none" stroke="#fff8ed" stroke-width="4" stroke-linecap="round" stroke-dasharray="4 96"/>')
    return '\n'.join(parts)


def hero(mobile=False):
    w,h=(560,490) if mobile else (960,408)
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
           '<title id="title">Abisanka Bhattacharjee</title>',
           '<desc id="desc">From first principles to production systems. AI engineering, machine learning, and real-time vision. Original orbital wire sculpture.</desc>',
           '<style>.signal{animation:travel 4.5s ease-in-out 1}@keyframes travel{from{stroke-dashoffset:100}to{stroke-dashoffset:0}}@media(prefers-reduced-motion:reduce){.signal{animation:none}}</style>',
           f'<rect width="{w}" height="{h}" rx="14" fill="#234cdf"/>',
           f'<path d="M0 {h-9}H{w}" stroke="#ffac95" stroke-width="18"/>',
           '<g font-family="Trebuchet MS, Segoe UI, Arial, sans-serif" fill="#fff8ed">']
    if mobile:
        parts += ['<text x="30" y="78" font-size="60" font-weight="700" letter-spacing="-2">Abisanka</text>',
                  '<text x="30" y="134" font-size="49" font-weight="700" letter-spacing="-1.7">Bhattacharjee.</text>',
                  '<text x="30" y="210" font-size="30" font-weight="700">From first principles</text>',
                  '<text x="30" y="248" font-size="30" font-weight="700">to production systems.</text>',
                  '<text x="30" y="341" font-size="20">AI engineering.</text>',
                  '<text x="30" y="370" font-size="20">Machine learning.</text>',
                  '<text x="30" y="399" font-size="20">Real-time vision.</text>',
                  '<text x="30" y="453" font-size="15" fill="#d8e3ff">@lolbruhXD</text>','</g>',orbital_mesh(399,374,94)]
    else:
        parts += ['<text x="44" y="100" font-size="79" font-weight="700" letter-spacing="-2.5">Abisanka</text>',
                  '<text x="44" y="170" font-size="65" font-weight="700" letter-spacing="-2">Bhattacharjee.</text>',
                  '<text x="46" y="260" font-size="34" font-weight="700">From first principles</text>',
                  '<text x="46" y="304" font-size="34" font-weight="700">to production systems.</text>',
                  '<text x="46" y="363" font-size="17" fill="#e3eaff">AI engineering · Machine learning · Real-time vision</text>',
                  '<text x="902" y="363" text-anchor="end" font-size="15" fill="#e3eaff">@lolbruhXD</text>',
                  '</g>',orbital_mesh(763,179,128)]
    return '\n'.join(parts)+ '</svg>'


def work():
    s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 116" role="img" aria-labelledby="title">',
       '<title id="title">Learning systems, product engineering, visual interaction, computer vision</title>',
       '<rect width="960" height="116" rx="10" fill="#eef2ff"/>',
       '<g stroke="#bdc9ed" fill="none"><path d="M240 22V94M480 22V94M720 22V94"/></g>',
       '<g stroke="#234cdf" stroke-width="2" fill="#eef2ff">']
    nodes=[(55,34),(55,82),(115,58),(180,34),(180,82)]
    for a,b in [(0,2),(1,2),(2,3),(2,4)]:
        x,y=nodes[a]; xx,yy=nodes[b]
        s.append(f'<path d="M{x},{y}L{xx},{yy}"/>')
    for x,y in nodes:
        s.append(f'<circle cx="{x}" cy="{y}" r="8"/>')
    s+=['<rect x="312" y="26" width="70" height="66" rx="4"/><rect x="331" y="18" width="70" height="66" rx="4"/><path d="M341 32H391M341 43H380M341 54H374M341 65H384"/>',
        '<ellipse cx="600" cy="58" rx="52" ry="20" transform="rotate(-30 600 58)"/><ellipse cx="600" cy="58" rx="52" ry="20" transform="rotate(30 600 58)"/><ellipse cx="600" cy="58" rx="52" ry="20" transform="rotate(90 600 58)"/>',
        '<circle cx="840" cy="30" r="10"/><path d="M840 40V65M812 51H867M840 65L819 90M840 65L863 90M791 21V13H805M874 13H888V26M791 88V102H805M874 102H888V88"/>',
        '</g><g fill="#bd5c43"><circle cx="115" cy="58" r="5"/><rect x="361" y="59" width="39" height="17" rx="3"/><circle cx="600" cy="58" r="9"/><circle cx="840" cy="65" r="5"/></g></svg>']
    return '\n'.join(s)


def main():
    assets=ROOT/'assets'
    assets.mkdir(exist_ok=True)
    (assets/'hero.svg').write_text(hero())
    (assets/'hero-mobile.svg').write_text(hero(True))
    (assets/'work.svg').write_text(work())
    (assets/'footer.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 100" role="img" aria-labelledby="title"><title id="title">Understand deeply. Build deliberately.</title><rect width="960" height="100" rx="10" fill="#234cdf"/><path d="M36 50H118M96 30L118 50L96 70" stroke="#ffac95" stroke-width="3" fill="none"/><text x="148" y="60" fill="#fff8ed" font-size="28" font-weight="700" font-family="Trebuchet MS, Segoe UI, Arial, sans-serif">Understand deeply. Build deliberately.</text></svg>''')
    print('Built four original SVG assets.')


if __name__=='__main__':
    main()
