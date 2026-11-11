import streamlit as st
import base64

st.set_page_config(page_title="Sede Central GYAI", page_icon="🏢", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #060B19; color: #FFFFFF; }
.block-container { padding-top: 0.8rem; padding-bottom: 1rem; }
div[data-testid="stButton"] button {
    background-color: #0F172A;
    color: #00F5D4;
    border: 1.5px solid #00F5D4;
    border-radius: 10px;
    font-weight: bold;
    transition: 0.3s;
}
div[data-testid="stButton"] button:hover {
    background-color: #00F5D4;
    color: #060B19;
}
.panel-agente {
    background-color: #0F172A;
    border: 1px solid #38BDF8;
    border-radius: 12px;
    padding: 15px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

if "escritorio_activo" not in st.session_state:
    st.session_state.escritorio_activo = "Jorge GYAI"

try:
    with open("image_2b74a7b8.jpg", "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode()
    st.markdown(f"""
    <div style="position: relative; max-width: 750px; margin: auto; border-radius: 16px; overflow: hidden; border: 2px solid #00F5D4; box-shadow: 0 0 25px rgba(0, 245, 212, 0.25);">
        <img src="data:image/jpeg;base64,{img_base64}" style="width: 100%; display: block;">
        <div style="position: absolute; top: 12px; left: 12px; background: rgba(6,11,25,0.85); padding: 5px 12px; border-radius: 20px; border: 1px solid #10B981; font-size: 12px;">
            🟢 <b>JORGE GYAI:</b> En línea
        </div>
        <div style="position: absolute; top: 12px; right: 12px; background: rgba(6,11,25,0.85); padding: 5px 12px; border-radius: 20px; border: 1px solid #10B981; font-size: 12px;">
            🟢 <b>JAMES GYAI:</b> En línea
        </div>
    </div>
    """, unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("⚠️ No se encontró el archivo image_2b74a7b8.jpg en el repositorio.")

st.write("")

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🏢 Entrar Oficina JORGE", use_container_width=True):
        st.session_state.escritorio_activo = "Jorge GYAI"
with c2:
    if st.button("🌐 Pasillo Central GYAI", use_container_width=True):
        st.session_state.escritorio_activo = "Pasillo Central"
with c3:
    if st.button("🏢 Entrar Oficina JAMES", use_container_width=True):
        st.session_state.escritorio_activo = "James GYAI"

if st.session_state.escritorio_activo == "Jorge GYAI":
    st.markdown("""
    <div class="panel-agente">
        <h4 style="color:#00F5D4; margin:0;">💻 Escritorio 01: JORGE GYAI (Mercado Latino & España)</h4>
        <p style="font-size:13px; color:#CBD5E1; margin-top:5px;"><b>Rol:</b> Prospección en español, agendar demos y cierre en Perú, México, Colombia y España.</p>
        <p style="font-size:13px; color:#38BDF8;"><b>Actividad actual:</b> Preparando mensajes para clínicas dentales y estudios contables.</p>
    </div>
    """, unsafe_allow_html=True)
    orden_j = st.text_input("✍️ Dar orden directa a Jorge GYAI:", placeholder="Ej: Redacta un mensaje para una clínica dental en Madrid...")
    if st.button("🚀 Enviar orden a Jorge"):
        st.success(f"Jorge GYAI recibió la orden: '{orden_j}'. Listo para conectar motor IA.")

elif st.session_state.escritorio_activo == "James GYAI":
    st.markdown("""
    <div class="panel-agente">
        <h4 style="color:#A855F7; margin:0;">💻 Escritorio 02: JAMES GYAI (Mercado Inglés & Global)</h4>
        <p style="font-size:13px; color:#CBD5E1; margin-top:5px;"><b>Rol:</b> Prospección High-Ticket en EE. UU., Canadá y Europa para empresas de servicios.</p>
        <p style="font-size:13px; color:#E879F9;"><b>Actividad actual:</b> Escaneando empresas de limpieza e inmobiliarias en Miami y Texas.</p>
    </div>
    """, unsafe_allow_html=True)
    orden_ja = st.text_input("✍️ Dar orden directa a James GYAI:", placeholder="Ej: Write a pitch for a cleaning company in Miami...")
    if st.button("🚀 Enviar orden a James"):
        st.success(f"James GYAI recibió la orden: '{orden_ja}'. Listo para conectar motor IA.")

else:
    st.markdown("""
    <div class="panel-agente" style="border-color:#00F5D4;">
        <h4 style="color:#00F5D4; margin:0;">🏛️ Recepción & Pasillo Central — GYAI (Growth & Yield AI)</h4>
        <p style="font-size:13px; color:#CBD5E1; margin-top:5px;"><b>Estado de la Fábrica:</b> 2 Secretarios Activos | Simulador conectado: <code>gyai-demo.streamlit.app</code></p>
        <p style="font-size:13px; color:#10B981;"><b>Meta actual:</b> Concretar los primeros 3 clientes globales.</p>
    </div>
    """, unsafe_allow_html=True)
