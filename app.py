
import streamlit as st
import pandas as pd
import numpy as np
 
st.set_page_config(
    page_title="Componentes básicos de Streamlit",
    page_icon=":material/rocket_launch:",
    layout="wide"
)
 
st.title("🚀 Explorando Streamlit")
st.write("Catálogo básico de componentes organizados por categorías.")
 
########################################################
#################### Menú de navegación ################
########################################################
 
categoria = st.sidebar.selectbox(
    "Selecciona una categoría",
    [
        "Texto y contenido",
        "Datos y métricas",
        "Widgets",
        "Layouts",
        "Gráficos",
        "Mensajes y estado"
    ]
)
 
# --------------------------------------------------
# 1. TEXTO Y CONTENIDO
# --------------------------------------------------
if categoria == "Texto y contenido":
    st.header("1. Texto y contenido")
    
    st.title("st.title()")
    st.header("st.header()")
    st.subheader("st.subheader()")

    st.text("st.text(): texto plano")
    st.write("st.write(): permite mostrar diferentes tipos de contenido.")
    st.markdown("**st.markdown():** permite usar formato Markdown.")
    st.caption("st.caption(): texto pequeño o aclaraciones.")

    st.code("print('Hola Streamlit')", language="python")

    st.latex(r"E = mc^2")

 
# --------------------------------------------------
# 2. DATOS Y MÉTRICAS
# --------------------------------------------------
elif categoria == "Datos y métricas":
    st.header("2. Datos y métricas")
    
    df = pd.DataFrame({
        "Nombre": ["Ana", "Juan", "Laura", "Pedro"],
        "Edad": [25, 30, 28, 35],
        "Ventas": [120, 200, 150, 300]
    })
 
    st.subheader("DataFrame")
    st.dataframe(df)
 
    st.subheader("Tabla")
    st.table(df)
 
    st.subheader("Métricas")
    col1, col2, col3 = st.columns(3)
 
    col1.metric("Ventas", "770", "+15%")
    col2.metric("Clientes", "120", "+8%")
    col3.metric("Promedio", "192.5", "-2%")

 
# --------------------------------------------------
# 3. WIDGETS
# --------------------------------------------------
elif categoria == "Widgets":
    st.header("3. Widgets de entrada")
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", min_value=0, max_value=100)
 
    ciudad = st.selectbox(
        "Ciudad",
        ["Bogotá", "Medellín", "Cali","Caparrapí"]
    )
 
    intereses = st.multiselect(
        "Intereses",
        ["Python", "Machine Learning", "Data Engineering"]
    )
 
    nivel = st.slider("Nivel de experiencia", 1, 10, 5)
 
    acepta = st.checkbox("Acepto los términos")
 
    modalidad = st.radio(
        "Modalidad",
        ["Presencial", "Virtual", "Híbrida"]
    )
 
    comentario = st.text_area("Comentarios")
 
    if st.button("Enviar información"):
        st.success("¡Información enviada!")
        st.write({
            "nombre": nombre,
            "edad": edad,
            "ciudad": ciudad,
            "intereses": intereses,
            "nivel": nivel,
            "acepta": acepta,
            "modalidad": modalidad,
            "comentario": comentario
        })

 
# --------------------------------------------------
# 4. LAYOUTS
# --------------------------------------------------
elif categoria == "Layouts":
    st.header("4. Organización de la interfaz")
    
    st.subheader("Columnas")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("Columna 1")
        st.button("sisa") 

    # col1.info("Columna 1")
    col2.success("Columna 2")
    col3.warning("Columna 3")
 
    st.divider()
 
    st.subheader("Pestañas")
    tab1, tab2, tab3 = st.tabs(
        ["Información", "Datos", "Resultados"]
    )
 
    with tab1:
        st.write("Contenido de la pestaña Información.")
 
    with tab2:
        st.write("Contenido de la pestaña Datos.")
 
    with tab3:
        st.write("Contenido de la pestaña Resultados.")
 
    st.divider()
 
    st.subheader("Expander")
    with st.expander("Ver más información"):
        st.write("Este contenido aparece al expandir.")
 
    st.subheader("Container")
    with st.container(border=True):
        st.write("Contenido agrupado dentro de un container.")

    
# --------------------------------------------------
# 5. GRÁFICOS
# --------------------------------------------------
elif categoria == "Gráficos":
    st.header("5. Visualización de datos")

    df = pd.DataFrame(
        np.random.randint(10, 100, (10, 3)),
        columns=["Ventas", "Costos", "Utilidad"]
    )
 
    st.subheader("Gráfico de líneas")
    st.line_chart(df)
 
    st.subheader("Gráfico de barras")
    st.bar_chart(df)
 
    st.subheader("Gráfico de área")
    st.area_chart(df)


# --------------------------------------------------
# 6. MENSAJES Y ESTADO
# --------------------------------------------------
elif categoria == "Mensajes y estado":
    st.header("6. Mensajes y estado")

    st.success("Operación exitosa")
    st.info("Mensaje informativo")
    st.warning("Advertencia")
    st.error("Ha ocurrido un error")
 
    st.subheader("Barra de progreso")
    st.progress(70)
 
    st.subheader("Estado de sesión")
    if "contador" not in st.session_state:
        st.session_state.contador = 0
 
    if st.button("Incrementar contador"):
        st.session_state.contador += 1
 
    st.write("Contador:", st.session_state.contador)
