# import streamlit as st
# from streamlit_gsheets import GSheetsConnection
# import pandas as pd
 

# st.markdown("""
#     <style>
#         .stApp {
#             text-align: center;
#             background-color: black;
#             color: white;
#             font-family: Times New Roman, serif;
#             padding: 40px; 
#         }
#         div.stButton > button:first-child {
#             background-color: #e57373;
#             color: white;
#             padding: 0.6em 2em;
#             border-radius: 8px;
#             border: none;
#             display: block;
#             margin: 0 auto;
#             }
#         div.stButton > button:first-child:hover {
#             background-color: #ef9a9a;
#         }
#         card {
#             background-color: #2b2b2b;
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#             color: white;
#         }
#     </style>
# """, unsafe_allow_html=True)






# def run_matching():
#     st.title("Co-founder Matching")
#     st.markdown("Enter your info to get your match")

#     conn = st.connection("gsheets", type=GSheetsConnection)
    
#     # List of options...
#     background_types = ["Business", "Technical"]
#     goals = ["Impact", "Outcome"]
#     work_styles = ["Creative Thinkers", "Practical Doers"]

#     # Form creation
#     with st.form(key="Profile_data"):
#         user_name = st.text_input(label="Name*")
#         email = st.text_input(label="Email*")
#         background = st.selectbox("Background*", options=background_types, index=None)
#         goal = st.selectbox("Goal*", options=goals)
#         work_style = st.selectbox("Work style*", options=work_styles)
#         submit_button = st.form_submit_button(label="Submit")

#     # Form submission handling (OUTSIDE the form block)
#     if submit_button:
#         # Create new row
#         new_row = pd.DataFrame({
#             'Name': [user_name],
#             'Email': [email],
#             'Background': [background],
#             'Goal': [goal],
#             'Work style': [work_style]
#         })
        
#         # Read existing data
#         existing_data = conn.read(worksheet='Profile_data', usecols=list(range(5)), ttl=0).dropna(how="all")
        
#         # Combine and update
#         updated_data = pd.concat([existing_data, new_row], ignore_index=True)
#         conn.update(worksheet='Profile_data', data=updated_data)
        
#         st.success("Your information has been submitted!")
        
# st.title("Muban")
# st.header("a tool to find the right co founder")
# st.write("")
# st.write("")
# st.write("")

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown("""
#     <div class="card">
#         <h3>Match</h3>
#         <p>We match you with a co-founder based on your profile.</p>
#     </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <div class="card">
#         <h3>Meet</h3>
#         <p>Meet your co-founder and get to know each other.</p>
#     </div>
#     """, unsafe_allow_html=True)

# with col3:
#     st.markdown("""
#     <div class="card">
#         <h3>Test & Evaluate</h3>
#         <p>Run a test project to check your fit and get feedback.</p>
#     </div>
#     """, unsafe_allow_html=True)
# st.write("")
# st.write("")
# st.write("")

# st.write("Click below to create a profile and start the matching")
# st.write("")
# st.write("")
# if st.button("Create a profile"):
#     # st.write("congrats")
#     run_matching()


#############################################################

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Initialize session state
if 'show_form' not in st.session_state:
    st.session_state.show_form = False

# ========== STYLING ==========
st.markdown("""
    <style>
        .stApp {
            text-align: center;
            background-color: black;
            color: white;
            font-family: Times New Roman, serif;
            padding: 40px; 
        }
        div.stButton > button:first-child {
            background-color: #e57373;
            color: white;
            padding: 0.6em 2em;
            border-radius: 8px;
            border: none;
            display: block;
            margin: 0 auto;
        }
        div.stButton > button:first-child:hover {
            background-color: #ef9a9a;
        }
        .card {
            background-color: #2b2b2b;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

def run_matching():
    st.title("Co-founder Matching")
    st.markdown("Enter your info to get your match")

    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        
        # Form options
        background_types = ["Business", "Technical"]
        goals = ["Impact", "Outcome"] 
        work_styles = ["Creative Thinkers", "Practical Doers"]

        with st.form(key="Profile_data"):
            user_name = st.text_input(label="Name*")
            email = st.text_input(label="Email*")
            background = st.selectbox("Background*", options=background_types, index=None)
            goal = st.selectbox("Goal*", options=goals)
            work_style = st.selectbox("Work style*", options=work_styles)
            submitted = st.form_submit_button("Submit")

        if submitted:
            if not all([user_name, email, background, goal, work_style]):
                st.warning("Please fill all required fields!")
            else:
                try:
                    new_row = pd.DataFrame({
                        'Name': [user_name],
                        'Email': [email],
                        'Background': [background],
                        'Goal': [goal],
                        'Work style': [work_style]
                    })
                    
                    existing_data = conn.read(
                        worksheet='Profile_data', 
                        usecols=list(range(5)), 
                        ttl=0
                    ).dropna(how="all")
                    
                    updated_data = pd.concat([existing_data, new_row], ignore_index=True)
                    conn.update(worksheet='Profile_data', data=updated_data)
                    
                    st.success("✅ Submitted successfully!")
                    st.balloons()
                    st.session_state.show_form = False  # Hide form after successful submission
                    
                except Exception as e:
                    st.error(f"❌ Failed to save data: {str(e)}")
                    st.error("Please check:")
                    st.error("1. Google Sheet permissions")
                    st.error("2. Worksheet name ('Profile_data')")
                    st.error("3. Column headers match")

    except Exception as e:
        st.error(f"❌ Connection failed: {str(e)}")
        st.error("Please check your Google Sheets connection setup")

# ========== LANDING PAGE ==========
st.title("Muban")
st.header("A tool to find the right co-founder")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="card">
        <h3>Match</h3>
        <p>We match you with a co-founder based on your profile.</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="card">
        <h3>Meet</h3>
        <p>Meet your co-founder and get to know each other.</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="card">
        <h3>Test & Evaluate</h3>
        <p>Run a test project to check your fit and get feedback.</p>
    </div>
    """, unsafe_allow_html=True)

if not st.session_state.show_form:
    if st.button("Create a profile"):
        st.session_state.show_form = True

if st.session_state.show_form:
    run_matching()
