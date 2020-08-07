class HTML:
    def __init__(self, output):
        """Обязательный аргумент output, в нем указываем имя html-файла"""
        self.output = output
        self.children = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """На выходе создаем переменную, в которой открываем наш html-файл
        в него записываем все теги с аргументами и текстом"""
        myhtml = open(self.output, 'w', encoding='utf-8')
        print('<html>', file=myhtml)
        for child in self.children:
            print(child, file=myhtml)
        print('</html>', file=myhtml)
        myhtml.close()


class TopLevelTag:
    def __init__(self, tagname):
        self.tagname = tagname
        self.children = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __str__(self):
        if self.children:
            opening = f'\t<{self.tagname}>\n'  # для записи в переменную используем f-строки
            internal = ''
            for child in self.children:
                internal += str(child)
            ending = f'\n\t</{self.tagname}>'
            return opening + internal + ending
        else:
            return f'<\t{self.tagname}></{self.tagname}>'


class Tag(TopLevelTag):
    def __init__(self, tagname, is_single=False, klass=None, **kwargs):
        self.tagname = tagname
        self.text = ''
        self.attributes = {}
        self.is_single = is_single
        self.children = []

        if klass is not None:
            self.attributes['class'] = ' '.join(klass)

        for attr, value in kwargs.items():
            if "_" in attr:
                attr = attr.replace("_", "-")
            self.attributes[attr] = value

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append(f' {attribute}="{value}"')
        attrs = "".join(attrs)

        if self.children:
            opening = f'\t\t<{self.tagname}{attrs}>\n'
            internal = f'{self.text}'
            for child in self.children:
                internal += str(child)
            ending = f'\n\t\t</{self.tagname}>'
            return opening + internal + ending
        else:
            if self.is_single:
                return f'\t\t<{self.tagname}{attrs}>'
            else:
                return f'\t\t<{self.tagname}{attrs}>{self.text}</{self.tagname}>\n'
