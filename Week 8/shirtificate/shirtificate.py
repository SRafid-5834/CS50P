# CS50 Shirtificate


from fpdf import FPDF


class Shirtificate:

    def __init__(self, name):
        self.name = name
        self.pdf(self.name)

    @classmethod
    def get_input(cls):
        name = input("Name: ").strip()
        return cls(name)

    @staticmethod
    def pdf(name):
        pdf = FPDF()
        pdf.add_page(orientation="portrait", format="a4")
        pdf.set_auto_page_break(auto=False, margin=0)

        pdf.set_font("Helvetica", "", 48)
        pdf.cell(0, 58, text="CS50 Shirtificate", align="C", center=True, new_x="LMARGIN")

        pdf.image("shirtificate.png", x=10, y=70, w=190)

        pdf.set_font("Helvetica", size=24)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 250, align="C", text=f"{name} took CS50")

        pdf.output("shirtificate.pdf")


def main():
    Shirtificate.get_input()


if __name__ == "__main__":
    main()
