from myclass import Tag, TopLevelTag, HTML

with HTML(output='test.html') as doc:
    with TopLevelTag("head") as head:
        with Tag("title") as title:
            title.text = "hello"
            head.children.append(title)
        doc.children.append(head)

    with TopLevelTag("body") as body:
        with Tag("h1", klass=("main-text",)) as h1:
            h1.text = "Test"
            body.children.append(h1)

        with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
            with Tag("p") as paragraph:
                paragraph.text = "Another text"
                div.children.append(paragraph)

            with Tag("img", is_single=True, src="icon.png", data_image="responsive") as img:
                div.children.append(img)

            body.children.append(div)

        doc.children.append(body)