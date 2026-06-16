from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.target_found = False

    def handle_starttag(self, tag, attrs):
        if tag == 'h1':
            self.target_found = True

    def handle_endtag(self, tag):
        if tag == 'h1':
            self.target_found = False

    def handle_data(self, data):
        if self.target_found:
            print(f"H1 Content: {data}")

parser = MyHTMLParser()
parser.feed('<html><body><h1>Head of the Page</h1><p>Paragraph content.</p></body></html>')
# Fungsi: Memfokuskan pada pengambilan data dari elemen tertentu dengan penghentian tag.
# Kondisi: Ketika Anda ingin menargetkan dan mengambil konten dari elemen spesifik.