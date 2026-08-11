# Humedales - Tributarios Cortos del Paraná

## Descripción

Cartografía de cuerpos de agua naturales (humedales nivel IV) de tributarios cortos del río Paraná.

## Metadatos

- **Licencia:** CC-BY-4.0
- **Extent espacial:** Entre Ríos, Argentina
- **Proveedores:** CEREGEO, Centro Regional de Geomática, IDE-FCyT

## Explorar datos

<iframe
  id="stac-browser-humedales"
  title="Humedales - STAC Browser"
  style="min-height: 600px; width: 100%; border: 1px solid #ddd;"
  allowfullscreen
  loading="lazy">
</iframe>

<script>
  (function() {
    const iframe = document.getElementById("stac-browser-humedales");
    if (!iframe) return;

    const basePath = window.location.pathname.split("/pages/")[0];
    const stacUrl = `${window.location.origin}${basePath}/catalog/humedales.json`;
    iframe.src = `https://radiantearth.github.io/stac-browser/#/external/${stacUrl}?.language=es`;
  })();
</script>

## Recursos adicionales

- [Ver en el mapa](https://raw.githack.com/FacuBoladeras/mis_proyectos/master/qgis2web_2025_08_18-09_56_58_347860/index.html)
- [Descarga de datos](https://drive.google.com/uc?export=download&id=1EQUl7XehmiWvuPCVSv56Fzg_52SGYhZe)
