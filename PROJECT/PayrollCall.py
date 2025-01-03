import tkinter as tk
from PayrollClass import DesignGUI

# Initialize the main window and the DesignGUI instance
window = tk.Tk()
design = DesignGUI(window)

# Create a class that will display design
class DisplayGUI:
    def create_header_section(self):
        # Header Section
        header_frame = design.frame(0, 0, 855, 100)
        design.label("SE-RI'S PAYROLL CHOICE", 172, 25, font=('Algerian', 33, 'bold'), bg_color='#f6f6f6')

    def create_basic_info_section(self):
        # Employee Basic Info
        design.label('EMPLOYEE BASIC INFO', 40, 130, font=('Segoe UI', 12, 'bold'))
        image_path = 'C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\PROFILE2.jpg'
        design.add_image(65, 160, image_path)

        # Left Side
        design.label('Employee Number:', 65, 270)
        design.entry(220, 270, width=27)
        design.label('Search Employee:', 65, 300)
        design.button('SEARCH', 220, 300, width=16, bg='red', fg='white')
        design.label('Department:', 65, 330)
        design.entry(220, 330, width=27)

        # Right Side
        fields_right = [
            ('First Name:', 140),
            ('Middle Name:', 170),
            ('Surname:', 200),
            ('Civil Status:', 230),
            ('Qualified Dependents:', 260),
            ('Pay Date:', 290),
            ('Employee Status:', 320),
            ('Designation:', 350),
        ]
        for label, y in fields_right:
            design.label(label, 470, y)
            design.entry(640, y, width=27)

    def create_income_section(self):
        # Income Sections
        income_sections = [
            ('BASIC INCOME', 390),
            ('Rate / Hour:', 420),
            ('No. of Hours / Cut Off:', 450),
            ('Income / Cut Off:', 480),
            ('HONORARIUM INCOME', 540),
            ('Rate / Hour:', 570),
            ('No. of Hours / Cut Off:', 600),
            ('Income / Cut Off:', 630),
            ('OTHER INCOME', 690),
            ('Rate / Hour:', 720),
            ('No. of Hours / Cut Off:', 750),
            ('Income / Cut Off:', 780),
            ('SUMMARY INCOME', 840),
            ('Gross Income:', 870),
            ('Net Income:', 900),
        ]
        for label, y in income_sections:
            if 'INCOME' in label or 'SUMMARY INCOME' in label:
                design.label(label, 50, y, font=('Segoe UI', 12, 'bold'))
            else:
                design.label(label, 65, y)
                design.entry(220, y, width=27)

    def create_deduction_section(self):
        # Deduction Sections
        deduction_start_y = 415
        deduction_sections = [
            ('REGULAR DEDUCTIONS', deduction_start_y),
            ('SSS Contribution:', deduction_start_y + 30),
            ('PhilHealth Contribution:', deduction_start_y + 60),
            ('Pag-IBIG Contribution:', deduction_start_y + 90),
            ('Income Tax Contribution:', deduction_start_y + 120),
            ('OTHER DEDUCTIONS', deduction_start_y + 175),
            ('SSS Loan:', deduction_start_y + 205),
            ('Pag-IBIG Loan:', deduction_start_y + 235),
            ('Faculty Savings Deposit:', deduction_start_y + 265),
            ('Faculty Savings Loan:', deduction_start_y + 295),
            ('Salary Loan:', deduction_start_y + 325),
            ('Other Loans:', deduction_start_y + 355),
            ('DEDUCTION SUMMARY', deduction_start_y + 410),
            ('Total Deductions:', deduction_start_y + 440),
        ]
        for label, y in deduction_sections:
            if 'DEDUCTIONS' in label or 'DEDUCTION SUMMARY' in label:
                design.label(label, 455, y, font=('Segoe UI', 12, 'bold'))
            else:
                design.label(label, 470, y)
                design.entry(640, y, width=27)

    def create_buttons(self):
        # Buttons
        design.button('GROSS INCOME', 455, 900, width=13, bg='#1379ab', fg='white')
        design.button('NET INCOME', 542, 900, width=13, bg='#1379ab', fg='white')
        design.button('SAVE', 630, 900, width=8, bg='#13abab', fg='white')
        design.button('UPDATE', 692, 900, width=8, bg='#13abab', fg='white')
        design.button('NEW', 755, 900, width=8, bg='#edd324', fg='black')

# Create an instance of DisplayGUI
payroll_gui = DisplayGUI()

# Call the methods from DisplayGUI instance
payroll_gui.create_header_section()
payroll_gui.create_basic_info_section()
payroll_gui.create_income_section()
payroll_gui.create_deduction_section()
payroll_gui.create_buttons()

# Runs the code
window.mainloop()