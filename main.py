# from .pages.dataVis import data_page
# from .pages.input_data import input_page

from pages import pages

import streamlit as st
from streamlit_multipage import MultiPage


app = MultiPage()
app.st = st
        
# app.add_app("Landing", landing_page, initial_page=True)
      
for app_name, app_function in pages.items():
    app.add_app(app_name, app_function)
    
app.run()



