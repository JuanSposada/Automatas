# ENTREGA 🎯
Este archivo contiene las funcionalidades hasta el momento 
de nuestro programa evaluador de archivos JSON,
ademas plantea las posibles actualizaciones, ademas las proyecciones
y alcances del proyecto.

## ¿Que hace nuestro programa? ⚙️
Nuestro Programa hasta el momento, realiza las siguientes tareas:

* Lee un archivo JSON externo. 
* Realiza una lista de cada uno de los caracteres
  asignandoles su respectivo token en valor unicode.
* Evalua si es un archivo JSON valido 
  verificando que el primer token es ```{```, si no es asi
  se detiene y manda un mensaje indicandolo.
* Verifica si las dobles comillas iniciales tienen su respectivo cierre,
  si no es asi, manda una alerta.
* Verfica si un elemento es 'string' y le asigna el token ```200```.
* Verifica si un elemento es un valor numerico y
  si es entero le asigna el token ```201```,
  si es flotante le asigna el ```202```.
* Verifica si un elemento cumple con el formato de tipo 'date'
  y le asigna el token ```203```. 

## ¿Que hace falta? 📝
Actualmente el programa continua en desarrollo, por lo cual es necesario
incluir las siguiente funcionalidades:

* Evaluar que el formato tipo date sea un formato valido.
* Validar que lo elementos de tipo flotante, solo pueden
  contener un solo punto.
* Evaluar si tambien se encuentra una llave ```}``` de cierre.
* Validar que despues de ```:``` debe de continuar con un elemento
  de tipo string, numerico, arreglo u objeto.
* Evaluar tipos de datos asignados por el programador.
* Designar validaciones especificas para caracterres especiales.
* Validador de espacios e identaciones dentro del archivo JSON.
* Formateador de sintaxis JSON mejorada


## Proyecciones y Alcance del proyecto 🚀
Este programa ha abarcado basicamente la perspectiva de un evaluador 
de archivos JSON de tipo lexico, sin embargo seria importante
ademas de interesante abarcar tambien el analisis sintactico y 
semantico.

Esto con el fin de que nuestro evaluador de archivos JSON
sea una especie de linter que nos ayudara con la creacion
y validacion de nuestros archivo JSON, ya que este tipo de formato
es ampliamente utilizado en una gran variedad de aplicaciones, por
lo cual seria de mucha ayuda una herramienta de este tipo.

Esperamos que en futuras actualizaciones de este programa logremos 
alcanzar esta meta. Para asi ofrecer una aplicacion de calidad
para todos los usuarios.

