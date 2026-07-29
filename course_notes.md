
## Python

## Definición

**Python** es un lenguaje de programación de alto nivel, interpretado y fácil de aprender. Se caracteriza por su sintaxis simple y legible.

## Usos

- Automatización

- Inteligencia artificial
    
- Ciencia de datos
    
- Desarrollo web
    
- Scripts
    

## Ejemplo

```python
print("Hola mundo")
```

 ## Curso dalto [[Python]] desde 0 (Completo)
 - [[Python]] es un lenguaje de programacion de alto nivel
 - Es leguaje interpretado
 - Es un lenguaje de tipado dinámico 
 - Es un lenguaje orientado a objetos
 -  Usa librerias (modulos)

 `#comentario`
 
## ==`#comentario`==:
Simplemente sirve para crear comentarios en el codigo y q no lo lea el interprete

## Tipos de datos
### Datos simples
#### String (texto
-  String (texto): Significa cadena q viene de cadena de texto, se pude usar con: 
	- "x", 'x': para escribir una linea.
	- """x""", '''x''': Permiten hacer salto de linea.
#### Numeros
##### int
- int (integer/enteros): Son variables de numero entero osea nuemeros sin decimales.
##### float
- float (flotante): Numeros con decimales.
#### Bool (boolean)
- Bool (Boolean): Es un tipo de dato que solo pude ser True o Flase sirve para representar decisiones o condiciones.
#### None
Represent q una variable no tiene ningun valor
Ejemplo:
```python
resultado = None
```
Se usa mucho para indicar que algo todavía no existe o no se ha calculado.

### Datos complejos

Los datos complejos son un tipo de datos q sirven para alamacenar varios datos simples o otros datos complejos pero basicamente sirve para agrupar datos.
#### lista
==lista==: es un dato complejo q sirve para agrupar datos
	`lista`: Lee todo el contenido de la lista
	`lista[n]`:Lee el elemento `n`de la lista.
	lista
	`lista[n] = <nombre>`: Modifica un elemento a la posicion q indiques.
#### tupla

==tupla==: Son igual a las listas pero con la diferencia q son inmodificables una vez creado se usa `()`para crearlo pero despues ya se usa las [] para lo demas.
Permite usar empaquetado:
t2 = "dato1", "dato2"
Tambien se pude hacer con un solo dato:
t3 = "dato",  
Es 'tuple' (sin la coma sería un 'str')

Función integrada tuple() (Convierte otros iterables): 
```python
t1 = tuple(["dato1", "dato2"]) # Convierte una lista en tupla
```
#### set (conjunto)
==set (conjunto)==:
- Elementos sin orden fijo
- No se puden duplicar conjuntos
- Se pude reconstruir pero no como en un lista con indices
##### frozenset():
- Es una versión inmutable de un `set`.
- Al igual que un conjunto, no tiene orden fijo y no permite elementos duplicados. 
- La diferencia es que una vez creado no se pueden añadir, eliminar ni modificar elementos.
##### .issubset()
Comprueba si un conjunto está contenido completamente dentro de otro conjunto.

Devuelve:

- `True` si todos sus elementos están dentro del otro conjunto.
- `False` si falta algún elemento.
##### .issuperset()
Comprueba si un conjunto contiene completamente a otro conjunto.

Devuelve:

- `True` si contiene todos los elementos del otro conjunto.
- `False` si no los contiene.
#### dict diccionario
==dict (diccionario)==: Es parecido a una lista pero en vez de usar un sistema de referenica por indice es personlizado. (y se usa {} y , para separar datos):
`key : value`
```python
diccionario = {

"nombre" : "Pablo",

"edad" : 16,

"esta_motivado" : True

}
```

##### .fromkeys()
`.fromkeys()` es un método de diccionarios que crea un diccionario con unas claves y les asigna el mismo valor. Si no se indica el valor, se usa `None`.


| Tipo               | Ordenado              | Índices    | Mutable |
| ------------------ | --------------------- | ---------- | ------- |
| Lista `list`       | Sí                    | Sí         | Sí      |
| Tupla `tuple`      | Sí                    | Sí         | No      |
| Conjunto `set`     | No                    | No         | Sí      |
| Diccionario `dict` | Sí (desde Python 3.7) | Por claves | Sí      |



### Otros
#### bytes
- bytes: Tipo de dato que almacena información binaria (datos en formato de bytes).
- Se usa principalmente en archivos, redes, criptografía y comunicación entre programas.
- No suele usarse al principio de Python.


