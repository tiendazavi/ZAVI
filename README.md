# ZAVI – Tienda web

Tienda de ropa importada **ZAVI** ("encuentra tu estilo"), Huancayo, Junín, Perú.
Sitio estático de un solo archivo (HTML + CSS + JS), sin servidor ni dependencias.

## Estructura
- `index.html` – la tienda completa (logo, QR de Yape y productos incrustados).
- `zavi-compartir.jpg` – imagen de vista previa al compartir el enlace.
- `panel-local/admin-zavi.html` – panel de administración, **solo para usar en tu PC (sin contraseña, no se sube a GitHub)**.
- `fuentes/` – fuentes y script de construcción (solo para desarrollo).

## Publicar con GitHub Pages
1. Sube todo el contenido a un repositorio (público para el plan gratuito).
2. Settings → Pages → *Deploy from a branch* → rama `main`, carpeta `/ (root)`.
3. La tienda queda en `https://TU-USUARIO.github.io/NOMBRE-REPO/` .
4. En el panel, pestaña **Datos de la tienda**, escribe esa dirección en "Dirección web" y descarga la tienda; reemplaza `index.html` en GitHub.

## Panel de administración
Abre `panel-local/admin-zavi.html` con doble clic en tu computadora. Allí puedes:
- Agregar, duplicar, ordenar y eliminar prendas; cambiar fotos, precios, tallas y etiquetas.
- **Agregar varias con fotos** (una prenda por foto) y **importar una planilla Excel/CSV** (⬇ Planilla Excel descarga el ejemplo).
- **Seleccionar varias prendas** y aplicar en lote: descuento %, quitar oferta, agotado/disponible, ocultar/mostrar, eliminar.
- Filtrar por categoría, estado, *sin foto*, *sin precio* o *en oferta*.
- En cada prenda: hasta **6 fotos extra** (galería de la ficha, con zoom y pantalla completa) y una **descripción** opcional.
- Pestaña **Ofertas de la semana**: prendas que aparecen solo en esa sección.
- Pestaña **Imágenes de portada**: cambia la foto, el título, el texto y el botón de los 3 banners; las fotos de las categorías (Mujer, Hombre, Zapatillas, Accesorios, Por mayor) y la foto de “Nosotros”. Solo se guarda lo que cambias.
- **Datos de la tienda**: WhatsApp, Yape y QR, envío (S/ 5), recojo, condiciones de cambio, fecha de fin de ofertas, enlaces.

Flujo: abre el panel → carga tu `index.html` más reciente → edita → *Descargar tienda actualizada* → renómbrala a `index.html` y reemplázala en GitHub. Parte siempre del `index.html` más reciente para no perder cambios.

## Seguridad
El panel no tiene contraseña porque se usa solo en tu computadora: no lo subas a GitHub (la carpeta `panel-local/` está en `.gitignore` por si usas git). Solo modifica una copia local; lo que protege tu tienda publicada es tu cuenta de GitHub (activa la verificación en dos pasos).

## Políticas actuales
Envío a domicilio S/ 5 (recojo en tienda sin costo, configurable). Se aceptan cambios; no hay devoluciones.

## Catálogo y ficha de producto
- Los filtros son coherentes: solo muestran tallas, tipos y precios que existen con tu selección (con su cantidad); si un filtro deja de aplicar, se quita solo y se avisa.
- La ficha de cada prenda muestra galería con miniaturas, precio con descuento, talla, cantidad, “Agregar al carro”, favoritos, detalles e información adicional.

## Accesibilidad y honestidad
- Enlace para saltar al contenido, foco visible, navegación por teclado, ventana de pago con foco controlado y respeto por "reducir movimiento".
- Sin opiniones ni cifras inventadas: la sección de opiniones invita a compartir experiencias reales.
- La cuenta regresiva de ofertas solo aparece si configuras una fecha futura.
- La tienda es estática: el pedido se prepara como mensaje de WhatsApp y el flujo de Yape muestra los datos de pago. **No procesa ni verifica pagos**, ni guarda pedidos ni controla stock.

## Pendiente (depende del dueño)
Fotos, precios y tallas reales (el catálogo actual es de demostración), publicar y poner la dirección web en el panel, enlace del Libro de reclamaciones, condiciones de cambio y política de privacidad.

## Reconstruir desde las fuentes
`python3 fuentes/build_all.py` (conserva tus productos actuales) o `--reset-datos` para volver a los de ejemplo.

## Actualizar el diseño SIN perder tus productos, precios y fotos

Tus datos (productos, precios, fotos, ajustes) viven **dentro** de tu `index.html` publicado. Por eso **nunca reemplaces tu `index.html` con el del zip de una actualización**: traería los datos de ejemplo y borraría lo tuyo.

Haz esto:

1. Abre `panel-local/admin-zavi.html` y elige **tu** `index.html` actual (el que está publicado en GitHub, con tus datos).
2. Toca **⟳ Actualizar diseño** y elige el `index.html` **nuevo** que viene en la actualización.
3. Toca **Descargar tienda actualizada**, renómbralo a `index.html` y súbelo a GitHub.

El diseño es el nuevo; tus productos, fotos, precios y ajustes se quedan como estaban. Guarda una copia de tu `index.html` antes de cada actualización como respaldo.
