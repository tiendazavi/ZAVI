# ZAVI – Tienda web

Tienda de ropa importada **ZAVI** ("encuentra tu estilo"), Huancayo, Junín, Perú.
Sitio estático de un solo archivo (HTML + CSS + JS), sin servidor ni dependencias.

## Estructura
- `index.html` – la tienda completa (logo, QR de Yape y productos incrustados).
- `zavi-compartir.jpg` – imagen de vista previa al compartir el enlace.
- `panel-local/admin-zavi.html` – panel para editar productos, precios, fotos, tallas, ofertas y envío sin tocar código. Se abre en tu computadora; carga `index.html`, editas y descargas la tienda actualizada (renómbrala a `index.html` y súbela).
- `fuentes/` – archivos fuente y script de construcción (solo para desarrollo).

## Publicar con GitHub Pages
1. Sube todo el contenido a un repositorio (público para el plan gratuito).
2. Settings → Pages → Source: *Deploy from a branch* → rama `main`, carpeta `/ (root)`.
3. Tu dirección será `https://TU-USUARIO.github.io/NOMBRE-REPO/`.
4. Abre el panel, pestaña **Ajustes**, escribe esa dirección en "Dirección web" y descarga la tienda; reemplaza `index.html` en GitHub. Así se completan las etiquetas para compartir y Google.

## Actualizar productos
Panel → cargar `index.html` → editar → *Descargar tienda actualizada* → subir como `index.html`.
Antes de cambiar algo, parte siempre del `index.html` más reciente para no perder tus ediciones.

## Políticas actuales
Envío a domicilio S/ 5 (recojo en tienda sin costo, configurable). Se aceptan cambios; no hay devoluciones.

## Nota de seguridad
El panel no tiene contraseña y no guarda nada en internet: solo modifica una copia local. Aun así, `panel-local/` quedará visible si el repositorio es público; no contiene claves ni datos privados.
