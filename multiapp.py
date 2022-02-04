"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []
        self.language = "en"
    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })
    def get_language(self):
        print("get: " + self.language)
        return self.language
    
    def run(self):
        st.set_page_config(page_title = "Text To Speech App", layout="wide")
        #space because of menu
        menu_div = """
            <div style="padding-top: 1rem;">
                &nbsp;
            </div>
        """
        #st.markdown(menu_div, unsafe_allow_html=True)
        #language menu
        """languages = {"vi_VN": "Việt Nam", "en": "English", "de_DE": "Deutsch"}
        if 'key' not in st.session_state:
            st.session_state['key'] = 'en'
        st.session_state['key'] = st.sidebar.selectbox("Select language", languages.keys(), format_func=lambda x:languages[ x ])   
        """
        #top-menu
        css_menu="""
            <style>
                .wrapMenuHeader,
                .wrapMenuHeader * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }
                .wrapMenuHeader a {
                    text-decoration: none;
                }
                .wrapMenuHeader {
                    position: fixed;
                    width: calc(100% - 6rem);
                    z-index: 100;
                    top: 0;
                    left: 3rem;
                    background-color: green;
                    padding-left: 20px;
                    padding-right: 20px;
                    padding-top: 15px;
                    padding-bottom: 1px;
                    display: flex;
                    align-items: center;
                }
                .wrapMenuHeader .wrapLogoMenu {
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    width: 100%;
                }
                .wrapMenuHeader .logoName {
                    font-size:18px;
                    font-weight: 700px;
                    color: white;
                }
                .wrapMenuHeader .wrapMenu {
                    list-style: none;
                    display: flex;
                    gap: 15px;
                }
                .wrapMenuHeader .wrapMenu .MenuLink {
                    color: white;
                    font-size: 16px;
                    font-weight: 700px;
                }
                .wrapMenuHeader .wrapMenu .MenuLink:hover {
                    color : white;
                }
                .wrapMenuHeader .btnBurger {
                    position: absolute;
                    top: 10px;
                    right: 20px;
                    cursor: pointer;
                    width: 40px;
                    height: 40px;
                    border: 2px solid #49A3DF;
                    display: none;
                    justify-content: center;
                    align-items: center;
                    color: #9ACCED;
                    border-radius: 5px;
                    -webkit-border-radius: 5px;
                    -moz-border-radius: 5px;
                    -ms-border-radius: 5px;
                    -o-border-radius: 5px;
                    font-size: 22px
                }
                .wrapMenuHeader .btnBurger:hover {
                    color : white;
                }
                input[id="collapseMenuMoile"]:checked ~ .wrapLogoMenu {
                    max-height: 100vh !important;
                    transition: all .5s;
                    -webkit-transition: all .5s;
                    -moz-transition: all .5s;
                    -ms-transition: all .5s;
                    -o-transition: all .5s;
                }
                @media screen and (max-width: 1000px) {
                    .wrapMenuHeader .btnBurger {
                        display: flex;
                    }
                    .wrapMenuHeader .wrapLogoMenu {
                        display: flex;
                        height: auto;
                        align-items: flex-start;
                        gap: 0px;
                        flex-direction: column;
                        max-height: 30px;
                        overflow: hidden;
                        transition: all .2s;
                        -webkit-transition: all .2s;
                        -moz-transition: all .2s;
                        -ms-transition: all .2s;
                        -o-transition: all .2s;
                    } 
                    .wrapMenuHeader .wrapMenu {
                        flex-direction:column;
                        gap: 0px;
                        width: 100%;
                        margin-top: 10px;
                    }
                    .wrapMenuHeader .wrapMenu .MenuLink {
                        width: 100%;
                        display: flex;
                        padding-top: 8px;
                        padding-bottom: 8px;
                    }
                }
            </style>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous"></head>
        """
        st.markdown(css_menu, unsafe_allow_html=True)
        ex_menu = """
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" integrity="sha512-Fo3rlrZj/k7ujTnHg4CGR2D7kSs0v4LLanw2qksYuRlEzO+tcaEPQogQ0KaoGN26/zrn20ImR1DfuLWnOo7aBA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
            <div class="wrapMenuHeader">
                <input type="checkbox" hidden id="collapseMenuMoile">
                <div class="wrapLogoMenu">
                    <a href="http://thanhnga.tk" class="logoName" style="color: white;">Thanh Nga</a>
                    <ul class="wrapMenu">
                        <li class="menuItem">
                            <a href="http://khuonchauthanhphuc.tk" class="MenuLink" style="color: white;" target="_blank">
                                Khuôn chậu Thanh Phúc
                            </a>
                        </li>    
                        <li class="menuItem">
                            <a href="http://bazancider.tk" style="color: white;" class="MenuLink" target="_blank">
                                Bazan cider
                            </a>
                        </li>    
                        <li class="menuItem">
                            <a href="https://www.linguar.com/groups" style="color: white;" class="MenuLink" target="_blank">
                                Language Exchange
                            </a>
                        </li>    
                        <li class="menuItem">
                            <a href="http://thanhnga.tk" style="color: white;" class="MenuLink" target="_blank">
                                My website
                            </a>
                        </li>            
                    </ul>
                </div>
                <label for="collapseMenuMoile" class="btnBurger">
                    <i class="fas fa-bars"></i>
                </label>
            </div>
        """
        st.markdown(ex_menu, unsafe_allow_html=True)
         
        PINNED_NAV_STYLE = """
            <style>
            .sidebar{
                padding-top: 1rem;
            }
            .reportview-container .sidebar-content {
                padding-top: 0rem;

            }
            .reportview-container .main .block-container {
                padding-top: 0rem;
                padding-right: 3rem;
                padding-left: 3rem;
                padding-bottom: 0rem;
            }
            </style>
        """
        st.markdown(PINNED_NAV_STYLE,unsafe_allow_html=True)

        #footer:
        footer_style = """
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
       
            footer:after {
                content:'Made by: ngattt@hcmuaf.edu.vn'; 
                visibility: visible;
                display: block;
                position: relative;
                #background-color: green;
                padding: 5px;
                top: 2px;
            }
        </style>      
        """
        
        st.markdown(footer_style, unsafe_allow_html=True)
        #app = st.selectbox(     
      
        app = st.sidebar.radio(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])
        
        app['function']()