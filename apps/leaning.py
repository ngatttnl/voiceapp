
import streamlit as st
from apps.db import *
from apps.functions import *
import pandas as pd
from streamlit_quill import st_quill
from gtts import gTTS
from googletrans import Translator, LANGUAGES
from PIL import Image
import os

def add_button(track_ids):
    """for t in track_ids:
        audio_file1 = open(t, "rb")
        audio_bytes1 = audio_file1.read()
        radio = st.audio(audio_bytes1, format='audio/ogg',start_time=0) 
    return radio
    """
    
    return [f'mp3/{t}.mp3' for t in track_ids]
def make_clickable2(url, text):
    return f"""<a href="javascript:alert('{url}')">{text}</a>"""

def add_stream_url(track_ids):
    return [f'mp3/{t}.mp3' for t in track_ids]

def make_clickable(bin_file, text):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<center><a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}" class="btn btn-info" role="button"> {text}</a></center>'
    return href
    #return f'<a target="_blank" href="{url}">{text}</a>'

def app():
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
    try:  
        st.header("Words list")
        df = pd.DataFrame(view_vocab_by_topic(idTopic), columns=['Word'])  
        """df['Listening'] = add_button(df['Word'])  
        df['Listening'] = df['Listening'].apply(make_clickable2, args = ('Click',))
        filename = 'nga'
        # show data
        #if st.checkbox('Include Preview URLs'):
        df['Download'] = add_stream_url(df['Word'])         
        df['Download'] = df['Download'].apply(make_clickable, args = ('',))
        st.write(df.to_html(escape = False), unsafe_allow_html = True)
        #else:
        #st.write(df)
        #st.table(df)
        """
        if len(df.index>0):
            col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 3, 2])
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
                col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 3, 2])
                word = df.iloc[i][0]
                translated_text = ''
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
                    ta_tts1 = gTTS(translated_text, lang=to_lang)
                    filename = "{word}.mp3"
                    ta_tts1.save(filename)
                    #st.write("Listening")
                    audio_file1 = open(filename, "rb")
                    audio_bytes1 = audio_file1.read()
                    st.audio(audio_bytes1, format='audio/ogg',start_time=0)
                    
                with col5:
                    st.write("")
                    st.markdown(get_binary_file_downloader_html(filename, 'Download'), unsafe_allow_html=True)
        
        else:
            st.write("No data!")
          
    except:
            st.warning("Something went wrong!")
    

    
        
        
        

	
