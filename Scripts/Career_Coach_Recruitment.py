#Import necessary libraries

import pandas as pd
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import requests
from io import StringIO  # Import StringIO directly from the io module
from io import BytesIO
from datetime import datetime
#from supabase import create_client, Client
from supabase.client import ClientOptions
import gspread
from google.oauth2 import service_account
import json
import numpy as np
import boto3
from sqlalchemy import create_engine
from sqlalchemy import create_engine, text
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
load_dotenv()

# AWS credentials setup
import os

# Use environment variables for AWS credentials
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
s3_bucket_name = os.getenv('BUCKET_NAME')
# os.environ['AWS_DEFAULT_REGION'] = 'your_preferred_region'

# Configure boto3 with the credentials
boto3.setup_default_session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def upload_to_s3(file, bucket_name, s3_file_name):
    s3 = boto3.client('s3')
    try:
        s3.upload_fileobj(file, bucket_name, s3_file_name)
        return True
    except NoCredentialsError:
        st.error("AWS credentials not available")
        return False
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False


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
#primary_key = f"{Number}_{Name}"



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


comments=['Soft skills and Professional Development Trainer |\n Teach job/career readiness Master Classes |\n Virtual engagement | 1.5 hours, 3-4 times a year','Career coach | Conduct job/career readiness workshops |\n In-person engagement |\n 2 - 4 hours, 1-2 times a year']
comments_a=st.selectbox("How would you like to join VigyanShaala's #SheforSTEM movement?*",comments)

if comments_a == "Career coach | Conduct job/career readiness workshops |\n In-person engagement |\n 2 - 4 hours, 1-2 times a year":
     travel_cost=st.radio('If we cover travel costs, are you willing to travel out-of-town for conducting these in-person workshops?*',('Yes','No'))


session_to_attend=['Crafting a winning STEM resume','Writing effective cover letters for STEM positions','Leveraging LinkedIn for STEM career advancement','Strategies for securing STEM internships','Mastering technical interviews','Navigating the STEM job market','Negotiating salary and benefits in STEM roles',
                   'Excelling in STEM job interviews','Developing leadership skills in STEM','Building your personal brand in STEM','Enhancing technology proficiency for STEM careers',
                   'Improving basic computer skills for STEM professionals','Utilizing online learning platforms for STEM skill development','Applying design thinking principles in STEM projects',
                   'Cultivating emotional intelligence in STEM environments','Stress management and time optimization in STEM careers','Financial planning and management for STEM professionals',
                    'Effective communication strategies for STEM fields','Polishing presentation skills for STEM presentations','Fostering teamwork in STEM settings','Critical thinking and decision-making skills for STEM professionals','Adapting to changes in the STEM industry','Project management techniques for STEM projects',
                    'Networking strategies for advancing in STEM careers','Personal and professional growth in STEM fields']

session=st.multiselect('Which of the following worskshops would you like to conduct? Please select all that apply.*',session_to_attend)


Binary=st.radio('Based on the choices you made in the previous question, do you have experience in conducting those specific workshops or similar sessions?*',('Yes','No'))
workshop=st.text_input('Are there any other workshop topics that you would like to cover?')
conducted=st.radio('How many such workshops have you conducted so far?*',("None","1-10","11-20","More than 20"))



# File upload for sample work
upload1 = st.file_uploader(' If possible, please upload a sample of your work.', accept_multiple_files=False, type=["pdf", "txt"])
if upload1:
    s3_file_name = f"sample_work/{Name}_{upload1.name}" #name can be modified
    if upload_to_s3(upload1, s3_bucket_name, s3_file_name):
        st.success(f"Sample work uploaded successfully to S3: {s3_file_name}")

# File upload for CV/Resume
upload2 = st.file_uploader('Upload your Curriculum Vitae/Resume*', accept_multiple_files=False, type=["pdf", "txt"])
if upload2:
    s3_file_name = f"cv_resume/{Name}_{upload2.name}"
    if upload_to_s3(upload2, s3_bucket_name, s3_file_name):
        st.success(f"CV/Resume uploaded successfully to S3: {s3_file_name}")

# File upload for bio and headshot
upload3 = st.file_uploader('Please upload your bio and a professional headshot.', accept_multiple_files=False, type=["pdf", "txt", "jpg", "png"])
if upload3:
    s3_file_name = f"Bio_headshot/{Name}_{upload3.name}"
    if upload_to_s3(upload3, s3_bucket_name, s3_file_name):
        st.success(f"Bio and headshot uploaded successfully to S3: {s3_file_name}")

call=st.radio('Would you be open to schedule a 10-15 minute call with us to discuss the structure/content of your class and tailor the workshop to our target audience?*',('Yes','No'))


