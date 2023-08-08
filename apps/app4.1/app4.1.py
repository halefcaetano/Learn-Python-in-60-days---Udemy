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

pdf.output(f"/Users/halefcaetano/Desktop/python/Learn-Python-in-60-days---Udemy/apps/app4.1/Files/output.pdf")