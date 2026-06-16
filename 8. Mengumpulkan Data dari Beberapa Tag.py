from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []

    def handle_data(self, data):
        self.data.append(data)

parser = MyHTMLParser()
parser.feed("<div>Data 1</div><div>Data 2</div>")
print(self.data)  # Menampilkan semua data yang dikumpulkan
# Fungsi: Mengumpulkan semua data dari tag yang diparsing.
# Kondisi: Ketika Anda ingin mengumpulkan data dari beberapa elemen dalam satu proses.