from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from PyPDF2 import PdfMerger
import os

def checking_tryagain_():
    while True:
        # Ask the user if they want to try again or exit
        print("\nDo you want to try again ? ")
        print("1) Try Again ")
        print("2) Exit To Main Menu ")
        Choice = (input())
        if Choice == "1":
            break
        elif Choice == "2":
            main()
        else:
            print("Invalid Choice, Please Choose 1 or 2 \n")

##############################################################################################
                           # Merge Pdfs function
            
def Merge_pdf():
    # Function to merge multiple PDFs into a single PDF
    def merge_pdfs(input_paths, output_path):
        merger = PdfMerger()

        for path in input_paths:
            merger.append(path)

        merger.write(output_path)
        merger.close()

    # Function to get a valid PDF path from the user
    def taking_path(number):
        while True:
            constant = number
            if number == 1:
                number = input("Please Enter the 1st Pdf path 'Right-click on the pdf and copy the path'\n").strip('"')
                if os.path.isfile(number) == False:
                    print(f"Error: PDF not found \n")
                    number = constant
                    continue
                else:
                    break
                
            elif number == 2: 
                number = input("Please Enter the 2nd Pdf path 'Right-click on the pdf and copy the path'\n").strip('"')
                if os.path.isfile(number) == False:
                    print(f"Error: PDF not found \n")
                    number = constant
                    continue
                else:
                    break

        return number

    def main():
        while True:
            print("###############################")
            print("######### PDF Merger ##########")
            print("###############################\n")
            First_path = taking_path(1)
            Second_path = taking_path(2)
            Merged_pdf_name = input("Please Enter the name of the merged PDF\n")
            Merged_pdf_path = input("Enter the path of the merged pdf \n")
            Merged_pdf_path = os.path.join(Merged_pdf_path, Merged_pdf_name + ".pdf" )
            merge_pdfs([First_path, Second_path], Merged_pdf_path)
            print(f"[{Merged_pdf_name}.pdf] is in >>> '{Merged_pdf_path}'\n")
            checking_tryagain_() 

    main()

##############################################################################################
                           # Extract Pdfs function
    
def Extract_pdf():
    # Function to check and return a valid page number from the user
    def check_page_num():
        while True:
            page_number = input("\nEnter the page number you want to extract: ")
            if page_number.isdigit():
                page_number = int(page_number)
                return page_number
            else:
                print("Please Enter an integer number\n")

    def main():
        while True:             
            print("###############################")
            print("######### Extract Pdf #########")
            print("###############################\n")
            while True:
                main_pdf_path = input("Please Enter the Pdf path 'Right-click on the pdf and copy the path'\n").strip('"')
                if os.path.isfile(main_pdf_path) == False:
                    print(f"Error: PDF not found \n")
                    continue
                else:
                    break

            page_number = check_page_num()
            while True:
                with open(main_pdf_path, "rb") as pdf:
                    reader = PdfReader(pdf)
                    writer = PdfWriter()
                    if 1 <= page_number <= len(reader.pages):
                        page = reader.pages[page_number - 1]  # Page numbering is 0-based
                        writer.add_page(page)
                        page_path= input("Enter the path of the extracted page: ")
                        page_name = input("\nEnter the name of the file: ")
                        page_pdf = os.path.join(page_path, page_name + ".pdf" )
                        with open(page_pdf, "wb") as page_pdf:
                            writer.write(page_pdf) 
                        print(f"\n[{page_name}.pdf] saved in >>> {page_path}")
                        checking_tryagain_()
                        break
                    else:
                        print("Invalid Page")
                        page_number = check_page_num()

    main()

##############################################################################################
                           # Split Pdfs function

def Splitter_pdf():
    # Function to get a range of pages from the user
    def get_pages_from_to():
        first_page = int(input("Enter the first page: "))
        last_page = int(input("Enter the last page: "))
        pages = list(range(first_page, last_page + 1))
        return pages

    # Function to split the PDF based on the provided page range
    def split_pdf(main_file_path, pages, splited_pdf_path):
        with open(main_file_path, "rb") as pdf:
            reader = PdfReader(pdf)
            for idx, page_num in enumerate(pages, start=1):
                if 1 <= page_num <= len(reader.pages):
                    page = reader.pages[page_num - 1]
                    writer = PdfWriter()
                    writer.add_page(page)
                    output_file = f"{os.path.splitext(splited_pdf_path)[0]}-{idx}.pdf"
                    save_pdf(writer, output_file)
                    print(f"Page {page_num} saved as [{os.path.basename(output_file)}]")

    # Function to save the split PDF
    def save_pdf(pdf_writer, file_path):
        with open(file_path, "wb") as f:
            pdf_writer.write(f)

    def main():
        while True:
            print("###############################")
            print("########## Split Pdf ##########")
            print("###############################\n")
            while True:
                main_file_path = input("Please Enter the Pdf path 'Right-click on the pdf and copy the path'\n").strip('"')
                if os.path.isfile(main_file_path) == False:
                    print(f"Error: PDF not found \n")
                    continue
                else:
                    break
            pages = get_pages_from_to()
            splited_pdf_path = input("Enter the path of the splited pdf: ")
            splited_pdf_name = input("Enter the name of the splited pdf: ")
            splited_pdf_path = os.path.join(splited_pdf_path, splited_pdf_name + ".pdf")
            split_pdf(main_file_path, pages, splited_pdf_path)
            checking_tryagain_()

    main()



##############################################################################################
                           # Main Program

def main():
    while True:
        print("***************************")
        print("*********Pdf Tools*********")
        print("***************************")
        while True:
            print("Choose Program from the following:")
            print("1) Merge two files \n2) Extract a page from file \n3) Split file into separate pages \n4) Exit")
            Choice = input()
            # Validate if the input is a digit and within the valid range
            if Choice.isdigit():
                Choice = int(Choice)
                if Choice in range(1, 5):
                    break
                else:
                    print("Please Enter a number between 1 and 4\n")
            else:
                print("Please, Enter integer\n")
        # Execute the chosen program based on the user's input
        if Choice == 1:
            Merge_pdf()
            break
        elif Choice == 2:
            Extract_pdf()
            break
        elif Choice == 3:
            Splitter_pdf()
            break
        elif Choice == 4:
            exit()

main()
