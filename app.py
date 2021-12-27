
# Core Pkgs
import streamlit as st 
st.set_page_config(page_title="Text-To-Voice", layout='centered', initial_sidebar_state='auto')

from newspaper import Article
import wikipedia

from gtts import gTTS
import os
import base64

from googletrans import Translator, LANGUAGES

def main():
    """App for Web Articles and Wikipedia Pages Retrieval and Summarization.
    Articles are coverted to MP3 files via Text-To-Speech and sent by email"""

    title_templ = """
    <div>
    <h1>Text-To-Voice App</h1>
    </div>
    """

    st.markdown(title_templ,unsafe_allow_html=True)
    st.markdown(
            f"""
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script type="text/javascript" src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
            <a class="navbar-brand" href="https://thanhnga.herokuapp.com" target="_blank">Thanh Nga</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item active">
                    <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
                    </li>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="http://ngattt.tk" target="_blank">Investing world</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="http://khuonchauthanhphuc.tk" target="_blank">Khuôn chậu Thanh Phúc</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="http://bazancider.tk" target="_blank">Rượu trái cây Bazan</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="https://www.linguar.com" target="_blank">Học ngoại ngữ</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="http://thanhnga.tk" target="_blank">My Wordpress website</a>
                    </li>
                </ul>
            </div>
        </nav>
            """, unsafe_allow_html=True)

    activity = ["Translate", "Text to Voice", "Play Audio", "About"]
    choice = st.sidebar.radio("Menu", activity)

    lang_dict = {'English':'en', 'Vietnamese':'vi', 'German':'de', 'Italian':'it'}
    lang = st.sidebar.selectbox('Select input language',('English', 'Vietnamese', 'German', 'Italian'))
    
    if choice == "Translate":
        to_lang = st.sidebar.selectbox('Select output language',('Vietnamese', 'English', 'German', 'Italian'))
        yourtext = st.text_area("Please input your sentences here:", value="Here is example text", height = 200, key=1, placeholder="Input your sentences here")
        #yourtext2= st.sidebar.text_area("Input your sentence here", key=2, placeholder="Input your sentence here")
        #yourtext3 = st.sidebar.text_area("Input your sentence here", key=3, placeholder="Input your sentence here")
        #yourtext4 = st.sidebar.text_area("Input your sentence here", key=4, placeholder="Input your sentence here")
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

            audio_file1 = open("trans1.mp3", "rb")
            audio_bytes1 = audio_file1.read()
            st.audio(audio_bytes1, format='audio/ogg',start_time=0)
            
            st.markdown(get_binary_file_downloader_html('trans1.mp3', 'Audio'), unsafe_allow_html=True)
     
        except:
            st.warning("Welcome to our Text-To-Voice app")
    elif choice =='Text to Voice':
        story = "You can never understand one language until you understand at least two."
        yourtext = st.text_area("Please input your sentences here:", value=story, height = 200, key=1, placeholder="Input your sentences here")
        if len(yourtext)  == 0:
            st.warning("Enter your sentences...")
        try:
            lang=lang_dict[lang]
             
            ta_tts1 = gTTS(yourtext, lang=lang)

            ta_tts1.save("textToVoice.mp3")

            audio_file1 = open("textToVoice.mp3", "rb")
            audio_bytes1 = audio_file1.read()
            st.audio(audio_bytes1, format='audio/ogg',start_time=0)
            
            st.markdown(get_binary_file_downloader_html('textToVoice.mp3', 'Audio'), unsafe_allow_html=True)
     
        except:
            st.warning("Welcome to our Text-To-Voice app")
    elif choice == 'Play Audio':

        st.subheader("Play Your MP3 translation")
        #if st.button("Play"):

        try:
            audio_file = open('trans1.mp3', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')

        except:
            st.warning("No file to play. Please translate any sentence first!")

    elif choice=='About': #About
        st.subheader("About")

        st.markdown("""
        ###  ngattt@hcmuaf.edu.vn
        """)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<center><a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a></center>'
    return href

if __name__ == '__main__':
	main()