def wrap_in_html_tag(tag, content):

    valid_tags = {'a', 'abbr', 'b', 'body', 'caption', 'cite', 'code', 'div', 
                  'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'i', 's'}

    if tag in valid_tags:
        return f"{content}"
    else:
        return "Введён неверный тег"

tag = input("Введите тег: ")
content = input("Введите строку: ")
result = wrap_in_html_tag(tag, content)
print(result)
