# Formulario de Alta de Objetos Geometricos IDERA


## A) Campos obligatorios IDERA

| Campo | Valor esperado (ejemplo)
|---|---|
| Tema IDERA | (Ej: Cobertura de la Tierra) | 
| Clase | (Ej: Vegetacion) | Obligatorio IDERA |
| Subclase | (Ej: Bosque nativo) | Obligatorio IDERA |
| Objeto geografico | (Ej: Bosque en galeria) |
| `codigo_subclase_idera` (4 digitos) | (Ej: 1234) |
| `codigo_objeto_idera` (6 digitos) | (Ej: 123456) |

> Nota: completar contra la version vigente del Catalogo de Objetos Geograficos IDERA.

---

## B) Metadatos secundarios opcionales (IDERA/recomendados)

| Campo | Valor esperado (ejemplo) |
|---|---|
| Tipo de geometria | (`Point`/`LineString`/`Polygon`, etc.) |
| Sistema de referencia (CRS) | (Ej: WGS84) |
| Código numérico que identifica un sistema de referencia de coordenadas (EPSG) | (Ej: 4326) |
| Extension geografica (`bbox`) | (xmin, ymin, xmax, ymax) |
| `acceso` | (`publico`/`restringido`/`interno`) |
| `estado_publicacion` | (`borrador`/`publicado`) |
| `url_descarga` | (URL directa al recurso) |
| Fuente de codificacion (archivo/version) | (Ej: `Catalogo_Objetos_Geograficos_IDERA_V2.2.xlsm`) |
| Palabras clave | (lista breve de terminos) |
| Licencia | (Ej: CC BY 4.0) |

---

## C) Datos opcionales de gestion interna IDE-FCyT

| Campo | Valor esperado (ejemplo) |
|---|---|
| ID interno de alta | (Codigo interno de tramite) |
| Fecha de solicitud | (dd/mm/aaaa) |
| Solicitante | (Nombre y apellido) |
| Area/Proyecto | (Ej: CeReGeo / Proyecto Humedales) |
| Responsable tecnico | (Nombre y apellido de supervisor/a) |
| Estado del alta | (`borrador`/`revision`/`aprobado`) |
| Revisor de metadatos | (Nombre y apellido) |
| Fecha de aprobacion | (dd/mm/aaaa) |
| Observaciones finales | (texto breve) |

---

## Checklist de validacion previa a publicacion
Esta sección del formulario debe ser completada por el/la responsable técnico/a del proyecto para validar que la información esté lista para publicarse.


### Validacion normativa y semantica
- [ ] Tema, Clase, Subclase y Objeto validados contra COG IDERA vigente.
- [ ] `codigo_subclase_idera` y `codigo_objeto_idera` verificados.
- [ ] No hay campos clasificados como "Obligatorio IDERA" vacios.

### Validacion tecnica (opcional recomendada)
- [ ] Geometrias validas y sin nulos.
- [ ] CRS/EPSG consistentes.
- [ ] Metadatos de acceso/licencia definidos si aplica.

### Validacion interna IDE-FCyT
- [ ] Responsable tecnico asignado.
- [ ] Estado de alta actualizado.
- [ ] Evidencia de revision archivada.

