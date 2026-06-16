from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Tag dibuka: {tag}")

parser = MyHTMLParser()
parser.feed("<html><body><h1>Title</h1><p>Paragraph</p></body></html>")
# Fungsi: Mencetak semua tag saat parsing dokumen.
# Kondisi: Ketika Anda ingin melakukan analisis lengkap terhadap semua tag yang ada di HTML.