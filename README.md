# Practica_4_Redes
Pimero se debe ejecutar el archivo ayuda.py ya que ahí vienen las instrucciones de cómo se corre clientHTTP.py; para esto se debe poner en terminarl:
python ayuda.py

Por otro lado, aunque las instrucciones ya están en ayuda.py, también se mencionan a continuación:
Para ejecutar el archivo clientHTTP.py se debe ingresar lo siguiente en terminal:
python clientHTTP.py host http_method url user_agent encoding connection
donde:
host = dirección IP o nombre de dominio del servidor HTTP
  Ejemplo: www.fciencias.unam.mx
http_method = GET o HEAD
url = archivo o recurso solicitado al servidor web
  Ejemplo: / para el directorio raíz
user_agent = 1, 2, 3 o 4; dependiendo de el user-agent que se quiera utilizar de la siguiente lista
    1: Firefox
    2: Chrome
    3: Miscrosoft Edge
    4: Safari
encoding = Parámetro de la solicitud de la codificación de la respuesta
  Ejemplo: gzip, deflate o indetity
connection = forma del establecimiento de la conexión
  Ejemplo: keep-alive o close

EJEMPLO 

En la primer línea se ve un error en la ejecución ya que faltó especificar el atributo "url"
![Ejemplo1](https://github.com/TaniaRmz/Practica_4_Redes/assets/88344062/4a25c4ae-fd63-4a55-95c8-8eaa46a455bb)
En la úlitma línea se ve un ejemplo de cómo ejecutar correctamente el programa

A continuación, se muestra la salida de la instrucción anterior
![Ejemplo2](https://github.com/TaniaRmz/Practica_4_Redes/assets/88344062/0123d26c-f3c2-4147-aa4b-55a90d22a1f8)
Notemos que lo primero que muestra la terminal es "HTTP/1.1 200 OK" lo que indica que se estableció una conexión con el servidor HTTP

Al final, la terminal mostrará lo siguiente
![Ejemplo3](https://github.com/TaniaRmz/Practica_4_Redes/assets/88344062/db58d603-51c3-4bc0-bbc1-b7cf4968643e)
El mensaje "Conexión con el servidor finalizada" indica que la tarea a realizar concluyó

RESPUESTAS

1.1 HEAD: El método head regresa la información del encabezado de la respuesta, sin incluir el cuerpo. Se utiliza para obtener información sobre un recurso (por ejemplo, verificar la última fecha de modificación),
sin requerir detalles del mismo.

1.2 GET: Solicita recursos o información de un servidor web, la respuesta que devuelve el servidor generalmente es en forma de página web, archivo o datos.

1.3 POST: Su función principal es enviar datos al servidor para que sean procesados. Además, con este método es más seguro enviar datos confidenciales ya que no se muestran en la URL.

1.4 PUT: Su función principal es actualizar o crear un recurso en el servidor.

1.5 DELETE: Su función principal es eliminar un recurso específico del servidor web.


2 Categorías de códigos de estado que usa HTTP

  2.1 Informativos (1xx)
  
    Proporcionan información adicional sobre el proceso de la solicitud 
    
      Ejemplo: 100 (Continue)-> La solicitud ha sido recibida y el servidor esáa esperando la siguiente parte de la solicitud del cliente

      
  2.2 De Éxito (2xx)
  
    Indican si la conexión fue recibida, entendida y procesada con éxito por el servidor
    
      Ejemplo: 200 (OK)-> La solicitud se completó satisfactoriamente
      
                204 (No Content) -> La solicitud se completó satisfactoriamente pero no se devuelve el contenido en la respuesta

                
  2.3 De Redirección (3xx)
  
    Indican que el cliente debe realizar una acción adicional para completar la solicitud.
    
      Ejemplo:  300 (Moved Permanently)->  El recurso solicitado se ha movido permanentemente a una nueva ubicación.
      
                302 (Found) -> La solicitud se puede encontrar en una ubicación diferente temporalmente.

                
  2.4 De Error del Cliente (4xx)
  
    Indican que la solicitud del cliente contiene errores o no puede ser cumplida debido a problemas en el lado del cliente. 
    
      Ejemplo:  400 (Bad Request)-> La solicitud del cliente es incorrecta o está mal formada.
      
                404 (Not Found) -> El recurso solicitado no se encuentra en el servidor.

                
  2.5 De Error del Servidor (5xx)
  
    Indican que la solicitud del cliente es válida, pero el servidor no pudo cumplirla debido a un error en el lado del servidor
    
      Ejemplo:  500 (Internal Server Error)-> Se produce un error interno en el servidor que impide que se complete la solicitud.
      

3.1 El campo encoding se usa para indicar cómo se ha comprimido o codificado el cuerpo del mensaje.

3.2 El campo connection se usa para controlar la conexión entre el cliete y el servidor, y para identificar si la conexión debe mantenerse abierta o cerrarse después de alguna solicitud.
              
