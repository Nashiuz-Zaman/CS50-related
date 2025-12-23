from fpdf import FPDF


def main():
    name = input('Name: ').strip()

    class PDF():
        def __init__(self, name, file_name):
            self._pdf = FPDF()
            self._pdf.add_page()
            self._pdf.set_font("helvetica", style="B", size=40)
            self._pdf.cell(0, 40, 'CS50 Shirtificate',
                           new_x="LMARGIN", new_y="NEXT", align='C')
            self._pdf.image("shirtificate.png", w=self._pdf.epw)
            self._pdf.set_font_size(20)
            self._pdf.set_text_color(255, 255, 255)
            self._pdf.text(x=70, y=120, text=f"{name} took CS50")
            self._pdf.output(file_name)

    pdf1 = PDF(name, 'shirtificate.pdf')


if __name__ == '__main__':
    main()
