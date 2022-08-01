# turn link into title
# auto-py-to-exe to compile
import re


def linktotitle():
    start = input("\nEnter link\n")
    link = ''

    try:
        text = start.rpartition('.com')[2]  # clean the string
    except:
        print("Wrong link format")
        pass

    link += text
    try:
        link = link.replace('/ru', '')
    except:
        pass
    text = text.replace('/', '')
    text = text.replace('line', '')

    # sport = str(re.search('(\w*\d+)', text).group(1))
    # sport = re.sub(r'[^\w\s]+|\d+', r'', sport).strip()
    text = re.sub(r'\d*', '', text)

    text = text.split('-')
    text.pop(0)
    first_name = text
    text = ' '.join(text)
    text = text.title()
    print(first_name)
    # choose correct one
    # sports = ['tennis', 'football', 'basketball', 'ice-hockey', 'esports']

    print(f'\nTitle: \n{text}')
    print(f'Link: \n{link}')


while True:
    linktotitle()
