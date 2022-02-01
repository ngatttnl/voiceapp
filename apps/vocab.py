
import streamlit as st
from apps.db import *
from apps.functions import *
import pandas as pd
from streamlit_quill import st_quill
from gtts import gTTS
from googletrans import Translator, LANGUAGES
import os

#@st.cache
#def trans_make_audio(word, country):
def clear_form():
    st.session_state["word"] = ""
    st.session_state["spelling"] = ""
    

def app():
    menu = ["Add Vocabulary", "List Vocabulary", "Edit Vocabulary", "Delete Vocabulary"]
    choice = st.sidebar.selectbox("Menu", menu)
    countries = ['English', 'French', 'German', 'Korean', 'Spanish', 'Swedish', 'Italian', 'Vietnamese']
    lang_dict = {'Korean':'ko', 'Swedish':'sv', 'English':'en', 'Vietnamese':'vi', 'German':'de', 'French':'fr', 'Spanish':'es', 'Italian':'it'}
    
    #lang = st.sidebar.selectbox('Select input language', countries, list(countries).index('English'))
    to_lang = st.sidebar.selectbox('Select language', countries, list(countries).index('Vietnamese'))
    lang='en' #lang_dict[lang]
    to_lang = lang_dict[to_lang]

    dfTopic = pd.DataFrame(get_topics(), columns=['ID', 'Name'])
    dfTopic = dfTopic.sort_values(by=['Name']) 
    topics = dfTopic.set_index(['ID'])['Name'].to_dict()
    idTopic = st.selectbox("Select topic:", options=topics, format_func=lambda x:topics[ x ])
    if choice=="List Vocabulary": 
        try:  
            st.header("Words list")
            df = pd.DataFrame(view_vocab_by_topic(idTopic), columns=['Word', 'Spelling'])         
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
        with st.form("myform"):
            st.text_input("Enter a word:", key="word", max_chars=100)
            st.text_input("Enter a spelling:", key="spelling", max_chars=100)
            f1, f2 = st.columns([2, 2])
            with f1:
                submit = st.form_submit_button(label="Submit")
            with f2:
                clear = st.form_submit_button(label="Clear", on_click=clear_form)

        if submit:
            #if word!="":
            try:      
                vword = st.session_state.word
                vspelling = st.session_state.spelling     
                add_vocab(vword, vspelling, idTopic)
                filename_en = "mp3/en/" + str(vword) + ".mp3"
                ta_tts1 = gTTS(vword)
                ta_tts1.save(filename_en)
            except:
                st.warning("Something went wrong!")

        if clear:
            st.write('')
        #st.warning("You can't add vocabs now!") 
        #print(idTopic)
        st.header("Words list")
        df = pd.DataFrame(view_vocab_by_topic(idTopic), columns=['Word', 'Spelling'])         
        st.table(df)  
    elif choice=="Edit Vocabulary":
        st.subheader("Edit Vocabulary")
        #word - to choose
        df_vocab = pd.DataFrame(get_vocab_by_topic(idTopic), columns=['ID', 'Word'])
        df_vocab = df_vocab.sort_values(by=['Word']) 
        vocabs = df_vocab.set_index(['ID'])['Word'].to_dict()
        
        old_word = st.selectbox("Select word:", options=vocabs, format_func=lambda x:vocabs[ x ])
        if len(df_vocab.index>0):
            #topic
            df = pd.DataFrame(get_topics(), columns=['ID', 'Name'])
            df = df.sort_values(by=['Name']) 
            topics = df.set_index(['ID'])['Name'].to_dict()
            with st.form("myform"):
                idTopic = st.selectbox("Select topic to edit:", options=topics, format_func=lambda x:topics[ x ])

                word = st.text_input("Enter a word: ", max_chars=100)
                spelling = st.text_input("Enter spelling of the word: ", max_chars=100)
                f1, f2 = st.columns([2, 2])
                with f1:
                    submit = st.form_submit_button(label="Submit")
                with f2:
                    clear = st.form_submit_button(label="Clear", on_click=clear_form)
       
            #st.warning("You can't edit vocab now!")
        
            if st.button("Edit"):
                edit_vocab(old_word, word, spelling, idTopic)
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

    
        
        
        

	
