# Merge Multiple PDF Files into One

from PyPDF2 import PdfMerger
import os


files = input("Enter PDF file names separated by commas: ").split(",")
files_list = [f.strip() for f in files]


new_file = input("Enter name for the merged file: ")


merger = PdfMerger()
for f in files_list:
    if os.path.exists(f):
        merger.append(f)
        print(f"Added: {f}")
    else:
        print(f"File not found: {f}")

merger.write(new_file)
merger.close()

print(f"\nSuccessfully merged into '{new_file}'")
