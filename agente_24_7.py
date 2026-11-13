from email.message import EmailMessage
import os
import smtplib
from google import genai
from google.genai import types

# 1. Cargar variables de entorno
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")

# 2. Definir el prompt de prospección comercial para Jorge y James
prompt = """
Actúen como Jorge y James, Directores Comerciales de GYAI. Su misión es realizar una investigación comercial basada en su conocimiento general para identificar empresas y sectores clave tanto en el mercado hispano (Latinoamérica y España) como en el mercado anglosajón (Estados Unidos, Reino Unido, Canadá) que sean prospectos ideales para implementar agentes de Inteligencia Artificial (automatización de atención al cliente, ventas, soporte técnico y operaciones).

Para cada mercado (Hispano e Inglés), seleccionen al menos 5 tipos de empresas o casos de estudio representativos (10 en total) que presenten señales claras de crecimiento, alto volumen de atención al cliente o necesidad de escalar sus procesos operativos.

El reporte completo debe estar redactado íntegramente en español, con un tono ejecutivo, estratégico y listo para acción comercial, incluyendo para cada caso:
1. Sector y tipo de empresa / perfil de cliente objetivo.
2. País / Mercado al que pertenece.
3. Por qué es un prospecto ideal para GYAI (dolor operativo detectado o oportunidad de automatización con IA).
4. Propuesta de valor específica (qué agente de IA ofrecerles exactamente).
5. Estrategia de acercamiento recomendada para Jorge y James (canal ideal, perfil del tomador de decisiones a contactar y ángulo del mensaje inicial).

Finalicen el reporte con un resumen ejecutivo de prioridades para la jornada de hoy.
"""

# 3. Inicializar el cliente de Gemini y ejecutar la consulta (sin herramientas externas)
client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=0.4,
    ),
)

reporte = response.text

# 4. Configurar y enviar el correo electrónico mediante Gmail (SMTP SSL)
destinatario = "yanixamalave6@gmail.com"

msg = EmailMessage()
msg["Subject"] = "Reporte Diario de Prospección Comercial - GYAI (Jorge & James)"
msg["From"] = EMAIL_USER
msg["To"] = destinatario
msg.set_content(
    "Hola,\n\n"
    "Adjunto en el cuerpo de este correo encontrarás el reporte diario de prospección comercial generado por Jorge y James:\n\n"
    "------------------------------------------------------------\n\n"
    f"{reporte}\n\n"
    "------------------------------------------------------------\n"
    "Enviado automáticamente por Agente 24/7 - GYAI Systems."
)

try:
  with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL_USER, EMAIL_PASS)
    server.send_message(msg)
  print("Reporte comercial generado y enviado exitosamente a yanixamalave6@gmail.com")
except Exception as e:
  print(f"Error al enviar el correo: {e}")
