# PsicologoVirtual

PsicologoVirtual es una aplicación web innovadora basada en Django que utiliza modelos de inteligencia artificial avanzados para proporcionar asistencia psicológica virtual. La aplicación emplea el modelo LLaMA 3 de Meta y varias APIs de Replicate para ofrecer una experiencia interactiva y personalizada.

## Descripción

PsicologoVirtual permite a los usuarios interactuar con un asistente de IA especializado en psicología. La aplicación puede comunicarse en múltiples idiomas, procesar entrada de voz, generar respuestas de texto a voz, y mantener un contexto de conversación para cada usuario.

### Características principales:

- Interfaz de chat interactiva
- Procesamiento de lenguaje natural basado en LLaMA 3
- Detección automática de idioma
- Conversión de voz a texto y texto a voz
- Memoria de conversación para cada usuario
- Soporte para múltiples idiomas
- Generación de resúmenes de sesión

## Capturas de pantalla

<table>
  <tr>
    <td>![image](https://github.com/user-attachments/assets/7d9315e2-5ceb-451f-b0f3-f4b4c82a3db4)</td>
    <td>![image]<(https://github.com/user-attachments/assets/fec01567-6160-4ebf-ba42-32d7d72a355b)></td>
  </tr>
</table>


## Modelos de IA utilizados

PsicologoVirtual utiliza los siguientes modelos de IA a través de la API de Replicate:

1. **LLaMA 3 (meta/meta-llama-3.1-405b-instruct)**: Modelo principal para el procesamiento de lenguaje natural y generación de respuestas.
2. **Whisper (vaibhavs10/incredibly-fast-whisper)**: Utilizado para la conversión de voz a texto.
3. **XTTS v2 (lucataco/xtts-v2)**: Empleado para la síntesis de voz a partir de texto.

## Requisitos

- Python 3.8+
- Django 3.2+
- Acceso a la API de Replicate

## Configuración

1. Clona este repositorio:
   ```
   git clone https://github.com/your_username/PsicologoVirtual.git
   ```
2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
3. Configura las variables de entorno, incluyendo tu token de API de Replicate.
4. Ejecuta las migraciones de Django:
   ```
   python manage.py migrate
   ```
5. Inicia el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

## Uso

1. Accede a la aplicación a través de tu navegador web.
2. Inicia una nueva conversación o continúa una existente.
3. Escribe o habla para interactuar con el asistente de IA.
4. Utiliza las funciones de voz a texto o texto a voz según sea necesario.
5. Al finalizar, puedes generar un resumen de la sesión.

## Licencia

Este proyecto se ha creado de manera Open-Source bajo la licencia GPL (Licencia Pública General de GNU). Esto significa que puedes copiar, modificar y distribuir el código, siempre y cuando mantengas la misma licencia y hagas público cualquier cambio que realices.

## Soporte

Si tienes algún problema o duda con respecto a PsicologoVirtual, no dudes en abrir un issue en este repositorio. Estoy aquí para ayudar y mejorar continuamente este recurso para la comunidad.

Por favor, ten en cuenta que este proyecto se mantiene con la intención de ser un recurso útil y profesional. Cualquier contribución o sugerencia para mejorar es siempre bienvenida.

## Créditos

- Este proyecto ha sido desarrollado por Diego Martínez Fernández (@Dgmtnz)
- Basado en el modelo LLaMA 3 de Meta
- Utiliza APIs de Replicate para funcionalidades adicionales de IA

Gracias por utilizar PsicologoVirtual. Esperamos que esta herramienta sea útil para proporcionar apoyo psicológico accesible y personalizado.
