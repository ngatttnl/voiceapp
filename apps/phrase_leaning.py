
import streamlit as st
from apps.db import *
from apps.functions import *
import pandas as pd
from streamlit_quill import st_quill
from gtts import gTTS
from googletrans import Translator, LANGUAGES
from PIL import Image
import os.path

st.cache
def app():
    countries = ['English', 'French', 'German', 'Korean', 'Spanish', 'Swedish', 'Italian', 'Vietnamese']
    lang_dict = {'Korean':'ko', 'Swedish':'sv', 'English':'en', 'Vietnamese':'vi', 'German':'de', 'French':'fr', 'Spanish':'es', 'Italian':'it'}
    #
    to_lang = st.sidebar.selectbox('Select language', countries, list(countries).index('Vietnamese'))
    lang='en' #lang_dict[lang]
    to_lang = lang_dict[to_lang]

    #print(word + lang + to_lang) 
    dfTopic = pd.DataFrame(get_topic_for_phrase(), columns=['ID', 'Name'])
    dfTopic = dfTopic.sort_values(by=['Name']) 
    topics = dfTopic.set_index(['ID'])['Name'].to_dict()
    idTopic = st.selectbox("Select topic:", options=topics, format_func=lambda x:topics[ x ])
    try:  
        df = pd.DataFrame(get_phrase_by_topic(idTopic), columns=['ID', 'Content'])
        if len(df.index>0):
            st.header("Sentence list")
            if (to_lang=='en'):
                english_to_lang = st.sidebar.selectbox('Select output language', countries, list(countries).index('Vietnamese'))
                english_to_lang = lang_dict[english_to_lang]
                col1, col2, col3, col4, col6 = st.columns([1, 3, 2, 3, 1])
                with col1:
                    st.write("Number")
                with col2:
                    st.write("Phrase")
                with col3:
                    st.write("Listen")
                with col4:
                    st.write("Meaning")
                
                with col6:
                    st.write("Download")
                translator = Translator()

                for i in range(len(df.index)):
                    col1, col2, col3, col4, col6 = st.columns([1, 3, 2, 3, 1])
                    id = df.iloc[i][0]
                    sentence = df.iloc[i][1]
                    translated_text = ''
                    filename = "phrase/en/" + str(id) + ".mp3"
                    with col1:
                        st.write(i+1)
                    with col2:
                        if not os.path.isfile(filename):
                            ta_tts1 = gTTS(sentence)
                            ta_tts1.save(filename)
                        st.write(sentence)
                    with col3:
                        #st.write(id)
                        filename_en = "phrase/en/" + str(id) + ".mp3"
                        audio_file1 = open(filename_en, "rb")
                        audio_bytes1 = audio_file1.read()
                        st.audio(audio_bytes1, format='audio/ogg',start_time=0)
                        
                    with col4:  
                        text = translator.translate(sentence, src=lang, dest=english_to_lang)
                        translated_text = text.text
                        st.write(translated_text)
                    
                    with col6:
                        st.write("")
                        st.markdown(get_binary_file_downloader_html(filename, '    '), unsafe_allow_html=True)
            else:
                col1, col2, col4, col5, col6 = st.columns([1, 3, 3, 2, 1])
                with col1:
                    st.write("Number")
                with col2:
                    st.write("Phrase") 
                with col4:
                    st.write("Meaning")
                with col5:
                    st.write("Listen")
                with col6:
                    st.write("Download")
                translator = Translator()

                for i in range(len(df.index)):
                    col1, col2, col4, col5, col6 = st.columns([1, 3, 3, 2, 1])
                    id = df.iloc[i][0]
                    content = df.iloc[i][1]
                    translated_text = ''
                    filename = "phrase/" + to_lang + "/" + str(id) + ".mp3"
                    with col1:
                        st.write(i+1)
                    with col2:
                        st.write(content)
                    
                    with col4:  
                        text = translator.translate(content, src=lang, dest=to_lang)
                        translated_text = text.text
                        st.write(translated_text)
                    with col5:
                        #st.write("abc")
                        if not os.path.isfile(filename):
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
    

    
        
        
        

	
