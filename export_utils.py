import re
from fpdf import FPDF

import re
from io import BytesIO

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = text.replace("–", "-").replace("—", "-")
    text = text.replace("“", '"').replace("”", '"').replace("’", "'")
    text = re.sub(r"[^\x00-\xFF]+", "", text)
    return text


class PDFReport(FPDF):
    def __init__(self, orientation="P", unit="mm", format="A4"):
        super().__init__(orientation, unit, format)
        self.set_auto_page_break(auto=True, margin=15)
        self.set_font("Times", "", 12)

    def header(self):
        self.set_font("Times", "B", 14)
        self.cell(0, 10, "Research Paper Insights Report", ln=True, align="C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Times", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)


    def write_markdown(self, text: str):
        if not text:
            return
        tokens = re.split(r'(\*\*.*?\*\*|\*.*?\*)', text)

        for token in tokens:
            if not token:
                continue
            token = clean_text(token)

            if token.startswith("**") and token.endswith("**"):
                self.set_font("Times", "I", 11)
                self.write(8, token[2:-2])  # remove **..**
            elif token.startswith("*") and token.endswith("*"):
                self.set_font("Times", "B", 11)
                self.write(8, token[1:-1])  # remove *..*
            else:
                self.set_font("Times", "", 11)
                self.write(8, token)

        self.ln(10)

   

    def chapter_body(self, body):
        # Process multi-line body with Markdown support
        for line in body.splitlines():
            self.write_markdown(line)

    def add_pdf_summary(self, file_name, summary, tags=None, relevance=None):
        self.add_page()
        self.chapter_title(f"File: {file_name}")

        if summary:
            self.chapter_title("Summary:")
            self.chapter_body(summary)

        if tags:
            self.chapter_title("Tags:")
            self.chapter_body(tags)

        if relevance:
            self.chapter_title("Relevance Info:")
            self.chapter_body(relevance)

    def clear(self):
        """Reset PDF so a new report starts fresh"""
        self.__init__()  # reinitialize

    def save(self, file_path="Final_Report.pdf"):
        self.output(file_path)
        return file_path


