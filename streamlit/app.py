import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="CityClick",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inicialización del estado de la página
if 'page' not in st.session_state:
    st.session_state.page = 0

# Estilo de la página
page_bg_style = """
    <style>
        .st-emotion-cache-1dp5vir {
            background-image: none;
        }
        .st-emotion-cache-1avcm0n {
            background-color: #7fb927;
            color: white;
        }
        .stApp {
            background-color: white;
            color: #3d3d3b;
        }
        .css-1v3t7p8 {
            background-color: white;
        }
        /* Centrar los botones */
        .stButton>button {
            background-color: #7fb927; /* Color verde */
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            transition: background-color 0.3s ease; /* Para transiciones suaves */
        }
        /* Eliminar el color de fondo rojo cuando se pasa el mouse o se hace clic */
        .stButton>button:hover,
        .stButton>button:active {
            background-color: #3d3d3b; /* Mantener el mismo color verde al hacer hover o al hacer clic */
            outline: none;  /* Eliminar el contorno que aparece al hacer clic */
            color: white;
        }
        .stButton>button:focus {
            background-color: #3d3d3b;
            color: white;
            outline: none;
        }

        /* Estilo del botón seleccionado */
        .stButton>button.selected {
            background-color: #3d3d3b; /* Mantener el color después de hacer clic */
            color: white;
        }
        /* Asegurarse que los botones estén centrados */
        .stButton {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .st-emotion-cache-19rxjzo:focus:not(:active) {
            color: white;
        }
        /* Marco personalizado para texto */
        .custom-box {
            border: 2px solid #7fb927;
            border-radius: 5px;
            padding: 10px;
            background-color: #f9f9f9;
            color: #3d3d3b;
            font-size: 16px;
            text-align:center;
        }
        .arrow {
            font-size: 35px;
            color: #7fb927;
        }
        .line {
            border-top: 2px solid #3d3d3b;
            margin: 20px 0;
        }
    </style>
"""
st.markdown(page_bg_style, unsafe_allow_html=True)

# Imagen
st.image("titol.png", use_column_width=True)

# Columna para los botones
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Predefined"):
        st.session_state.page = 1

with col2:
    if st.button("Custom"):
        st.session_state.page = 2

st.markdown('<div class="line"></div>', unsafe_allow_html=True)

# Mostrar tabla cuando se pulsa Predefined
if st.session_state.page == 1:
    # Datos de las secuencias
    secuencias = {
        1: [("Tramit 1", "Tramit 2")],
        2: [("Tramit 1", "Tramit 2")],
        3: [("Tramit 1", "Tramit 2")],
        4: [("Tramit 1", "Tramit 2")],
        5: [("Tramit 1", "Tramit 2")],
        6: [("Tramit 1", "Tramit 2")],
        7: [("Tramit 1", "Tramit 2")],
        8: [("Tramit 1", "Tramit 2")],
        9: [("Tramit 1", "Tramit 2")],
        10: [("Tramit 1", "Tramit 2")],
    }

    # Crear una lista de secuencias
    secuencias_list = []
    for i in range(1, 11):
        secuencias_list.append([f"Secuencia {i}", " → ".join([trámite for tramo in secuencias[i] for trámite in tramo])])

    # Crear el dataframe
    df = pd.DataFrame(secuencias_list, columns=["Sequence ID", "Process"])

    # Mostrar la tabla sin la columna de índice
    st.markdown("<h3 style='text-align: center; color: #3d3d3b;'>Predefined sequences</h3>", unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True, height=300, hide_index=True)

    # Dropdown para seleccionar secuencia
    st.markdown("<h4 style='text-align: center; color: #3d3d3b;'>Select the sequence to study:</h3>", unsafe_allow_html=True)
    selected_sequence_id = st.selectbox("", [f"Secuencia {i}" for i in range(1, 11)])
    selected_sequence_process = " → ".join([trámite for tramo in secuencias[int(selected_sequence_id.split()[1])] for trámite in tramo])

    # Mostrar la secuencia seleccionada en una caja
    st.markdown("<h5 style='text-align: center; color: #3d3d3b;'>Selected sequence:</h3>", unsafe_allow_html=True)
    st.markdown(f'<div class="custom-box">{selected_sequence_process}</div>', unsafe_allow_html=True)

elif st.session_state.page == 2:
    st.write("Página 2")
