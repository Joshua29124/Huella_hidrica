
import streamlit as st

st.set_page_config(page_title="Calculadora de Huella Hídrica", page_icon="💧")

st.title("💧 Calculadora de Huella Hídrica vs Uso de IA")
st.write("Estima tu consumo de agua semanal y compáralo con el uso que haces de la inteligencia artificial.")

st.header("🚿 Actividades personales")
duchas = st.number_input("¿Cuántas duchas de 10 minutos tomas por semana?", min_value=0, value=7)
cafe = st.number_input("¿Cuántas tazas de café consumes por semana?", min_value=0, value=14)
hamburguesas = st.number_input("¿Cuántas hamburguesas consumes por semana?", min_value=0, value=2)
lavadora = st.number_input("¿Cuántas veces usas la lavadora por semana?", min_value=0, value=3)
sanitario = st.number_input("¿Cuántas veces usas el sanitario por semana?", min_value=0, value=35)

agua_personal = (
    duchas * 100 +
    cafe * 140 +
    hamburguesas * 2500 +
    lavadora * 150 +
    sanitario * 9
)

st.header("🤖 Actividades con IA")
chatgpt = st.number_input("¿Cuántas sesiones de ChatGPT de 30 prompts usas por semana?", min_value=0, value=5)
imagenes_ia = st.number_input("¿Cuántas imágenes generas con IA por semana?", min_value=0, value=2)
traducciones = st.number_input("¿Cuántas veces usas traducciones con IA por semana?", min_value=0, value=4)

agua_ia = (
    chatgpt * 0.5 +
    imagenes_ia * 2.5 +
    traducciones * 1
)

st.header("📊 Resultados")
st.metric("Huella hídrica semanal (hábitos personales)", f"{agua_personal} litros")
st.metric("Huella hídrica semanal (uso de IA)", f"{agua_ia:.2f} litros")

if agua_ia > agua_personal:
    st.error("🚨 Tu uso de IA representa una huella hídrica considerable. ¡Úsala con conciencia!")
else:
    st.success("✅ Tu uso de IA es menor que tu consumo diario habitual de agua.")
