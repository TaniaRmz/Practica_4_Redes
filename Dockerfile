#Dockerfile

#Imagen base a usar para la construcción de la imagen a trabajar
#Es una imagen Python 2.7 basada en Alpine Linux
FROM python:2.7.17-alpine

#Se instalan los módulos de python que se requieran
#RUN pip install nombre_modulo

#Copia el archivo clientHTTP.py que se encuentra en el mismo directorio que el archivo Dockerfile al directorio /opt/ dentro de la imagen
ADD clientHTTP.py /opt/
