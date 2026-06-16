from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Tag dibuka: {tag}")

parser = MyHTMLParser()
parser.feed("<div><a href='example.com'>Link")
# Fungsi: Menangani kesalahan parsing karena tag yang tidak tertutup.
# Kondisi: Ketika Anda mengalami HTML yang tidak valid.