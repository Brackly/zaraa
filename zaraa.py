import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="zaraa for africa by africa",
        page_icon="👋",
    )

    st.write("# Hi there 👋")

    st.markdown(
        """
        ### Let's take  this chance to introduce **Zaraa!** 
        - Zaraa is a conversational engine that seeks to help small scale farmers get access to relevant information to inform their agricultural activities.
        #### **Zaraa** translated to english is  Agriculture.
        
    st.markdown(
        """
        ### Please note:
        - Zaraa was trained on publicly available data from the internet.
        - The data was scraped from the following sites:
        - https://ktdateas.com/
        - https://rikeshkanji.weebly.com/
        - https://www.teaboard.or.ke/kenya-tea/history-of-kenyan-tea
        - https://ktga.or.ke/
        - **Zaraa can only communicate in English for now, we are still yet to train zaraa to answer and accept questions in the kenyan local languages**

        - You can ask it any questions about and regarding:
        - **The suitable climatic conditions for tea cultivation**
        - **The economic importance of the tea industry in Kenya**
        - ** information on the types of teas produced, the regions where tea is grown, the ideal climate and soil conditions, and the methods of cultivation and processing.**
        - **details on the scientific innovations in tea cultivation, including the development of clonal planting materials and the use of environmental response tests to select the best clones for specific regions. **
        - **challenges  facing tea-dependent livelihoods in Kenya**
        - ** Different bodies and stakeholders for Tea in Kenya**
    """
    )



    st.write("Click [here](https://zaraaAi.streamlit.app) to launch the demo.")

if __name__ == "__main__":
    run()
