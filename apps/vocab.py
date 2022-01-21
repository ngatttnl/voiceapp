
import streamlit as st
from apps.db import *
from apps.functions import *
import pandas as pd
from streamlit_quill import st_quill
from gtts import gTTS
from PIL import Image
import os

def app():
    menu = ["List Vocabulary", "Add Vocabulary", "Edit Vocabulary", "Delete Vocabulary"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice=="List Vocabulary":
        countries = ['Chinese', 'Danish', 'Dutch', 'English', 'French', 'Filipino', 'German', 'Japanese', 'Korean', 'Norwegian', 'Russian', 'Spanish', 'Swedish', 'Italian', 'Vietnamese']
        lang_dict = {'Dutch':'nl', 'Russian':'da', 'Danish':'da', 'Korean':'ko', 'Korean':'ko', 'Filipino':'fi', 'Norwegian':'no', 'swedish':'sv', 'Chinese':'zh-tw', 'English':'en', 'Vietnamese':'vi', 'German':'de', 'Janpanese':'ja', 'French':'fr', 'Spanish':'es', 'Italian':'it'}
        #lang = st.sidebar.selectbox('Select input language', countries, list(countries).index('English'))
        #to_lang = st.sidebar.selectbox('Select output language', countries, list(countries).index('Vietnamese'))
        #lang=lang_dict[lang]
        to_lang = 'en' #lang_dict[to_lang]
        try:  
            st.header("Words list")
            df = pd.DataFrame(view_all_vocab(), columns=['Word', 'Spelling', 'Meaning', 'Topic'])
            #st.table(df)
            col1, col2, col3, col4, col5, col6 = st.columns([1, 2, 2, 3, 2, 1])
            with col1:
                st.write("Number")
            with col2:
                st.write("Word")
            with col3:
                st.write("Spelling")
            with col4:
                st.write("Meaning")
            with col5:
                st.write("Listen")
            with col6:
                st.write("Download")
            for i in range(len(df.index)):
                col1, col2, col3, col4, col5, col6 = st.columns([1, 2, 2, 3, 2, 1])
                word = df.iloc[i][0]
                spelling = df.iloc[i][1]  
                meaning = df.iloc[i][2]    
                filename = "mp3/" + str(word) + ".mp3"
                ta_tts1 = gTTS(word, lang=to_lang)
                if not os.path.isfile(filename):
                    ta_tts1.save(filename)
                with col1:
                    st.write(i+1)
                with col2:
                    st.write(word)
                with col3:
                    st.write(spelling)
                with col4:
                    st.write(meaning)
                with col5:
                    audio_file1 = open(filename, "rb")
                    audio_bytes1 = audio_file1.read()
                    st.audio(audio_bytes1, format='audio/ogg',start_time=0)
                with col6:
                    st.write("")
                    st.markdown(get_binary_file_downloader_html(filename, ''), unsafe_allow_html=True)
               
        except:
                st.warning("Something went wrong!")
                
    elif choice=="Add Vocabulary":
        df = pd.DataFrame(view_all_topic(), columns=['ID', 'Name', 'Description'])
        df = df.sort_values(by=['Name']) 
        topics = df.set_index(['ID'])['Name'].to_dict()

        idTopic = st.selectbox("Select topic to edit:", options=topics, format_func=lambda x:topics[ x ])

        word = st.text_input("Enter a word: ", max_chars=100)
        spelling = st.text_input("Enter spelling of the word: ", max_chars=100)
        meaning = st.text_input("Enter meaning of the word: ", max_chars=200)
        language = st.session_state.key
       
        #content = st_quill(html=True)  # Spawn a new Quill editor
        #st.warning("You can't add vocabs now!") 
        if st.button("Add"):
            try:
                if word!="":
                    add_vocab(word, spelling, meaning, idTopic, language)
                    st.success("Saved: ".format(word))
                else:
                    st.warning("Word is not empty!")
            except:
                st.warning("Something went wrong!")
        
    elif choice=="Edit Vocabulary":
        st.subheader("Edit Vocabulary")
        
        df = pd.DataFrame(view_all_vocab(), columns=['Word', 'Spelling', 'Meaning', 'Topic', 'Language'])
        df = df.sort_values(by=['Topic']) 
        vocabs = df.set_index(['Word'])['Spelling', 'Meaning', 'Topic', 'Language'].to_dict()
        
        idTopic = st.selectbox("Select topic:", options=vocabs, format_func=lambda x:vocabs[ x ])

        dfContent = df.loc[df['ID'] == idTopic]
       
        topic = st.text_input("Enter a topic: ", value=dfContent.iloc[0]['Topic'])
        content = st_quill(value= dfContent.iloc[0]['Content'], html=True)  # Spawn a new Quill editor 
        st.warning("You can't edit vocab now!")
        
        """if st.button("Edit"):
            #newContent = content.replace('"', '###')
            #print(newContent)
            edit_vocab(content, topic, idTopic)
            st.warning("Edited: '{}'".format(idTopic))
        """
    elif choice=="Delete Vocabulary":
        st.subheader("Delete Vocabulary")
        
        st.warning("You can't delete vocabs now!")
        """if st.button("Delete"):
            delete(name)
            st.warning("Deleted: '{}'".format(name))"""

        """if st.button("Delete Wrong stocks"):
            #delete_wrong()
            st.warning("Deleted: '{}'")"""

    
        
        
        

	
