# Normativas Nacionales - Ley 27.275 (Derecho de Acceso a la Informacion Publica)

## Alcance del analisis

Este documento registra los incumplimientos y brechas del portal IDE-FCyT frente a la **Ley 27.275** (Derecho de Acceso a la Informacion Publica), con foco en obligaciones de transparencia activa y mecanismos de acceso.

Fuente normativa analizada: `docs/Ley_27275_Derecho_Acceso_Informacion_Publica.txt`.

## Nota de aplicabilidad

La ley alcanza a sujetos del articulo 7 (incluye universidades y entidades con fondos publicos, segun los supuestos del propio articulo).  
Este informe se centra en brechas de cumplimiento documental/publicacion observables en el repositorio.

## Matriz de incumplimientos principales

| Base legal | Exigencia | Evidencia en el proyecto | Estado | Incumplimiento / desfase |
|---|---|---|---|---|
| Art. 9, 10, 11 | Canal formal de solicitud, tramitacion y plazos de respuesta | Solo hay contacto general por correo en `docs/pages/contacto.md` | No cumple | No existe procedimiento formal de solicitud de informacion, ni constancia de tramite, ni plazos oficiales de respuesta |
| Art. 13, 14, 15 | Mecanismo de denegatoria fundada y vias de reclamo | No hay seccion de reclamos/denegatorias | No cumple | Falta circuito de reclamo administrativo/judicial informado al publico |
| Art. 30, 31 | Designacion de Responsable de Acceso a la Informacion Publica y funciones | En `docs/pages/acerca.md` hay equipo tecnico, pero no responsable legal de acceso | No cumple | No hay figura ni funciones publicadas de responsable de acceso |
| Art. 32 (caput) | Transparencia activa en sitio oficial, clara y reutilizable | Hay STAC y acceso a contenidos (`docs/pages/catalogo.md`, `docs/index.md`) | Parcial | Existe apertura de datos geoespaciales, pero no se cumple bloque completo de transparencia activa obligatoria |
| Art. 32.a | Indice de informacion publica + donde y como solicitar | No existe indice legal de informacion publica ni instructivo de solicitud | No cumple | Falta indice oficial orientado al derecho de acceso |
| Art. 32.b | Estructura organica y funciones | Informacion institucional general en `docs/pages/acerca.md` | Parcial | No hay organigrama/estructura organica formal ni funciones institucionales completas por area |
| Art. 32.c-d | Nomina de autoridades/personal y escalas salariales | No se publican nominas completas ni escalas salariales | No cumple | Ausencia total de publicacion requerida |
| Art. 32.e | Presupuesto y ejecucion trimestral | No se encuentra informacion presupuestaria | No cumple | Ausencia total de publicacion requerida |
| Art. 32.f-g | Transferencias, contrataciones, licitaciones, proveedores | No se encuentra seccion de compras/contrataciones | No cumple | Ausencia total de publicacion requerida |
| Art. 32.h-i | Actos/resoluciones, dictamenes, auditorias/evaluaciones | Se cita una resolucion de aprobacion en `docs/pages/acerca.md` | Parcial / No cumple | No hay repositorio sistematico de actos, dictamenes, auditorias ni evaluaciones |
| Art. 32.l-m | Mecanismos para peticiones y autoridad competente para solicitudes | Solo correo de contacto general en `docs/pages/contacto.md` | No cumple | No hay formulario, mesa de entradas digital ni autoridad de acceso identificada |
| Art. 32.n-o | Indice de tramites y canal para denuncias/solicitudes directas | No se detecta indice de tramites ni canal de denuncias | No cumple | Ausencia total de publicacion requerida |
| Art. 32.p-r | Guia de gestion documental + informacion frecuentemente solicitada | No se detecta guia de archivo documental ni FAQ de solicitudes frecuentes | No cumple | Ausencia total de publicacion requerida |
| Art. 32.s | Declaraciones juradas (si corresponde) | No se detecta seccion de DDJJ | No cumple | Ausencia total de publicacion requerida |

## Evidencia puntual del repositorio

### Lo que no se encontro (busqueda en `docs/` y `mkdocs.yml`)

No hay evidencia publicada de:

1. `responsable de acceso a la informacion publica`
2. `solicitud de informacion publica` (formulario/procedimiento/plazos)
3. `reclamo por denegatoria`
4. `indice de informacion publica` (en sentido legal del art. 32.a)
5. `presupuesto`, `ejecucion`, `contrataciones`, `auditorias`, `declaraciones juradas`

## Evaluacion de riesgo de cumplimiento

Riesgo **alto** por incumplimiento estructural de transparencia activa y ausencia de procedimiento formal de acceso a informacion publica, mas alla de la disponibilidad de contenidos tecnicos del portal.

## Acciones correctivas recomendadas

1. Crear una pagina oficial `Acceso a la informacion publica` con:
   - responsable designado,
   - correo y formulario,
   - plazos legales,
   - circuito de reclamo.
2. Publicar un **indice de informacion publica** (art. 32.a) y mapearlo a secciones del portal.
3. Incorporar modulo de transparencia activa (art. 32) con:
   - estructura/autoridades,
   - presupuesto/ejecucion,
   - contrataciones,
   - auditorias,
   - tramites,
   - datos de solicitudes frecuentes.
4. Agregar politica de proteccion/disociacion de datos personales para publicaciones de datasets.
5. Definir rutina de actualizacion (mensual/trimestral segun item) y responsable de mantenimiento.

## Cierre

El portal presenta una base tecnica valiosa en datos geoespaciales abiertos, pero actualmente no cumple en forma suficiente con las obligaciones de acceso a la informacion publica y transparencia activa exigibles por la Ley 27.275.
