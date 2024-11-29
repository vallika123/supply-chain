import streamlit as st 
from pathlib import Path 
from PIL import Image
import base64


#--Path Settings--
current_dir = Path(__file__).parent  if "__file__" in locals() else Path.cwd()
css_file = current_dir /"styles"/ "main.css"
resume_file = current_dir / "pages" /"Vallika Kasibhatla_Supply Chain_GN.pdf"

#--basic info--
email=" vallika.kasibhatla25@gmail.com "
phone_number="+1 (437)-998-5255"
social_media= {"LinkedIn" : ("https://www.linkedin.com/in/vallika-kasibhatla-9b75a1225/","https://static-00.iconduck.com/assets.00/linkedin-emoji-512x512-mx3d67rm.png") }
linkedin_icon = '<i class="fa fa-linkedin-square" style="font-size:24px;color:#0e76a8;"></i>'
core_skills = [
    {"label": "Supply Chain", "details": " Inventory Management, Demand Forecasting, Procurement & Purchasing, Logistics & Distribution"},
    {"label": "Supplier & Process Optimization", "details": "Supplier Relationship Management (SRM), Process Optimization, Vendor Relations, Data Accuracy Management "},
    {"label": "ERP", "details": "SAP MM, Oracle"},
    {"label": "Project Management", "details": "Microsoft Project, Access, Primavera, Risk Management, Contingency Planning, Cost/Benefit Analysis, Budgeting"},
    {"label": "Excel", "details": "Pivot Tables, VLOOKUP / HLOOKUP / XLOOKUP, Index-Match, Conditional Formatting"},
    {"label": "Supply Chain & Data Analytics", "details": "Data-Driven Decision Making, Predictive Analytics, KPI Tracking, Python, Forecasting Methods, What-If Analysis, Safety Stock Calculations, Inventory Turnover Ratios"},
    {"label": "Data Visualization", "details": "Power BI, Tableau, Dashboards, Charts, Graphs"},
    {"label": "Soft Skills", "details": "Leadership, Team management, Communication, Problem solving, Adaptability, Quick learner, Creativity, Negotiation, Organization skills and Innovation  "},  
]





st.set_page_config(page_title="Digital CV | Vallika Kasibhatla", 
                   page_icon=":tada:", 
                   layout="centered")

#st.subheader("Hi, I am vallika :wave:")
custom_css = """
<style>
    body {
        background-color: #013328;  /* Force background to be white */
        color: #013328;  /* Force text color to be black */
    }
    .stApp {
        background-color: #F7F1ED;  /* Set main app background */
    }
    h1, h2, h3, h4, h5, h6,p {
        color: #013220;  /* Set header text colors */
    }
    .stButton button {
        background-color:#F7F1ED;  /* Customize button colors */
        color: #013328;
    }
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

#LOAD CSS, PDF ETC
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
    
with open(resume_file,"rb") as pdf_file:
    PDFbyte=pdf_file.read()
    


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #013328;">
  <a class="navbar-brand" target="_blank" style="pointer-events: none; cursor: default; color: pink;">Vallika Kasibhatla</a>

  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#core-skills">Core Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#professional-experience">Professional Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
     <li class="nav-item">
        <a class="nav-link" href="#projects" style="color: white;" onclick="streamlit.run('Projects.py')">Projects</a>
      </li>
       <li class="nav-item">
        <a class="nav-link" href="#certificate">Certificate</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)




#--HERO SECTION 

# Hero Section
st.markdown("""
    <style>
    .hero-section {
        text-align: center;
        margin-top: 0;
    }
    .hero-title {
        font-size: 2.5em;
        color: #013220;
        font-weight: bold;
    }
    .hero-subtitle {
        font-size: 1.2em;
        color: #013220;
    }
    </style>
    <div class="hero-section">
        <h1 class="hero-title">Vallika Kasibhatla <span style="font-size: 1.2em;"></span></h1>
        <p class="hero-subtitle">Supply Chain Professional | Materials Planner | M.Eng. in Engineering Management | B.Sc. in Computer Science </p>
    </div>
