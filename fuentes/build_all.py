import base64, re, json, mimetypes
S = '/tmp/claude-0/-home-claude/602786c5-6070-5e41-b7ce-0d78adb3dc11/scratchpad'
def uri(path):
    mime = mimetypes.guess_type(path)[0] or 'image/png'
    return f"data:{mime};base64," + base64.b64encode(open(path, 'rb').read()).decode()
logo, fav = uri(S + '/logo-zavi.png'), uri(S + '/favicon.png')
datos = json.load(open(S + '/datos.json', encoding='utf-8'))
datos['config']['qr'] = uri(S + '/qr-yape.jpg')
bloque = json.dumps(datos, ensure_ascii=False).replace('<', '\\u003c')
t = open('/home/claude/zavi-src.html', encoding='utf-8').read()
assert t.count('{{DATOS}}') == 1
t = t.replace('{{LOGO}}', logo).replace('{{FAVICON}}', fav).replace('{{DATOS}}', bloque)
open('/home/claude/tienda-zavi.html', 'w', encoding='utf-8').write(t)
open(S + '/app.js', 'w', encoding='utf-8').write(re.search(r'<script>(.*?)</script>', t, re.S).group(1))
a = open('/home/claude/admin-src.html', encoding='utf-8').read().replace('{{LOGO}}', logo)
open('/home/claude/admin-zavi.html', 'w', encoding='utf-8').write(a)
open(S + '/admin.js', 'w', encoding='utf-8').write(re.search(r'<script>(.*?)</script>', a, re.S).group(1))
print('tienda KB:', round(len(t)/1024, 1), '| admin KB:', round(len(a)/1024, 1))
