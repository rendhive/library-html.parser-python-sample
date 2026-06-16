from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print(f"Komentar: {data}")

parser = MyHTMLParser()
parser.feed("<div><!-- Ini komentar --></div>")
# Fungsi: Mengambil komentar dalam HTML.
# Kondisi: Ketika Anda ingin memproses atau mengabaikan komentar dalam dokumen HTML.