""", unsafe_allow_html=True)

col1,col2 = st.columns(2, gap="medium")
with col1: 
    st.markdown(""" <br> Supply Chain Analyst with SAP MM, Excel, Power BI, and R-Studio expertise for inventory optimization, demand forecasting, and data-driven decision-making. Proven success in automating workflows, improving inventory accuracy by 45%, and reducing costs by 23% within 12 months. Strong skills in streamlining operations and managing supplier relations.
     """,
    unsafe_allow_html=True
    )
    
with col2:
    st.markdown(
    """
    <style>
    .custom-link {
        color: black !important; /* Ensure the color is applied */
        text-decoration: none; /* Remove underline */
    }
    .custom-link:hover {
        color: black !important; /* Ensure the color remains black on hover */
        text-decoration: underline;
    }
    .social-media-icon {
        vertical-align: middle; /* Aligns image with text */
        width: 24px; /* Adjust size as needed */
        height: 24px; /* Adjust size as needed */
        margin-right: 8px; /* Space between image and text */
    }
    .contact-info {
        color: black; /* Set email and phone number text to black */
        font-size: 1.1em;
        line-height:2em;
         margin-bottom: 0.5em; 
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="contact-info">
        <strong>Email:</strong> {email}<br>
        <strong>Phone Number:</strong> {phone_number}<br>
    </div>
    """, unsafe_allow_html=True)
    
   
# Displaying social media links
    for platform, (link, image_url) in social_media.items():
        st.markdown(
        f"<a class='custom-link' href='{link}' target='_blank'>"
        f"<img class='social-media-icon' src='{image_url}' alt='{platform} icon' />"
        f"{platform}</a>", unsafe_allow_html=True
        )
        
    st.download_button(
    label="📝Download Resume",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream"
    )


st.markdown(
    """
    <style>
    .card {
        background-color: #fff9f9;
        padding: 15px;
        border-radius: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: 0.3s;
        margin-bottom: 10px;
        
    }
    .card:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    .card p {
        margin: 0;
        /* Remove margin between paragraphs */
    }
    .scrollable-block {
        max-width: 100%; /* Adjust width as needed */
        height: 600px; /* Fixed height for the block */
        overflow: auto; /* Enable scrolling if content overflows */
        border: 1px solid #ccc; /* Optional border for the block */
    }
    iframe {
        width: 100%; /* Make the iframe fill the width of the container */
        height: 100%; /* Make the iframe fill the height of the container */
        border: none; /* Remove iframe border */
    }
    .float-right {
         float: right;
}
    </style>
    """,
    unsafe_allow_html=True
)




###CORE SKILLS
#st.markdown('<p class="custom-subheader">CORE SKILLS</p>', unsafe_allow_html=True)
st.subheader("CORE SKILLS")


# Tabs creation with technical, software packages, and soft skills

    # Create a 4x4 grid layout
cols = st.columns(3, gap="small")
    
    # Calculate number of items per column
items_per_col = 3
total_items = len(core_skills)
    
for i in range(3):
    with cols[i]:
            # Display 4 items in each column
        for j in range(items_per_col):
            index = i * items_per_col + j
            if index < total_items:
                skill = core_skills[index]
                st.markdown(f"""
                <div class='card'>
                    <p style='margin-bottom: 5px;'>
                        <strong>{skill['label']}</strong>: {skill['details']}
                    </p> 
                </div>
                """, unsafe_allow_html=True)




####PROFESSIONAL EXPERIENCE
st.write ("---") 
st.subheader("PROFESSIONAL EXPERIENCE")

st.markdown(f""" <div class='card'>
    <h4 style='color: #013220; margin-bottom: 5px;'><strong>💼 Supply Chain Operations Analyst </strong></h4>
    <img src="https://static.cdnlogo.com/logos/c/18/chevron.png" style='width:100px; height:auto; position: absolute; top: 0; right: 10px;'>
    <i style='margin-bottom: 5px;'>Chevron  •  Dubai, United Arab Emirates  •  Jul 2022 - May 2023 </i></h6>
    <p style='margin-top: 5px;'>
    <ul>
        <li>Held positions in downstream operations in Bahrain and UAE, managing supply chain processes and serving as an additive material requirements planner to support day-to-day operations.<br></li>
        <li><strong>• Improved Vendor Relationships:</strong> Executed precise product ordering through SAP for external clients and ensured timely procurement of shipment details. Identified vendor issues and managed discontinued/expired products by organizing historical data, resulting in a <strong>60% improvement </strong> in vendor relationships.<br></li>
        <li><strong>• Automated Reporting Processes:</strong> Transformed manual report updates by automating Excel-to-Word links, saving <strong> 25 minutes </strong> per container-wise report and optimizing team productivity. This initiative contributed to overall process efficiency and reduced administrative workload.<br></li>
       <li> <strong>• Demand Planning and Production Scheduling:</strong> Optimized the company’s cost management and additives inventory purchasing by conducting data analysis using Excel and R-Studio, resulting in a <strong>45% increase </strong> in demand planning accuracy and contributing to a <strong>23%  </strong>overall reduction in costs.<br></li>
    </ul>

     """, unsafe_allow_html=True)


    
st.markdown(f""" <div class='card'>
    <h4 style='color: #013220'; margin-bottom: 5px;'><strong>💼 Data Analyst </strong> </h4>
    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Voltas_logo.png" style='width:100px; height:auto; position: absolute;  top: 10px; right:15px;'>
    <i style='margin-bottom: 5px;'> Voltas Limited TATA Enterprise  •  Doha, Qatar  •  Jan 2020 - Apr 2020 </i></h6>
    <p style='margin-top: 5px;'>
    <ul>
        <li><strong>• Data Analysis and Reporting:</strong> Analyzed employee and management datasets, identifying data gaps and producing a comprehensive report that increased HR analytical insights by <strong>35% </strong>. Utilized Power BI for data visualization, creating interactive dashboards to facilitate data-driven decision-making.<br></li>
        <li><strong>• Employee Engagement Initiatives:</strong> Facilitated monthly newsletters by providing detailed analyses of key company events and organized off-site gatherings, leading to a <strong>25% increase </strong>in employee satisfaction. Demonstrated strong interpersonal and communication skills in managing these initiatives.<br></li>
        <li><strong>• Project Management Optimization:</strong> Leveraged Primavera for project management and scheduling analysis. Evaluated KPI data to optimize workflows for <strong>8 </strong>construction managers and <strong>20</strong> subcontractors, resulting in improved operational efficiency and reduced project delays.<br></li>
        <li><strong>• Process Improvement:</strong> Contributed to process improvement projects by identifying inefficiencies and recommending changes, aligning with the company’s continuous improvement goals and enhancing overall project outcomes by regular collaboration with key stakeholders.<br>
    </ul>
    """, unsafe_allow_html=True)    


######---EDUCATION----####
st.write("---")
st.subheader("EDUCATION")  


st.markdown("""
<style>
    .bubble {
        display: inline-block;
        padding: 10px;
        background-color: #e0e0e0;
        border-radius: 15px;
        margin: 5px;
        font-size: 14px;
    }

    .edu-section {
        position: relative;
        margin-bottom: 30px;
    }
</style>

<div class="edu-section">
    <p style='margin-bottom: 5px;'><strong> Ontario Tech University </strong>
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6e/OntarioTech_primary_2019.svg" style='width:150px; height:auto; position: absolute; top: 0px; right: 15px;'>
        <br> M.Eng. of Engineering Management <br> 
        Oshawa, Ontario  <br>
        Grade: 4.18 / 4.30 <br><br>
        <i>Subjects:</i>
    </p>
    <br>
    <div class="bubble">Project Management</div>
    <div class="bubble">Foundation of Engineering Management</div>
    <div class="bubble">Production and Operations Management</div>
    <div class="bubble">Operations Research</div>
    <div class="bubble">Quality Management</div>
    <div class="bubble">Applied Risk Analysis</div>
    <div class="bubble">Accounting</div>
    
</div>

<div class="edu-section">
    <p style='margin-bottom: 5px;'><strong> American University of Sharjah </strong>
        <img src="https://upload.wikimedia.org/wikipedia/en/c/c8/American_University_of_Sharjah_%28emblem%29.png" style='width:120px; height:auto; position: absolute; top: 0px; right: 15px;'>
        <br> B.Sc. in Computer Science, Minor in Data Science <br> 
        Sharjah, United Arab Emirates  <br>
        Grade: 3.34 / 4.00 <br>
    </p>
</div> 
""", unsafe_allow_html=True)

st.write("---")



###PROJECTS

st.subheader("PROJECTS")

# Upload the PDF file


st.markdown(f"""
 
    <div class='card'>
        <h5><strong>Inventory forecasting and DIOH calculation</strong></h5>
        <p><strong>Project lead</strong></p>
        <ul>
            <li>• Faced with overstocking issues impacting financial efficiency, the task was to optimize and update the existing inventory plan as well as help in reducing holding costs. Inventory data was analyzed to compute Days of Inventory on Hand (DIOH) using forecasted consumption values.</li>
            <li>• Forecast models (moving averages) were developed in Excel and R-Studio for consumption and replenishment, implemented data mining techniques and historical averages to improve inventory predictions.</li>
            <li>• These efforts resulted in a significant reduction in holding costs and enhanced decision-making efficiency by preventing overstocking, aligning with the company's goals of cost management and process optimization.</li> 
        </ul>
       
    </div>
""", unsafe_allow_html=True)

###CERTIFICATES

st.write ("---")   
st.subheader("CERTIFICATE")

current_dir=Path(__file__).parent  if "__file__" in locals() else Path.cwd()
Paper1 = current_dir / "pages/lean six sigma green belt.pdf"
with open(Paper1,"rb") as pdf_file:
    PDFbyte_1=pdf_file.read()
    
pdf_base64_1 = base64.b64encode(PDFbyte_1).decode('utf-8')

st.markdown(f"""
        <h5><strong> Six Sigma Global Institute (SSGI): Lean Six Sigma Green Belt </strong></h5>
    """, unsafe_allow_html=True)

def display_pdf(pdf_base64):
    st.markdown(
        f'''
        <style>
        iframe {{
            width: 100%;
            height: 650px;
            border: none;
            overflow: hidden;
        }}
        </style>
        <iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="800" type="application/pdf"></iframe>
        ''',
        unsafe_allow_html=True
    )
# Button to display the PDF
if st.button(" :receipt: Open Certificate "):
    display_pdf(pdf_base64_1)
    
    
Paper2 = current_dir / "pages/CSCMP Supply Chain linkedln.pdf"
with open(Paper2,"rb") as pdf_file:
    PDFbyte_2=pdf_file.read()
    
pdf_base64_2 = base64.b64encode(PDFbyte_2).decode('utf-8')

st.markdown(f"""
        <h5><strong> Council of Supply Chain Management Professionals (CSCMP): Supply Chain, Inventory Management Professional Certificate </strong></h5>
       
    """, unsafe_allow_html=True)


# Button to display the PDF
if st.button(" :receipt: Open Certificate"):
    display_pdf(pdf_base64_2)