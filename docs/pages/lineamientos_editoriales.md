# Lineamientos editoriales

Este documento define una estructura comun para publicar y mantener contenidos en la IDE FCyT.

## Objetivos

- Mejorar la consistencia entre paginas.
- Facilitar la busqueda y lectura de informacion.
- Asegurar que cada proyecto publique metadatos minimos.

## Estructura recomendada de una pagina de proyecto

1. **Titulo del proyecto**
2. **Ficha breve** (autores, institucion, ubicacion, periodo)
3. **Resumen**
4. **Metodologia / datos utilizados**
5. **Resultados** (mapas, tablas, indicadores)
6. **Recursos asociados** (articulos, presentaciones, visores, scripts)
7. **Metadatos** (tabla de campos normalizados)

## Plantilla sugerida

```markdown
# Titulo del proyecto
---

**Autores:**
**Institucion:**
**Ubicacion geografica:**
**Ano / periodo:**

---

## Resumen

Breve descripcion del problema, objetivo y alcance.

## Metodologia

- Fuentes de datos:
- Escala / resolucion:
- Procesamiento principal:

## Resultados

- Resultado 1:
- Resultado 2:

## Recursos asociados

- [Visor o mapa web]()
- [Articulo o informe]()
- [Codigo o script]()

## Metadatos

| Campo | Valor |
|---|---|
| Tema | |
| Tipo de proyecto | |
| Palabras clave | |
| Licencia | |
| Fecha de actualizacion | |
```

## Criterios de redaccion

- Usar espanol claro y tecnico, con frases cortas.
- Mantener un solo estilo de titulos por nivel (`#`, `##`, `###`).
- Evitar mezclar estilos HTML complejos cuando Markdown alcanza.
- Priorizar enlaces relativos para archivos del repositorio.
- Incluir texto alternativo descriptivo en imagenes.

## Criterios de medios y enlaces

- Imagenes locales: guardar en `docs/images/`.
- Evitar hotlink directo a imagenes externas cuando sea posible.
- Verificar que iframes y videos sean responsivos.
- Revisar enlaces rotos al menos una vez por cuatrimestre.

## Campos minimos para homogeneizacion

Para que una pagina sea considerada completa, debe incluir:

- resumen,
- al menos un recurso verificable (mapa, informe o codigo),
- tabla de metadatos,
- fecha o periodo del trabajo,
- autores e institucion.
