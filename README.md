# ProyectoRobotica


*Object_detector*

En la carpeta Object_detector podrás encontrar todo lo correspondiente al código en python de nuestro detector de objeto,
dentro de la carpeta Yolov3 falta el yoloweights pero en el mismo hay un readme para ver como instalarlo. 
Para ejecutarlo através de spyder lo único que tendrás que hacer es descargar la carpeta ponerla en spyder y ejecutar el
main.py,siempre y cuando anteriormente ya hayas descargado el yoloweights, necesitaras tener descargado las librerias opencv
y numpy para poder ejecutar el proyecto.

Este código está calibrada con nuestra cámara puede ser que haya diferencias en el tamaño del objeto con respecto al que nos
sale en nuestras simulaciones.

*Arm Function*

En esta carpeta se encuentra el archivo Python que lleva la simulacion de las posiciones del brazo segun los angulos deseados, todo esta en un unico archivo. 
Para su ejecucción son necesarias las librerias mplot3d (from mpl_toolkits), numpy, math, matplotlib.pyplot, matplotlib.patches
