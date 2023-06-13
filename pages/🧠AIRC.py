
import streamlit as st
from streamlit_folium import folium_static
import folium


st.set_page_config( layout="wide",page_title="AI Voice Assistant",page_icon='🎙️')
st.title("Artificial Intelligence Center (AIRC)")
st.markdown("""The Artificial Intelligence Research Center (AIRC) at Ajman University was set-up in 2020 to strengthen the research related to Artificial Intelligence (AI) conducted by our faculty and students associated with the AI Graduate Program. The objective of this Center is to nurture and promote research, innovation and entrepreneurship in the area of Artificial Intelligence.

The AIRC consolidates our experience in the fields of AI, Robotics, evolutionary computation and Biomedical Data Science.

The aim of the AIRC is to achieve its objectives by fostering collaboration between professional research groups in the areas of AI, robotics, and biomedical engineering.
For more information visit the [AIRC official website](https://www.ajman.ac.ae/en/research/research-at-au/research-centers/artificial-intelligence-research-center-airc) 
""")
st.subheader("Our Vision")
st.write('''To become a leading center for AI-related research in the Arab region 
by making impactful research contributions in this field.''')
st.subheader("Our Mission")
st.write('''To nurture talent and an ecosystem of innovation in all areas related 
to AI and Machine Learning, with the active involvement and cooperation of industry
and society in the UAE. To conduct impactful applied research in AI and ML and to 
foster strong industry academic synergy for AI adoption.''')
st.subheader("Research Groups and areas of interest.")
st.markdown("""
The following research groups within the AIRC will 
conduct fundamental and applied research in the respective subject areas:
- Deep Learning/Machine Learning research group.
- Data Science research group.
- Robotics and Machine Vision research group.
- NLP and Speech Recognition research group.
- Evolutionary computation research group.
""")
st.subheader("AIRC Location")
st.markdown('**United Arab Emirates, Ajman**')
st.markdown("**University Street,Al jerf 1**")
st.markdown("**Building J2 (girls side), Block C, First Floor**")


# center on Liberty Bell
m = folium.Map(location=[25.412489292383068, 55.50657579596275], zoom_start=16)

# add marker for Liberty Bell
tooltip = "AIRC"
folium.Marker(
    [25.411936037037474, 55.50854628526483], popup="AIRC", tooltip=tooltip
    ).add_to(m)

# call to render Folium map in Streamlit
folium_static(m)




