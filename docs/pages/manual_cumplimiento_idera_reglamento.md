# Manual de Cumplimiento IDERA (Parte 1)

## Alcance

Este documento releva el cumplimiento del proyecto frente al **Reglamento de Funcionamiento de IDERA (Noviembre 2025)**, separando:

1. **Exigencias textuales del reglamento**.

Fuente base:
- `docs/Reglamento_IDERA_Nov2025_usuario.txt`

## Trazabilidad por item no cumplido/parcial (solo exigencias textuales)

| Item evaluado | Estado en el proyecto | Fragmento textual verbatim | Por que tecnicamente no cumple (o cumple parcial) | Como lograr cumplir este objetivo |
|---|---|---|---|---|
| Disponibilidad publica de informacion geoespacial | Parcial | `Difusión: Se promoverá que los datos geoespaciales y sus metadatos estén disponibles` | El portal publica recursos, pero no todos los datasets tienen nivel de disponibilidad y acceso declarado en metadatos estandarizados. | Definir un campo obligatorio por dataset (`acceso`, `estado_publicacion`, `url_descarga`) y validar su presencia en todas las colecciones STAC. |
| Datos + metadatos disponibles | Parcial | `datos geoespaciales y sus metadatos estén disponibles` | Hay metadatos, pero son heterogeneos: estructura desigual, campos faltantes y calidad inconsistente entre colecciones. | Implementar un perfil minimo de metadatos obligatorio (plantilla unica) y una verificacion automatica de completitud antes de publicar. |
| Estandarizacion / interoperabilidad | Parcial | `Estandarización: Se impulsará el empleo de metodologías` ; `Promover el acceso, la difusión, el uso y la interoperabilidad` | Hay STAC, pero con inconsistencias tecnicas (IDs repetidos/no normalizados, enlaces heterogeneos), lo que reduce interoperabilidad. | Corregir unicidad y formato de IDs, normalizar enlaces/relaciones STAC y agregar validacion STAC en CI o checklist de publicacion. |
| Condiciones de acceso por productor | Parcial | `estando a cargo del productor de los datos` | No existe una politica transversal visible de condiciones de acceso/restriccion por dataset; solo licencias aisladas. | Publicar politica institucional de acceso y agregar campos por dataset (`condiciones_acceso`, `restricciones`, `justificacion`). |


## Conclusion de esta Parte 1

1. El reglamento respalda en forma **textual** los ejes de difusion, metadatos, acceso y estandarizacion.
2. Este documento conserva solo items con respaldo textual explicito en el reglamento.
3. La validacion semantica de clases/objetos geograficos corresponde a la etapa de normativas tecnicas especificas (no a este reglamento funcional).
