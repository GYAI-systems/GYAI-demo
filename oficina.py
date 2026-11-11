import streamlit as st

st.set_page_config(page_title="Oficina Virtual GYAI", page_icon="🤖", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #0B132B; color: #FFFFFF; }
.oficina-box {
    background-color: #1C2541;
    border: 2px solid #00F5D4;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
}
.pasillo-logo {
    background: linear-gradient(180deg, #1C2541 0%, #0B132B 100%);
    border-left: 2px dashed #7B2CBF;
    border-right: 2px dashed #7B2CBF;
    padding: 30px 10px;
    text-align: center;
    height: 100%;
}
</style>
""", unsafe_allow_html=True)

col_jorge, col_pasillo, col_james = st.columns([2, 1.2, 2])

with col_jorge:
    st.markdown("""
    <div class='oficina-box'>
        <h3>🤖 JORGE GYAI</h3>
        <p style='color:#00F5D4;'>● TRABAJANDO - MERCADO LATINO</p>
        <p><b>Escritorio 01:</b> Prospección España y Latam</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.info("📋 Tarea actual: Buscando clínicas y estudios contables.")
    if st.button("✅ Aprobar mensajes de Jorge", use_container_width=True):
        st.success("¡Mensajes de Jorge aprobados y listos!")

with col_pasillo:
    st.markdown("""
    <div class='pasillo-logo'>
        <h1 style='color:#00F5D4; font-size: 38px; margin-bottom:0;'>GYAI</h1>
        <p style='color:#9D4EDD; font-size: 12px; letter-spacing: 2px;'>GROWTH & YIELD AI</p>
        <hr style='border-color:#3A506B;'>
        <p style='font-size: 13px;'>🏢 PASILLO CENTRAL</p>
        <p style='color:#00F5D4; font-size: 12px;'>2 Secretarios Activos</p>
    </div>
    """, unsafe_allow_html=True)

with col_james:
    st.markdown("""
    <div class='oficina-box'>
        <h3>🤖 JAMES GYAI</h3>
        <p style='color:#00F5D4;'>● TRABAJANDO - MERCADO INGLÉS</p>
        <p><b>Escritorio 02:</b> Prospección EE. UU. y Global</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.info("📋 Tarea actual: Buscando empresas de limpieza en Miami.")
    if st.button("✅ Aprobar mensajes de James", use_container_width=True):
        st.success("¡Mensajes de James aprobados y listos!")

st.divider()
st.subheader("📥 Buzón 'Te Toca' (Supervisión de Directora)")
orden = st.text_input("Dar nueva orden rápida a Jorge o James:")
if st.button("Enviar orden a la oficina"):
    if orden:
        st.toast(f"Orden enviada a los secretarios: {orden}")
      
