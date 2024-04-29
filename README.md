Vamos a crear una aplicación web a partir de un fichero JSON (puedes utilizar el mismo que empleaste en tu proyecto) con las siguientes características:

La aplicación debe tener una hoja de estilo. Para ello, lo mejor es que busques una plantilla HTML/CSS.
Las plantillas que uses en la aplicación se heredarán de la plantilla base.html(esta plantilla la puedes crear a partir de la plantilla HTML que has buscado).
La plantilla base tendrá al menos dos bloques: uno para indicar el título y otro para poner el contenido.
La página principal tendrá una imagen con el logotipo; al pulsar sobre esta imagen nos llevará a una página /xxxs.
La página /xxxsnos mostrará un buscador. Para ello, pon un formulario con un cuadro de texto donde puedas poner el nombre de un xxx que quieres buscar. Cuando presione el botón de buscar, envíe la información a la página /listaxxxs. El formulario envía los datos con el método POST.
En la página /listaxxxs(que solo se puede acceder por el método POST) aparecerán los xxxs cuyo nombre comenzará por la cadena que hemos añadido al formulario. Si no hemos indicado ninguna cadena, se mostrarán todos los xxxs.
La página /listaxxxsmostrará una tabla generada dinámicamente a partir de los datos de su fichero JSON y la búsqueda que se haya realizado.
La tabla tendrá al menos tres columnas: en la primera aparecerá el nombre, en la segunda otra información relevante y en la tercera habrá un enlace con la palabra “Detalle” que nos llevará a la página del xxx con la ruta /xxx/<identificador>o /xxx?id=xxxxxxxxxx.
Estamos utilizando el patrón de diseño: Lista - detalle. La lista está en la página /listaxxxy el detalle está en la página /xxx/<identificador>o /xxx?id=xxxxxxx, donde aparecerán todos los datos del xxx que tenga ese identificador. Si el identificador no existe, devolverá un 404. Tendrá un enlace que nos devuelve a la página /xxxs.
Debes una Plataforma como Servicio (PaaS) basada en la nube buscar de forma gratuita (Railway, Dokku, etc.) y desplegar tu aplicación en ella. Debes indicar el proceso de implementación.
Mejoras propuestas:
Realizar la búsqueda utilizando una sola ruta: Es decir, que en la página /xxxsesté el formulario de búsqueda y la lista de xxxs seleccionados. La información del formulario se enviará a la misma página. No existirá la página /listaxxxs.
Modifique el programa para que aparezca en el formulario la cadena que había introducido en la búsqueda.
Agregue otro criterio de búsqueda. Para buscar por ese segundo criterio, generarás dinámicamente una lista desplegable (elemento select) en el formulario con los valores de los xxx.
Programe la lista desplegable para que recuerde la opción elegida en la búsqueda.
Entrega:
La URL del repositorio GitHub donde ha desarrollado el programa. Recuerda que debes hacer el programa poco a poco y que los cambios los tienes que ir guardando con distintos commits.
La URL de la aplicación funcionando en la plataforma PaaS seleccionada.
Capturas de pantalla de las páginas de la aplicación desplegadas en la plataforma como servicio elegido donde se ven todos los elementos que se han solicitado.
Indica qué mejoras se han desarrollado.
