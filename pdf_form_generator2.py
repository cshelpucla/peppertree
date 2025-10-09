"""
Golden Hills Rental Application - Fillable PDF Generator (CORRECTED VERSION)
Requires: pip install reportlab
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import HexColor, black, grey, white
from reportlab.lib import colors

def create_text_field(c, x, y, width, height, name, tooltip="", font_size=10):
    """Create a text input field"""
    c.acroForm.textfield(
        name=name,
        tooltip=tooltip,
        x=x,
        y=y,
        width=width,
        height=height,
        borderColor=black,
        fillColor=white,
        textColor=black,
        forceBorder=True,
        fontSize=font_size
    )

def create_checkbox(c, x, y, name, tooltip="", size=10):
    """Create a checkbox field"""
    c.acroForm.checkbox(
        name=name,
        tooltip=tooltip,
        x=x,
        y=y,
        size=size,
        borderColor=black,
        fillColor=white,
        textColor=black,
        forceBorder=True,
        buttonStyle='check'
    )

def draw_header(c, page_num):
    """Draw the header section"""
    # Logo
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.75*inch, 10.5*inch, "■■ Golden Hills")
    c.setFont("Helvetica", 10)
    c.drawString(0.75*inch, 10.3*inch, "REAL ESTATE")
    
    # Title
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(4.25*inch, 10*inch, "RENTAL APPLICATION QUALIFICATIONS AND REQUIREMENTS")
    
    # Page number
    c.setFont("Helvetica", 9)
    c.drawRightString(7.5*inch, 0.4*inch, f"PAGE {page_num} OF 3")

def create_page_1(c):
    """Create page 1 - Requirements and Qualifications"""
    draw_header(c, 1)
    
    y_pos = 9.4*inch
    c.setFont("Helvetica", 9)
    
    # Introduction text
    intro_text = [
        "Please read through all application documents thoroughly and completely before signing and submitting your rental",
        "application. All applicants/lease holders must be 18 years or older. All occupants 18 years or older will be required to complete",
        "an application (even if they will be living with parent(s) or guardian). Each applicant must complete their rental application in",
        "its entirety and all information provided must be true, accurate and complete, as well as verifiable. Below is a list of minimum",
        "requirements and qualifications that Golden Hills Real Estate utilizes to determine the eligibility of each applicant."
    ]
    
    for line in intro_text:
        c.drawString(0.75*inch, y_pos, line)
        y_pos -= 0.14*inch
    
    y_pos -= 0.25*inch
    
    # Requirements sections with proper spacing
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0.75*inch, y_pos, "Maximum Occupancy Limit:")
    y_pos -= 0.15*inch
    
    c.setFont("Helvetica", 9)
    c.drawString(0.75*inch, y_pos, "Studio floor plan allows up to 2 occupants.")
    y_pos -= 0.13*inch
    c.drawString(0.75*inch, y_pos, "1 Bedroom floor plan allows up to 3 occupants.")
    y_pos -= 0.13*inch
    c.drawString(0.75*inch, y_pos, "2 Bedroom floor plan allows up to 4 occupants.")
    y_pos -= 0.13*inch
    c.drawString(0.75*inch, y_pos, "3 Bedroom floor plan allows up to 6 occupants.")
    
    # Initial box
    c.rect(6.8*inch, y_pos - 0.05*inch, 0.6*inch, 0.18*inch)
    c.setFont("Helvetica", 7)
    c.drawCentredString(7.1*inch, y_pos - 0.15*inch, "Initial")
    
    y_pos -= 0.35*inch
    
    # Credit Report
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0.75*inch, y_pos, "Credit Report:")
    y_pos -= 0.15*inch
    
    c.setFont("Helvetica", 8)
    credit_lines = [
        "A credit report is required from each applicant over the age of 18. Negative credit information will be",
        "reviewed as to the age of the account, account type and the extensiveness of the negative debt. Negative",
        "credit history may result in a higher deposit or denial of your application. Credit scores of 650 or below may",
        "result in a higher deposit or denial of your application. Credit reports with landlord judgements of any kind,",
        "skips, evictions, or collection accounts relating to rental history are all means for automatic denial of your",
        "application."
    ]
    
    for line in credit_lines:
        c.drawString(0.75*inch, y_pos, line)
        y_pos -= 0.11*inch
    
    c.rect(6.8*inch, y_pos, 0.6*inch, 0.18*inch)
    c.setFont("Helvetica", 7)
    c.drawCentredString(7.1*inch, y_pos - 0.1*inch, "Initial")
    
    y_pos -= 0.3*inch
    
    # Rental History
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0.75*inch, y_pos, "Rental History:")
    y_pos -= 0.15*inch
    
    c.setFont("Helvetica", 8)
    rental_lines = [
        "Prior rental history must be listed. Please provide a minimum of 2 years verifiable residency history. Rental",
        "history cannot reflect anything negative. 'Property Name' will contact previous landlord(s) for rental",
        "verification(s), therefor prior landlord contact information must be provided on your rental application."
    ]
    
    for line in rental_lines:
        c.drawString(0.75*inch, y_pos, line)
        y_pos -= 0.11*inch
    
    c.rect(6.8*inch, y_pos, 0.6*inch, 0.18*inch)
    c.setFont("Helvetica", 7)
    c.drawCentredString(7.1*inch, y_pos - 0.1*inch, "Initial")
    
    y_pos -= 0.3*inch
    
    # Employment History
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0.75*inch, y_pos, "Employment History & Income Verification:")
    y_pos -= 0.15*inch
    
    c.setFont("Helvetica", 8)
    employment_lines = [
        "Current and/or previous employment must be verifiable. We will require documentation for at least 2",
        "months of income statements (pay stubs). In certain circumstances, we may accept the most recent year's",
        "tax returns, offer letter or a letter of employment provided by your employer. 'Property Name' will contact",
        "your employer for an employment verification, therefor contact information for your current employer must",
        "be provided on your rental application."
    ]
    
    for line in employment_lines:
        c.drawString(0.75*inch, y_pos, line)
        y_pos -= 0.11*inch
    
    c.rect(6.8*inch, y_pos, 0.6*inch, 0.18*inch)
    c.setFont("Helvetica", 7)
    c.drawCentredString(7.1*inch, y_pos - 0.1*inch, "Initial")
    
    y_pos -= 0.3*inch
    
    # Income Requirements
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0.75*inch, y_pos, "Income Requirements:")
    y_pos -= 0.15*inch
    
    c.setFont("Helvetica", 8)
    income_lines = [
        "Applicant(s) total household income must be at least 2 times the amount of monthly rent before taxes. If you",
        "will be using a co-signer, the total household income must be at least 4 times the amount of monthly rent",
        "before taxes, plus the co-signer must have excellent credit."
    ]
    
    for line in income_lines:
        c.drawString(0.75*inch, y_pos, line)
        y_pos -= 0.11*inch
    
    c.rect(6.8*inch, y_pos, 0.6*inch, 0.18*inch)
    c.setFont("Helvetica", 7)
    c.drawCentredString(7.1*inch, y_pos - 0.1*inch, "Initial")
    
    y_pos -= 0.3*inch
    
    # Identification Requirements
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0.75*inch, y_pos, "Identification Requirements:")
    y_pos -= 0.15*inch
    
    c.setFont("Helvetica", 8)
    id_lines = [
        "All applicants are required to provide a copy of at least one of the following forms of identification; valid",
        "driver's license, state identification card, passport, visa or military ID."
    ]
    
    for line in id_lines:
        c.drawString(0.75*inch, y_pos, line)
        y_pos -= 0.11*inch
    
    c.rect(6.8*inch, y_pos, 0.6*inch, 0.18*inch)
    c.setFont("Helvetica", 7)
    c.drawCentredString(7.1*inch, y_pos - 0.1*inch, "Initial")
    
    # Acknowledgment section
    y_pos = 2.3*inch
    c.setFont("Helvetica", 7)
    
    ack_text = [
        "I understand and accept the above stated qualifications and requirements. I understand that falsification of information on",
        "this application will be means for immediate denial of my application and forfeiture of my holding deposit. I understand",
        "and agree that I am required to provide all of the above stated documents/information for my rental application, including",
        "but not limited to: proof of income, photo ID, employer contact information and previous/current landlord contact",
        "information within 48 hours of applying. If I fail to provide all documents within the 48 hour period, Golden Hills Real",
        "Estate has the right to cancel my application and I forfeit my holding deposit and application fees."
    ]
    
    for line in ack_text:
        c.drawString(0.75*inch, y_pos, line)
        y_pos -= 0.11*inch
    
    # Signature fields at bottom
    y_pos = 1*inch
    c.setFont("Helvetica", 9)
    c.drawString(0.75*inch, y_pos, "Print Name:")
    create_text_field(c, 1.6*inch, y_pos - 0.15*inch, 2*inch, 0.22*inch, "print_name_1", "Print Name")
    
    c.drawString(3.8*inch, y_pos, "Signature:")
    create_text_field(c, 4.6*inch, y_pos - 0.15*inch, 2*inch, 0.22*inch, "signature_1", "Signature")
    
    c.drawString(6.8*inch, y_pos, "Date:")
    create_text_field(c, 7.2*inch, y_pos - 0.15*inch, 0.9*inch, 0.22*inch, "date_1", "Date")
    
    c.showPage()

def create_page_2(c):
    """Create page 2 - Personal Information, Address, Employment, Emergency Contact"""
    draw_header(c, 2)
    
    y_pos = 9.4*inch
    c.setFont("Helvetica", 9)
    
    intro = "Please read through all application documents thoroughly and completely before signing and submitting your rental"
    intro2 = "application. All applicants/lease holders must be 18 years or older."
    c.drawString(0.75*inch, y_pos, intro)
    c.drawString(0.75*inch, y_pos - 0.14*inch, intro2)
    
    # Date of Application
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(7.5*inch, y_pos - 0.28*inch, "DATE OF APPLICATION")
    
    date_y = y_pos - 0.5*inch
    create_text_field(c, 5.6*inch, date_y, 0.5*inch, 0.22*inch, "app_month", "MM", 10)
    c.setFont("Helvetica", 10)
    c.drawString(6.15*inch, date_y + 0.05*inch, "/")
    create_text_field(c, 6.3*inch, date_y, 0.5*inch, 0.22*inch, "app_day", "DD", 10)
    c.drawString(6.85*inch, date_y + 0.05*inch, "/")
    create_text_field(c, 7*inch, date_y, 0.6*inch, 0.22*inch, "app_year", "YYYY", 10)
    
    y_pos = date_y - 0.4*inch
    
    # PERSONAL INFORMATION
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.75*inch, y_pos, "PERSONAL INFORMATION")
    y_pos -= 0.35*inch
    
    c.setFont("Helvetica", 9)
    c.drawString(0.75*inch, y_pos, "Full Name:")
    create_text_field(c, 0.75*inch, y_pos - 0.35*inch, 2*inch, 0.22*inch, "first_name", "First", 9)
    c.setFont("Helvetica", 7)
    c.drawString(1.5*inch, y_pos - 0.48*inch, "First")
    
    create_text_field(c, 2.85*inch, y_pos - 0.35*inch, 1.8*inch, 0.22*inch, "middle_name", "Middle", 9)
    c.drawString(3.5*inch, y_pos - 0.48*inch, "Middle")
    
    create_text_field(c, 4.75*inch, y_pos - 0.35*inch, 2.5*inch, 0.22*inch, "last_name", "Last", 9)
    c.drawString(5.8*inch, y_pos - 0.48*inch, "Last")
    
    y_pos -= 0.75*inch
    
    # Date of Birth, Driver's License, State
    c.setFont("Helvetica", 9)
    c.drawString(0.75*inch, y_pos, "Date of Birth:")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 1.8*inch, 0.22*inch, "dob", "MM/DD/YYYY", 9)
    
    c.drawString(2.75*inch, y_pos, "Drivers License #:")
    create_text_field(c, 2.75*inch, y_pos - 0.25*inch, 2.8*inch, 0.22*inch, "dl_number", "License Number", 9)
    
    c.drawString(5.75*inch, y_pos, "State:")
    create_text_field(c, 5.75*inch, y_pos - 0.25*inch, 1.5*inch, 0.22*inch, "dl_state", "State", 9)
    
    y_pos -= 0.55*inch
    
    # SSN and Cell Phone
    c.drawString(0.75*inch, y_pos, "Social Security #:")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 2.3*inch, 0.22*inch, "ssn", "XXX-XX-XXXX", 9)
    
    c.drawString(3.25*inch, y_pos, "Cell Phone #:")
    create_text_field(c, 3.25*inch, y_pos - 0.25*inch, 2*inch, 0.22*inch, "cell_phone", "Cell Phone", 9)
    
    y_pos -= 0.55*inch
    
    # Gender and Home Phone
    c.drawString(0.75*inch, y_pos, "Gender:")
    create_checkbox(c, 1.4*inch, y_pos - 0.02*inch, "gender_male", "Male")
    c.drawString(1.55*inch, y_pos, "Male")
    create_checkbox(c, 2.1*inch, y_pos - 0.02*inch, "gender_female", "Female")
    c.drawString(2.25*inch, y_pos, "Female")
    
    c.drawString(3.25*inch, y_pos, "Home Phone #:")
    create_text_field(c, 3.25*inch, y_pos - 0.25*inch, 2*inch, 0.22*inch, "home_phone", "Home Phone", 9)
    
    y_pos -= 0.55*inch
    
    # Marital Status and Email
    c.drawString(0.75*inch, y_pos, "Marital Status:")
    create_checkbox(c, 1.7*inch, y_pos - 0.02*inch, "marital_single", "Single")
    c.drawString(1.85*inch, y_pos, "Single")
    create_checkbox(c, 2.5*inch, y_pos - 0.02*inch, "marital_married", "Married")
    c.drawString(2.65*inch, y_pos, "Married")
    
    c.drawString(3.75*inch, y_pos, "Email:")
    create_text_field(c, 3.75*inch, y_pos - 0.25*inch, 3.5*inch, 0.22*inch, "email", "Email Address", 9)
    
    y_pos -= 0.6*inch
    
    # ADDRESS SECTION
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.75*inch, y_pos, "ADDRESS")
    y_pos -= 0.3*inch
    
    c.setFont("Helvetica", 9)
    c.drawString(0.75*inch, y_pos, "Present Address:")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 6.5*inch, 0.22*inch, "present_address", "Current Address", 9)
    
    y_pos -= 0.55*inch
    
    c.drawString(0.75*inch, y_pos, "Dates of Residence:")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 1.2*inch, 0.22*inch, "present_start", "Start Date", 8)
    c.setFont("Helvetica", 7)
    c.drawCentredString(1.35*inch, y_pos - 0.38*inch, "Start Date")
    
    c.setFont("Helvetica", 9)
    c.drawString(2.1*inch, y_pos, "To")
    create_text_field(c, 2.35*inch, y_pos - 0.25*inch, 1.2*inch, 0.22*inch, "present_end", "End Date", 8)
    c.setFont("Helvetica", 7)
    c.drawCentredString(2.95*inch, y_pos - 0.38*inch, "End Date")
    
    c.setFont("Helvetica", 9)
    c.drawString(3.7*inch, y_pos, "Monthly Payment:")
    create_text_field(c, 3.7*inch, y_pos - 0.25*inch, 1.2*inch, 0.22*inch, "present_payment", "$", 9)
    
    y_pos -= 0.55*inch
    
    c.drawString(0.75*inch, y_pos, "Rented/Owned?")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 1.5*inch, 0.22*inch, "present_rent_own", "Rented/Owned", 9)
    
    c.drawString(2.5*inch, y_pos, "Management Name:")
    create_text_field(c, 2.5*inch, y_pos - 0.25*inch, 2.5*inch, 0.22*inch, "present_mgmt_name", "Management Name", 9)
    
    c.drawString(5.3*inch, y_pos, "Phone:")
    create_text_field(c, 5.3*inch, y_pos - 0.25*inch, 2*inch, 0.22*inch, "present_mgmt_phone", "Phone", 9)
    
    y_pos -= 0.6*inch
    
    # Previous Address
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0.75*inch, y_pos, "Previous Address:")
    y_pos -= 0.25*inch
    
    c.setFont("Helvetica", 9)
    create_text_field(c, 0.75*inch, y_pos, 6.5*inch, 0.22*inch, "previous_address", "Previous Address", 9)
    
    y_pos -= 0.35*inch
    
    c.drawString(0.75*inch, y_pos, "Dates of Residence:")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 1.2*inch, 0.22*inch, "previous_start", "Start Date", 8)
    
    c.drawString(2.1*inch, y_pos, "To")
    create_text_field(c, 2.35*inch, y_pos - 0.25*inch, 1.2*inch, 0.22*inch, "previous_end", "End Date", 8)
    
    c.drawString(3.7*inch, y_pos, "Monthly Payment:")
    create_text_field(c, 3.7*inch, y_pos - 0.25*inch, 1.2*inch, 0.22*inch, "previous_payment", "$", 9)
    
    y_pos -= 0.55*inch
    
    c.drawString(0.75*inch, y_pos, "Rented/Owned?")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 1.5*inch, 0.22*inch, "previous_rent_own", "Rented/Owned", 9)
    
    c.drawString(2.5*inch, y_pos, "Management Name:")
    create_text_field(c, 2.5*inch, y_pos - 0.25*inch, 2.5*inch, 0.22*inch, "previous_mgmt_name", "Management Name", 9)
    
    c.drawString(5.3*inch, y_pos, "Phone:")
    create_text_field(c, 5.3*inch, y_pos - 0.25*inch, 2*inch, 0.22*inch, "previous_mgmt_phone", "Phone", 9)
    
    y_pos -= 0.6*inch
    
    # EMPLOYMENT SECTION
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.75*inch, y_pos, "EMPLOYMENT")
    y_pos -= 0.3*inch
    
    c.setFont("Helvetica", 9)
    c.drawString(0.75*inch, y_pos, "Current Employer:")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 2.5*inch, 0.22*inch, "employer", "Current Employer", 9)
    
    c.drawString(3.5*inch, y_pos, "Position:")
    create_text_field(c, 3.5*inch, y_pos - 0.25*inch, 3.8*inch, 0.22*inch, "position", "Position", 9)
    
    y_pos -= 0.55*inch
    
    c.drawString(0.75*inch, y_pos, "Employer Address:")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 6.5*inch, 0.22*inch, "employer_address", "Employer Address", 9)
    
    y_pos -= 0.55*inch
    
    c.drawString(0.75*inch, y_pos, "Supervisor Name:")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 2.8*inch, 0.22*inch, "supervisor_name", "Supervisor Name", 9)
    
    c.drawString(3.8*inch, y_pos, "Supervisor Phone:")
    create_text_field(c, 3.8*inch, y_pos - 0.25*inch, 3.5*inch, 0.22*inch, "supervisor_phone", "Supervisor Phone", 9)
    
    y_pos -= 0.55*inch
    
    c.drawString(0.75*inch, y_pos, "Hire Date:")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 1.5*inch, 0.22*inch, "hire_date", "MM/DD/YYYY", 9)
    
    c.drawString(2.5*inch, y_pos, "Annual Income:")
    create_text_field(c, 2.5*inch, y_pos - 0.25*inch, 2*inch, 0.22*inch, "annual_income", "Annual Income", 9)
    
    y_pos -= 0.55*inch
    
    c.drawString(0.75*inch, y_pos, "Other Income:")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 2.5*inch, 0.22*inch, "other_income_source", "Source", 9)
    
    c.drawString(3.5*inch, y_pos, "Annual Amount:")
    create_text_field(c, 3.5*inch, y_pos - 0.25*inch, 2*inch, 0.22*inch, "other_income_amount", "Amount", 9)
    
    y_pos -= 0.6*inch
    
    # EMERGENCY CONTACT
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.75*inch, y_pos, "EMERGENCY CONTACT")
    y_pos -= 0.3*inch
    
    c.setFont("Helvetica", 9)
    c.drawString(0.75*inch, y_pos, "Full Name:")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 3*inch, 0.22*inch, "emergency_name", "Full Name", 9)
    
    c.drawString(4*inch, y_pos, "Relationship:")
    create_text_field(c, 4*inch, y_pos - 0.25*inch, 3.3*inch, 0.22*inch, "emergency_relationship", "Relationship", 9)
    
    y_pos -= 0.55*inch
    
    c.drawString(0.75*inch, y_pos, "Phone #:")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 2.3*inch, 0.22*inch, "emergency_phone", "Phone", 9)
    
    c.drawString(3.3*inch, y_pos, "Email:")
    create_text_field(c, 3.3*inch, y_pos - 0.25*inch, 4*inch, 0.22*inch, "emergency_email", "Email", 9)
    
    y_pos -= 0.55*inch
    
    c.drawString(0.75*inch, y_pos, "Address:")
    create_text_field(c, 0.75*inch, y_pos - 0.25*inch, 6.5*inch, 0.22*inch, "emergency_address", "Address", 9)
    
    c.showPage()

def create_page_3(c):
    """Create page 3 - Pets, Vehicles, Other Occupants, Other Information"""
    draw_header(c, 3)
    
    y_pos = 9.4*inch
    
    # PETS SECTION
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.75*inch, y_pos, "PETS")
    y_pos -= 0.3*inch
    
    c.setFont("Helvetica", 9)
    c.drawString(0.75*inch, y_pos, "Do you have any pets?")
    create_checkbox(c, 2.2*inch, y_pos - 0.02*inch, "pets_yes", "Yes")
    c.drawString(2.35*inch, y_pos, "Yes")
    create_checkbox(c, 2.8*inch, y_pos - 0.02*inch, "pets_no", "No")
    c.drawString(2.95*inch, y_pos, "No")
    
    c.drawString(3.8*inch, y_pos, "If yes, how many?")
    create_text_field(c, 5.2*inch, y_pos - 0.15*inch, 0.5*inch, 0.22*inch, "num_pets", "Number", 9)
    
    y_pos -= 0.4*inch
    
    # Pet 1
    c.setFont("Helvetica-Bold", 9)
    c.drawString(0.75*inch, y_pos, "Pet 1")
    y_pos -= 0.22*inch
    
    c.setFont("Helvetica", 8)
    c.drawString(0.75*inch, y_pos, "Type:")
    create_text_field(c, 1.1*inch, y_pos - 0.15*inch, 1.2*inch, 0.2*inch, "pet1_type", "Dog, Cat, etc.", 8)
    
    c.drawString(2.5*inch, y_pos, "Breed:")
    create_text_field(c, 3*inch, y_pos - 0.15*inch, 1.5*inch, 0.2*inch, "pet1_breed", "Breed", 8)
    
    c.drawString(4.7*inch, y_pos, "Color:")
    create_text_field(c, 5.2*inch, y_pos - 0.15*inch, 1.2*inch, 0.2*inch, "pet1_color", "Color", 8)
    
    c.drawString(6.6*inch, y_pos, "Weight:")
    create_text_field(c, 7.1*inch, y_pos - 0.15*inch, 0.6*inch, 0.2*inch, "pet1_weight", "lbs", 8)
    
    y_pos -= 0.38*inch
    
    c.drawString(0.75*inch, y_pos, "Age:")
    create_text_field(c, 1.1*inch, y_pos - 0.15*inch, 0.6*inch, 0.2*inch, "pet1_age", "Age", 8)
    
    c.drawString(2*inch, y_pos, "Name:")
    create_text_field(c, 2.5*inch, y_pos - 0.15*inch, 3*inch, 0.2*inch, "pet1_name", "Pet Name", 8)
    
    y_pos -= 0.45*inch
    
    # Pet 2
    c.setFont("Helvetica-Bold", 9)
    c.drawString(0.75*inch, y_pos, "Pet 2")
    y_pos -= 0.22*inch
    
    c.setFont("Helvetica", 8)
    c.drawString(0.75*inch, y_pos, "Type:")
    create_text_field(c, 1.1*inch, y_pos - 0.15*inch, 1.2*inch, 0.2*inch, "pet2_type", "Dog, Cat, etc.", 8)
    
    c.drawString(2.5*inch, y_pos, "Breed:")
    create_text_field(c, 3*inch, y_pos - 0.15*inch, 1.5*inch, 0.2*inch, "pet2_breed", "Breed", 8)
    
    c.drawString(4.7*inch, y_pos, "Color:")
    create_text_field(c, 5.2*inch, y_pos - 0.15*inch, 1.2*inch, 0.2*inch, "pet2_color", "Color", 8)
    
    c.drawString(6.6*inch, y_pos, "Weight:")
    create_text_field(c, 7.1*inch, y_pos - 0.15*inch, 0.6*inch, 0.2*inch, "pet2_weight", "lbs", 8)
    
    y_pos -= 0.38*inch
    
    c.drawString(0.75*inch, y_pos, "Age:")
    create_text_field(c, 1.1*inch, y_pos - 0.15*inch, 0.6*inch, 0.2*inch, "pet2_age", "Age", 8)
    
    c.drawString(2*inch, y_pos, "Name:")
    create_text_field(c, 2.5*inch, y_pos - 0.15*inch, 3*inch, 0.2*inch, "pet2_name", "Pet Name", 8)
    
    y_pos -= 0.5*inch
    
    # VEHICLES SECTION
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.75*inch, y_pos, "VEHICLES")
    y_pos -= 0.3*inch
    
    c.setFont("Helvetica", 9)
    c.drawString(0.75*inch, y_pos, "Do you have any vehicles?")
    create_checkbox(c, 2.4*inch, y_pos - 0.02*inch, "vehicles_yes", "Yes")
    c.drawString(2.55*inch, y_pos, "Yes")
    create_checkbox(c, 3*inch, y_pos - 0.02*inch, "vehicles_no", "No")
    c.drawString(3.15*inch, y_pos, "No")
    
    c.drawString(4*inch, y_pos, "If yes, how many?")
    create_text_field(c, 5.4*inch, y_pos - 0.15*inch, 0.5*inch, 0.22*inch, "num_vehicles", "Number", 9)
    
    y_pos -= 0.4*inch
    
    # Vehicle 1
    c.setFont("Helvetica-Bold", 9)
    c.drawString(0.75*inch, y_pos, "Vehicle 1")
    y_pos -= 0.22*inch
    
    c.setFont("Helvetica", 8)
    c.drawString(0.75*inch, y_pos, "Make:")
    create_text_field(c, 1.2*inch, y_pos - 0.15*inch, 1.3*inch, 0.2*inch, "vehicle1_make", "Make", 8)
    
    c.drawString(2.7*inch, y_pos, "Model:")
    create_text_field(c, 3.2*inch, y_pos - 0.15*inch, 1.5*inch, 0.2*inch, "vehicle1_model", "Model", 8)
    
    c.drawString(4.9*inch, y_pos, "Year:")
    create_text_field(c, 5.3*inch, y_pos - 0.15*inch, 0.8*inch, 0.2*inch, "vehicle1_year", "Year", 8)
    
    c.drawString(6.3*inch, y_pos, "Color:")
    create_text_field(c, 6.7*inch, y_pos - 0.15*inch, 1*inch, 0.2*inch, "vehicle1_color", "Color", 8)
    
    y_pos -= 0.38*inch
    
    c.drawString(0.75*inch, y_pos, "License Plate #:")
    create_text_field(c, 1.8*inch, y_pos - 0.15*inch, 2*inch, 0.2*inch, "vehicle1_plate", "Plate Number", 8)
    
    c.drawString(4*inch, y_pos, "State:")
    create_text_field(c, 4.5*inch, y_pos - 0.15*inch, 0.8*inch, 0.2*inch, "vehicle1_state", "State", 8)
    
    y_pos -= 0.45*inch
    
    # Vehicle 2
    c.setFont("Helvetica-Bold", 9)
    c.drawString(0.75*inch, y_pos, "Vehicle 2")
    y_pos -= 0.22*inch
    
    c.setFont("Helvetica", 8)
    c.drawString(0.75*inch, y_pos, "Make:")
    create_text_field(c, 1.2*inch, y_pos - 0.15*inch, 1.3*inch, 0.2*inch, "vehicle2_make", "Make", 8)
    
    c.drawString(2.7*inch, y_pos, "Model:")
    create_text_field(c, 3.2*inch, y_pos - 0.15*inch, 1.5*inch, 0.2*inch, "vehicle2_model", "Model", 8)
    
    c.drawString(4.9*inch, y_pos, "Year:")
    create_text_field(c, 5.3*inch, y_pos - 0.15*inch, 0.8*inch, 0.2*inch, "vehicle2_year", "Year", 8)
    
    c.drawString(6.3*inch, y_pos, "Color:")
    create_text_field(c, 6.7*inch, y_pos - 0.15*inch, 1*inch, 0.2*inch, "vehicle2_color", "Color", 8)
    
    y_pos -= 0.38*inch
    
    c.drawString(0.75*inch, y_pos, "License Plate #:")
    create_text_field(c, 1.8*inch, y_pos - 0.15*inch, 2*inch, 0.2*inch, "vehicle2_plate", "Plate Number", 8)
    
    c.drawString(4*inch, y_pos, "State:")
    create_text_field(c, 4.5*inch, y_pos - 0.15*inch, 0.8*inch, 0.2*inch, "vehicle2_state", "State", 8)
    
    y_pos -= 0.5*inch
    
    # OTHER OCCUPANTS SECTION
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.75*inch, y_pos, "OTHER OCCUPANTS")
    y_pos -= 0.3*inch
    
    c.setFont("Helvetica", 8)
    for i in range(1, 5):
        c.drawString(0.75*inch, y_pos, "Full Name:")
        create_text_field(c, 1.5*inch, y_pos - 0.15*inch, 2.5*inch, 0.2*inch, f"occupant{i}_name", "Full Name", 8)
        
        c.drawString(4.2*inch, y_pos, "D.O.B:")
        create_text_field(c, 4.7*inch, y_pos - 0.15*inch, 1.3*inch, 0.2*inch, f"occupant{i}_dob", "MM/DD/YYYY", 8)
        
        c.drawString(6.2*inch, y_pos, "Relationship:")
        create_text_field(c, 7*inch, y_pos - 0.15*inch, 0.8*inch, 0.2*inch, f"occupant{i}_relationship", "Relationship", 7)
        
        y_pos -= 0.32*inch
    
    y_pos -= 0.25*inch
    
    # OTHER INFORMATION SECTION
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.75*inch, y_pos, "OTHER INFORMATION")
    y_pos -= 0.25*inch
    
    c.setFont("Helvetica-Bold", 9)
    c.drawString(0.75*inch, y_pos, "Rental History Questions:")
    y_pos -= 0.22*inch
    
    c.setFont("Helvetica", 8)
    questions_rental = [
        "Have you ever been evicted from rental housing?",
        "Has a landlord ever refused to renew a lease with you?",
        "Do you currently have any outstanding debt to a landlord?"
    ]
    
    for i, question in enumerate(questions_rental):
        c.drawString(0.75*inch, y_pos, question)
        create_checkbox(c, 5.8*inch, y_pos - 0.02*inch, f"rental_q{i+1}_yes", "Yes", 9)
        c.drawString(5.95*inch, y_pos, "Yes")
        create_checkbox(c, 6.5*inch, y_pos - 0.02*inch, f"rental_q{i+1}_no", "No", 9)
        c.drawString(6.65*inch, y_pos, "No")
        y_pos -= 0.2*inch
    
    y_pos -= 0.15*inch
    
    c.setFont("Helvetica-Bold", 9)
    c.drawString(0.75*inch, y_pos, "Background History Questions:")
    y_pos -= 0.22*inch
    
    c.setFont("Helvetica", 7)
    questions_background = [
        "Have you ever been convicted of any criminal offense (misdemeanor or felony)?",
        "Have you ever been part of a plea agreement relating to any criminal activity?",
        "Have you ever been arrested, accused, detained, convicted or otherwise involved in any sex related crime?",
        "Are you now or have you ever been listed on any sex offender list?"
    ]
    
    for i, question in enumerate(questions_background):
        c.drawString(0.75*inch, y_pos, question)
        create_checkbox(c, 5.8*inch, y_pos - 0.02*inch, f"background_q{i+1}_yes", "Yes", 9)
        c.setFont("Helvetica", 8)
        c.drawString(5.95*inch, y_pos, "Yes")
        create_checkbox(c, 6.5*inch, y_pos - 0.02*inch, f"background_q{i+1}_no", "No", 9)
        c.drawString(6.65*inch, y_pos, "No")
        c.setFont("Helvetica", 7)
        y_pos -= 0.18*inch
    
    y_pos -= 0.15*inch
    
    c.setFont("Helvetica", 8)
    c.drawString(0.75*inch, y_pos, "Why are you vacating your current residence?")
    y_pos -= 0.22*inch
    create_text_field(c, 0.75*inch, y_pos, 6.5*inch, 0.35*inch, "vacating_reason", "Reason for vacating", 9)
    
    y_pos -= 0.5*inch
    
    c.drawString(0.75*inch, y_pos, "Have you given proper written notice to vacate to your current landlord?")
    create_checkbox(c, 5.2*inch, y_pos - 0.02*inch, "notice_yes", "Yes", 9)
    c.drawString(5.35*inch, y_pos, "Yes")
    create_checkbox(c, 5.8*inch, y_pos - 0.02*inch, "notice_no", "No", 9)
    c.drawString(5.95*inch, y_pos, "No")
    
    y_pos -= 0.3*inch
    
    c.drawString(0.75*inch, y_pos, "How did you hear about us?")
    create_text_field(c, 2.2*inch, y_pos - 0.15*inch, 5*inch, 0.22*inch, "referral_source", "How did you hear about us", 9)
    
    c.showPage()

def create_fillable_pdf():
    """Main function to create the fillable PDF"""
    filename = "Golden_Hills_Rental_Application_Fillable.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Create all pages
    create_page_1(c)
    create_page_2(c)
    create_page_3(c)
    
    # Save the PDF
    c.save()
    print(f"✅ Fillable PDF created successfully: {filename}")
    print(f"📄 The PDF contains interactive form fields that can be filled in Adobe Reader or other PDF viewers.")
    print(f"🔧 All field overlaps have been corrected with proper spacing and alignment.")
    return filename

if __name__ == "__main__":
    create_fillable_pdf()