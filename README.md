# Career Coach Recruitment

**Career Coach Recruitment** is a web application designed to facilitate the recruitment of career coaches for our program. Unlike standard Google Forms, which may be restricted in some organizations, this platform provides a seamless alternative hosted on our EC2 instance, connected to an RDS database, with PDF files stored securely in Amazon S3.  

---

## Features

- **Streamlined Recruitment Form:** Coaches can submit their details, CVs, and other documents easily.  
- **Database Integration:** All submissions are stored in a secure RDS database for easy management and retrieval.  
- **Document Storage:** Uploaded PDF files are stored in Amazon S3 for secure access and scalability.  
- **Production Ready:** Hosted on an EC2 instance, making it accessible to the intended audience reliably.  


## Project Structure

```
Career-Coach-Recruitment/
├── Scripts/
│   ├── Career_Coach_Recruitment.py  # Main Streamlit application
│   ├── GUI_1.bat                    # Windows GUI launcher
│   ├── requirements.txt             # Python dependencies
│   └── .streamlit/                  # Streamlit configuration
├── image/                           # Project images and assets
├── .env                            # Environment variables
└── README.md                       # Project documentation
```
