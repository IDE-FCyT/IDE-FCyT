# Normativas Nacionales - Resolucion 792/2014 (Observatorio de Transporte)

## Base analizada

- `docs/Observatorio_Transporte_Resolucion_792_2014.txt`

## Desfases / incumplimientos detectados

1. **No hay alineacion normativa explicita del portal con la Resolucion 792/2014**  
   Base: Art. 1 y 2 (creacion del Programa y lineamientos generales).  
   Evidencia: no se detectan referencias a `Resolucion 792/2014` ni al `Programa Observatorio Nacional de Transporte` en la documentacion operativa del proyecto.

2. **No existe implementacion documentada de una red de nodos con roles y flujo de informacion**  
   Base: Art. 3, Art. 4, Anexo I y Anexo II (red de nodos + nodo central + competencias).  
   Evidencia: el proyecto no publica estructura de nodos, responsables por nodo, ni mecanismos de coordinacion tecnica equivalentes.

3. **No hay evidencia de clasificacion formal de informacion publica/sensible por dataset**  
   Base: Anexo II, punto 1 (clasificar informacion de caracter publica y sensible).  
   Evidencia: en `docs/catalog/*.json` no se detecta etiquetado o politica de sensibilidad/criticidad de datos.

4. **No se evidencia procedimiento institucional para asegurar fiabilidad, calidad y actualizacion periodica**  
   Base: Anexo II, punto 2 (asegurar fiabilidad, calidad y actualizacion periodica).  
   Evidencia: no hay politica de QA/QC ni periodicidad de actualizacion formal publicada para catalogo y capas.

5. **No hay trazabilidad de indicadores y estadisticas oficiales con esquema de actualizacion y comparabilidad**  
   Base: Anexo I, componente Estadistica del Transporte (indicadores globales/especificos y actualizacion).  
   Evidencia: el portal no publica un modulo institucional de indicadores/series con metodologia y frecuencia definida.

6. **No se detecta componente formal de normativa consolidada (digesto) ni repositorio normativo estructurado**  
   Base: Anexo I, componente Normativa de Transporte (digesto actualizado y accesible).  
   Evidencia: hay documentos sueltos en `docs/`, pero no un digesto normativo estructurado con politica de mantenimiento.

7. **No se evidencia politica tecnica transversal de software libre con controles de seguridad de datos**  
   Base: Anexo II, punto 5 (desarrollo con software libre garantizando proteccion, integridad, confidencialidad, accesibilidad, interoperabilidad y compatibilidad).  
   Evidencia: hay uso puntual de herramientas libres, pero no politica institucional formal ni controles documentados sobre esas garantias.

8. **No hay plan de capacitacion tecnica institucional para equipos de gestion de geodatos**  
   Base: Art. 3 y Anexo II, punto 4.h (capacitacion de nodos/equipos).  
   Evidencia: no se publica un programa de capacitacion interno continuo con contenidos, frecuencia y responsables.

## Nota de alcance

La Resolucion 792/2014 fue emitida para un programa sectorial especifico del sistema de transporte.  
Los desfases consignados se registran como brechas de gobernanza, calidad y trazabilidad para un portal IDE academico que busca alineacion normativa.
