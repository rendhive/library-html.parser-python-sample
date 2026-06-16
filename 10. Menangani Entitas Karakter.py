from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print(f"Data: {data}")

parser = MyHTMLParser()
parser.feed("<div>&copy; 2023 by My Company</div>")
# Fungsi: Mengambil entitas karakter dan menampilkannya sebagai data.
# Kondisi: Ketika Anda ingin memproses teks yang mengandung karakter khusus.