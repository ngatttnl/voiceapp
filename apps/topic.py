
import streamlit as st
from apps.db import *
import pandas as pd
from streamlit_quill import st_quill
import streamlit.components.v1 as components
from PIL import Image


def app():
    menu = [ "Add Topic", "List Topic", "Edit Topic", "Delete Topic"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice=="List Topic":
        try:
            result = view_all_topic()
            #print(result)
            count = 0
            for i in result:
                count = count + 1
                name = i[1]       
                
                html_content2 = f"""
                <div>{name}</div>
                """
                st.markdown(html_content2, unsafe_allow_html=True)
        except:
                st.warning("Something went wrong!")
                
    elif choice=="Add Topic":
        name = st.text_input("Topic name: ", max_chars=200)
        #st.warning("You can't add topics now!") 
        if st.button("Add"):
            try:
                if name!="":
                    add_topic(name)
                    st.success("Saved: " + str(name))
                else:
                    st.warning("Topic name is not empty!")
            except:
                st.warning("Something went wrong!")
        
    elif choice=="Edit Topic":
        st.subheader("Edit Topic")
        
        df = pd.DataFrame(view_all_topic(), columns=['ID', 'Name', 'Description'])
        df = df.sort_values(by=['Name']) 
        topics = df.set_index(['ID'])['Name'].to_dict()
        
        idTopic = st.selectbox("Select topic to edit:", options=topics, format_func=lambda x:topics[ x ])

        dfContent = df.loc[df['ID'] == idTopic]
       
        topic = st.text_input("Enter a name: ", value=dfContent.iloc[0]['Name'])
        
        #st.warning("You can't edit topic now!")
        
        if st.button("Edit"):
            edit_topic(topic, idTopic)
            st.warning("Edited: '{}'".format(idTopic))
        
    elif choice=="Delete Topic":
        st.subheader("Delete Topic")
        
        st.warning("You can't delete topics now!")
        """if st.button("Delete"):
            delete(name)
            st.warning("Deleted: '{}'".format(name))"""

        """if st.button("Delete Wrong stocks"):
            #delete_wrong()
            st.warning("Deleted: '{}'")"""

    
        
        
        

	
