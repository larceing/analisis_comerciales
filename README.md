# Informe_Clientes · Prioridad comercial sin saturar
Contenido

📊 Informe_Clientes.pbix (Power BI)

📁 customers.xlsx, reps.xlsx, sales.xlsx (datos de ejemplo)

🐍 generate_powerbi_seed.py (opcional para regenerar Excel)

📝 README.md

# Requisitos

💻 Power BI Desktop

🐍 Python 3.10+ si quieres generar los Excel (pandas, numpy)

# Uso rápido

⬇️ Descarga o clona el repo

▶️ Abre Informe_Clientes.pbix

🔧 Ve a Transformar datos → Power Query

🛠️ Parámetro de Power Query: usa un único parámetro (p. ej. UNIDAD_ARCHIVOS) para la carpeta que contiene customers.xlsx, reps.xlsx, sales.xlsx.

🧭 Dónde cambiarlo: Inicio → Administrar parámetros → Editar parámetros → establece UNIDAD_ARCHIVOS a tu carpeta local.

🔁 Ventaja: todas las consultas leen la ruta desde UNIDAD_ARCHIVOS; no hay que editar cada origen.

▶️ Pasos:

Abre Informe_Clientes.pbix.

Ve a Transformar datos.

Editar parámetros → define UNIDAD_ARCHIVOS.

Cerrar y aplicar.

✅ Cerrar y aplicar

🎚️ Ajusta MinDays / MaxDays y usa filtros de rep, ciudad/ZIP y fechas

# Qué incluye el informe

🔗 Modelo simple: customers ↔ sales y reps ↔ customers

🧭 Flags: Saturado, Desatendido, Saludable basados en recencia

🎯 KPIs y mapa para decidir dónde actuar sin saturar

🕹️ Parámetros de días para una ventana de acción dinámica

# Regenerar datos (opcional)

▶️ Ejecuta generate_powerbi_seed.py para crear/sobrescribir customers.xlsx, reps.xlsx, sales.xlsx

🧩 Si cambias esquemas, actualiza las consultas en Power Query

# Personalización

🛠️ Sustituye los Excel por tus orígenes reales

⚙️ Revisa relaciones del modelo

🎚️ Ajusta umbrales y medidas a tu negocio

# Datos

📎 Los Excel son sintéticos y se usan solo para demostración

# Contacto

📧 luiscontacto3@gmail.com

💼 LinkedIn (mensaje directo)


# Descargo de responsabilidad

⚠️ Este proyecto se ofrece “tal cual”, sin garantías de ningún tipo.

🧪 Es material demostrativo/educativo; los datos son sintéticos.

🛠️ Úsalo bajo tu responsabilidad: valida cálculos antes de tomar decisiones.

🔒 El tratamiento de datos reales, privacidad y seguridad depende de ti.

🗂️ Cambiar rutas/parámetros puede romper el modelo; haz copias de seguridad.

💥 No asumo responsabilidad por pérdidas, daños o costes derivados del uso.

📨 Soporte best-effort, sin SLA ni compromiso de mantenimiento.
