# Manual de Cumplimiento IDERA (Parte 1)

## Alcance de esta parte

Este documento cubre solo el **Reglamento de Funcionamiento de IDERA (version 2025)** y su contraste con el codigo actual del portal IDE-FCyT.

No reemplaza las normativas tecnicas de objetos geograficos (COG u otras). Esa comparacion se incorpora en la **Parte 2 (Normativas)**.

## Fuentes usadas

- Reglamento extraido a texto: `docs/Reglamento_IDERA_Nov2025.txt`
- Codigo revisado:
  - `mkdocs.yml`
  - `docs/index.md`
  - `docs/pages/*.md`
  - `docs/catalog/*.json`
  - `qgis_maps/**/data/*.js`

## Criterios del reglamento tomados para control

Se tomaron criterios operativos del reglamento (no tecnicos de geometria):

1. Publicacion y difusion de datos geoespaciales y metadatos.
2. Interoperabilidad y estandarizacion (alineacion con estandares y normativa vigente).
3. Definicion de condiciones de acceso por parte del productor.
4. Servicio a la comunidad (acceso publico).
5. Cooperacion y articulacion institucional.

## Matriz de desfase (estado actual)

| Item de control (Reglamento) | Evidencia en codigo | Estado | Desfase detectado |
|---|---|---|---|
| Disponibilidad publica de informacion geoespacial | `docs/index.md` define portal academico y acceso abierto | Parcial | Hay acceso y difusion, pero sin politica formal de niveles de acceso por dataset |
| Datos + metadatos disponibles | Existe catalogo STAC y metadatos por coleccion en `docs/catalog/*.json` | Parcial | La calidad de metadatos es heterogenea entre colecciones |
| Estandarizacion/interoperabilidad | Uso de STAC en `docs/pages/catalogo.md` y `docs/catalog/stac_catalog.json` | Parcial | Inconsistencias de identificadores afectan interoperabilidad |
| Integridad semantica del catalogo | Enlace de hijos en `docs/catalog/stac_catalog.json` | No cumple | IDs repetidos en enlaces `child` y titulos duplicados en temas distintos |
| Identificacion unica de recursos | Campo `id` en cada coleccion | No cumple | Se reutiliza el mismo `id` en multiples colecciones no equivalentes |
| Condiciones de uso/acceso por productor | Hay `license` y enlaces de licencia en colecciones | Parcial | No hay esquema comun para restricciones/accesibilidad por nivel de dato |
| Servicio a la comunidad y articulacion | `docs/index.md` contiene adhesion a IDERA y enlaces institucionales | Cumple | Sin desfase relevante en esta parte |

## Hallazgos tecnicos concretos

### 1) Duplicacion de IDs en el catalogo raiz

En `docs/catalog/stac_catalog.json` aparecen IDs `child` repetidos:

- `espinal` (lineas 70 y 91)
- `humedales` (lineas 84 y 98)

Esto rompe unicidad y dificulta consumo automatico de catalogos.

### 2) Reutilizacion de `id` de coleccion en datasets distintos

El mismo `id` se repite en varias colecciones:

- `projects/earthengine-legacy/assets/projects/sat-io/open-datasets/CSRL_soil_properties/chemical/cec`
  - `docs/catalog/UA.json:7`
  - `docs/catalog/apn.json:7`
  - `docs/catalog/chana.json:7`
  - `docs/catalog/laguna.json:7`
  - `docs/catalog/monte.json:7`
  - `docs/catalog/paracao.json:8`

Tambien se repite:

- `cuenca-arroyo-las-conchas`
  - `docs/catalog/las_tunas.json:8`
  - `docs/catalog/cuencaEspinillo.json:8`

### 3) IDs no normalizados

- `docs/catalog/corrientesER.json:8` usa `id` con espacios (`Análisis cambio climatico`), lo que no es recomendable para identificadores interoperables.

### 4) Falta de modelo de clase para objetos espaciales

No se detectaron campos de clase/categoria de objeto en `docs/catalog/*.json` (ejemplo esperado: clase `agua`, `vegetacion`, etc.).

## Enfasis requerido: objetos espaciales por clase

Para normalizar desfases con foco en objetos espaciales, se propone agregar en cada coleccion (y luego en Items STAC cuando corresponda) un bloque comun:

| Campo propuesto | Tipo | Ejemplo |
|---|---|---|
| `idera:clase` | string controlado | `agua` |
| `idera:subclase` | string controlado | `rio` |
| `idera:tipo_objeto` | string | `curso_agua` |
| `idera:fuente_clasificacion` | string/url | `COG-IDERA-vX` |
| `idera:version_clasificacion` | string | `2025-10` |

Ejemplo rapido:

```json
{
  "idera:clase": "agua",
  "idera:subclase": "rio",
  "idera:tipo_objeto": "curso_agua",
  "idera:fuente_clasificacion": "COG-IDERA",
  "idera:version_clasificacion": "2025-10"
}
```

## Checklist minimo para cerrar esta Parte 1

1. Corregir IDs repetidos en `stac_catalog.json`.
2. Garantizar `id` unico por cada `Collection`.
3. Normalizar `id` a formato slug (sin espacios, minusculas, guiones).
4. Definir politica de acceso por dataset (abierto/restringido y motivo).
5. Incorporar campos de clase de objeto espacial (esquema preliminar de arriba).

## Limite de esta parte

El reglamento analizado es **funcional/institucional** y no define por si solo un catalogo tecnico de clases geograficas completo.  
La validacion semantica fina de clases, atributos y relaciones de objetos se debe cerrar en la **Parte 2 (Normativas tecnicas IDERA)**.
