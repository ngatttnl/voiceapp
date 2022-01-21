import streamlit as st
from gtts import gTTS
from googletrans import Translator, LANGUAGES
from apps.functions import *

def app():
    countries = ['Chinese', 'Danish', 'Dutch', 'English', 'French', 'Filipino', 'German', 'Japanese', 'Korean', 'Norwegian', 'Russian', 'Spanish', 'Swedish', 'Italian', 'Vietnamese']
    lang_dict = {'Dutch':'nl', 'Russian':'da', 'Danish':'da', 'Korean':'ko', 'Korean':'ko', 'Filipino':'fi', 'Norwegian':'no', 'swedish':'sv', 'Chinese':'zh-tw', 'English':'en', 'Vietnamese':'vi', 'German':'de', 'Janpanese':'ja', 'French':'fr', 'Spanish':'es', 'Italian':'it'}
    lang = st.sidebar.selectbox('Select input language', countries, list(countries).index('English'))

    to_lang = st.sidebar.selectbox('Select output language', countries, list(countries).index('Vietnamese'))
    yourtext = st.text_area("Please input your sentences here:", value="Here is an example text", height = 200, key=1, placeholder="Input your sentences here")
    if len(yourtext)  == 0:
        st.warning("Enter your sentences...")
    try:
        lang=lang_dict[lang]
        to_lang = lang_dict[to_lang]
        
        translator = Translator()
        text_to_translate = translator.translate(yourtext, src=lang, dest=to_lang)
        translated_text = text_to_translate.text
        
        st.info(str(translated_text))
        ta_tts1 = gTTS(translated_text, lang=to_lang)

        ta_tts1.save("trans1.mp3")
        col1, col2 = st.columns([3,1])
        with col1:
            audio_file1 = open("trans1.mp3", "rb")
            audio_bytes1 = audio_file1.read()
            st.audio(audio_bytes1, format='audio/ogg',start_time=0)
        with col2:
            st.write("")
            st.markdown(get_binary_file_downloader_html('trans1.mp3', 'Audio'), unsafe_allow_html=True)
    
    except:
        st.warning("Welcome to our Text-To-Voice app")
