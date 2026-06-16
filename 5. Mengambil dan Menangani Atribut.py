from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if attrs:
            for attr in attrs:
                print(f"Atribut {attr[0]}: {attr[1]}")

parser = MyHTMLParser()
parser.feed("<img src='image.jpg' alt='gambar'>")
# Fungsi: Mengambil atribut dari tag HTML.
# Kondisi: Ketika Anda ingin mendapatkan informasi dalam atribut dari tag tertentu.