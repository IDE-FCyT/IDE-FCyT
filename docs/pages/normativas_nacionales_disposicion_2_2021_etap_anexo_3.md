# Normativas Nacionales - Disposicion ONTI 2/2021 (ETAP v25) - Anexo III

Fuente normativa evaluada: `docs/Disposicion_2_2021_ONTI_ETAP_Anexo_3.txt`

## Desfases detectados en LI - Geotecnologias

| Item evaluado | Estado en el proyecto | Fragmento textual verbatim | Por que tecnicamente existe desfase (o cumple parcial) | Como lograr cumplir este objetivo |
|---|---|---|---|---|
| Publicacion de datos geoespaciales mediante servicios OGC recomendados por la norma | Desfase parcial | `Siempre que sea posible se debera emplear el formato WFS (Web Feature Service) en el caso de informacion vectorial o WCS (Web Coverage Service) en el caso de informacion raster para su publicacion` | El portal publica catalogo STAC y JSON, pero no expone endpoints WFS/WCS verificables para consumo interoperable de capas vectoriales/raster. | Publicar servicios OGC (WFS para vectorial y WCS para raster) y documentar sus URL/capacidades en la pagina de catalogo y en metadatos de cada recurso. |
| Descarga de datos en formatos geoespaciales con metadatos XML asociados | Desfase total | `sin perjuicio a que los mismos esten disponibles para descarga en formato Shapefile y .kmz, acompanados por sus metadatos en formato .xml` | En `docs/catalog/` no se evidencian enlaces a descargas `.shp` o `.kmz`, ni archivos de metadatos `.xml` asociados a los datasets publicados. | Incorporar paquetes de descarga (al menos `.shp` y/o `.kmz` segun corresponda) y publicar metadatos `.xml` por dataset, enlazados desde el catalogo STAC. |

## Alcance general del Anexo III

Fuera de LI - Geotecnologias, el Anexo III mantiene un enfoque mayormente de lineamientos/recomendaciones y, en varios apartados, condicional a escenarios de contratacion o implementacion especificos.
