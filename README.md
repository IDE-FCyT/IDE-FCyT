# IDE-FCyT

Infraestructura de Datos Espaciales de la Facultad de Ciencia y Tecnología UADER

https://ide-fcyt.github.io/IDE-FCyT/

# EJECUTAR DE MANERA LOCAL

## Requisitos: Python 3.8+ y pip.

Crear entorno (opcional pero recomendado):

```
    python -m venv .venv

    # Activar: Windows -> .venv\Scripts\activate
    # Linux/Mac -> source .venv/bin/activate
```

Instalar MkDocs y el tema:

```
    pip install mkdocs mkdocs-material
```

Desde la raíz del repo (donde está mkdocs.yml):

```
    mkdocs serve
```

Abrí http://127.0.0.1:8000/IDE-FCyT/ (o la URL que te indique la consola) y tendrás recarga en caliente al editar archivos.

Compilar el sitio estático (si querés generar site/):

```
    mkdocs build
```

Publicar (opcional, si tenés permisos):

```
    mkdocs gh-deploy
```
