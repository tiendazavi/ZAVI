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


## Mejoras de experiencia ZAVI
- Diseño visual refinado con mejor jerarquía, tarjetas de producto, estados de foco y navegación móvil.
- Catálogo más cómodo de explorar en pantallas pequeñas; menú de categorías desplazable.
- Enlace para saltar directamente al contenido y soporte reforzado para navegación por teclado y movimiento reducido.
- La sección de opiniones ya no muestra reseñas ni cifras de clientes ficticias: invita a compartir experiencias reales.
- Se mantiene la compra por WhatsApp, el carrito, favoritos, selección de tallas y pago informativo con Yape.
- `fuentes/build_all.py` ahora usa rutas relativas y puede reconstruir `index.html` desde `fuentes/zavi-src.html` y `fuentes/datos.json`, recuperando los recursos gráficos embebidos del `index.html` actual.

## Importante sobre pagos y pedidos
La tienda es estática: el botón de pedido prepara el mensaje para WhatsApp y el flujo de Yape muestra los datos de pago; no procesa tarjetas ni confirma pagos automáticamente, y no guarda pedidos en una base de datos. Para automatizar inventario, pagos y pedidos se necesitaría integrar un backend o una plataforma de comercio electrónico.


## Revisión técnica adicional
- La cuenta regresiva de ofertas solo aparece cuando se configura una fecha de vencimiento futura; no se inventa un cierre semanal.
- El botón del carrito describe el flujo como instrucciones de pago con Yape. La tienda informa expresamente que no procesa ni verifica pagos automáticamente.
- El diálogo de pago mueve el foco al abrirse, limita la navegación con Tab dentro de la ventana y devuelve el foco al control que lo abrió al cerrarse.
- Las imágenes del catálogo usan decodificación asíncrona además de carga diferida.
- El panel-local se conserva sin modificaciones.

## Límites que siguen pendientes
- El catálogo incluido contiene artículos e imágenes de demostración: reemplázalos por inventario, fotos, precios y tallas reales antes de vender.
- Los pedidos se coordinan por WhatsApp; no hay persistencia centralizada, control de stock compartido ni conciliación automática de pagos.
- Para pagos en línea e inventario multiusuario se requiere un backend o una plataforma externa con credenciales privadas almacenadas del lado del servidor.
