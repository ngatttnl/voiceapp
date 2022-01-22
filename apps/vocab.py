
import streamlit as st
from apps.db import *
from apps.functions import *
import pandas as pd
from streamlit_quill import st_quill
from gtts import gTTS
from googletrans import Translator, LANGUAGES
from PIL import Image
import os

def app():
    menu = ["List Vocabulary", "Add Vocabulary", "Edit Vocabulary", "Delete Vocabulary"]
    choice = st.sidebar.selectbox("Menu", menu)
    countries = ['Chinese', 'Danish', 'Dutch', 'English', 'French', 'Filipino', 'German', 'Japanese', 'Korean', 'Norwegian', 'Russian', 'Spanish', 'Swedish', 'Italian', 'Vietnamese']
    lang_dict = {'Dutch':'nl', 'Russian':'da', 'Danish':'da', 'Korean':'ko', 'Korean':'ko', 'Filipino':'fi', 'Norwegian':'no', 'swedish':'sv', 'Chinese':'zh-tw', 'English':'en', 'Vietnamese':'vi', 'German':'de', 'Janpanese':'ja', 'French':'fr', 'Spanish':'es', 'Italian':'it'}
    #lang = st.sidebar.selectbox('Select input language', countries, list(countries).index('English'))
    to_lang = st.sidebar.selectbox('Select language', countries, list(countries).index('Vietnamese'))
    lang='en' #lang_dict[lang]
    to_lang = lang_dict[to_lang]

    #print(word + lang + to_lang)
    
    dfTopic = pd.DataFrame(get_topics(), columns=['ID', 'Name'])
    dfTopic = dfTopic.sort_values(by=['Name']) 
    topics = dfTopic.set_index(['ID'])['Name'].to_dict()
    idTopic = st.selectbox("Select topic:", options=topics, format_func=lambda x:topics[ x ])
    if choice=="List Vocabulary": 
       
        try:  
            st.header("Words list")
            df = pd.DataFrame(view_vocab_by_topic(idTopic), columns=['Word'])         
            st.table(df)
            """if len(df.index>0):
                col1, col2, col3, col4, col5 = st.columns([1, 2, 3, 2, 2])
                with col1:
                    st.write("Number")
                with col2:
                    st.write("Word")
                with col3:
                    st.write("Meaning")
                with col4:
                    st.write("Listen")
                with col5:
                    st.write("Download")
                for i in range(len(df.index)):
                    #col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 3, 2])
                    word = df.iloc[i][0]
                    
                    filename = "mp3/" + str(word) + ".mp3"
                    with col1:
                        st.write(i+1)
                    with col2:
                        st.write(word)
                    with col3:                   
                        #st.write(meaning)
                        translator = Translator()
                        text = translator.translate(word, src=lang, dest=to_lang)
                        translated_text = text.text
                        st.write(translated_text)
                    with col4:
                        audio_file1 = open(filename, "rb")
                        audio_bytes1 = audio_file1.read()
                        st.audio(audio_bytes1, format='audio/ogg',start_time=0)
                    with col5:
                        st.write("")
                        st.markdown(get_binary_file_downloader_html(filename, ''), unsafe_allow_html=True)
            
            else:
                st.write("No data!")
            """   
        except:
                st.warning("Something went wrong!")
    elif choice=="Add Vocabulary":  
                 
        word = st.text_input("Enter a word: ", max_chars=100)
        spelling = '' #st.text_input("Enter spelling of the word: ", max_chars=100)
        #meaning = st.text_input("Enter meaning of the word: ", max_chars=200)
        #language = st.session_state.key
    
        #content = st_quill(html=True)  # Spawn a new Quill editor
        #st.warning("You can't add vocabs now!") 
        #if st.button("Add"):
        if word!="":
            try: 
                add_vocab(word, idTopic)
                """filename = "mp3/" + str(word) + ".mp3"
                if not os.path.isfile(filename):
                    ta_tts1 = gTTS(word)
                    ta_tts1.save(filename)
                """
            except:
                st.warning("Something went wrong!")
        st.header("Words list")
        df = pd.DataFrame(view_vocab_by_topic(idTopic), columns=['Word'])         
        st.table(df)  
    elif choice=="Edit Vocabulary":
        st.subheader("Edit Vocabulary")
        #word - to choose
        df = pd.DataFrame(get_vocab_by_topic(idTopic), columns=['Word', 'Word'])
        df = df.sort_values(by=['Word']) 
        vocabs = df.set_index(['Word'])['Word'].to_dict()
        
        old_word = st.selectbox("Select word:", options=vocabs, format_func=lambda x:vocabs[ x ])
        #topic
        df = pd.DataFrame(get_topics(), columns=['ID', 'Name'])
        df = df.sort_values(by=['Name']) 
        topics = df.set_index(['ID'])['Name'].to_dict()

        idTopic = st.selectbox("Select topic to edit:", options=topics, format_func=lambda x:topics[ x ])

        word = st.text_input("Enter a word: ", max_chars=100)
        spelling = st.text_input("Enter spelling of the word: ", max_chars=100)
        meaning = st.text_input("Enter meaning of the word: ", max_chars=200)
        #content = st_quill(value= dfContent.iloc[0]['Content'], html=True)  # Spawn a new Quill editor 
        #st.warning("You can't edit vocab now!")
        
        if st.button("Edit"):
            #newContent = content.replace('"', '###')
            #print(newContent)
            edit_vocab(old_word, word, spelling, meaning, idTopic)
            filename = "mp3/" + str(word) + ".mp3"
            if not os.path.isfile(filename):
                ta_tts1 = gTTS(word, lang=lang)
                ta_tts1.save(filename)
                st.success("Saved: ".format(word))
            st.warning("Edited: '{}'".format(idTopic))
        
    elif choice=="Delete Vocabulary":
        st.subheader("Delete Vocabulary")
        
        st.warning("You can't delete vocabs now!")
        """if st.button("Delete"):
            delete(name)
            st.warning("Deleted: '{}'".format(name))"""

        """if st.button("Delete Wrong stocks"):
            #delete_wrong()
            st.warning("Deleted: '{}'")"""

    
        
        
        

	
