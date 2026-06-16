from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'script':
            print(f"Tag dibuka: {tag}")

parser = MyHTMLParser()
parser.feed("<div><script>console.log('test');</script></div>")
# Fungsi: Mengabaikan tag tertentu saat parsing.
# Kondisi: Ketika Anda tidak ingin memproses tag tertentu dalam HTML.