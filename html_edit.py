# create html here
# add курсивный текст support
from templates import html, html2

def convert_html(file):
    # file = ''.join(file)
    pass


def create_html_1(pic_link, but_title, but_link, sec_but_title, sec_but_link,
                  aftertext, logolink, mail_name, theme, message, intext_link, intext_link_title,
                  sec_intext_link, sec_intext_link_title, listing, italic, path):
    # template to edit

    '''  # replace with <meta charset="cp1251"> for rus language'''

    # preset of html parts to edit
    cur_pic = 'https://example.top//genfiles/cms/65-29/desktop/img/big5winn3.jpg'
    cur_theme = 'CHEERS FOR THE WINNER!'
    cur_message = '''Dear User! 
                                                                                <br><br>
                                                                                You've taken the 1st place in the final prize draw of the <a href="https://example.com/promotions/big-five/">BIG 5</a> tournament and got 500 mBTC, congratulations! 
                                                                                <br><br>
                                                                                Your reward has been credited to your personal account.
                                                                                <br>'''
    cur_but_title = 'CLAIM THE PRIZE'
    cur_but_title2 = 'Join in NOW'
    cur_but_link = 'https://example.com/office/'
    cur_but_link2 = 'https://example.com/office2/'
    cur_aftertext = 'Thank you for being part of example, we appreciate every player!'
    cur_logolink = 'https://example.top/genfiles/cms/65-29/desktop/img/logo_white.png'
    find_button = '''<span class="es-button-border" style="border-style:solid;border-color:#808080;background:#E60D0D;border-width:0px;display:inline-block;border-radius:5px;width:auto;"> <a href="https://example.com/office/"                                                                    class="es-button" target="_blank"                                                                    style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:roboto, 'helvetica neue', helvetica, arial, sans-serif;font-size:15px;color:#FFFFFF;border-style:solid;border-color:#E6770E;border-width:10px 40px;display:inline-block;background:#E6770E;font-weight:normal;font-style:normal;line-height:120%;width:auto;text-align:center;border-radius: 5px;"><b>CLAIM THE PRIZE</b></a> </span>
'''
    add_button = '''<span class="es-button-border" style="border-style:solid;border-color:#808080;background:#E60D0D;border-width:0px;display:inline-block;border-radius:5px;width:auto;"> <a href="https://example.com/office/"                                                                    class="es-button" target="_blank"                                                                    style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:roboto, 'helvetica neue', helvetica, arial, sans-serif;font-size:15px;color:#FFFFFF;border-style:solid;border-color:#E6770E;border-width:10px 40px;display:inline-block;background:#E6770E;font-weight:normal;font-style:normal;line-height:120%;width:auto;text-align:center;border-radius: 5px;"><b>CLAIM THE PRIZE</b></a> </span>
<span class="es-button-border" style="border-style:solid;border-color:#808080;background:#E60D0D;border-width:0px;display:inline;border-radius:5px;width:auto;"> <a href="https://example.com/office2/"                                                                    class="es-button" target="_blank"                                                                    style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:roboto, 'helvetica neue', helvetica, arial, sans-serif;font-size:15px;color:#FFFFFF;border-style:solid;border-color:#E6770E;border-width:10px 40px;display:inline-block;background:#E6770E;font-weight:normal;font-style:normal;line-height:120%;width:auto;text-align:center;border-radius: 5px;"><b>Join in NOW</b></a> </span>
'''

    # edit preset html
    new_html = html.replace(cur_pic, pic_link)
    new_html = new_html.replace(cur_theme, theme)

    if sec_but_title != 'название второй кнопки':
        new_html = new_html.replace(find_button, add_button)

    if but_title == 'название кнопки':
        new_html = new_html.replace(find_button, ' ')

    new_html = new_html.replace(cur_but_link, but_link)
    new_html = new_html.replace(cur_but_title, but_title)

    if sec_but_title != 'название второй кнопки':
        new_html = new_html.replace(cur_but_link2, sec_but_link)
        new_html = new_html.replace(cur_but_title2, sec_but_title)

    new_message = message.replace('\n', '<br>')
    intext_link = f'<a href=\"{intext_link}\">{intext_link_title}</a>'
    sec_intext_link = f'<a href=\"{sec_intext_link}\">{sec_intext_link_title}</a>'

    new_message = new_message.replace(intext_link_title, intext_link)
    if sec_intext_link_title != 'якорь второй ссылки в тексте':
        new_message = new_message.replace(sec_intext_link_title, sec_intext_link)

    new_html = new_html.replace(cur_message, new_message)
    new_html = new_html.replace(cur_message, new_message)

    if aftertext != 'текст после кнопок':
        new_html = new_html.replace(cur_aftertext, aftertext)

    if logolink != 'ссылка под лого':
        new_html = new_html.replace(cur_logolink, logolink)

    # clean interface hints
    mailto = '<a href="mailto:support@partnersexample.com">support@partnersexample.com</a>'
    try:
        new_html = new_html.replace('support@partnersexample.com', mailto)
        new_html = new_html.replace("ссылка на картинку", "")
        new_html = new_html.replace("тема письма", "")
        new_html = new_html.replace("текст после первой картинки", "")
        new_html = new_html.replace("название кнопки", "")
        new_html = new_html.replace("ссылка под кнопку", "")
    except:
        pass
    # write new html to a file
    full_path = f'{path}/{mail_name}.html'
    new = open(full_path, 'w')
    new.write(new_html)
    new.close()


