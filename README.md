# Blog personal
### Usando Django y Bootstrap
En este repositorio se encuentra el código correspondiente a un blog que creé a modo de proyecto para aprender sobre Django, Bootstrap y HTML.

## Dependencias
- crispy-forms
- crispy-bootstrap4
- tinymce

## Posteos
Los posteos se realizan desde la página admin provista por Django, donde cuenta con un RTE (Rich Text Editor) integrado para postear. En el index se muestran todos los posts, y en la seccion Featured se muestran sólamente aquellos posts que fueron marcados como featured al crearlos.

En la vista detallada de cada post se cuenta con la posibilidad de likear el post y comentarlo. Tanto los posts como los comentarios pueden ser eliminados (sólamente por aquel que los creó).

## Users
El blog cuenta con un sistema de usuarios. El usuario se registra, y luego se loggea para poder comentar y likear posts.

## TODO:
- [] Landing page en caso de registro inválido.
- [] Sistema de posteo para cualquier usuario registrado
- [] Respuestas a comentarios
- [] RTE para comentarios
