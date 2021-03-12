![chupalasiu](https://user-images.githubusercontent.com/36340014/110862472-46406100-829e-11eb-9d1b-faed900322b4.png)

> El año es 2021.
> 
> En un mundo universitario estríctamente online, tiránicos y arcaicos sistemas de inscripción arrasan a su paso, llevándose de víctima a cualquiera que se atreva -- que siquiera *piense* en inscribirse a una materia.
> 
> En una distopía tan arraiga, pocas son las mentes que conservan esperanza por un sistema de inscripción. En silencio, se anhela una herramienta de disrupción masiva - una tán poderosa que podría acabar con la maldición que es presionar F5 cada quince minutos para revisar la lista de cupos, para que no haya nada.
> 
> En una noche de bronca dirigida exclusivemente a estas convenciones arcaicas, un universitario hizo lo imposible.
>
>¿El nombre de aquella herramienta? **CHUPALA SIU**.

#### ChupalaSIU es un *web scraper* creado en Python que hace el proceso de inscripción de materias más soportable.

Esta herramienta permite escaneár de una lista de materias/comisiones las cuales el alumn@ esté interesado en inscribirse, y automágicamente revisarlas con poca interacción del usuario. No más presionar F5 para revisar si se añadieron más cupos. ¡*Opcionalmente*, también se puede mandar un correo electrónico cuando haya cupos disponibles en una materia asignada, o si se crearon nuevas comisiones!

# [Descargá el script](https://github.com/despedite/chupala-siu/archive/main.zip) | [¿Cómo se usa?](https://github.com/despedite/chupala-siu/wiki/Instalaci%C3%B3n)

### Instrucciones básicas (para el universitario apurado):

- [Conseguí Python](https://www.python.org/downloads/). [Instalá las dependencias que te pida](https://packaging.python.org/tutorials/installing-packages/).
- Descargá un Webdriver, dependiendo del navegador que tengas. ([Chrome](https://sites.google.com/a/chromium.org/chromedriver/home)|[Firefox](https://github.com/mozilla/geckodriver/releases))
- Abrí `siu.py` en un editor de texto, y de "VARIABLES A MODIFICAR" para abajo, editá las variables necesarias.

(Si no sos familiar con Python, [visitá la guia completa.](https://github.com/despedite/chupala-siu/wiki/Instalaci%C3%B3n))

---

### Preguntas frecuentes:

#### ¡El código es demasiado rápido y me tira errores!
Es posible que se pase la velocidad un poco, y trate de escribir en un campo antes de que se haya cargado la página. Volvé a correr el comando `python siu.py (DNI)` y se suele arreglar solo. Si tenés una mala conexión de Internet, metete al script y subí el valor de la variable cooldown (en segundos).

#### No me funciona en la versión de mi universidad de SIU Guaraní.
El código fue exclusivamente pensado en mente con la versión de SIU Guaraní que utiliza la Universidad Nacional de Quilmes. El soporte para otros SIUs es experimental... *porque no tengo forma de probarlo.* Si te das maña con Python y encontrás fixes para tu versión específica, ¡por favor commitealos a este repo! Así podemos usarlo todos.

#### ¿Podés añadir XYZ?
Si tiene que ver con inscripciones, ¿probablemente no? Es un periodo muy corto en el cual tengo para probar si todo anda bien... es decir, *las fechas de inscripción en mi universidad.* Si tuviese algún tipo de acceso fuera de hora, talvez.

Si no tiene que ver con eso (digamos, soporte para inscripción a materias, cosas que no necesiten testeo, etecé), ¡sentite libre de crear un Issue! O pasame cambios en código para añadir. Eso me haría la vida más fácil.

#### ¿Puedo cerrar Python/el navegador mientras corre?
Mmmm... *no.* Corre usando Selenium, que simula ser un usuario haciendo operaciones en un sitio web por código. Requiere que haya una ventana de navegador activa, lamentablemente.

#### ¿Porqué se llama... *así*?
Me parece graciosa la idea que una persona que trabaja en SIU se encuentre con este programa y discuta maneras de eliminar vulnerabilidades, y para ejemplizar su descubrimiento tenga que referir a este pedazo de código que encontró en la internet llamado "...Chupala... SIU".

#### Sos un groso. ¿Te puedo comprar una cerveza?
Vos sos más groso. Pero si insistís, [prefiero cafes.](https://ko-fi.com/retobot)

(Ahora en serio - ¡si te gustó, compartilo con alguien que le pueda llegar a servir!)

#### Hola, soy José SIU Guaraní y vengo a pedirte que elimines todo, maestro.
Uh-oh.
