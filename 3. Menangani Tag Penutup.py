from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_endtag(self, tag):
        print(f"Tag ditutup: {tag}")

parser = MyHTMLParser()
parser.feed("<div><a href='example.com'>Link</a></div>")
# Fungsi: Mengimplementasikan kelas parser untuk menangani tag penutup.
# Kondisi: Ketika Anda ingin berinteraksi dengan tag penutup dalam dokumen HTML.