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
#     # Display title & description
#     st.title("Co-founder Matching")
#     st.markdown("Enter your info to get your match")

#     # Establishing a Google Sheets connection
#     conn = st.connection("gsheets", type=GSheetsConnection)
#     existing_data = conn.read(worksheet='Profile_data', usecols=list(range(5)), ttl=5)
#     existing_data = existing_data.dropna(how="all")

#     # List of background, personality, goals & work styles
#     background_types = [
#         "Business", "Technical"
#     ]
#     goals = [
#         "Impact", "Outcome"
#     ]
#     work_styles = [
#         "Creative Thinkers", "Practical Doers"
#     ]

#     # Onboarding into co-founder matching form
#     with st.form(key="Profile_data"):
#         user_name = st.text_input(label="Name*")
#         email = st.text_input(label="Email*")
#         background = st.selectbox("Background*", options=background_types, index=None)
#         goal = st.selectbox("Goal*", options=goals)
#         work_style = st.selectbox("Work style*", options=work_styles)

#         submit_button = st.form_submit_button(label="Submit")

#     # If the form is submitted, process the data
#     if submit_button:
#       new_row = pd.DataFrame({
#           'Name': [user_name],
#           'Email': [email],
#           'Background': [background],
#           'Goal': [goal],
#           'Work style': [work_style]
#       })
  
#       # Read the sheet fresh each time without caching
#       existing_data = conn.read(worksheet='Profile_data', usecols=list(range(5)), ttl=0).dropna(how="all")
  
#       # Append the new row
#       updated_data = pd.concat([existing_data, new_row], ignore_index=True)
  
#       # Save back to the sheet
#       conn.update(worksheet='Profile_data', data=updated_data)
  
#       st.success("Your information has been submitted!")
     
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
        card {
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

    # Define your expected columns exactly as in your Google Sheet
    

    # Connect to Google Sheets
    conn = st.connection("gsheets", type=GSheetsConnection)

    background_types = ["Business", "Technical"]
    goals = ["Impact", "Outcome"]
    work_styles = ["Creative Thinkers", "Practical Doers"]
    columns = ['Name', 'Email', 'Background', 'Goal', 'Work style']

    with st.form(key="Profile_data"):
        user_name = st.text_input(label="Name*")
        email = st.text_input(label="Email*")
        background = st.selectbox("Background*", options=background_types)
        goal = st.selectbox("Goal*", options=goals)
        work_style = st.selectbox("Work style*", options=work_styles)

        submit_button = st.form_submit_button(label="Submit")

        if submit_button:
            new_row = pd.DataFrame([{
                'Name': user_name,
                'Email': email,
                'Background': background,
                'Goal': goal,
                'Work style': work_style
            }])

            # Read existing data fresh without cache
            existing_data = conn.read(worksheet='Profile_data', usecols=list(range(len(columns))), ttl=0)

            if existing_data.empty:
                updated_data = new_row
            else:
                # Make sure columns match before concatenating
                existing_data = existing_data.reindex(columns=columns)
                updated_data = pd.concat([existing_data, new_row], ignore_index=True)

            try:
                # Update sheet with new combined data
                conn.update(worksheet='Profile_data', data=updated_data)
                st.success("Your information has been submitted!")
            except Exception as e:
                st.error(f"Error saving data to sheet: {e}")

st.title("Muban")
st.header("a tool to find the right co founder")
st.write("")
st.write("")
st.write("")

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

st.write("")
st.write("")
st.write("")

st.write("Click below to create a profile and start the matching")
st.write("")
st.write("")

if st.button("Create a profile"):
    run_matching()
