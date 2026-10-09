# Genera las guías SEO de altamonotributo.com en /guias/ y actualiza sitemap.xml.
# Uso: python _herramientas/generar_guias.py   (desde la raíz del repo)
# El contenido vive en _herramientas/guias_contenido.py. GitHub Pages (Jekyll) no
# publica carpetas que empiezan con "_", así que esto no queda visible en el sitio.
import html, io, json, os, sys

sys.path.insert(0, os.path.dirname(__file__))
from guias_contenido import GUIAS, ACTUALIZADO, ACTUALIZADO_ISO  # noqa: E402

SITIO = 'https://altamonotributo.com'
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WA = 'https://wa.me/5491124039191?text='
TS = 'https://tributosimple.com/?utm_source=altamonotributo&utm_medium=guias&utm_campaign={slug}'

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--negro:#10233F;--azul:#00B894;--azul-dark:#0055BA;--azul-light:#E7F7F3;--sub:#3F5269;--gris:#8496A9;--borde:#DCE5EE;--fondo:#F1F6FB;--nav-h:60px}
body{font-family:'Inter',system-ui,sans-serif;color:var(--negro);background:#fff;-webkit-font-smoothing:antialiased;font-size:16px;line-height:1.7}
nav{position:fixed;top:0;left:0;right:0;z-index:400;height:var(--nav-h);display:flex;align-items:center;justify-content:space-between;padding:0 40px;background:rgba(18,21,29,.92);backdrop-filter:blur(20px)}
.logo{display:flex;align-items:center;gap:8px;font-size:14px;font-weight:700;color:#fff;text-decoration:none}
.logo img{display:block;height:20px;width:auto}
.logo span{background:linear-gradient(120deg,#00B894,#2E9BF0);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.nav-links{display:flex;align-items:center;gap:22px}
.nav-links a{font-size:13px;font-weight:500;color:rgba(255,255,255,.6);text-decoration:none}
.nav-links a:hover{color:#fff}
.btn-nav{background:linear-gradient(135deg,#00B894,#0055BA);color:#fff!important;font-weight:600;padding:7px 16px;border-radius:8px}
header.hero{background:var(--negro);color:#fff;padding:calc(var(--nav-h) + 48px) 24px 48px}
.wrap{max-width:780px;margin:0 auto}
.migas{font-size:13px;color:rgba(255,255,255,.55);margin-bottom:14px}
.migas a{color:rgba(255,255,255,.75);text-decoration:none}
h1{font-size:clamp(28px,4.4vw,40px);line-height:1.15;letter-spacing:-.02em;font-weight:800}
.bajada{margin-top:14px;font-size:17px;color:rgba(255,255,255,.78)}
.meta{margin-top:16px;font-size:13px;color:rgba(255,255,255,.5)}
main{padding:40px 24px 64px}
.respuesta{background:var(--azul-light);border-left:4px solid var(--azul);padding:18px 20px;border-radius:10px;margin-bottom:32px;font-size:16.5px}
main h2{font-size:24px;line-height:1.25;letter-spacing:-.015em;margin:40px 0 12px}
main h3{font-size:18px;margin:24px 0 8px}
main p{margin:0 0 14px;color:#24364F}
main ul,main ol{margin:0 0 16px 22px;color:#24364F}
main li{margin:6px 0}
main a{color:var(--azul-dark)}
.tabla{overflow-x:auto;margin:16px 0 8px;border:1px solid var(--borde);border-radius:12px}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{padding:9px 12px;border-bottom:1px solid var(--borde);text-align:left;white-space:nowrap}
th{background:var(--fondo);font-weight:700}
tr:last-child td{border-bottom:0}
.nota{font-size:13px;color:var(--gris);margin-bottom:20px}
.cta{margin:40px 0;padding:24px;border-radius:16px;background:var(--negro);color:#fff}
.cta h2{color:#fff;margin:0 0 8px;font-size:21px}
.cta p{color:rgba(255,255,255,.78);margin-bottom:16px}
.cta .botones{display:flex;flex-wrap:wrap;gap:10px}
.btn{display:inline-block;padding:11px 18px;border-radius:10px;font-weight:600;font-size:15px;text-decoration:none}
.btn-p{background:linear-gradient(135deg,#00B894,#0055BA);color:#fff!important}
.btn-s{background:rgba(255,255,255,.1);color:#fff!important;border:1px solid rgba(255,255,255,.2)}
.ts{margin:28px 0;padding:18px 20px;border:1px solid var(--borde);border-radius:14px;background:var(--fondo)}
.ts p{margin:0}
details{border:1px solid var(--borde);border-radius:12px;padding:14px 16px;margin:10px 0}
summary{font-weight:700;cursor:pointer}
details p{margin:10px 0 0}
.relacionadas{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px;margin-top:12px}
.relacionadas a{display:block;padding:14px 16px;border:1px solid var(--borde);border-radius:12px;text-decoration:none;color:var(--negro);font-weight:600;font-size:15px;line-height:1.35}
.relacionadas a:hover{border-color:var(--azul)}
.fuentes{font-size:13px;color:var(--gris)}
.aviso{background:var(--fondo);font-size:13px;color:var(--sub);padding:14px 24px;text-align:center}
footer{background:var(--negro);color:rgba(255,255,255,.6);font-size:13px;padding:24px 40px;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
footer a{color:rgba(255,255,255,.75);text-decoration:none}
@media(max-width:700px){nav{padding:0 16px}.nav-links a:not(.btn-nav){display:none}footer{padding:24px 16px}}
"""

HEAD_COMUN = """  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <meta name="theme-color" content="#10233F">
  <script async src="https://www.googletagmanager.com/gtag/js?id=AW-18313714699"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag('js',new Date());gtag('config','AW-18313714699');</script>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..800&display=swap" rel="stylesheet"/>"""

NAV = """<nav>
  <a class="logo" href="/"><img src="/logo-ts-80.png" alt="" width="40" height="20">Alta<span>Monotributo</span></a>
  <div class="nav-links">
    <a href="/guias/">Guías</a>
    <a href="/acerca-de-nosotros">Nosotros</a>
    <a href="/#formulario" class="btn-nav">Darme de alta</a>
  </div>
</nav>"""

PIE = """<div class="aviso"><strong>Aviso legal:</strong> AltaMonotributo.com es un servicio privado de asistencia operado por Tributo Simple S.A.S. No somos ARCA ni estamos afiliados al gobierno. La información de estas guías es general: para tu caso puntual, consultá con un contador.</div>
<footer>
  <div>© 2026 AltaMonotributo · un servicio de <a href="https://tributosimple.com/?utm_source=altamonotributo&amp;utm_medium=footer" target="_blank" rel="noopener" style="font-weight:600">Tributo Simple ®</a></div>
  <div style="display:flex;gap:16px;flex-wrap:wrap">
    <a href="/guias/">Guías</a>
    <a href="/acerca-de-nosotros">Nosotros</a>
    <a href="/terminos-y-condiciones">Términos y condiciones</a>
    <a href="/politica-de-privacidad">Política de privacidad</a>
  </div>
</footer>"""


def esc(s):
    return html.escape(s, quote=True)


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'


def pagina(titulo, descripcion, url, cuerpo_header, cuerpo_main, schemas):
    return f"""<!DOCTYPE html>
<html lang="es-AR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{esc(titulo)}</title>
  <meta name="description" content="{esc(descripcion)}"/>
  <meta name="robots" content="index, follow, max-image-preview:large"/>
  <link rel="canonical" href="{url}"/>
  <meta property="og:type" content="article"/>
  <meta property="og:url" content="{url}"/>
  <meta property="og:title" content="{esc(titulo)}"/>
  <meta property="og:description" content="{esc(descripcion)}"/>
  <meta property="og:image" content="{SITIO}/og-image.png"/>
  <meta property="og:locale" content="es_AR"/>
  <meta property="og:site_name" content="AltaMonotributo"/>
{HEAD_COMUN}
  <style>{CSS}</style>
  {''.join(ld(s) for s in schemas)}
</head>
<body>
{NAV}
<header class="hero"><div class="wrap">
{cuerpo_header}
</div></header>
<main><div class="wrap">
{cuerpo_main}
</div></main>
{PIE}
</body>
</html>
"""


def guia(g, todas):
    url = f"{SITIO}/guias/{g['slug']}"
    migas = f'<div class="migas"><a href="/">Inicio</a> / <a href="/guias/">Guías</a> / {esc(g["corto"])}</div>'
    header = (f'{migas}\n<h1>{esc(g["h1"])}</h1>\n<p class="bajada">{esc(g["bajada"])}</p>\n'
              f'<p class="meta">Actualizado: {ACTUALIZADO} · Equipo de contadores de Tributo Simple</p>')
    faq_html = ''.join(f'<details><summary>{esc(q)}</summary><p>{a}</p></details>' for q, a in g['faq'])
    rel = [x for x in todas if x['slug'] != g['slug']][:4]
    rel_html = ''.join(f'<a href="/guias/{x["slug"]}">{esc(x["h1"])}</a>' for x in rel)
    fuentes = ' · '.join(f'<a href="{u}" target="_blank" rel="noopener">{esc(t)}</a>' for t, u in g['fuentes'])
    wa = WA + html.escape(g['wa'].replace(' ', '%20'))
    cta = f"""<div class="cta">
  <h2>{esc(g['cta_titulo'])}</h2>
  <p>{esc(g['cta_texto'])}</p>
  <div class="botones"><a class="btn btn-p" href="/#formulario">Darme de alta en 24 hs</a><a class="btn btn-s" href="{wa}" target="_blank" rel="noopener">Consultar por WhatsApp</a></div>
</div>"""
    ts = (f'<div class="ts"><p><strong>¿Ya sos monotributista?</strong> En <a href="{TS.format(slug=g["slug"])}" '
          f'target="_blank" rel="noopener">Tributo Simple</a> te llevamos el monotributo todos los meses desde una app: '
          f'facturación, pagos, recategorización y un contador cuando lo necesitás.</p></div>')
    main = (f'<div class="respuesta">{g["respuesta"]}</div>\n{g["cuerpo"]}\n{cta}\n'
            f'<h2>Preguntas frecuentes</h2>\n{faq_html}\n{ts}\n'
            f'<h2>Seguí leyendo</h2>\n<div class="relacionadas">{rel_html}</div>\n'
            f'<p class="fuentes" style="margin-top:28px">Fuentes oficiales: {fuentes}</p>')
    schemas = [
        {'@context': 'https://schema.org', '@type': 'Article', 'headline': g['h1'], 'description': g['descripcion'],
         'datePublished': ACTUALIZADO_ISO, 'dateModified': ACTUALIZADO_ISO, 'inLanguage': 'es-AR',
         'mainEntityOfPage': url, 'image': f'{SITIO}/og-image.png',
         'author': {'@type': 'Organization', 'name': 'Tributo Simple S.A.S.', 'url': 'https://tributosimple.com'},
         'publisher': {'@type': 'Organization', 'name': 'AltaMonotributo', 'url': SITIO,
                       'logo': {'@type': 'ImageObject', 'url': f'{SITIO}/android-chrome-512x512.png'}}},
        {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
            {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': html.unescape(_sin_tags(a))}}
            for q, a in g['faq']]},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Inicio', 'item': SITIO + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Guías', 'item': SITIO + '/guias/'},
            {'@type': 'ListItem', 'position': 3, 'name': g['corto'], 'item': url}]},
    ]
    return pagina(g['titulo'], g['descripcion'], url, header, main, schemas)


def _sin_tags(s):
    import re
    return re.sub(r'<[^>]+>', '', s)


def indice(todas):
    url = f'{SITIO}/guias/'
    header = ('<div class="migas"><a href="/">Inicio</a> / Guías</div>\n<h1>Guías de monotributo</h1>\n'
              '<p class="bajada">Todo lo que necesitás saber del monotributo, explicado simple y con los valores vigentes. '
              'Escrito por el equipo de contadores de Tributo Simple.</p>'
              f'\n<p class="meta">Actualizado: {ACTUALIZADO}</p>')
    items = ''.join(f'<a href="/guias/{g["slug"]}">{esc(g["h1"])}</a>' for g in todas)
    main = (f'<div class="relacionadas">{items}</div>'
            '<div class="cta"><h2>¿Todavía no sos monotributista?</h2><p>Hacemos tu alta en menos de 24 hs hábiles: '
            'elegimos tu categoría y te entregamos la constancia oficial.</p><div class="botones">'
            '<a class="btn btn-p" href="/#formulario">Darme de alta</a></div></div>')
    schemas = [{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Guías de monotributo', 'url': url,
                'hasPart': [{'@type': 'Article', 'headline': g['h1'], 'url': f"{SITIO}/guias/{g['slug']}"} for g in todas]}]
    return pagina('Guías de monotributo 2026 | AltaMonotributo',
                  'Guías claras sobre el monotributo: categorías y cuotas 2026, factura C, recategorización, relación de dependencia y qué pasa si no pagás.',
                  url, header, main, schemas)


def escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, 'w', encoding='utf-8', newline='\n') as f:
        f.write(texto)


def main():
    for g in GUIAS:
        escribir(os.path.join(RAIZ, 'guias', g['slug'] + '.html'), guia(g, GUIAS))
    escribir(os.path.join(RAIZ, 'guias', 'index.html'), indice(GUIAS))
    urls = [('/', '1.0'), ('/guias/', '0.8')] + [(f"/guias/{g['slug']}", '0.8') for g in GUIAS] + \
           [('/acerca-de-nosotros', '0.5'), ('/terminos-y-condiciones', '0.2'), ('/politica-de-privacidad', '0.2')]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml += [f'  <url><loc>{SITIO}{u}</loc><lastmod>{ACTUALIZADO_ISO}</lastmod><priority>{p}</priority></url>' for u, p in urls]
    xml.append('</urlset>')
    escribir(os.path.join(RAIZ, 'sitemap.xml'), '\n'.join(xml) + '\n')
    print(f'{len(GUIAS)} guías + índice + sitemap ({len(urls)} URLs)')


if __name__ == '__main__':
    main()
