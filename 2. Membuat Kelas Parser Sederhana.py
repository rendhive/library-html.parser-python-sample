from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Tag dibuka: {tag}, Atribut: {attrs}")

parser = MyHTMLParser()
parser.feed("<div><a href='example.com'>Link</a></div>")
# Fungsi: Mengimplementasikan kelas parser untuk menangani tag pembuka.
# Kondisi: Ketika Anda ingin berinteraksi dengan tag pembuka dalam dokumen HTML.