
# Context manager class Create a class “Makeparagraph” that “decorates” a text with an html <p> tag.


class MakeParagraph:

    def __enter__(self):
        print('<h1>', end='')

    def __exit__(self, *args):
        print('</h1>', end='')