def create_html_2(pic_link, sec_pic_link, but_title, but_link, sec_but_title, sec_but_link,
                  aftertext, logolink, mail_name, theme, message, intext_link, intext_link_title,
                  sec_intext_link, sec_intext_link_title, listing, italic, path, message_2):
    # replace with <meta charset="cp1251"> for rus language

    # preset of html parts to edit
    cur_pic = 'https://example.top//genfiles/cms/65-29/desktop/img/big5winn3.jpg'
    cur_pic_2 = 'https://example.top/genfiles/cms/65-29/desktop/bonus/rules/ben-season-winners.jpg'
    cur_theme = 'CHEERS FOR THE WINNER!'
    cur_message = '''Dear User! 
                                                                                <br><br>
                                                                                You’ve taken the 1st place in the final prize draw of the <a href="https://example.com/promotions/big-five/">BIG 5</a> tournament and got 500 mBTC, congratulations! 
                                                                                <br><br>
                                                                                Your reward has been credited to your personal account.
                                                                                <br>'''
    cur_message_2 = '''Dear User! 
                                                                                <br><br>
                                                                                You’ve taken the 2st place in the final prize draw of the <a href="https://example.com/promotions/bigger-five/">BIG 5</a> tournament and got 500 mBTC, congratulations! 
                                                                                <br><br>
                                                                                Your reward has been credited to your personal account.
                                                                                <br>'''
    cur_but_title = 'CLAIM THE PRIZE'
    cur_but_title2 = 'Join in NOW'
    cur_but_link = 'https://example.com/office/'
    cur_but_link2 = 'https://example.com/office2/'
    cur_aftertext = 'Thank you for being part of example, we appreciate every player!'
    cur_logolink = 'https://example.top/genfiles/cms/65-29/desktop/img/logo_white.png'
    find_button = '''<span class="es-button-border" style="border-style:solid;border-color:#808080;background:#E60D0D;border-width:0px;display:inline-block;border-radius:5px;width:auto;"> <a href="https://example.com/office/"                                                                    class="es-button" target="_blank"                                                                    style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:roboto, 'helvetica neue', helvetica, arial, sans-serif;font-size:15px;color:#FFFFFF;border-style:solid;border-color:#E6770E;border-width:10px 40px;display:inline-block;background:#E6770E;font-weight:normal;font-style:normal;line-height:120%;width:auto;text-align:center;border-radius: 5px;"><b>CLAIM THE PRIZE</b></a> </span>
    '''
    add_button = '''<span class="es-button-border" style="border-style:solid;border-color:#808080;background:#E60D0D;border-width:0px;display:inline-block;border-radius:5px;width:auto;"> <a href="https://example.com/office/"                                                                    class="es-button" target="_blank"                                                                    style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:roboto, 'helvetica neue', helvetica, arial, sans-serif;font-size:15px;color:#FFFFFF;border-style:solid;border-color:#E6770E;border-width:10px 40px;display:inline-block;background:#E6770E;font-weight:normal;font-style:normal;line-height:120%;width:auto;text-align:center;border-radius: 5px;"><b>CLAIM THE PRIZE</b></a> </span>
    <span class="es-button-border" style="border-style:solid;border-color:#808080;background:#E60D0D;border-width:0px;display:inline;border-radius:5px;width:auto;"> <a href="https://example.com/office2/"                                                                    class="es-button" target="_blank"                                                                    style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:roboto, 'helvetica neue', helvetica, arial, sans-serif;font-size:15px;color:#FFFFFF;border-style:solid;border-color:#E6770E;border-width:10px 40px;display:inline-block;background:#E6770E;font-weight:normal;font-style:normal;line-height:120%;width:auto;text-align:center;border-radius: 5px;"><b>Join in NOW</b></a> </span>
    '''

    # edit preset html
    new_html = html2.replace(cur_pic, pic_link)
    new_html = new_html.replace(cur_pic_2, sec_pic_link)
    new_html = new_html.replace(cur_theme, theme)

    if sec_but_title != 'название второй кнопки':
        new_html = new_html.replace(find_button, add_button)

    if but_title == 'название кнопки':
        new_html = new_html.replace(find_button, ' ')

    new_html = new_html.replace(cur_but_link, but_link)
    new_html = new_html.replace(cur_but_title, but_title)

    if sec_but_title != 'название второй кнопки':
        new_html = new_html.replace(cur_but_link2, sec_but_link)
        new_html = new_html.replace(cur_but_title2, sec_but_title)

    new_message = message.replace('\n', '<br>')
    new_message_2 = message_2.replace('\n', '<br>')
    intext_link = f'<a href=\"{intext_link}\">{intext_link_title}</a>'
    sec_intext_link = f'<a href=\"{sec_intext_link}\">{sec_intext_link_title}</a>'

    new_message = new_message.replace(intext_link_title, intext_link)
    new_message_2 = new_message_2.replace(sec_intext_link_title, sec_intext_link)

    new_html = new_html.replace(cur_message, new_message)
    new_html = new_html.replace(cur_message_2, new_message_2)

    if aftertext != 'текст после кнопок':
        new_html = new_html.replace(cur_aftertext, aftertext)

    if logolink != 'ссылка под лого':
        new_html = new_html.replace(cur_logolink, logolink)

    # clean interface hints
    mailto = '<a href="mailto:support@partnersexample.com">support@partnersexample.com</a>'
    try:
        new_html = new_html.replace('support@partnersexample.com', mailto)
        new_html = new_html.replace("ссылка на картинку", "")
        new_html = new_html.replace("тема письма", "")
        new_html = new_html.replace("текст после первой картинки", "")
        new_html = new_html.replace("текст после второй картинки", "")
        new_html = new_html.replace("название кнопки", "")
        new_html = new_html.replace("ссылка под кнопку", "")
    except:
        pass
    # write new html to a file
    full_path = f'{path}/{mail_name}.html'
    new = open(full_path, 'w')
    new.write(new_html)
    new.close()


if __name__ == '__main__':
    convert_html()
