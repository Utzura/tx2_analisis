import streamlit as st
from textblob import TextBlob
from deep_translator import GoogleTranslator

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Análisis de Texto",
    page_icon="💬",
    layout="centered"
)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    body {
        background-color: #101820; 
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .stTextInput>div>div>input, textarea {
        background-color: #181f29 !important;
        color: white !important;
        border-radius: 8px !important;
    }
    .stButton>button {
        background-color: #cf1020 !important;
        color: white !important;
        border-radius: 10px !important;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #a60d1a !important;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)


# --- TÍTULO ---
st.title("💬 Análisis de Texto con TextBlob")

st.markdown(
    "Esta aplicación permite analizar la **polaridad** y **subjetividad** de un texto, "
    "así como realizar una **corrección gramatical** en inglés."
)

# --- SIDEBAR ---
with st.sidebar:
    st.subheader("📘 Conceptos clave")
    st.markdown("""
    **Polaridad:**  
    Mide si el sentimiento es positivo, negativo o neutral.  
    Rango: `-1` (muy negativo) → `1` (muy positivo).

    **Subjetividad:**  
    Indica cuánto del texto es opinión o emoción.  
    Rango: `0` (objetivo) → `1` (muy subjetivo).
    """)

# --- EXPANDER 1: ANÁLISIS DE SENTIMIENTOS ---
with st.expander("🧠 Analizar Polaridad y Subjetividad en un texto"):
    text1 = st.text_area("✍️ Escribe aquí tu texto en español:")

    if text1:
        # Traducción al inglés con Deep Translator
        trans_text = GoogleTranslator(source="auto", target="en").translate(text1)

        # Análisis con TextBlob
        blob = TextBlob(trans_text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.markdown(f"**Polarity:** {polarity}")
        st.markdown(f"**Subjectivity:** {subjectivity}")

        # Interpretación de resultados
        if polarity >= 0.5:
            st.success("😊 El texto expresa un sentimiento **positivo**.")
        elif polarity <= -0.5:
            st.error("😔 El texto expresa un sentimiento **negativo**.")
        else:
            st.info("😐 El texto expresa un sentimiento **neutral**.")

        # Interacción pequeña
        if st.button("🔁 Traducir texto al inglés"):
            st.write("**Traducción automática:**")
            st.write(trans_text)


# --- EXPANDER 2: CORRECCIÓN EN INGLÉS ---
with st.expander("📝 Corrección ortográfica en inglés"):
    text2 = st.text_area("Escribe o pega un texto en inglés:", key="text_correction")

    if text2:
        blob2 = TextBlob(text2)
        corrected_text = str(blob2.correct())

        st.write("**Texto corregido:**")
        st.success(corrected_text)

        # Botón de comparación
        if st.button("👀 Mostrar comparación"):
            st.write("**Original:**")
            st.code(text2)
            st.write("**Corregido:**")
            st.code(corrected_text)
