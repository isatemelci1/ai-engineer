
from fpdf import FPDF


class Shirtificate(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 30)
        self.set_text_color(0, 0, 0)
        self.set_y(15)
        self.cell(0, 20, "CS50 Shirtificate", align="C")


def main():
    name = input("Name: ")

    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    # Center the shirt image horizontally.
    pdf.image("shirtificate.png", x=0, y=55, w=210)

    # Overlay the name in white text.
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(140)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
