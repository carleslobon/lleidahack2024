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
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("Predefined"):
        st.session_state.page = 1
with col2:
    if st.button("Custom"):
        st.session_state.page = 2
with col3:
    if st.button("About us"):
        st.session_state.page = 3

st.markdown('<div class="line"></div>', unsafe_allow_html=True)

if st.session_state.page == 1:
    secuencias = {
        1: [["Certificats del padró d'habitants. Expedició automàtica", "AFST"], ["Sol·licitud genèrica", "AFIT"]],
        2: [["Consulta de parcel·les d'IBI rústic", "AFIT"]],
        3: [["Multes de circulació (consulta de fotografies, identificació de conductors, interposició d'al·legacions o recursos, petició o aportació de proves)", "AFIT"], ["Consulta de fotografies de multes per infraccions", "AFIT"]],
        4: [["Padró d'Habitants: gestions d'alta, canvi de domicili, sol·licitud de certificats i altres gestions relacionades", "AFIT"], ["Sol·licitar certificats d'empadronament", "AFIT"]],
        5: [["Certificats del padró d'habitants. Expedició automàtica", "PFST"], ["Certificats del padró d'habitants. Expedició automàtica", "AFIT"], ["Cessió de dades personals al Padró Municipal d'Habitants", "AFIT"], ["Cessió de dades personals al Padró Municipal d'Habitants", "AFST"]],
        6: [["Sol·licitar certificats d'empadronament", "AFIT"], ["Certificats del padró d'habitants. Expedició automàtica", "AFIT"]],
        7: [["Llicències i comunicacions d'activitats", "AFIT"], ["Aportació de documentació de tràmits ja iniciats de l'àrea de Llicències d'activitats", "AFIT"]],
        8: [["Aportació de documentació de tràmits ja iniciats de l'àrea de Llicències d'activitats", "AFIT"]],
        9: [["Sol·licitar certificats d'empadronament", "AFIT"], ["Certificats del padró d'habitants. Expedició automàtica", "AFIT"]],
        10: [["Padró d'Habitants: gestions d'alta, canvi de domicili, sol·licitud de certificats i altres gestions relacionades", "AFIT"], ["Sol·licitar certificats d'empadronament", "AFIT"], ["Certificats del padró d'habitants. Expedició automàtica", "AFIT"]],
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
            st.markdown("<h4 style='text-align: center; color: #3d3d3b;'>Top 3 suggested processes (sorted by probability):</h4>", unsafe_allow_html=True)
            for i, tramite in enumerate(result, start=1):
                st.markdown(f"""
                    <div style='
                        background-color: #f9f9f9;
                        border: 2px solid #7fb927;
                        border-radius: 8px;
                        border-color: #ff4b4b;
                        padding: 10px;
                        margin: 10px 0;
                        font-size: 16px;
                        color: #3d3d3b;
                    '>
                        <strong>{i}. {tramite}</strong>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("A process couldn't be found. Try again.")
elif st.session_state.page == 2:
    st.markdown("<h3 style='text-align: center; color: #3d3d3b; font-weight: bold;'>Create your custom sequence</h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: #3d3d3b;'>Search and select a process</h3>", unsafe_allow_html=True)
    tramite_busqueda = st.text_input("", "")

    similares = []
    if tramite_busqueda:
        try:
            similares = ActionsPredictor().find_similarities(tramite_busqueda)
        except Exception as e:
            st.error(f"Error calling find_similarities: {e}")

    if similares:
        tramite_seleccionado = st.selectbox("Select the process you meant:", similares)
    else:
        tramite_seleccionado = None

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
                st.markdown("<h4 style='text-align: center; color: #3d3d3b;'>Top 3 suggested processes (sorted by probability):</h4>", unsafe_allow_html=True)
                for i, tramite in enumerate(result, start=1):
                    st.markdown(f"""
                        <div style='
                            background-color: #f9f9f9;
                            border: 2px solid #7fb927;
                            border-radius: 8px;
                            border-color: #ff4b4b;
                            padding: 10px;
                            margin: 10px 0;
                            font-size: 16px;
                            color: #3d3d3b;
                        '>
                            <strong>{i}. {tramite}</strong>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("A process couldn't be found. Try again.")
    else:
        st.markdown('<div class="empty-sequence">No processes added yet.</div>', unsafe_allow_html=True)


else:
    st.markdown("""
    <h2 style="color:#3d3d3b; text-align:center;">Why We Made These Decisions</h2>
    <p style="text-align:center; font-size: 18px; color:#7f7f7f;">In this project, we made several key decisions in order to deliver a high-quality solution that meets the needs of the challenge we worked on. Below, you'll find the reasons behind these decisions and our thought process.</p>
    """, unsafe_allow_html=True)

    # Preprocessing
    st.markdown("""
        <h3 style="color:#3d3d3b;">1. Preprocessing</h3>
        <p>We understand that the quality of the data is critical to the performance of any machine learning model. Therefore, we dedicated a significant amount of time to cleaning the datasets we used. This included:
        <ul>
            <li>Removing rows where the process was not valid.</li>
            <li>Grouping by sessions because we thought this had meaning and provided a sequential order.</li>
            <li>Reducing the number of consecutive rows that had identical session, action, and process features to just one.</li>
            <li>Deleting rows that had only one process per session, as we thought we couldn’t extract any useful information from them.</li>
        </ul>
        This process helped ensure that our models received clean, high-quality data, which improved the final results.</p>
        """, unsafe_allow_html=True)

    # Models
    st.markdown("""
        <h3 style="color:#3d3d3b;">2. Models</h3>
        <p>When selecting the models for our predictions, we aimed for both accuracy and efficiency. We decided to use a combination of pre-trained models and custom fine-tuned solutions. The key reasons for this approach include:
        <ul>
            <li>We used an LSTM model to predict the results.</li>
            <li>The sequential nature of the data made LSTM the best choice for capturing temporal dependencies and patterns.</li>
            <li>We adjusted hyperparameters such as learning rate and batch size to maximize performance.</li>
        </ul>
        Ultimately, this approach ensured that our model delivered reliable results while remaining performant.</p>
        """, unsafe_allow_html=True)

    # Other Solutions
    st.markdown("""
    <h3 style="color:#3d3d3b;">3. Other Solutions</h3>
    <p>In addition to machine learning models, we also explored other potential solutions that could improve the user experience and the accuracy of our predictions. Some of the strategies we considered included:
    <ul>
        <li>Data augmentation techniques to improve model generalization.</li>
        <li>Hybrid approaches that combine machine learning with rule-based systems.</li>
        <li>Utilizing cloud services to scale the system and handle large datasets efficiently.</li>
        <li>Implementing ensemble methods to combine predictions from multiple models.</li>
        <li>Exploring clustering techniques like DBSCAN and K-Nearest Neighbors (KNN) to identify patterns in the data and group similar processes.</li>
        <li>Testing more advanced Recurrent Neural Networks (RNNs), such as Transformers, to capture complex relationships in sequential data.</li>
        <li>Testing Graph Neural Networks (GNNs) to model the relationships between different processes as a graph structure.</li>
    </ul>
    While we decided to prioritize machine learning models for the core of our solution, we continue to evaluate other techniques to enhance performance in the future.</p>
    """, unsafe_allow_html=True)

    # Conclusions
    st.markdown("""
        <h3 style="color:#3d3d3b;">4. Conclusions</h3>
        <p>In conclusion, the decisions we made throughout the development of this project have been aimed at ensuring the best possible user experience and model performance. By focusing on clean data, efficient models, and continuous exploration of other solutions, we are confident that our approach will deliver the results that our users need. We are excited about the potential of this solution and will continue to refine it as we gather more insights and feedback.</p>
        """, unsafe_allow_html=True)

    # LinkedIn Profiles Section
    st.markdown("""
        <h3 style="color:#3d3d3b;">5. Meet the Team</h3>
        <p>We are a dedicated team of students who worked collaboratively to bring this project to life. Below, you can find our LinkedIn profiles to learn more about us:</p>
        <ul>
            <li><a href="https://www.linkedin.com/in/gerard-gispert-carreras-34b290265/" target="_blank">Gerard Gispert</a> - Software student at UPC</li>
            <li><a href="https://www.linkedin.com/in/carles-lobon-quilez-715149275/" target="_blank">Carles Lobon</a> - Software student at UPC</li>
        </ul>
        <p style="color:#7f7f7f; font-size: 14px;">Feel free to connect with us on LinkedIn to discuss our project or collaborate on future opportunities!</p>
        """, unsafe_allow_html=True)