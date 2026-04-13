# Normativas Nacionales - Ley 26.209 (Ley Nacional de Catastro)

## Alcance del analisis

Este documento releva brechas del portal IDE-FCyT frente a la **Ley 26.209** (Ley Nacional de Catastro), tomando como base el texto:

- `docs/Ley_26209_Nacional_de_Catastro.txt`

El analisis se enfoca en cumplimiento documental, metadatos y trazabilidad dentro del repositorio.

## Nota de aplicabilidad

La Ley 26.209 regula principalmente a los catastros jurisdiccionales (provincias y CABA).  
Por lo tanto, parte de sus obligaciones son de autoridad catastral y no de un portal academico.  
Aun asi, cuando el portal publica informacion territorial vinculada a inmuebles/objetos territoriales, corresponde explicitar alcance, fuente y condicion catastral para evitar ambiguedades.

## Matriz de desfases

| Base legal | Exigencia normativa | Evidencia en el proyecto | Estado | Desfase detectado |
|---|---|---|---|---|
| Art. 1 y 3.c | Registro/publicidad de objetos territoriales legales bajo jurisdiccion catastral | El portal publica capas y visores territoriales (ej. `docs/pages/mapaweb.md`, `docs/pages/carta_de_suelos.md`) | Parcial / No verificable | No se explicita en cada recurso si es informacion catastral oficial, derivada, o solo divulgativa |
| Art. 3.j | Estandares y metadatos compatibles con IDE | Hay STAC y metadatos minimos (`docs/pages/catalogo.md`, `docs/catalog/*.json`) | Parcial | Falta perfil de metadatos catastrales (fuente catastral, vigencia parcelaria, precision, responsable jurisdiccional) |
| Art. 4 y 5 | Definicion parcelaria y elementos esenciales/complementarios (ubicacion georreferenciada, limites, medidas, superficie, linderos, valuacion fiscal) | No se detectan campos parcelarios en catalogo STAC | No cumple (si se pretendiera publicar datos parcelarios) | No hay estructura de datos/atributos para estado parcelario |
| Art. 6, 7, 9, 10 | Mensura, constitucion/verificacion y registro formal de objetos territoriales legales | No hay evidencia de trazabilidad de plano de mensura, profesional actuante ni acto registral | No verificable | Falta trazabilidad legal-técnica cuando un recurso pudiera interpretarse como parcelario/legal |
| Art. 11, 12, 13 | Certificacion catastral habilitante en actos sobre derechos reales | No hay referencia a certificacion catastral en publicaciones | No cumple (en terminos documentales) | Ausencia de advertencia y/o enlace a certificaciones cuando corresponda |
| Art. 14 | Valuacion parcelaria de base tecnica | No se publica informacion de valuacion parcelaria | No aplica / No cumple documental | No hay declaracion de no inclusion de valuacion catastral oficial |

## Hallazgos tecnicos concretos

1. No se encontraron en `docs/catalog/` campos asociados a:
   - `parcela`
   - `estado_parcelario`
   - `certificacion_catastral`
   - `mensura`
   - `valuacion_fiscal`
2. En paginas de proyectos cartograficos hay publicacion territorial, pero sin leyenda clara sobre estatus catastral/legal del dato.
3. No existe una politica de “uso catastral” para distinguir:
   - datos oficiales catastrales,
   - datos tematicos de investigacion,
   - productos de divulgacion.

## Riesgo de cumplimiento

Riesgo **medio** por potencial confusion de usuarios: un portal de IDE puede ser interpretado como fuente catastral oficial si no declara expresamente el alcance legal de cada capa.

## Acciones correctivas recomendadas

1. Crear una seccion `Alcance catastral del dato` en cada dataset/proyecto con valores:
   - `oficial_catastral`,
   - `derivado_de_fuente_catastral`,
   - `no_catastral`.
2. Incorporar campos STAC de trazabilidad minima:
   - `catastro:jurisdiccion`
   - `catastro:organismo_fuente`
   - `catastro:fecha_vigencia`
   - `catastro:es_estado_parcelario` (true/false)
   - `catastro:certificacion_ref` (si corresponde)
3. Agregar disclaimer institucional en capas no catastrales: “No constituye certificacion catastral habilitante”.
4. Enlazar, cuando aplique, a organismo catastral provincial competente y su normativa operativa.
5. Actualizar `docs/pages/lineamientos_editoriales.md` con checklist legal para publicaciones territoriales.

## Cierre

El proyecto muestra avances en interoperabilidad geoespacial (STAC), pero no tiene aun un esquema explicito para distinguir y documentar el estatus catastral/legal de la informacion territorial en terminos de la Ley 26.209.
