# iClean

# Descripció del projecte
Descripció del projecte
És un robot amb un estil semblant a un camió de la brossa però amb 3 rodes en comptes de 4, una càmera i un sensor d’ultraso a la part  posterior  i un braç robòtic a la part dreta.  La funció del robot és netejar d’obstacles una àrea delimitada. Segons els tamany de l’objecte que es va trobant, el robot té una funció o una altra, hem dividit els tamanys  en 4 seccions: tamany molt petit, petit, mitjà i gran. En el cas que es trobi un objecte molt petit el robot li passarà per sobre (el xafa) suposant que és un insecte i no hauria d’estar a casa; En el cas que l’objecte no sigui tan petit el robot té l’ordre de posar-se al davant del objecte de manera que el pugui agafar amb les pinces del braç , un cop el té agafat el braç puja uns 130º i deixa l’objecte a la capsa buida que carrega sobre. En cas que l’objecte sigui mitjà el robot l’ha d’emputjar o apartar de manera que quedi fora de l’àrea delimitada. Per últim, quan es troba un objecte més gran de l’establert considerem que l’objecte és massa gran i no podem fer res, aleshores el robot l’esquiva i segueix en busca d’objectes dins de l’àrea.


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