### Desempaquetado (Unpacking)
El desempaquetado es una forma rápida de extraer los elementos de una lista o tupla y asignarlos a varias variables en una sola línea de código.

Regla principal:
La cantidad de variables a la izquierda debe ser exactamente igual a la cantidad de elementos a la derecha.

Ejemplo:
datos = ["Lucas", "Dalto", 1000000]

nombre, apellido, suscriptores = datos

print(suscriptores) # Muestra: 1000000

## Operadores

### Operadores arimeticos

| Operador | Q hace          |                                                             |
| -------- | --------------- | ----------------------------------------------------------- |
| `+`      | Suma            |                                                             |
| `-`      | Resta           |                                                             |
| `*`      | Multipliacion   |                                                             |
| `**`     | Exponente       |                                                             |
| `/`      | Division simple | El type siempre sera float.                                 |
| `//`     | Division int    | El type siempre dara un valor int redondeando (para abajo). |
| `%`      | Resto           | Muestra el resto de la division.                            |
|          |                 |                                                             |
### Operadores de comparacion

| Operad. | Q significa       |
| ------- | ----------------- |
| ==      | Igual que         |
| `!=`    | Diferente         |
| `<`     | Menor que         |
| `>`     | Mayor que         |
| `<=`    | Menor o igual que |
| `>=`    | Mayor igual que   |
|         |                   |

### Operadores logicos

#### and
`and` es un operador lógico que devuelve `True` únicamente si todas las condiciones que une son `True`. Si alguna condición es `False`, el resultado será `False`.
#### `or`
Es un operador lógico que devuelve `True` si **al menos una** de las condiciones es `True`. Si **todas** las condiciones son `False`, devuelve `False`.

#### `not`

Es un operador lógico que **invierte** el valor de una condición. Si la condición es `True`, devuelve `False`; y si es `False`, devuelve `True`.

## Metodo
Todos los metodos son funciones 
perono todas las funciones son metodos
pq los metodos son funciones especificas de objetos
### Estrucutra
Un metodo siempre usa esta estrucutra:
dato.metodo()

### dir 
Es una funciona que  basicamente te dice q puedes hacer con lo que contiene q metodos.s
### Metodos de cadena





### Metodos Strings (cadena de texto)
Convierten el valor:
#### .upper()
Convierte todo mayuscula.

#### .lower()
Convierte todo a minisculas. (el antonimo de upper)

#### .capitalize()
Convierte todo en miniscula y despues pone la primera letra en mayuscula.

Buscan un valor:
#### .find(`<x>`)
Busca la poscion de una cadena de texto dentro de otra cadena de texto.
(Si no encuntra esa cadena da -1)

#### .index(`<x>`)
Haze lo mismo q index PERO si no existe la cadena de texto q le pases en vez de dar -1 como find da una excepción (error).

Consultan si son numericos o alfanumericos:

#### .isnumeric()
Devulve True si todos los caracteres son numericos osino devulve False.
#### .isalpha()
Devuelve True cuando el string contiene puramente valores alpha (del Alphabet) osino devuelve False. (por ejemplo si tiene un espacio q es un caracter especial)

Cuentan numero de coincidencias:
#### .count()
Devulve el numero de veces de coincidencias q encontro. 
#### len()
Cuenta cuantos caracteres tiene una cadena.
NO es un metodo solo es una funcion.

Comienza/acaban con:

#### .startswith(`<x>`)
Comprueba si un string comienza con `<x>` cadena de texto si coinciden da `True` y si no `False`
#### .endswith(`<x>`)
Comprueba si un string acaba con `<x>` cadena de texto si coinciden da `True` y si no `False`

Otros:
#### .replace(x, y)
Busca en el string si existe x caracter en el string y si existe lo remplaza por x.

#### .split(`<x>`)
Convierte una cadena (`str`) en una lista (`list`) separándola por un delimitador.`<x>`.

### Metodos y funciones list
#### list()
Es una funcion q crea un lista.
#### len()
Se usa para contar los elementos de una lista
#### .append()
Agrega un elemento a una lista.
#### .insert(`<índice>`,`<elemento>`)
Agrega un elemento a un índice especifico.
#### `.extend([<lista>])`
Agrega **varios** elementos a una lista.
Se añade dentro de los () con type lista pero se añaden como diferentes elementos.