def create_feedback_dataframe(Name, Email_id, Number, Profile, Institute, Current_job, Degree, Country, Current_city, selected_options, comments_a, travel_cost, session, Binary, workshop, conducted, upload1, call, upload2, upload3):
    if comments_a == "Career coach | Conduct job/career readiness workshops |\n In-person engagement |\n 2 - 4 hours, 1-2 times a year":
        data = {
            'Enter your full name *': [Name],
            'Enter your email address *': [Email_id],
            "Enter your WhatsApp number (with country code, DONOT ADD '+') *": [Number],
            'Enter your LinkedIn profile link here': [Profile],
            'Enter your current Institute/University/Organization *': [Institute],
            'Current Job title/Designation': [Current_job],
            'Highest degree obtained *': [Degree],
            'Country you currently reside in *': [Country],
            'Your current city *': [Current_city],
            'What communication languages are you comfortable in?  *': [', '.join(selected_options)],
            "How would you like to join VigyanShaala's #SheforSTEM movement?": [comments_a],
            'If we cover travel costs, are you willing to travel out-of-town': [travel_cost],
            'Which of the following workshops would you like to conduct? Ple': [', '.join(session)],
            'Based on the choices you made in the previous question, do you': [Binary],
            'Are there any other workshop topics that you would like to cove': [workshop],
            'How many such workshops have you conducted so far? *': [conducted],
            'If possible, please upload a sample of your work.': [f"s3://{s3_bucket_name}/sample_work/{Name}_{upload1.name}" if upload1 else None],
            'Would you be open to schedule a 10-15 minute call with us to di': [call],
            'Upload your Curriculum Vitae/Resume *': [f"s3://{s3_bucket_name}/cv_resume/{Name}_{upload2.name}" if upload2 else None],
            'Please upload your bio and a professional headshot.': [f"s3://{s3_bucket_name}/bio_headshot/{Name}_{upload3.name}" if upload3 else None]
        }
    else:
        data = {
            'Enter your full name *': [Name],
            'Enter your email address *': [Email_id],
            "Enter your WhatsApp number (with country code, DONOT ADD '+') *": [Number],
            'Enter your LinkedIn profile link here': [Profile],
            'Enter your current Institute/University/Organization *': [Institute],
            'Current Job title/Designation': [Current_job],
            'Highest degree obtained *': [Degree],
            'Country you currently reside in *': [Country],
            'Your current city *': [Current_city],
            'What communication languages are you comfortable in?  *':[', '.join(selected_options)],
            "How would you like to join VigyanShaala's #SheforSTEM movement?": [comments_a],
            'If we cover travel costs, are you willing to travel out-of-town': [''],
            'Which of the following workshops would you like to conduct? Ple': [', '.join(session)],
            'Based on the choices you made in the previous question, do you': [Binary],
            'Are there any other workshop topics that you would like to cove': [workshop],
            'How many such workshops have you conducted so far? *': [conducted],
            'If possible, please upload a sample of your work.': [f"s3://{s3_bucket_name}/sample_work/{Name}_{upload1.name}" if upload1 else None],
            'Would you be open to schedule a 10-15 minute call with us to di': [call],
            'Upload your Curriculum Vitae/Resume *': [f"s3://{s3_bucket_name}/cv_resume/{Name}_{upload2.name}" if upload2 else None],
            'Please upload your bio and a professional headshot.': [f"s3://{s3_bucket_name}/bio_headshot/{Name}_{upload3.name}" if upload3 else None]
        }

    df = pd.DataFrame(data)
    return df


if not Name or not Email_id or not Number or not Institute or not Degree or not Country or not Current_city or not selected_options or not comments_a or not session or not Binary or not conducted or not call or not upload2:
    st.error("Please fill in all the compulsory fields marked with * before proceeding.")
    st.stop()


if comments_a == "Career coach | Conduct job/career readiness workshops |\n In-person engagement |\n 2 - 4 hours, 1-2 times a year":
    combined_df = create_feedback_dataframe( Name, Email_id, Number, Profile, Institute, Current_job, Degree, Country, Current_city, selected_options, comments_a,travel_cost,session,Binary,workshop,conducted,upload1,call,upload2,upload3)
else:
    combined_df = create_feedback_dataframe( Name, Email_id, Number, Profile, Institute, Current_job, Degree, Country, Current_city, selected_options, comments_a,' ',session,Binary,workshop,conducted,upload1,call,upload2,upload3)


# Create a button in Streamlit
combined_button_text = "Submit"
if st.button(combined_button_text):
    
    # AWS RDS database connection info
    db_username = 'vigyan'
    db_password = '321#Dev'
    db_name = 'vigyan'
    db_port = '3306'
    db_endpoint = '35.154.220.255'


    # Create the connection string
    engine_str = f"mysql+mysqlconnector://{db_username}:{db_password}@{db_endpoint}:{db_port}/{db_name}"

    # Create the SQLAlchemy engine
    engine = create_engine(engine_str)


    # Store the DataFrame in the database table
    table_name = 'Career_Recruitment'  # Replace with your table name
    data_to_insert = combined_df.values.tolist()
    data_to_insert = pd.DataFrame(data_to_insert,columns=combined_df.columns)
    data_to_insert.to_sql(name=table_name, con=engine, if_exists='append', index=False)
    #combined_df.to_sql(name='Career_rec', con=engine, if_exists='append', index=False)
    st.success('Thankyou for your response.')

    
