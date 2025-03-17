import streamlit as st
from get_jd import extract_job_description
import os
import json
import re
from typing import Dict, List, Any
from groq import Groq
from keywords import extract_keywords
from content import get_content
import re
import ast





def main():
    
    

    job_url = st.text_input('Enter the job url')
    job_desc= extract_job_description(job_url)
    keywords = extract_keywords(job_desc)
    data=get_content(keywords)
    st.write(data)
    


    



    
if __name__ == "__main__":
    main()
