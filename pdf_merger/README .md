# 📚 PDF Merger Tool

This project is a simple **Python script** that helps you merge multiple
PDF files into a single file.\
Users can input file names through the console, and the script will
automatically merge them into a new PDF.

------------------------------------------------------------------------

## 🚀 Features

-   Merge multiple PDF files into one\
-   Shows warning if a file is not found\
-   Easy console/terminal input\
-   Custom name for the merged file

------------------------------------------------------------------------

## 🛠️ Requirements

-   **Python 3.x**\
-   **PyPDF2** library

Install using:

``` bash
pip install PyPDF2
```

------------------------------------------------------------------------

## 📂 How to Use

1.  Open terminal/command prompt\

2.  Run the script:

    ``` bash
    python pdf_merger.py
    ```

3.  Enter PDF file names separated by commas:

        Enter PDF file names separated by commas: file1.pdf, file2.pdf, file3.pdf

4.  Enter name for the merged file:

        Enter name for the merged file: merged.pdf

5.  The script will confirm success:

        Successfully merged into 'merged.pdf'

------------------------------------------------------------------------

## 📸 Example

Input:

    Enter PDF file names separated by commas: Lecture1.pdf, Lecture2.pdf
    Enter name for the merged file: All_Lectures.pdf

Output:

    Added: Lecture1.pdf
    Added: Lecture2.pdf

    Successfully merged into 'All_Lectures.pdf'

------------------------------------------------------------------------

## ⚠️ Notes

-   File names must be correct (case-sensitive).\
-   If files are not in the same folder, provide full path.\
-   Don't forget to add `.pdf` at the end of the output file name.

------------------------------------------------------------------------

## 🤝 Contributing

Feel free to open a Pull Request or Issue if you have ideas for
improvement.

------------------------------------------------------------------------

## 📜 License

This project is released under the **MIT License**.
