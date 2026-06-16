from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_error(self, error):
        print(f"Error: {error}")

parser = MyHTMLParser()
parser.feed("<div><p>Paragraph <div><p>Invalid</p>")  # Input berantakan
# Fungsi: Menangani kesalahan saat parsing HTML yang tidak valid.
# Kondisi: Ketika Anda menghadapi HTML yang tidak terformat dengan baik.