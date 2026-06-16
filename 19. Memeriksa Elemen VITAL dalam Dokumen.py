from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'meta':
            attrs_dict = dict(attrs)
            if attrs_dict.get('name') == 'description':
                print(f"Meta description found: {attrs_dict.get('content')}")

parser = MyHTMLParser()
parser.feed('<html><head><meta name="description" content="This is a test page"></head></html>')
# Fungsi: Mencari elemen yang penting seperti meta description.
# Kondisi: Ketika Anda memerlukan data meta dalam analisis dokumen HTML.