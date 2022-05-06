class Makeparagraph:

    def __enter__(self):
        print('<h1>')

    def __exit__(self, *args):
        print('</h1>')
