# Blog personal
En este repositorio se encuentra el código correspondiente a un blog que creé a modo de proyecto para aprender sobre **Django, Bootstrap y HTML.** También utilicé **Ionicons** para mejorar el aspecto del blog. Es una web responsive.

Para correrlo localmente, ejecutar (en personal_blog, donde se encuentra el archivo manage.py):
```
python manage.py runserver 
```
y dirigirse a http://127.0.0.1:8000/

## Dependencias
- crispy-forms
```
pip install django-crispy-forms
```
- crispy-bootstrap5
```
pip install crispy-bootstrap5
```
- tinymce
```
pip install django-tinymce
```

## Posteos
Los posteos se realizan desde la página admin provista por Django, donde cuenta con un RTE (Rich Text Editor) (TinyMCE) integrado para postear. En el index se muestran todos los posts, y en la seccion Featured se muestran sólamente aquellos posts que fueron marcados como featured al crearlos.

En la vista detallada de cada post se cuenta con la posibilidad de likear el post y comentarlo. Tanto los posts como los comentarios pueden ser eliminados (sólamente por aquel que los creó).

## Users
El blog cuenta con un sistema de usuarios. El usuario se registra, y luego se loggea para poder comentar y likear posts.

## TODO:
- [ ] Landing page en caso de registro inválido.
- [ ] Sistema de posteo para cualquier usuario registrado
- [ ] Respuestas a comentarios
- [ ] RTE para comentarios
