from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if "discard" not in data:
            print(f"Valid Data: {data}")

parser = MyHTMLParser()
parser.feed("<div>Valid Data 1</div><div>discard this</div><div>Valid Data 2</div>")
# Fungsi: Memfilter teks tertentu saat mem-parsing HTML.
# Kondisi: Ketika Anda ingin mengabaikan data yang tidak relevan.