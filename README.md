# iCLean


# *Object_detector*

En la carpeta Object_detector podrás encontrar todo lo correspondiente al código en python de nuestro detector de objeto,
dentro de la carpeta Yolov3 falta el yoloweights pero en el mismo hay un readme para ver como instalarlo. 
Para ejecutarlo através de spyder lo único que tendrás que hacer es descargar la carpeta ponerla en spyder y ejecutar el
main.py,siempre y cuando anteriormente ya hayas descargado el yoloweights, necesitaras tener descargado las librerias opencv
y numpy para poder ejecutar el proyecto.

Este código está calibrada con nuestra cámara puede ser que haya diferencias en el tamaño del objeto con respecto al que nos
sale en nuestras simulaciones.

# *Arm Function*

En esta carpeta se encuentra el archivo Python que lleva la simulacion de las posiciones del brazo segun los angulos deseados, todo esta en un unico archivo. 
Para su ejecucción son necesarias las librerias mplot3d (from mpl_toolkits), numpy, math, matplotlib.pyplot, matplotlib.patches

# *Path Planning*

En la carpeta de path planning se encuentran los dos algoritmos, el A* y el PRM.

- A*: Simulación que require de PyGame.
- PRM: Requiere shapely.

# *3D Simulation*

"Unity"
Dins de la carpeta Unity tenim el Codi de la Simulació on robem la part per editar el projecte i per altra part trobem l'executable de la simulació, per executar la simulació hem de clickar a "Robotica_nuevaversion.exe".

"Funcionament simulació Unity:"
Amb les fletxes es mou i gira el robot. (Davant, enrere, dreta, esquerra)
El braç té 2 posicions, amb la "w" puja el braç i amb la "s" baixa el braç.
Quan tenim un objecte a la posició de la pinça presionem "e" i agafa l'objecte, si tornem a pitjar "e" aleshores la pinça deixa l'objecte.
Per agafar un objecte i guardar-lo dins el robot anirem on es troba l'objecte, l'agafarem "e" i "w" per pujar-lo amb el braç, un cop és a dalt fem "e" i després "s", si el braç no és abaix el robot no es mourà cap endavant ni enrere per seguretat.
