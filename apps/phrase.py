
import streamlit as st
from apps.db import *
import pandas as pd


def clear_form():
    st.session_state["content"] = ""
def get_phrase_list(idTopic):
    st.header("Phrase list")
    df = pd.DataFrame(get_phrase_by_topic(idTopic), columns=['ID', 'Content'])         
    st.table(df)  
def app():
    menu = ["Add Phrase", "List Phrase", "Edit Phrase", "Delete Phrase"]
    choice = st.sidebar.selectbox("Menu", menu)

    dfTopic = pd.DataFrame(get_topic_for_phrase(), columns=['ID', 'Name'])
    dfTopic = dfTopic.sort_values(by=['Name']) 
    topics = dfTopic.set_index(['ID'])['Name'].to_dict()
    idTopic = st.selectbox("Select topic:", options=topics, format_func=lambda x:topics[ x ])

    if choice=="List Phrase":
        get_phrase_list(idTopic)
    elif choice=="Add Phrase":
        with st.form("myform"):
            content = st.text_area("Please input your sentences here:", height = 200, key="content", placeholder="Write something...")
            f1, f2 = st.columns([2, 2])
            with f1:
                submit = st.form_submit_button(label="Submit")
            with f2:
                clear = st.form_submit_button(label="Clear", on_click=clear_form)

        if submit:
            try:      
                content = st.session_state.content     
                add_phrase(content, idTopic)  
            except:
                st.warning("Something went wrong!")

        if clear:
            st.write('')
        #st.warning("You can't add vocabs now!") 
        #print(idTopic)
        get_phrase_list(idTopic)
       
    elif choice=="Edit phrase":
        st.subheader("Edit phrase")
        
        df = pd.DataFrame(get_phrase(), columns=['ID', 'Topic', 'Content'])
        df = df.sort_values(by=['Topic']) 
        phrases = df.set_index(['ID'])['Topic'].to_dict()
        
        idTopic = st.selectbox("Select topic:", options=phrases, format_func=lambda x:phrases[ x ])

        dfContent = df.loc[df['ID'] == idTopic]
       
        topic = st.text_input("Enter a topic: ", value=dfContent.iloc[0]['Topic'])
        st.warning("You can't edit phrase now!")
        
        """if st.button("Edit"):
            #newContent = content.replace('"', '###')
            #print(newContent)
            edit_phrase(content, topic, idTopic)
            st.warning("Edited: '{}'".format(idTopic))
        """
        get_phrase_list(idTopic)
    elif choice=="Delete phrase":
        st.subheader("Delete Stock")
        
        st.warning("You can't delete phrases now!")
        """if st.button("Delete"):
            delete(name)
            st.warning("Deleted: '{}'".format(name))"""
        get_phrase_list(idTopic)

   