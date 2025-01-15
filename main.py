from PyPDF2 import PdfWriter, PdfReader
import getpass
import os

# Function to validate PDF extension
def is_pdf(file_name):
    return file_name.lower().endswith('.pdf')

# Prompt user for the input file name
input_file = input("Enter the name of the PDF file to encrypt (e.g., '1.pdf'): ")

# Check if the input file exists and is a PDF
if not os.path.exists(input_file):
    print(f"Error: The file '{input_file}' does not exist.")
elif not is_pdf(input_file):
    print("Error: The file is not a PDF. Please provide a valid PDF file.")
else:
    # Prompt user for the output file name
    output_file = input("Enter the name of the output encrypted PDF (e.g., 'ho.pdf'): ")

    # Ensure the output file has a '.pdf' extension
    if not output_file.lower().endswith('.pdf'):
        print("Error: The output file must have a '.pdf' extension. Please try again.")
    else:
        # Check if the output file already exists and ask for overwrite confirmation
        if os.path.exists(output_file):
            confirm = input(f"The file '{output_file}' already exists. Do you want to overwrite it? (yes/no): ")
            if confirm.lower() != 'yes':
                print("Operation cancelled. Exiting.")
                exit()

        try:
            pdfwriter = PdfWriter()
            pdf = PdfReader(input_file)

            for page_num in range(len(pdf.pages)):
                pdfwriter.add_page(pdf.pages[page_num])

            # Prompt user for password securely
            while True:
                passw = getpass.getpass(prompt='Enter Password: ')
                confirm_passw = getpass.getpass(prompt='Confirm Password: ')
                if passw == confirm_passw:
                    break
                else:
                    print("Passwords do not match. Try again.")

            pdfwriter.encrypt(passw)

            with open(output_file, 'wb') as f:
                pdfwriter.write(f)

            print(f"PDF encrypted and saved as '{output_file}' successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")




# created by Sayan Mandal
