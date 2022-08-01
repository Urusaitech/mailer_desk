# turn link into title
# auto-py-to-exe to compile
import re
# import main


def linktotitle(insert):
    link = ''
    try:
        text = insert.rpartition('.com')[2]  # clean the string
    except:
        pass

    link += text
    try:
        link = link.replace('/ru', '')
    except:
        pass
    text = text.replace('/', '')
    text = text.replace('line', '')

    text = re.sub(r'\d*', '', text)

    text = text.split('-')
    text.pop(0)
    first_name = text
    text = ' '.join(text)
    text = text.title()


    # main.plainTextEdit_title.toPlainText(text)


if __name__ == '__main__':
    linktotitle()
