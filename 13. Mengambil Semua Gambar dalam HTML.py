from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            src = dict(attrs).get('src', None)
            print(f"Image source: {src}")

parser = MyHTMLParser()
parser.feed("<html><body><img src='image1.jpg'><img src='image2.png'></body></html>")
# Fungsi: Mengumpulkan semua sumber gambar dari dokumen HTML.
# Kondisi: Ketika Anda ingin menganalisis semua gambar dalam dokumen HTML.