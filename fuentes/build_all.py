#!/usr/bin/env python3
"""Construye la tienda estática ZAVI usando rutas relativas al proyecto."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
FUENTES = ROOT / "fuentes"
INDEX = ROOT / "index.html"
TEMPLATE = FUENTES / "zavi-src.html"
DATOS = FUENTES / "datos.json"


def data_uri_from(html: str, pattern: str) -> str:
    match = re.search(pattern, html, re.S)
    if not match:
        raise RuntimeError(f"No se encontró el recurso embebido: {pattern}")
    return match.group(1)


def main():
    current = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    if not current:
        raise RuntimeError("No existe index.html para recuperar el logo y el QR iniciales.")

    logo = data_uri_from(current, r'class="logo-img" src="(data:image/[^"]+)"')
    favicon = data_uri_from(current, r'<link rel="icon"[^>]+href="(data:image/[^"]+)"')
    data_match = re.search(r'<script[^>]*id="zavi-datos"[^>]*>(.*?)</script>', current, re.S)
    if not data_match:
        raise RuntimeError("No se encontró el bloque zavi-datos en index.html.")
    datos_actuales = json.loads(data_match.group(1))
    datos_nuevos = json.loads(DATOS.read_text(encoding="utf-8"))
    if not datos_nuevos.get("config", {}).get("qr"):
        datos_nuevos.setdefault("config", {})["qr"] = datos_actuales.get("config", {}).get("qr", "")
    bloque = json.dumps(datos_nuevos, ensure_ascii=False).replace("<", "\\u003c")

    tienda = TEMPLATE.read_text(encoding="utf-8")
    for token in ("{{LOGO}}", "{{FAVICON}}", "{{DATOS}}"):
        if tienda.count(token) != 1:
            raise RuntimeError(f"El marcador {token} debe aparecer exactamente una vez.")
    tienda = tienda.replace("{{LOGO}}", logo).replace("{{FAVICON}}", favicon).replace("{{DATOS}}", bloque)
    INDEX.write_text(tienda, encoding="utf-8")

    print(f"Tienda generada: {INDEX} ({len(tienda) / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
