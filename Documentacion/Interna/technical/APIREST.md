# API REST

Especificación de la API REST entre la lógica de negocio y el cliente *web*.

- Ruta: URL de acceso al recurso
- Petición: tipo de petición HTTP: GET, POST, PUT, DELETE, PATH
- Parámetros: Datos esperados. En la query o en el cuerpo. En principio, irán todos los datos en el cuerpo a excepción de los marcados con "param:" en la columna de Parámetros 
- Acción: Breve descripción
- Respuesta: Respuesta esperada y códigos de error.
- Descripción: Descripción extensa del recurso.

Los datos de las peticiones y las respuestas se envían principlamente en formato JSON.
El *token* se envía en la cabecera HTTP.

### Autenticación
| Ruta | Petición | Parámetros | Acción | Respuesta | Descripción |
|-|-|-|-|-|-|
| /api/auth/login | POST | JSON login | inicio de sesión | 200: session token. 401: Unauthorized. 400: Bad Request. 500: Internal Server Error. | Autenticación del usuario. |
| /api/auth/login | GET | JSON captcha | generar sesión | 200: session token. 400: Invalid captcha. 401: Unauthorized. 500: Internal Server Error. | Genera un token de sesión para los usuarios no autenticados después de verificar el captcha. |
| /api/auth/logout/ | POST | *token* | Cierra la sesión | 204: No Content. 400: Bad Request. 401: Unauthorized. 404: Not Found. | Cierra la sesión del usuario. |
| /api/users/register | POST | JSON register | Crea un usuario | 201: Created. 400: Bad Request. 409: Conflict. 500: Internal Server Error. | Crea un nuevo usuario pendiente de confirmación. |
| /api/auth/:userId/verifyId | POST | userId | Confirma un usuario | 200: OK. 400: Bad Request. 404: Not Found. 500: Internal Server Error. | Valida el correo electrónico. |
| /api/users/register | DELETE | *token*, JSON register | Desactiva/elimina un usuario | 204: No Content. 400: Bad Request. 404: Not Found. 500: Internal Server Error. | Desactiva/elimina el usuario. |
| /api/users/:usersId/export |  | GET | exportar usuarios | Códigos | Exporta toda la informaciín del ususario. |

### Chat
| Ruta | Petición | Parámetros | Acción | Respuesta | Descripción |
|-|-|-|-|-|-|
| /api/chats/:chatId | PATH | JSON text | pregunta al chat | 200: JSON response. 400: Bad Request. 500: Internal Server Error. | Envía la pregunta al chat y devuelve la respuesta. |
| /api/chats/:chatId | GET | JSON text | devuelve conversación completa | 200: JSON texts. 404: Not Found. 500: Internal Server Error. | Solicita y devuelve la conversación completa. |
| /api/chats/:chatId | DELETE | JSON text | Elimina la conversación | 200: JSON texts. 404: Not Found. 500: Internal Server Error. | Elimina una conversación específica. |
| /api/chats/:chatId | PUT | JSON text | Importa la conversación | 200: JSON texts. 400: Bad Request. 500: Internal Server Error. | Importa una conversación. |
| /api/conversation | GET | OK | Devuelve lista de conversaciones | 200: JSON conversations. 401: Unauthorized. 500: Internal Server Error. | Devuelve una lista con los títulos e identificadores de las conversaciones del usuario. |


## JSON especificación

Estructura de los JSON empleados en la comunicación

### JSON register
```
{
    "email": "example@domain.com",
    "password": "example"
}
```
### JSON text
```
{
    "model": "modelVersion"
    "text": "message"
}
```
### JSON texts
```
{
    "text": "message"
}
```
### JSON captcha
```
{
    "capthca": "example"
}
```
### JSON conversations
```
{
    {
        "conversation1": {
            "idChat": ""ID1
            "Título": "Título1"
            },
        "conversation2": {
            "idChat": ""ID2
            "Título": "Título2"
            },
        "conversation3": {
            "idChat": ""ID3
            "Título": "Título3"
            },
        ...
    }
}
```
