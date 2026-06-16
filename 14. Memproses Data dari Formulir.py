from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "input":
            name = dict(attrs).get('name', None)
            value = dict(attrs).get('value', None)
            print(f"Form Input: {name} with value: {value}")

parser = MyHTMLParser()
parser.feed('<form><input type="text" name="username" value="user1"><input type="password" name="password" value="pass123"></form>')
# Fungsi: Mengambil data dari input formulir di dalam HTML.
# Kondisi: Ketika Anda perlu menganalisis data input dalam formulir.