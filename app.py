import streamlit as st
import pandas as pd

st.set_page_config(page_title="GYAI | Fábrica de IA", page_icon="⚡", layout="wide")

st.title("⚡ GYAI — Fábrica de Sistemas de Inteligencia Artificial")
st.caption("Growth & Yield AI | Demo Interactivo de Automatización, Datos y Ventas")

tab1, tab2, tab3 = st.tabs([
    "🧹 1. Limpieza de Datos (Python)",
    "🧠 2. Cerebro Empresarial (RAG)",
    "💼 3. Agente Vendedor Autónomo"
])

with tab1:
    st.subheader("Motor de Saneamiento e Integridad de Datos")
    st.write("Transforma inventarios o reportes desordenados en datos listos para operar en segundos.")
    
    datos_sucios = pd.DataFrame({
        "SKU": ["prod-01 ", "PROD-01", "prod-02", " prod-03", "prod-04"],
        "Producto": ["Laptop Pro 15", "laptop pro 15", "Monitor 27 UHD", "Teclado Mecánico", None],
        "Precio_USD": ["$1,200.00", "1200", "350 usd", "85.50", "ERROR"],
        "Stock": ["15 uds", "15", "0", "42", "-5"]
    })
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**❌ Archivo Original del Cliente (Con errores):**")
        st.dataframe(datos_sucios, use_container_width=True)
        
    if st.button("⚡ Ejecutar Limpieza Automática GYAI"):
        datos_limpios = pd.DataFrame({
            "SKU": ["PROD-01", "PROD-02", "PROD-03"],
            "Producto": ["Laptop Pro 15", "Monitor 27 UHD", "Teclado Mecánico"],
            "Precio_USD": [1200.00, 350.00, 85.50],
            "Stock_Disponible": [15, 0, 42]
            "Estado_Auditoria": ["✅ Validado", "⚠️ Sin Stock", "✅ Validado"]
        })
        with col2:
            st.markdown("**✅ Datos Auditados y Listos (100% Integridad):**")
            st.dataframe(datos_limpios, use_container_width=True)
        st.success("Auditoría GYAI completada: 1 duplicado eliminado, 1 fila corrupta aislada y formatos estandarizados.")

with tab2:
    st.subheader("Consulta Instantánea sobre Documentos y Políticas (RAG)")
    st.write("Tus empleados o clientes preguntan y la IA responde usando solo la información oficial de tu empresa.")
    
    pregunta = st.selectbox("Selecciona una consulta de prueba:", [
        "¿Cuál es el tiempo de entrega para pedidos mayoristas en Lima?",
        "¿Qué descuento aplica por compras mayores a 10 unidades?",
        "¿Cuál es la política de garantía de equipos importados?"
    ])
    
    respuestas_rag = {
        "¿Cuál es el tiempo de entrega para pedidos mayoristas en Lima?": "📦 **Respuesta GYAI (Fuente: Manual Logístico 2026):** Los pedidos mayoristas confirmados antes de las 2:00 PM se entregan en **24 horas hiles** en Lima Metropolitana sin costo adicional.",
        "¿Qué descuento aplica por compras mayores a 10 unidades?": "💰 **Respuesta GYAI (Fuente: Tarifario Comercial):** Aplica un **12% de descuento corporativo** automático en pedidos de 10 a 25 unidades, y **18%** para compras superiores a 25 unidades.",
        "¿Cuál es la política de garantía de equipos importados?": "🛡️ **Respuesta GYAI (Fuente: Política Postventa):** Todos los equipos cuentan con **12 meses de garantía directa** con reemplazo inmediato en las primeras 72 horas por fallas de fábrica."
    }
    st.info(respuestas_rag[pregunta])

with tab3:
    st.subheader("Simulador de Vendedor Autónomo 24/7")
    st.write("Prueba cómo la IA de GYAI cotiza, verifica inventario y genera una orden de compra automáticamente.")
    
    producto_sel = st.selectbox("Cliente solicita:", [
        "Laptop Pro 15 ($1,200 USD)",
        "Teclado Mecánico ($85.50 USD)"
    ])
    cantidad = st.number_input("Cantidad solicitada:", min_value=1, max_value=20, value=5)
    
    if st.button("🤖 Generar Cotización y Orden"):
        precio = 1200.00 if "Laptop" in producto_sel else 85.50
        subtotal = precio * cantidad
        descuento = subtotal * 0.12 if cantidad >= 10 else 0.0
        total = subtotal - descuento
        
        st.markdown(f"""
        **🧾 Pre-Orden Generada Automáticamente por GYAI:**
        * **Producto:** {producto_sel}
        * **Cantidad:** {cantidad} unidades (Stock verificado ✅)
        * **Subtotal:** ${subtotal:,.2f} USD
        * **Descuento corporativo:** -${descuento:,.2f} USD
        * **Total a pagar:** **${total:,.2f} USD**
        * *Listo para emitir comprobante electrónico y link de pago.*
        """)
