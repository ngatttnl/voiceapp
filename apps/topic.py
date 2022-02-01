
from operator import index
import streamlit as st
from apps.db import *
import pandas as pd
from streamlit_quill import st_quill
import streamlit.components.v1 as components
from PIL import Image

def view_topic():
    st.header("Topic list")
    df = pd.DataFrame(view_all_topic(), columns=['ID', 'Name', 'isPhrase'])   
    st.table(df)
def app():
    menu = [ "Add Topic", "List Topic", "Edit Topic", "Delete Topic"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice=="List Topic":
        try:
            view_topic()
        except:
            st.warning("Something went wrong!")
                
    elif choice=="Add Topic":
        name = st.text_input("Topic name: ", max_chars=200)
        is_phrase = st.checkbox("For phrase?")
        #st.warning("You can't add topics now!") 
        if st.button("Add"):
        #if name!="":
            try:
                phrase = 0
                if is_phrase:
                    phrase = 1
                #print(is_phrase)
                add_topic(name, phrase)
                st.success("Saved: " + str(name))
                
            except:
                st.warning("Something went wrong!")
        view_topic()
        
    elif choice=="Edit Topic":
        st.subheader("Edit Topic")
        
        df = pd.DataFrame(view_all_topic(), columns=['ID', 'Name', 'isPhrase'])
        df = df.sort_values(by=['Name']) 
        topics = df.set_index(['ID'])['Name'].to_dict()
        
        idTopic = st.selectbox("Select topic to edit:", options=topics, format_func=lambda x:topics[ x ])

        dfContent = df.loc[df['ID'] == idTopic]
       
        topic = st.text_input("Enter a name: ", value=dfContent.iloc[0]['Name'])
        is_phrase = st.checkbox("For phrase?")
        #st.warning("You can't edit topic now!")
        
        if st.button("Edit"):
            phrase = 0
            if is_phrase:
                phrase = 1
            edit_topic(topic, phrase, idTopic)
            st.warning("Edited: '{}'".format(topic))
        view_topic()
        
    elif choice=="Delete Topic":
        st.subheader("Delete Topic")
        
        st.warning("You can't delete topics now!")
        """if st.button("Delete"):
            delete(name)
            st.warning("Deleted: '{}'".format(name))"""

        """if st.button("Delete Wrong stocks"):
            #delete_wrong()
            st.warning("Deleted: '{}'")"""

    
        
        
        

	