Eliminar elementos:
#### .pop(`<índice>`)
Elimina elementos de una lista a traves de índices.
Si pones `.pop()` sin poner ninguna indice se eliminara el ultimo elemento de la lista.
O índice -1 para el ultimo, -2 para el penultimo ...

#### .remove(`<elemento>`)
Elimina un `<elemento>` de una lista siplemente poniendo el nombre del `<elemento>`.
#### .clear()
Simplemte deja la lista vacia (no la elimina, la deja sin elementos).

Cambio de orden:
#### .sort()
Ordena una lista de ascendentemente por defecto, solo puede ordenar numeros y booleanos.
En orden ascendente primero pone a los False despues los True y ya despues todos los numeros descendentemente.
Si le puede añadir un propiedad de reverse:
lista.sort(reverse=True)
Y los ordena de forma descendente (de la manera contraria q dije antes).
#### .reverse()
Hace como la propiedad reverse de .sort() pero este es un metodo como tal q basicamente revierte el orden de los elementos de una lista.

.index(`<elemento>`)
Busca elemento en la lista (completos no como en string) y te da el indice de donde se encuentra y si no lo encunetra lanza una excepción.

### Metodos de diccionario

#### .keys()
Muestra las claves del diccionario.
#### .get(`<clave>`)
Devuelve el valor de la `<clave>` q le pasemos.
A diferencia del metodo tradicional de obtener valores de un diccionario este si no existe la calve no lanza una excepción.

.clear()
Elimina todos los elementos de la lista (la deja vacia pero existe).

#### .pop(`<elemento>`)
Elimina un elemento de la lista. Si quieres elimiar varios elementos los separas por una coma.

#### .items()
Devuelve todos los elementos del diccionario en forma de pares **(clave, valor)**.

Se usa sobre todo para recorrer un diccionario obteniendo la clave y el valor al mismo tiempo.

## Input
Es una funcion nativa (integrada) de [[Python]], qur sirve para q el medio de un programa el usuario puda introducir un dato.
(El output q da siempre es en string si necesitas trabajar un numero necesitaras hacer un int() )


## Funciones integradas

Las funciones integradas (built-in functions) son funciones que vienen incluidas en Python y se pueden usar directamente sin importar ninguna librería.

### Conversión de tipos

#### int()
Es una función integrada que convierte un valor a un número entero (`int`), siempre que sea posible.
#### float()
Es una función integrada que convierte un valor a un número decimal (`float`).

#### tuple()
Es una función integrada que convierte un objeto iterable (como una lista o un texto) a una tupla (tuple).

#### set()
Es una función integrada que convierte un objeto iterable (como una lista o un texto) a una set (conjunto).

#### dict()
Es una función integrada que convierte un objeto iterable de pares clave-valor (como una lista de tuplas) a un diccionario (`dict`).



### Conversión de tipos
- int()
- float()
- str()
- bool()

### Información
- type()
- len()
- dir()

### Matemáticas
- abs()
- round()
- min()
- max()
- sum()

### Iterables
- range()
- enumerate()
- zip()
- sorted()

### Entrada y salida
- print()
- input()
- open()
## Bucles
### For
Es un tipo de bucle que sirve para recorrer un objeto iterable elemento por elemento.
#### zip()
Es una funciona integrada de python q es muy util junto a for para iterar dos listas en un mismo for.

#### range()

Genera una secuencia de números. Se usa sobre todo con `for`.

```python
range(fin)
range(inicio, fin)
range(inicio, fin, paso)
```

- `fin`: No se incluye.
- `paso`: Por defecto es `1`.
#### enumerate()

Devuelve el índice y el valor de cada elemento de un iterable en for se usa para poder trabajar con el índice y el valor a la vez.
Se pude desenpaquetar en el mismo for con:

```python
for indice, valor in enumerate(variable):
	print(f"El indice es {indice} y el valor es {valor}.")
```
#### else
Los else dentro de los for sirven para comprobar si un for se a completado completo sin ningun `break` q seria el unico caso q no se ejecutaria.
#### continue
sirve para saltarse iteraciones.
#### break
sirve para romper toda la iteracion completa.

### while
Es un tipo de bucle de python se ejecuta siempre q sea True en cunato sea false se rompe y sigue el codigo.

Ejemplos de iterables:
- list
- tuple 
- set
- dict
- str
- range()
