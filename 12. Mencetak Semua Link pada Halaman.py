from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get('href', None)
            if href:
                print(f"Link: {href}")

parser = MyHTMLParser()
parser.feed("<html><body><a href='http://example.com'>Link 1</a><a href='http://example.org'>Link 2</a></body></html>")
# Fungsi: Mengambil dan mencetak semua link (href) pada halaman.
# Kondisi: Ketika Anda ingin menganalisis dan mengumpulkan data link dalam dokumen HTML.