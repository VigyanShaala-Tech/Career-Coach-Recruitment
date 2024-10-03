#Import necessary libraries

import pandas as pd
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import requests
#from supabase_py import create_client,Client
from io import StringIO  # Import StringIO directly from the io module
from io import BytesIO
from datetime import datetime
#import gotrue
from supabase import create_client, Client
from supabase.client import ClientOptions


# Function to get the current timestamp
def get_timestamp():
    return datetime.now()

# Display the PNG image in the top centre of the Streamlit sidebar with custom dimensions
image_path = 'https://twetkfnfqdtsozephdse.supabase.co/storage/v1/object/sign/stemcheck/VS-logo.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzdGVtY2hlY2svVlMtbG9nby5wbmciLCJpYXQiOjE3MjE5NzA3ODUsImV4cCI6MTc1MzUwNjc4NX0.purLZOGk272W80A4OlvnavqVB9u-yExhzpmI3dZrjdM&t=2024-07-26T05%3A13%3A02.704Z'
st.markdown(
    f'<div style="text-align:center"><img src="{image_path}" width="150"></div>',
    unsafe_allow_html=True
)

#Display the title of the Google form
st.markdown(
    "<h1 style='color: black; font-weight: bold;'>Kalpana - She for STEM Soft Skill Trainer and Career Coach Recruitment Form</h1>", 
    unsafe_allow_html=True
)

#Google form Questions

Name=st.text_input("Enter your full name*")
Email_id=st.text_input("Enter your email address*")
Number=st.text_input("Enter your WhatsApp number (Please Add Country Code, DONOT ADD '+')*")

Profile=st.text_input("Enter your LinkedIn profile link here")
Institute=st.text_input("Enter your current Institute/University/Organization*")
Current_job=st.text_input("Current Job title/Designation")
Degree = st.selectbox('Highest degree obtained*',("B.Sc.","M.Sc.","B.E./B.Tech.","M.Tech.","B.Pharm.","M.Pharm.","MBA","Ph.D."))
primary_key = f"{Number}_{Name}"


country_names = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","The Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin",
"Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon",
"Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo, Democratic Republic of the Congo", "Republic of the","Costa Rica",
"Côte d’Ivoire","Croatia","Cuba","Cyprus","Czech Republic","Denmark",
"Djibouti","Dominica","Dominican Republic","East Timor (Timor-Leste)","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini",
"Ethiopia","Fiji","Finland","France","Gabon","The Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana"
"Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya",
"Kiribati","Korea", "North Korea", "South Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania",
"Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia, Federated States of","Moldova",
"Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar (Burma)","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger",
"Nigeria","North Macedonia","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal",
"Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia",
"Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","Spain","Sri Lanka",
"Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad and Tobago","Tunisia",
"Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu",
"Vatican City","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]

Country=st.selectbox('Country you currently reside in*',country_names)
Current_city=st.text_input("Your current city*")

options = ['English','Hindi','Marathi','Malayalam','Kannada','Telgu','Assamese','Bengali','Gujarati','Manipuri','Tamil','Odia','Punjabi','Urdu','Maithili','Konkani','Kashmiri']
selected_options = st.multiselect("What communication languages are you comfortable in? * ", options)


comments=['Soft skills and Professional Development Trainer |/n Teach job/career readiness MasterClasses |/n Virtual engagement | 1.5 hours, 3-4 times a year','Career coach | Conduct job/career readiness workshops |/n In-person engagement |/n 2 - 4 hours, 1-2 times a year']
comments_a=st.selectbox("How would you like to join VigyanShaala's #SheforSTEM movement?*",comments)


travel_cost=st.radio('If we cover travel costs, are you willing to travel out-of-town for conducting these in-person workshops?*',('Yes','No'))

