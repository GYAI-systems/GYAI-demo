from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
import os
import smtplib
from google import genai
from google.genai import types

# 1. Configurar fecha actual exacta en hora de Perú (UTC-5)
peru_timezone = timezone(timedelta(hours=-5))
fecha_actual = datetime.now(peru_timezone).strftime("%d/%m/%Y")

# 2. Cargar variables de entorno
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")

# 3. Definir el prompt estructurado para Jorge y James
prompt = f"""
Actúen como Jorge y James, Directores Comerciales de GYAI. Fecha actual del reporte: {fecha_actual}. 
Su misión es generar una prospección comercial estratégica enfocada estrictamente en empresas medianas y negocios locales en expansión de cierre rápido (donde el dueño o gerente decide en 24 a 48 horas), ideales para conseguir clientes antes del lunes.

Debes generar el contenido utilizando etiquetas HTML de tabla (`<table>`, `<tr>`, `<th>`, `<td>`) para dos tablas separadas:
1. Tabla 1: Mercado Hispano (5 prospectos gestionados por Jorge - Latinoamérica y España).
2. Tabla 2: Mercado Inglés (5 prospectos gestionados por James - EE.UU., Reino Unido, Canadá).

Cada tabla debe tener exactamente estas 6 columnas en el orden indicado:
- Columna 1: Nombre de la empresa o perfil específico de negocio
- Columna 2: A quién contactar (cargo exacto del tomador de decisiones)
- Columna 3: Qué están comprando o invirtiendo actualmente
- Columna 4: Rubro y país
- Columna 5: Qué tipo de agente de IA anda necesitando exactamente
- Columna 6: Enlace directo a LinkedIn. Incluye un botón HTML con este formato exacto:
  <a href="https://www.linkedin.com/search/results/people/?keywords=CARGO%20RUBRO%20PAIS" target="_blank" style="background-color: #0a66c2; color: white; padding: 6px 10px; text-decoration: none; border-radius: 4px; display: inline-block; font-size: 11px; font-weight: bold;">Buscar en LinkedIn</a>
  (Reemplaza CARGO, RUBRO y PAIS con los términos clave reales de cada fila, usando %20 para los espacios).

Estructura tu respuesta incluyendo títulos claros ("### Mercado Hispano (Jorge)" y "### Mercado Inglés (James)") seguidos de sus respectivas tablas HTML limpias.
"""

# 4. Inicializar el cliente de Gemini y ejecutar la consulta (sin herramientas externas)
client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=0.4,
    ),
)

reporte_html_generado = response.text

# 5. Construir el correo con diseño HTML profesional tipo Excel (compatible con Android)
destinatario = "yanixamalave6@gmail.com"

msg = EmailMessage()
msg["Subject"] = (
    f"Reporte Comercial GYAI - Jorge y James ({fecha_actual})"
)
msg["From"] = EMAIL_USER
msg["To"] = destinatario

# Texto plano de respaldo
msg.set_content(
    f"Reporte Comercial GYAI - {fecha_actual}\n\nPor favor, visualiza este correo"
    " en un cliente compatible con HTML para ver las tablas de prospección y"
    " botones de LinkedIn."
)

# Cuerpo HTML enriquecido
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: Arial, sans-serif;
            color: #333333;
            background-color: #f4f6f9;
            margin: 0;
            padding: 10px;
        }}
        .email-container {{
            background-color: #ffffff;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            max-width: 800px;
            margin: 0 auto;
        }}
        h2 {{
            color: #107C41;
            font-size: 18px;
            border-bottom: 2px solid #107C41;
            padding-bottom: 6px;
            margin-top: 20px;
        }}
        p, li {{
            font-size: 13px;
            line-height: 1.4;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin-top: 10px;
            margin-bottom: 20px;
            font-size: 12px;
        }}
        th, td {{
            border: 1px solid #d0d0d0;
            text-align: left;
            padding: 8px;
            vertical-align: middle;
        }}
        th {{
            background-color: #107C41;
            color: #ffffff;
            font-weight: bold;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        .header-info {{
            background-color: #e8f5e9;
            padding: 10px;
            border-radius: 6px;
            margin-bottom: 15px;
            font-size: 13px;
        }}
        .footer {{
            font-size: 11px;
            color: #666666;
            text-align: center;
            margin-top: 20px;
            border-top: 1px solid #e0e0e0;
            padding-top: 10px;
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <h2 style="margin-top: 0; color: #0f5132;">📊 Reporte de Prospección Comercial GYAI</h2>
        <div class="header-info">
            <strong>Fecha:</strong> {fecha_actual} (Hora Perú)<br>
            <strong>Directores:</strong> Jorge (Hispano) & James (Inglés)<br>
            <strong>Enfoque:</strong> Cierre rápido 24-48h (Negocios en expansión)
        </div>
        
        {reporte_html_generado}
        
        <div class="footer">
            Enviado automáticamente por Agente 24/7 - GYAI Systems.
        </div>
    </div>
</body>
</html>
"""

msg.add_alternative(html_content, subtype="html")

# 6. Envío seguro mediante SMTP SSL de Gmail
try:
  with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL_USER, EMAIL_PASS)
    server.send_message(msg)
  print(
      "Reporte comercial en formato HTML enviado exitosamente a"
      " yanixamalave6@gmail.com"
  )
except Exception as e:
  print(f"Error al enviar el correo: {e}")
