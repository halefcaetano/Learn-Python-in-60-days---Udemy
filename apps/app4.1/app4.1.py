import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("/Users/halefcaetano/Desktop/python/Learn-Python-in-60-days---Udemy/apps/app4.1/Files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem.capitalize()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=filename)

    with open(filepath, "r") as file:
        content = file.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output(f"/Users/halefcaetano/Desktop/python/Learn-Python-in-60-days---Udemy/apps/app4.1/Files/output.pdf")