1. **Configuración inicial**

Debemos disponer de una versión de python superior a la 3.4 en nuestro equipo para poder trabajar con entornos virtuales a través de venv
Documentación a [entornos virtuales](https://python.land/virtual-environments/virtualenv) de Python

2. **Configuración entorno virtual**

Para poder usar el entorno virtual del proyecto debemos hacer lo siguiente desde la consola y estando en la raíz del proyecto introducimos el siguiente comando **source ./3.11.2/bin/activate**, para activar el entorno virtual y sus dependencias

- si introducimos en la consola deactivate dejaremos de usar el entorno de python virtual


3. **Configuración de credenciales**
Para poder hacer uso de este script se deben seguir los siguientes pasos.
Es un script desarrollado en python, este script forma parte de una colección de scripts que son llamados a través del fichero main.py.

**NOTA:** Debemos obtener la siguiente información

- [ ] environment = ITG (default)
- [ ] login = usuario en sonarqube (Required)
- [ ] password = contraseña en sonarqube (Required)
- [ ] token = token sonarqube (Required)


4. **Ejecución**
Ya podríamos ejecutar el script de la siguiente manera:

`python main.py -e <entorno> -l <login> -p <password> -t <token>`

5. **Funcionamiento del Script**

> Extrae los datos por:
> - Portfolio (Division)
> - Aplicación
> - Projecto
> 
> Extiende la infromación de Portfolio, y Aplicación para obtener los projectos/applicaciones asignadas.
> 
> Compara los datos obtenidos al principio, que son los totales con los projectos/applicaciones asignadas.
