# Servicios ecosistémicos del Espinal

## Descripción

Sistema de Información Geográfico (SIG) realizado en el marco del Programa ImpaCT.AR Ciencia y Tecnología (Proyecto Desafío 155) promovido por el Ministerio de Ciencia, Tecnología e Innovación de Argentina (MINCyT).

## Autores

- Alan Evequoz
- Pamela Zamboni

## Metadatos

- **Licencia:** CC-BY-4.0
- **Extensión espacial:** Argentina (región del Espinal)

## Explorar datos

<iframe
  id="stac-browser-servicios-ecosistemicos-espinal"
  title="Servicios ecosistémicos del Espinal - STAC Browser"
  style="min-height: 600px; width: 100%; border: 1px solid #ddd;"
  allowfullscreen
  loading="lazy">
</iframe>

<script>
  (function() {
    const iframe = document.getElementById("stac-browser-servicios-ecosistemicos-espinal");
    if (!iframe) return;

    const basePath = window.location.pathname.split("/pages/")[0];
    const stacUrl = `${window.location.origin}${basePath}/catalog/servicios_ecosistemicos_esp.json`;
    iframe.src = `https://radiantearth.github.io/stac-browser/#/external/${stacUrl}?.language=es`;
  })();
</script>

## Recursos adicionales

- [Ver en el mapa](https://rawcdn.githack.com/FacuBoladeras/servicios_ecosistemicos_espinal/17e0d5ba6ee11e498a0d6c91efc7ef7eecf1b73d/index.html)