session_to_attend=['Crafting a winning STEM resume','Writing effective cover letters for STEM positions','Leveraging LinkedIn for STEM career advancement','Strategies for securing STEM internships','Mastering technical interviews','Navigating the STEM job market','Negotiating salary and benefits in STEM roles',
                   'Excelling in STEM job interviews','Developing leadership skills in STEM','Building your personal brand in STEM','Enhancing technology proficiency for STEM careers',
                   'Improving basic computer skills for STEM professionals','Utilizing online learning platforms for STEM skill development','Applying design thinking principles in STEM projects',
                   'Cultivating emotional intelligence in STEM environments','Stress management and time optimization in STEM careers','Financial planning and management for STEM professionals',
                    'Effective communication strategies for STEM fields','Polishing presentation skills for STEM presentations','Fostering teamwork in STEM settings','Critical thinking and decision-making skills for STEM professionals','Adapting to changes in the STEM industry','Project management techniques for STEM projects',
                    'Networking strategies for advancing in STEM careers','Personal and professional growth in STEM fields']

session=st.multiselect('Which of the following workshops would you like to conduct? Please select all that apply.*',session_to_attend)


Binary=st.radio('Based on the choices you made in the previous question, do you have experience in conducting those specific workshops or similar sessions?*',('Yes','No'))
workshop=st.text_input('Are there any other workshop topics that you would like to cover?')
conducted=st.radio('How many such workshops have you conducted so far?*',("None","1-10","11-20",">20"))
upload1=st.file_uploader(' If possible, please upload a sample of your work.',accept_multiple_files=False, type=["pdf", "txt"])
call=st.radio('Would you be open to schedule a 10-15 minute call with us to discuss the structure/content of your class and tailor the workshop to our target audience?*',('Yes','No'))
upload2=st.file_uploader('Upload your Curriculum Vitae/Resume*',accept_multiple_files=False, type=["pdf", "txt"])
upload3=st.file_uploader('Please upload your bio and a professional headshot.',accept_multiple_files=False, type=["pdf", "txt"])

if not Name or not Email_id or not Number or not Institute or not Current_job or not Degree or not Country or not Current_city or not selected_options or not comments or not travel_cost or not session or not Binary or not conducted or not call or not upload2:
    st.error("Please fill in all the compulsory fields marked with * before proceeding.")
    st.stop()


#Create Data Frame for the inputs in the GUI's element

def create_feedback_dataframe(primary_key, Name, Email_id, Number, Profile, Institute, Current_job, Degree, Country, Current_city, selected_options, comments_a,travel_cost,session,Binary,workshop,conducted,upload1,call,upload2,upload3):
    data = {
        'ID': primary_key,
        'Enter your full name *': Name,
        'Enter your email address *':Email_id ,
        "Enter your WhatsApp number (with country code, DONOT ADD '+') *":Number,
        'Enter your LinkedIn profile link here': Profile,
        'Enter your current Institute/University/Organization *':Institute,
        'Current Job title/Designation': Current_job ,
        'Highest degree obtained *':Degree ,
        'Country you currently reside in *': Country,
        'Your current city *':Current_city ,
        'What communication languages are you comfortable in?  *': selected_options,
        "How would you like to join VigyanShaala's #SheforSTEM movement?": comments_a,
        'If we cover travel costs, are you willing to travel out-of-town': travel_cost,
        'Which of the following workshops would you like to conduct? Ple': session,
        'Based on the choices you made in the previous question, do you ': Binary,
        'Are there any other workshop topics that you would like to cove': workshop,
        'How many such workshops have you conducted so far? *':conducted, 
        'If possible, please upload a sample of your work.':upload1.name if upload1 else None ,
        'Would you be open to schedule a 10-15 minute call with us to di':call,
        'Upload your Curriculum Vitae/Resume *':upload2.name if upload2 else None,
        'Please upload your bio and a professional headshot.':upload3.name if upload3 else None
    }

    feedback_df = pd.DataFrame([data])
    return feedback_df


#Supabase Credential to store data to database 

