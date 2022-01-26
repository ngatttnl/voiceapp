
import streamlit as st
from apps.db import *
from apps.functions import *
import pandas as pd
from streamlit_quill import st_quill
from gtts import gTTS
from googletrans import Translator, LANGUAGES
from PIL import Image
import os

st.cache
def app():
    countries = ['French', 'German', 'Korean', 'Spanish', 'Swedish', 'Italian', 'Vietnamese']
    lang_dict = {'Korean':'ko', 'Swedish':'sv', 'Vietnamese':'vi', 'German':'de', 'French':'fr', 'Spanish':'es', 'Italian':'it'}
    #lang = st.sidebar.selectbox('Select input language', countries, list(countries).index('English'))
    to_lang = st.sidebar.selectbox('Select language', countries, list(countries).index('Vietnamese'))
    lang='en' #lang_dict[lang]
    to_lang = lang_dict[to_lang]

    #print(word + lang + to_lang)
    
    dfTopic = pd.DataFrame(get_topics(), columns=['ID', 'Name'])
    dfTopic = dfTopic.sort_values(by=['Name']) 
    topics = dfTopic.set_index(['ID'])['Name'].to_dict()
    idTopic = st.selectbox("Select topic:", options=topics, format_func=lambda x:topics[ x ])
    try:  
        df = pd.DataFrame(view_vocab_by_topic(idTopic), columns=['Word', 'Spelling'])
        if len(df.index>0):
            st.header("Words list")
            col1, col2, col3, col4, col5, col6 = st.columns([1, 2, 2, 2, 2, 2])
            with col1:
                st.write("Number")
            with col2:
                st.write("Word")
            with col3:
                st.write("Listen")
            with col4:
                st.write("Meaning")
            with col5:
                st.write("Listen")
            with col6:
                st.write("Download")
            translator = Translator()

            for i in range(len(df.index)):
                col1, col2, col3, col4, col5, col6 = st.columns([1, 2, 2, 2, 2, 2])
                word = df.iloc[i][0]
                spelling = df.iloc[i][1]
                translated_text = ''
                filename = "mp3/" + to_lang + "/" + str(word) + ".mp3"
                with col1:
                    st.write(i+1)
                with col2:
                    st.write(word + " /" + spelling + "/")
                with col3:
                    filename_en = "mp3/en/" + str(word) + ".mp3"
                    #ta_tts1 = gTTS(word)
                    #ta_tts1.save(filename_en)
                    audio_file1 = open(filename_en, "rb")
                    audio_bytes1 = audio_file1.read()
                    st.audio(audio_bytes1, format='audio/ogg',start_time=0)
                with col4:  
                    text = translator.translate(word, src=lang, dest=to_lang)
                    translated_text = text.text
                    st.write(translated_text)
                with col5:
                    ta_tts1 = gTTS(translated_text, lang=to_lang)
                    ta_tts1.save(filename)
                    audio_file1 = open(filename, "rb")
                    audio_bytes1 = audio_file1.read()
                    st.audio(audio_bytes1, format='audio/ogg',start_time=0)
                with col6:
                    st.write("")
                    st.markdown(get_binary_file_downloader_html(filename, '    '), unsafe_allow_html=True)
        
        else:
            st.header("No data!")
          
    except:
            st.warning("Something went wrong!")
    

    
        
        
        

	
