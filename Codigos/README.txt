Nuestro trabajo consiste en crear un modelo para administrar los autos de una concecionaria que trabaja con diferentes marcas y tipos.
El programa consta de 2 grillas, en una se muestran los vehiculos y en la otra las marcas, cada una con diferentes herramientas para
la mejor organizacion de los vehiculos de la concesionaria:

Si se selecciona la grilla "Vehiculos" se veran las siguiente opciones:

-Nuevo Vehiculo: Al clickear este boton se abrira un formulario el cual debe ser completado por el usuario en su totalidad, una vez 
completado el formulario correctamente se podra clickear el boton "Aceptar" para agregar un nuevo elemento con los datos del formulario 
en la base de datos.
En el formulario de agrego una opcion para agregar una nueva marca y un nuevo tipo, para el caso en que se ingrese un vehiculo con una marca
nueva.

-Editar Vehiculo: Para que este boton este activo, es necesario seleccionar un elemento de la grilla de vehiculos, al clickearlo
 se mostrara en pantalla el formulario con los datos del vehiculo seleccionado, donde se pueden modificar en el caso de querer cambiar 
alguno de los datos del vehiculo seleccionado, luego para confirmar los cambios se debe presionar el boton "Aceptar".

-Eliminar Vehiculo: Para que esta opcion este habilitada es necesario tener seleccionado un elemento de la grilla de vehiculos, luego de seleccionar un elemento y hacer click en el boton "Eliminar Vehiculo" surgira una ventana preguntandole al usuario si esta seguro de eliminar el elemento en caso de que haya sido un error debe presionar "cancelar", si esta seguro de eliminar el elemento debe presionar "Save", el vehiculo de eliminara de la base de datos y ya no se mostrara en la grilla dicho elemento.

-Filtro: Hay una barra de texto para buscar rapida y eficientemente un vehiculo, donde segun se vaya escribiendo el modelo en la grilla se iran
mostrando solo los vehiculos en que el modelo coincida con lo escrito.


Si el seleccionada la opcion "Marcas" se mostraran las siguientes funciones:

-Nueva Marca: Al clickear este boton emergera un formulario en el que se deben completar todos los campos, y luego presionar el boton aceptar
para que la marca sea agregada a la base de datos.

-Editar Marca: Se debe seleccionar una marca para que se habilite el boton "Editar Marca" donde aparecera el formulario con los datos de 
dicha marca, donde se podra modificar a voluntad los datos. 

-Eliminar Marca: Se debe seleccionar una marca en la grilla previamente para poder utilizar este boton, antes de eliminar una marca se
preguntara al usuario si esta seguro de eliminarla, si de verdad desea eliminarla debe hacer click en Save y la marca se eliminara y
desaparecera de la grilla.

-Filtro: En la barra de texto se puede ingresar el nombre de una marca para acceder mas rapido a la informacion de dicha marca.

*En el formulario para vehiculos en los campos "Peso" y "Rendimiento" solo se deben ingresar numeros.

**En los formularios(Marcas, Vehiculos y Tipos) todos los campos son obligatorios.

***No se puede eliminar una marca si existen vehiculos asociados a esa marca.

****Cada ventana emergente tiene un boton cancelar para el caso en que el usuario se equivoque o se arrepienta de realizar una accion.
