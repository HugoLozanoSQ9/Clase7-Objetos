# Objetos dentro de python

La programación orientada a objetos tal cual es un paradigma, No es una característica que tengan los lenguajes
Es la forma en la que algunos lenguajes se basan para representar objetos de la vida real o "Entidades" (Entities)

Estas entidades también se le conocen como clases (en python), de hecho recordando un poco, cuando hacemos un type('algo') por defecto nos va a mostrar una clase (str, int, float etc...), para python todos los tipos de datos son entidades (clases), por eso tenemos métodos de string, o métodos de lista etc... 

En python todo tipo de datos es una clase

Se pueden crear los tipos de datos por que se pueden crear clases :D! y se realiza con la palabra resevada class

Por convección 

class: PascalCase
vars: snake_case
const: UPPER_SNAKE_CASE

## Entidades

Esto se refiere a conceptos que van a ser parte de nuestro código 
Estos conceptos pueden ser objetos de la vida real, por decir los carros
Pueden ser abstractos por decir una factura 
Los usuarios también serían una entidad
Los post también serían una entidad

Cada objeto va a tener propiedades 

Por decir: 
-Color 
-Modelo
-Marca
-Serial Number

## Métodos  (acciones)

Todas las aciones que se pueden hacer con esa entidad
-Pintar()
Por decir: pintar nos va a ayudar a cambiar la propiedad "Color", si el carro por defecto era azul, entonces con pintar podemos cambiar esa propiedad a algún argumento que le entreguemos a pintar por decir: ("Rojo")

Todo esto en base a que cada entidad es un objeto.

Vamos a pensar como nucleo los objetos, esto ayuda a que tengamos un orden, inicio o un final del objeto, por decir: 
-Vender()
El carro con el Serial number 123 con el método vender podríamos hacer el ejercicio de ya sea reducirlo del inventario o pasarlo directamente a el store de vendidos, o bien asignarle un nuevo dueño (todo esto a través de el nuevo método)

## Instancias

Cada uno de los objetos con diferentes valores 

Si tenemos una clase que es usuario  y en el nombre tiene el valor alfredo, entonces esta sería una instancia, si tengo otro usuario llamado francisco sería otra instancia

De hecho para eso tenemos el isinstance, tal cual el isinstance está preguntando si el valor es de la instancia "x" (la que queramos evaluar)

Para crear una instancia de algún método solo debemos escribir el método y abrimos y cerramos paréntesis

Cada que se crea una instancia se está ejecutando el método dunder __init__

Como conlución:
__init__ es la que nos va a permitir declarar los argumentos que van a formar parte de las propiedades de la clase
Si no se declara el método dunder init no van a poder declarar propiedades que varíen entre instancias



### Ejemplos

User:

-Name
-Last_name
-birth_date
-User_name
-Password
-E-mail
-ID

-Sing_in()
-Change_password()
-Confirm_email()
-ceate_post()
-Delete_post()

Articles:

-Content
-Created_dy
-Created
-Status
-Images

-Edit()
-Publish()
-Delete()
-Image()

Comments:

-Content
-Created_by
-Created
-Article
-Status

-Publish()
-Delete()


