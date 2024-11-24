import streamlit as st
import pandas as pd
#from .predict_action import ActionsPredictor

st.set_page_config(
    page_title="CityClick",
    layout="centered",
    initial_sidebar_state="collapsed"
)

tramites = [
    "Trámite 1", "Trámite 2", "Trámite 3", "Trámite 4", "Trámite 5",
    "Trámite 6", "Trámite 7", "Trámite 8", "Trámite 9", "Trámite 10"
]

acciones = ["AFIT", "AFST", "PFST"]

def add_tramite_to_secuencia(tramite, accion):
    st.session_state.secuencia.append((tramite, accion))  # Guardar como tupla

if 'page' not in st.session_state:
    st.session_state.page = 0

if 'secuencia' not in st.session_state:
    st.session_state.secuencia = []

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
        .stButton>button {
            background-color: #7fb927;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover,
        .stButton>button:active {
            background-color: #3d3d3b;
            outline: none;
            color: white;
        }
        .stButton>button:focus {
            background-color: #3d3d3b;
            color: white;
            outline: none;
        }
        .stButton {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .st-emotion-cache-19rxjzo:focus:not(:active) {
            color: white;
        }
        .custom-box {
            border: 2px solid #7fb927;
            border-radius: 5px;
            padding: 10px;
            background-color: #f9f9f9;
            color: #3d3d3b;
            font-size: 16px;
            text-align:center;
            font-weight: bold;
            margin-bottom: 50px;
        }
        .arrow {
            font-size: 35px;
            color: #7fb927;
        }
        .line {
            border-top: 2px solid #3d3d3b;
            margin: 20px 0;
        }
        .sequence-box {
            border: 2px solid #7fb927;
            border-radius: 8px;
            padding: 15px;
            background-color: #f9f9f9;
            color: #3d3d3b;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 50px;
        }
        .empty-sequence {
            color: #ff4c4c;
            font-size: 16px;
            text-align: center;
            margin-top: 20px;
            font-weight: normal;
            margin-bottom: 50px;
        }
    </style>
"""
st.markdown(page_bg_style, unsafe_allow_html=True)

st.image("titol.png", use_column_width=True)

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Predefined"):
        st.session_state.page = 1

with col2:
    if st.button("Custom"):
        st.session_state.page = 2

st.markdown('<div class="line"></div>', unsafe_allow_html=True)

if st.session_state.page == 1:
    secuencias = {
        1: [["Tramit 1", "AFST"], ["Tramit 2", "AFIT"]],
        2: [["Tramit 1", "AFST"], ["Tramit 2", "AFIT"]],
        3: [["Tramit 1", "AFST"], ["Tramit 2", "AFIT"]],
        4: [["Tramit 1", "AFST"], ["Tramit 2", "AFIT"]],
        5: [["Tramit 1", "AFST"], ["Tramit 2", "AFIT"]],
        6: [["Tramit 1", "AFST"], ["Tramit 2", "AFIT"]],
        7: [["Tramit 1", "AFST"], ["Tramit 2", "AFIT"]],
        8: [["Tramit 1", "AFST"], ["Tramit 2", "AFIT"]],
        9: [["Tramit 1", "AFST"], ["Tramit 2", "AFIT"]],
        10: [["Tramit 1", "AFST"], ["Tramit 2", "AFIT"]],
    }

    secuencias_list = []
    for i in range(1, len(secuencias) + 1):
        # Crear la cadena de texto con formato "(Tramit X, Acción)" y separarlas con "→"
        secuencia_formateada = " → ".join([f"({tramite}, {accion})" for tramite, accion in secuencias[i]])
        secuencias_list.append([f"Secuencia {i}", secuencia_formateada])

    df = pd.DataFrame(secuencias_list, columns=["Sequence ID", "Process"])

    st.markdown("<h3 style='text-align: center; color: #3d3d3b;  font-weight: bold;'>Predefined sequences</h3>", unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True, height=300, hide_index=True)

    st.markdown("<h5 style='text-align: center; color: #3d3d3b;'>Select the sequence to study:</h3>", unsafe_allow_html=True)
    selected_sequence_id = st.selectbox("", [f"Secuencia {i}" for i in range(1, len(secuencias) + 1)])

    # Aquí obtenemos el proceso seleccionado
    selected_sequence_process = " → ".join([f"({tramite}, {accion})" for tramite, accion in secuencias[int(selected_sequence_id.split()[1])]])

    # Mostrar la secuencia seleccionada
    st.markdown("<h5 style='text-align: center; color: #3d3d3b;'>Selected sequence:</h3>", unsafe_allow_html=True)
    st.markdown(f'<div class="custom-box">{selected_sequence_process}</div>', unsafe_allow_html=True)

    # Agregar la secuencia seleccionada a la sesión
    st.session_state.secuencia = secuencias[int(selected_sequence_id.split()[1])]

    st.write(st.session_state.secuencia)

    selected_sequence_process = " → ".join([trámite for tramo in secuencias[int(selected_sequence_id.split()[1])] for trámite in tramo])

    st.markdown("<h5 style='text-align: center; color: #3d3d3b;'>Selected sequence:</h3>", unsafe_allow_html=True)
    st.markdown(f'<div class="custom-box">{selected_sequence_process}</div>', unsafe_allow_html=True)
    
    if st.button("Calculate"):
        result = ActionsPredictor.calculate(st.session_state.secuencia)
        if result:
            st.success(f"¡Calculated correctly! The action is: **{result['accion']}**.")
            st.markdown(f"**Process details**:\n- **ID:** {result['id_tramite']}")
        else:
            st.warning("A process couldn't be found. Try again.")

elif st.session_state.page == 2:
    st.markdown("<h3 style='text-align: center; color: #3d3d3b; font-weight: bold;'>Create your custom sequence</h3>", unsafe_allow_html=True)
    
    st.markdown("<h5 style='text-align: center; color: #3d3d3b;'>Search and select a process</h3>", unsafe_allow_html=True)
    tramite_busqueda = st.text_input("Search for a trámite", "")

    tramite_seleccionado = "Search" # BORRAR
    # similares = []
    # if tramite_busqueda:
    #     try:
    #         similares = ActionsPredictor().find_similarities(tramite_busqueda)
    #     except Exception as e:
    #         st.error(f"Error calling find_similarities: {e}")

    # if similares:
    #     tramite_seleccionado = st.selectbox("Select the process you meant:", similares)
    # else:
    #     tramite_seleccionado = None
    #     st.warning("No similar process found. Please try another search.")
    
    st.markdown("<h5 style='text-align: center; color: #3d3d3b;'>Select an action</h3>", unsafe_allow_html=True)
    accion_seleccionada = st.selectbox("", acciones)

    if st.button("Add sequence"):
        add_tramite_to_secuencia(tramite_seleccionado, accion_seleccionada)

    st.write(st.session_state.secuencia)

    if st.session_state.secuencia:
        sequence_text = " → ".join([f"({tramite}, {accion})" for tramite, accion in st.session_state.secuencia])
        st.markdown(f'<div class="sequence-box">{sequence_text}</div>', unsafe_allow_html=True)
        if st.button("Calculate"):
            result = ActionsPredictor.calculate(st.session_state.secuencia)
            if result:
                st.success(f"¡Calculated correctly! The action is: **{result['accion']}**.")
                st.markdown(f"**Process details**:\n- **ID:** {result['id_tramite']}")
            else:
                st.warning("A process couldn't be found. Try again.")
    else:
        st.markdown('<div class="empty-sequence">No processes added yet.</div>', unsafe_allow_html=True)

