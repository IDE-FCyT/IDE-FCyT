# Normativas Nacionales - Ley 22.963 (Ley de la Carta - IGN)

## Alcance del analisis

Este documento evalua el desfase del portal IDE-FCyT frente a la **Ley 22.963 (1983)**, conocida como Ley de la Carta (actual autoridad: Instituto Geografico Nacional, IGN).

Fuente legal analizada (texto extraido): `docs/Ley_22963_1983.txt`.

## Criterios legales aplicables al portal

Se relevaron como criterios principales los articulos 1, 16, 18, 19 y 19 bis de la ley.

1. Toda representacion del territorio argentino debe ajustarse a cartografia oficial (art. 1 y 19.a).
2. La publicacion de representaciones parciales debe respetar condiciones especificas (art. 19.c).
3. La publicidad/publicacion de material cartografico requiere aprobacion previa del IGN (art. 18).
4. El material aprobado debe incluir la leyenda visible "Aprobado por el Instituto Geografico Nacional" y numero de expediente (art. 19 bis).

## Matriz de desfase (Ley 22.963 vs portal)

| Requisito legal | Evidencia en el proyecto | Estado | Desfase |
|---|---|---|---|
| Ajuste a cartografia oficial (art. 1, 19.a) | El portal publica mapas y visores en multiples paginas, por ejemplo `docs/pages/carta_de_suelos.md`, `docs/pages/mapaweb.md`, `docs/pages/incendioislapuente.md` | Parcial / No verificable | No se encontro en el repositorio una declaracion o trazabilidad explicita que certifique ajuste a cartografia oficial del IGN para cada publicacion |
| Representaciones parciales con referencia al territorio completo (art. 19.c) | Se publican recortes/areas tematicas (cuencas, humedales, suelos, etc.) | No verificable | No hay evidencia sistematica en plantillas/editorial de incluir mapa nacional marginal de situacion relativa |
| Aprobacion previa IGN para publicar representaciones del territorio (art. 18) | El portal expone cartografia, mapas y visores (propios o embebidos) | No cumple (sin evidencia) | No se encontro registro de expediente de aprobacion IGN asociado a cada recurso cartografico publicado |
| Leyenda obligatoria de aprobacion + expediente (art. 19 bis) | Busqueda en todo el proyecto sin resultados de la frase obligatoria | No cumple | Falta leyenda visible de aprobacion IGN y numero de expediente en publicaciones cartograficas alcanzadas |

## Evidencia tecnica puntual

### Publicaciones cartograficas detectadas

- `docs/pages/carta_de_suelos.md` (vista previa + visor externo)
- `docs/pages/mapaweb.md` (mapa web y flujo QGIS/Leaflet)
- `docs/pages/incendioislapuente.md` (visor GEE embebido)
- `docs/pages/handsen.md` (visor GEE embebido)
- `docs/pages/catalogo.md` (catalogo STAC visible al publico)

### Hallazgo de incumplimiento documental

No se encontro en `docs/`, `qgis_maps/` ni `site/` la inscripcion:

`Aprobado por el Instituto Geografico Nacional`

ni un campo equivalente con numero de expediente de aprobacion.

## Riesgo de cumplimiento

Riesgo **alto** para contenido cartografico publicado sin evidencia de aprobacion IGN cuando corresponda por alcance legal.

## Recomendaciones de normalizacion (acciones concretas)

1. Crear un registro interno de control legal por recurso cartografico:
   - `id_recurso`
   - `requiere_aprobacion_ign` (si/no)
   - `nro_expediente_ign`
   - `fecha_aprobacion`
   - `observaciones`
2. Incorporar en metadatos STAC (Collection/Item) campos de cumplimiento:
   - `legal:ley_22963_aplica`
   - `legal:ign_aprobado`
   - `legal:ign_expediente`
3. Agregar leyenda visible en paginas/publicaciones alcanzadas por art. 19 bis.
4. Actualizar `docs/pages/lineamientos_editoriales.md` con un bloque obligatorio de control normativo nacional antes de publicar mapas.
5. Definir circuito de validacion (responsable institucional + evidencia documental) previo a publicacion.

## Nota de alcance

Este analisis identifica brechas documentales y de trazabilidad en el repositorio.  
La determinacion juridica final de aplicabilidad por tipo de publicacion debe validarse con asesoria legal institucional.