url: str = 'https://twetkfnfqdtsozephdse.supabase.co'
key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR3ZXRrZm5mcWR0c296ZXBoZHNlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjE5Njk0MzcsImV4cCI6MjAzNzU0NTQzN30.D76H5RoTel0M7Wj6PTRSAXxxYGic7K25BSaeQDZqIN0'
# Create a Supabase client
supabase: Client = create_client(url, key, options=ClientOptions(
    postgrest_client_timeout=10,
    storage_client_timeout=10,
    schema="public",
  ))


combined_button_text = "Submit"   

#Button to push data to supabase 

if st.button(combined_button_text):
    feedback_df = create_feedback_dataframe(primary_key, Name, Email_id, Number, Profile, Institute, Current_job, Degree, Country, Current_city, selected_options, comments_a,travel_cost,session,Binary,workshop,conducted,upload1,call,upload2,upload3)

    # Prepare the JSON data
    json_data = feedback_df[['ID','Enter your full name *','Enter your email address *',"Enter your WhatsApp number (with country code, DONOT ADD '+') *",'Enter your LinkedIn profile link here','Enter your current Institute/University/Organization *','Current Job title/Designation','Highest degree obtained *','Country you currently reside in *','Your current city *','What communication languages are you comfortable in?  *',"How would you like to join VigyanShaala's #SheforSTEM movement?",'If we cover travel costs, are you willing to travel out-of-town','Which of the following workshops would you like to conduct? Ple','Based on the choices you made in the previous question, do you ','Are there any other workshop topics that you would like to cove','How many such workshops have you conducted so far? *','If possible, please upload a sample of your work.','Would you be open to schedule a 10-15 minute call with us to di','Upload your Curriculum Vitae/Resume *','Please upload your bio and a professional headshot.']].to_dict(orient='records')[0]

    table_name = "Career_Coach_Recruitment"

    # Insert the JSON data into Supabase
    response_json = supabase.table(table_name).insert([json_data]).execute()

    #Demo code to add the google drive API . Please give it a AWS backend connection. 
    #####################
    #Define google drive API Scope here
    #SCOPES = ['https://www.googleapis.com/auth/drive.file']
    #PARENT_FOLDER_ID = "14OXiGuiaksXmeTigOtHHRtky7bU8dOpG"

    ## Function to upload a Pdf/text file to Google Drive

    #def upload_csv(uploaded_file):
        #try:
            # Get the current directory of the script
            #current_dir = os.path.dirname(os.path.abspath(__file__))
        
            # Path to the service account JSON file
            #json_file_path = os.path.join(current_dir, 'strong-jetty-435412-q0-a8ef3686d38f.json')

            ##Please add this json file obtained from google cloud console to the aws cloud , for now it it present on the supabase.

            # Load the credentials from the service account JSON file
            #creds = service_account.Credentials.from_service_account_file(
                #json_file_path,
                #scopes=SCOPES
            #)

            # Build the Drive service
            #service = build('drive', 'v3', credentials=creds)
        
            # Create a temporary file to save the uploaded file
            #with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                #temp_file.write(uploaded_file.read())  # Save the uploaded file to the temp file
                #temp_file_path = temp_file.name  # Get the temp file path

                # Metadata for the file
                #file_metadata = {
                    #'name': uploaded_file.name,  # Use the uploaded file name
                    #'parents': ['your_parent_folder_id']  # The ID of the folder where the file will be uploaded
                #}

                # Upload the file with the appropriate MIME type
                #media = MediaFileUpload(temp_file_path, mimetype='text/csv', resumable=True)
                #file = service.files().create(
                    #body=file_metadata,
                    #media_body=media,
                    #fields='id'
                #).execute()

                # File uploaded successfully
                #st.success(f"CSV file uploaded successfully with ID: {file.get('id')}")

                # Clean up the temporary file after uploading
                #os.remove(temp_file_path)

        #except Exception as e:
            #st.error(f"An error occurred: {e}")

# Assuming uploaded_file is a file uploaded using Streamlit file uploader
# Call the upload function
    #upload_csv(uploaded_file)
    

    
   


    
