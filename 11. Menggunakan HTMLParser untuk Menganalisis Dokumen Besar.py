from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.record_data = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.record_data = True
            
    def handle_endtag(self, tag):
        if tag == "title":
            self.record_data = False
            
    def handle_data(self, data):
        if self.record_data:
            print(f"Title: {data}")

parser = MyHTMLParser()
parser.feed("<html><head><title>This is a Title</title></head></html>")
# Fungsi: Mengambil elemen spesifik dari dokumen besar.
# Kondisi: Ketika Anda ingin mengekstrak informasi dari dokumen yang lebih kompleks.