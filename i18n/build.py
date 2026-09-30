#!/usr/bin/env python3
"""Generate the Greek, Italian and Spanish pages from the English ones.

Run from the repository root:  python3 i18n/build.py
Translations live in i18n/<lang>.json as {"english string": "translation"}.
Strings with no entry stay in English (publication titles, names, tool names)."""
import json, os, re, time
STAMP = time.strftime('%Y%m%d%H%M')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = ['index.html', 'research.html', 'projects.html', 'services.html', 'teaching.html', 'cv.html']
LANGS = {'el': 'Ελληνικά', 'it': 'Italiano', 'es': 'Español'}
NAMES = {'en': 'English', 'el': 'Ελληνικά', 'it': 'Italiano', 'es': 'Español'}

FLAGS = {
    'en': '<svg viewBox="0 0 60 40" aria-hidden="true"><rect width="60" height="40" fill="#1f3a66"/><path d="M0 0l60 40M60 0L0 40" stroke="#fff" stroke-width="8"/><path d="M0 0l60 40M60 0L0 40" stroke="#c8312b" stroke-width="3"/><path d="M30 0v40M0 20h60" stroke="#fff" stroke-width="12"/><path d="M30 0v40M0 20h60" stroke="#c8312b" stroke-width="6"/></svg>',
    'el': '<svg viewBox="0 0 60 40" aria-hidden="true"><rect width="60" height="40" fill="#1d5fb5"/><path d="M0 6.7h60M0 15.6h60M0 24.4h60M0 33.3h60" stroke="#fff" stroke-width="4.4"/><rect width="22" height="22" fill="#1d5fb5"/><path d="M11 0v22M0 11h22" stroke="#fff" stroke-width="4.4"/></svg>',
    'it': '<svg viewBox="0 0 60 40" aria-hidden="true"><rect width="20" height="40" fill="#1a8a4a"/><rect x="20" width="20" height="40" fill="#f6f1e7"/><rect x="40" width="20" height="40" fill="#c8312b"/></svg>',
    'es': '<svg viewBox="0 0 60 40" aria-hidden="true"><rect width="60" height="40" fill="#c8312b"/><rect y="10" width="60" height="20" fill="#f2c318"/></svg>',
}

def switcher(current, depth):
    """depth 0 for root pages, 1 for pages inside a language folder."""
    up = '../' if depth else ''
    out = ['    <div class="lang" aria-label="Language">']
    for code in ['en', 'el', 'it', 'es']:
        folder = '' if code == 'en' else code + '/'
        cur = ' aria-current="true"' if code == current else ''
        out.append('      <a href="%s%s{page}"%s hreflang="%s" title="%s">%s<span>%s</span></a>' % (up, folder, cur, code, NAMES[code], FLAGS[code], code.upper()))
    out.append('      <button class="theme" id="theme-toggle" type="button" aria-label="Switch theme"><svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></svg><svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/></svg></button>')
    out.append('    </div>')
    return '\n'.join(out)

def hreflang_links(page):
    base = 'https://mariossal.github.io/'
    links = ['<link rel="alternate" hreflang="en" href="%s%s">' % (base, page)]
    for code in LANGS:
        links.append('<link rel="alternate" hreflang="%s" href="%s%s/%s">' % (code, base, code, page))
    links.append('<link rel="alternate" hreflang="x-default" href="%s%s">' % (base, page))
    return '\n'.join(links)

def translate(html, table):
    # text nodes, longest keys first so partial phrases never pre-empt full sentences
    for en in sorted(table, key=len, reverse=True):
        tr = table[en].replace('\\', '\\\\')
        html = re.sub(r'>(\s*)' + re.escape(en) + r'(\s*)<', lambda m: '>' + m.group(1) + tr + m.group(2) + '<', html)
        html = html.replace('="' + en + '"', '="' + table[en] + '"')
        html = html.replace('<title>' + en, '<title>' + table[en])
    return html

def localize_paths(html):
    # assets and links move one level up; page links stay relative within the folder
    html = re.sub(r'href="style\.css(?:\?v=\d+)?"', 'href="style.css"', html)
    html = re.sub(r'(href|src)="(style\.css|favicon\.svg|apple-touch-icon\.png|logo\.svg|portrait(?:-2)?\.jpg|logos/[^"]+|cv-block\.js|theme\.js)"', r'\1="../\2"', html)
    html = re.sub(r'href="\.\./style\.css"', 'href="../style.css?v=%s"' % STAMP, html)
    return html

def main():
    for page in PAGES:
        src = open(os.path.join(ROOT, page), encoding='utf-8').read()
        # English page gets the switcher and hreflang links
        en = src
        if '<div class="lang"' not in en:
            en = en.replace('    </nav>\n', '    </nav>\n' + switcher('en', 0).replace('{page}', page) + '\n', 1)
        else:
            en = re.sub(r'    <div class="lang".*?    </div>', switcher('en', 0).replace('{page}', page), en, count=1, flags=re.S)
        en = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+">\n?', '', en)
        en = re.sub(r'href="style\.css(?:\?v=\d+)?"', 'href="style.css?v=%s"' % STAMP, en)
        en = en.replace('<link rel="icon"', hreflang_links(page) + '\n<link rel="icon"', 1) if '<link rel="icon"' in en else en
        open(os.path.join(ROOT, page), 'w', encoding='utf-8').write(en)
        for code in LANGS:
            table = json.load(open(os.path.join(ROOT, 'i18n', code + '.json'), encoding='utf-8'))
            out = translate(en, table)
            out = localize_paths(out)
            out = re.sub(r'    <div class="lang".*?    </div>', switcher(code, 1).replace('{page}', page), out, count=1, flags=re.S)
            out = out.replace('<html lang="en">', '<html lang="%s">' % code)
            out = out.replace('href="index.html#contact"', 'href="index.html#contact"')
            os.makedirs(os.path.join(ROOT, code), exist_ok=True)
            open(os.path.join(ROOT, code, page), 'w', encoding='utf-8').write(out)
    print('built', ', '.join(LANGS))

if __name__ == '__main__':
    main()
