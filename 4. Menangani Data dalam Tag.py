from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print(f"Data: {data}")

parser = MyHTMLParser()
parser.feed("<div>Ini adalah contoh data.</div>")
# Fungsi: Mengambil dan mencetak data yang ada di dalam tag.
# Kondisi: Ketika Anda ingin mengumpulkan teks dalam tag tertentu.