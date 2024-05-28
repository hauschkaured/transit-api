class Feed:
    def __init__(self, publisher, url, lang, start, end, version):
        self.publisher = publisher
        self.url = url
        self.lang = lang
        self.start = start
        self.end = end
        self.version = version

    def __repr__(self):
        return f'''PUB {self.publisher} URL {self.url} LANG {self.lang} \n
        ST {self.start} END {self.end} VER {self.version}'''


def agency(foo):
    print(foo)
    if foo == "pgh":
        text = open("static/pittsburgh/agency.txt", "r")
        text_reading(text)
    elif foo == "satx":
        text = open("static/san_antonio/agency.txt", "r")
        text_reading(text)


def text_reading(text):
    textdata = text.read()
    data = textdata.splitlines()
    info = data[1]
    item_list = info.split(',')

    publisher = item_list[0]
    url = item_list[1]
    lang = item_list[2]
    start = item_list[3]
    end = item_list[4]
    version = item_list[5]

    obj = Feed(publisher, url, lang, start, end, version)
    print(obj)
    return obj
