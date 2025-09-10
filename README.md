Informe_Clientes · Prioridad comercial sin saturar

Este repositorio contiene un informe de Power BI y un script de Python para generar datos de ejemplo. El objetivo es mostrar cómo priorizar zonas/clientes en función de su recencia de compra y evitar la saturación comercial.

Contenido

Informe_Clientes.pbix – Informe en Power BI Desktop.

customers.xlsx, reps.xlsx, sales.xlsx – Datos de ejemplo.

generate_powerbi_seed.py – Script opcional para (re)generar los ficheros Excel.

README.md – Este documento.

Requisitos

Power BI Desktop (cualquier versión reciente).

Python 3.9+ (solo si quieres regenerar los Excel).

Librerías: pandas, numpy (instalación abajo).

Cómo usarlo (rápido)

Descarga o clona el repositorio.

Abre Informe_Clientes.pbix en Power BI Desktop.

Ve a Transformar datos → Power Query y cambia la ruta de origen de cada consulta:

Selecciona la consulta (customers, reps, sales) → icono del engranaje en Fuente → apunta al archivo .xlsx de tu carpeta local.

Cerrar y aplicar.

Ajusta los deslizadores (MinDays / MaxDays) y los filtros (rep, ciudad, fechas) para ver cómo cambian las prioridades.

Si aparece un aviso de permisos de origen, ve a Archivo → Opciones y configuración → Orígenes de datos y edita/elimina permisos para volver a aceptar la ubicación local.

Regenerar los datos (opcional)

Si prefieres crear nuevos datos sintéticos:

# (opcional) crear y activar entorno virtual
# python -m venv .venv
# .venv\Scripts\activate  (Windows)   |   source .venv/bin/activate (macOS/Linux)

pip install pandas numpy
python generate_powerbi_seed.py


El script sobrescribe/crea customers.xlsx, reps.xlsx, sales.xlsx en la carpeta del repo.

¿Qué contiene el informe?

Modelo simple con tres tablas: customers, reps, sales.

Cálculos de recencia y banderas de estado (Saturado, Desatendido, Saludable).

Parámetros MinDays/MaxDays para ajustar la ventana de acción.

KPIs y un mapa para decidir dónde actuar y a quién contactar según el contexto (representante, ciudad/ZIP, periodo).

Puedes adaptar las medidas y las reglas a tu negocio. La idea es que el informe sea didáctico y fácil de trasladar a datos reales.

Personalización recomendada

Sustituye los Excel por tus tablas reales (mismos campos o ajusta en Power Query).

Revisa relaciones customers → sales y reps → customers.

Ajusta umbrales en los deslizadores y las reglas de negocio de las medidas.

Datos

Los ficheros .xlsx son sintéticos y sirven únicamente para demostración.

Contacto

Cualquier duda o sugerencia: luiscontacto3@gmail.com

También puedes escribirme por LinkedIn.
