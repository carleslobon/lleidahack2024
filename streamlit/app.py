import streamlit as st
import pandas as pd
from predict_action import ActionsPredictor
import streamlit.components.v1 as components

st.set_page_config(page_title="CityClick", layout="centered", initial_sidebar_state="collapsed")

tramites = ["Trámite 1", "Trámite 2", "Trámite 3", "Trámite 4", "Trámite 5",
            "Trámite 6", "Trámite 7", "Trámite 8", "Trámite 9", "Trámite 10"]
acciones = ["AFIT", "AFST", "PFST"]

if 'page' not in st.session_state:
    st.session_state.page = 0
if 'secuencia_predefinida' not in st.session_state:
    st.session_state.secuencia_predefinida = []
if 'secuencia_custom' not in st.session_state:
    st.session_state.secuencia_custom = []

# CSS para diseño
page_bg_style = """
<style>
.st-emotion-cache-1dp5vir {background-image: none;}
.st-emotion-cache-1avcm0n {background-color: #7fb927;color: white;}
.stApp {background-color: white;color: #3d3d3b;}
.css-1v3t7p8 {background-color: white;}
.stButton>button {
    background-color: #7fb927;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 16px;
    transition: background-color 0.3s ease;
}
.stButton>button:hover,.stButton>button:active {
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
.st-emotion-cache-19rxjzo:focus:not(:active) {color: white;}
.custom-box {
    border: 2px solid #7fb927;
    border-radius: 5px;
    padding: 10px;
    background-color: #f9f9f9;
    color: #3d3d3b;
    font-size: 16px;
    text-align: center;
    font-weight: bold;
    margin-bottom: 50px;
}
.arrow {font-size: 35px;color: #7fb927;}
.line {border-top: 2px solid #3d3d3b;margin: 20px 0;}
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
        1: [["Certificats del padró d'habitants. Expedició automàtica", "AFST"], ["Sol·licitud genèrica", "AFIT"]],
        2: [["Consulta de parcel·les d'IBI rústic", "AFIT"]],
        3: [["Multes de circulació (consulta de fotografies, identificació de conductors, interposició d'al·legacions o recursos, petició o aportació de proves)", "AFIT"], ["Consulta de fotografies de multes per infraccions", "AFIT"]],
        4: [["Padró d'Habitants: gestions d'alta, canvi de domicili, sol·licitud de certificats i altres gestions relacionades", "AFIT"], ["Sol·licitar certificats d'empadronament", "AFIT"]],
        5: [["Certificats del padró d'habitants. Expedició automàtica", "PFST"], ["Certificats del padró d'habitants. Expedició automàtica", "AFIT"], ["Cessió de dades personals al Padró Municipal d'Habitants", "AFIT"], ["Cessió de dades personals al Padró Municipal d'Habitants", "AFST"]],
    }

    secuencias_list = []
    for i in range(1, len(secuencias) + 1):
        secuencia_formateada = " → ".join([f"({tramite}, {accion})" for tramite, accion in secuencias[i]])
        secuencias_list.append([f"Secuencia {i}", secuencia_formateada])
    df = pd.DataFrame(secuencias_list, columns=["Sequence ID", "Process"])

    st.markdown("<h3 style='text-align: center; color: #3d3d3b;  font-weight: bold;'>Predefined sequences</h3>", unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True, height=300, hide_index=True)
    st.markdown("<h5 style='text-align: center; color: #3d3d3b;'>Select the sequence to study:</h3>", unsafe_allow_html=True)

    selected_sequence_id = st.selectbox("", [f"Secuencia {i}" for i in range(1, len(secuencias) + 1)])
    selected_sequence_process = " → ".join([f"({tramite}, {accion})" for tramite, accion in secuencias[int(selected_sequence_id.split()[1])]])

    st.markdown("<h5 style='text-align: center; color: #3d3d3b;'>Selected sequence:</h3>", unsafe_allow_html=True)
    st.markdown(f'<div class="custom-box">{selected_sequence_process}</div>', unsafe_allow_html=True)

    st.session_state.secuencia_predefinida = secuencias[int(selected_sequence_id.split()[1])]

    if st.button("Calculate"):
        result = ActionsPredictor().predict_action(st.session_state.secuencia_predefinida)
        if result:
            st.write(result)
        else:
            st.warning("A process couldn't be found. Try again.")
else:
    st.markdown("<h3 style='text-align: center; color: #3d3d3b; font-weight: bold;'>Create your custom sequence</h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: #3d3d3b;'>Search and select a process</h3>", unsafe_allow_html=True)
    tramite_busqueda = st.text_input("Search for a trámite", "")
    tramite_seleccionado = tramite_busqueda

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
        st.session_state.secuencia_custom.append((tramite_seleccionado, accion_seleccionada))

    if st.session_state.secuencia_custom:
        sequence_text = " → ".join([f"({tramite}, {accion})" for tramite, accion in st.session_state.secuencia_custom])
        st.markdown(f'<div class="sequence-box">{sequence_text}</div>', unsafe_allow_html=True)

        if st.button("Calculate"):
            result = ActionsPredictor().predict_action(st.session_state.secuencia_custom)
            if result:
                st.write(result)
            else:
                st.warning("A process couldn't be found. Try again.")
    else:
        st.markdown('<div class="empty-sequence">No processes added yet.</div>', unsafe_allow_html=True)