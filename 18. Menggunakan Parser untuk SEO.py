from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'h1':
            print("H1 Tag is found! It may be important for SEO.")

parser = MyHTMLParser()
# Memeriksa elemen penting untuk SEO dalam dokumen HTML
parser.feed("<html><body><h1>Welcome to My Page</h1></body></html>")