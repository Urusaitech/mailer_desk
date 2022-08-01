# create html
# курсивный текст

def convert_html(file):
    #file = ''.join(file)
    pass


def create_html_1(pic_link, but_title, but_link, sec_but_title, sec_but_link,
                aftertext, logolink, mail_name, theme, message, intext_link, intext_link_title,
                sec_intext_link, sec_intext_link_title, listing, italic, path):

    html = '''
    <!DOCTYPE html>
<html style="width:100%;font-family: Tahoma, Geneva, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0;">

<head>
    <meta charset="cp1251">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <meta name="x-apple-disable-message-reformatting">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="telephone=no" name="format-detection">
    <title></title>
    <style type="text/css">
        @-ms-viewport {
            width: device-width;
        }
        
        @media only screen and (max-width: 600px) {
            p,
            ul li,
            ol li,
            a {
                font-size: 16px !important
            }
            h1 {
                font-size: 30px !important;
                text-align: center
            }
            h2 {
                font-size: 26px !important;
                text-align: center
            }
            h3 {
                font-size: 20px !important;
                text-align: center
            }
            h1 a {
                font-size: 30px !important
            }
            h2 a {
                font-size: 26px !important
            }
            h3 a {
                font-size: 20px !important
            }
            .es-menu td a {
                font-size: 13px !important
            }
            .es-header-body p,
            .es-header-body ul li,
            .es-header-body ol li,
            .es-header-body a {
                font-size: 16px !important
            }
            .es-footer-body p,
            .es-footer-body ul li,
            .es-footer-body ol li,
            .es-footer-body a {
                font-size: 16px !important
            }
            .es-infoblock p,
            .es-infoblock ul li,
            .es-infoblock ol li,
            .es-infoblock a {
                font-size: 12px !important
            }
            *[class="gmail-fix"] {
                display: none !important
            }
            .es-m-txt-c,
            .es-m-txt-c h1,
            .es-m-txt-c h2,
            .es-m-txt-c h3 {
                text-align: center !important
            }
            .es-m-txt-r,
            .es-m-txt-r h1,
            .es-m-txt-r h2,
            .es-m-txt-r h3 {
                text-align: right !important
            }
            .es-m-txt-l,
            .es-m-txt-l h1,
            .es-m-txt-l h2,
            .es-m-txt-l h3 {
                text-align: left !important
            }
            .es-m-txt-r img,
            .es-m-txt-c img,
            .es-m-txt-l img {
                display: inline !important
            }
            .es-button-border {
                display: block !important
            }
            .es-button {
                font-size: 16px !important;
                display: block !important;
                border-left-width: 0px !important;
                border-right-width: 0px !important
            }
            .es-btn-fw {
                border-width: 10px 0px !important;
                text-align: center !important
            }
            .es-adaptive table,
            .es-btn-fw,
            .es-btn-fw-brdr,
            .es-left,
            .es-right {
                width: 100% !important
            }
            .es-content table,
            .es-header table,
            .es-footer table,
            .es-content,
            .es-footer,
            .es-header {
                width: 100% !important;
                max-width: 600px !important
            }
            .es-adapt-td {
                display: block !important;
                width: 100% !important
            }
            .adapt-img {
                width: 100% !important;
                height: auto !important
            }
            .es-m-p0 {
                padding: 0px !important
            }
            .es-m-p0r {
                padding-right: 0px !important
            }
            .es-m-p0l {
                padding-left: 0px !important
            }
            .es-m-p0t {
                padding-top: 0px !important
            }
            .es-m-p0b {
                padding-bottom: 0 !important
            }
            .es-m-p20b {
                padding-bottom: 20px !important
            }
            .es-mobile-hidden,
            .es-hidden {
                display: none !important
            }
            .es-desk-hidden {
                display: table-row !important;
                width: auto !important;
                overflow: visible !important;
                float: none !important;
                max-height: inherit !important;
                line-height: inherit !important
            }
            .es-desk-menu-hidden {
                display: table-cell !important
            }
            table.es-table-not-adapt,
            .esd-block-html table {
                width: auto !important
            }
            table.es-social {
                display: inline-block !important
            }
            table.es-social td {
                display: inline-block !important
            }
        }
        
        #outlook a {
            padding: 0;
        }
        
        .ExternalClass {
            width: 100%;
        }
        
        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
            line-height: 100%;
        }
        
        .es-button {
            mso-style-priority: 100 !important;
            text-decoration: none !important;
        }
        
        a[x-apple-data-detectors] {
            color: inherit !important;
            text-decoration: none !important;
            font-size: inherit !important;
            font-family: inherit !important;
            font-weight: inherit !important;
            line-height: inherit !important;
        }
        
        .es-desk-hidden {
            display: none;
            float: left;
            overflow: hidden;
            width: 0;
            max-height: 0;
            line-height: 0;
            mso-hide: all;
        }

    </style>
</head>

<body style="width:100%;font-family: Tahoma, Geneva, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0;">
    <div class="es-wrapper-color" style="background-color:#151515;">
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top;">
            <tbody>
                <tr style="border-collapse:collapse;">
                    <td valign="top" style="padding:0;Margin:0;">
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td class="es-adaptive" align="center" style="padding:0;Margin:0;">

                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
                            <tbody>
                                <tr style="border-collapse:collapse;"></tr>
                                <tr style="border-collapse:collapse;">
                                    <td class="es-adaptive" align="center" style="padding:0;Margin:0;">
                                        <table class="es-header-body" width="600" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td style="padding:0;Margin:0;padding-left:20px;padding-right:20px;background-image:url(https://undergroundev.com/stock-img/bg-footer.jpg);background-color:#444444;background-position:left top;background-repeat:no-repeat;" bgcolor="#444444" align="left">
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td class="es-m-p0r" width="174" valign="top" align="center" style="padding:0;Margin:0;">
                                                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td class="es-m-p0l es-m-txt-c" align="left" style="padding:0;Margin:0;">
                                                                                        <a href="#logo-link#" target="_blank" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family: Tahoma, Geneva, sans-serif;font-size:14px;text-decoration:underline;color:#333333;"><img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/logo_white.png" alt="" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;padding:7%;" width="160"></a>
                                                                                    </td>
                                                                                </tr>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                        </table>
                                                        <table cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tr style="border-collapse:collapse;">
                                                                <td width="366" align="left" style="padding:0;Margin:0;">
                                                                    <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;border-left:0px solid #808080;border-right:0px solid #808080;border-top:0px solid #808080;border-bottom:0px solid #808080;" width="100%" cellspacing="0" cellpadding="0">
                                                                        <tr style="border-collapse:collapse;">
                                                                            <td style="padding:0;Margin:0;">
                                                                                <table class="es-menu" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">

                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                        </table>
                                    </td>
                                </tr>
                        </table>
                    </td>
                </tr>
                </tbody>
        </table>
        <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
            <tbody>
                <tr style="border-collapse:collapse;">
                    <td align="center" style="padding:0;Margin:0;">
                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td align="left" style="padding:0;Margin:0;">
                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td width="600" align="center" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td align="center" style="padding:0;Margin:0;">
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                <tr style="border-collapse:collapse;">
                                    <td align="left" style="padding:0;Margin:0;padding-left:20px;padding-right:20px;">
                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td width="560" valign="top" align="center" style="padding:0;Margin:0;">
                                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">

                                                                    <!-- Заголовок !-->
                                                                    <td align="left" style="padding:0;Margin:0;padding: 19px 19px">
                                                                        <h2 style="Margin-top: 20px;line-height:50%;mso-line-height-rule:exactly;font-size:20px;font-style:normal;font-weight:normal;text-align:center;">
                                                                            <b>CHEERS FOR THE WINNER!</b>
                                                                        </h2>
                                                                    </td>
                                                                    <!-- /Заголовок !-->

                                                                </tr>
                                                                <tr style="border-collapse:collapse;">

                                                                    <!-- Ссылка на картинку !-->
                                                                        <td align="left" style="padding:0;Margin:0;">
                                                                            <img src="https://1xbitdjqrc.top//genfiles/cms/65-29/desktop/img/big5winn3.jpg" style="width: 100%; margin-bottom: 2%;margin-top: 2%;" alt="" />
                                                                        </td>
                                                                    <!-- /Ссылка на картинку !-->

                                                                </tr>

                                                                <tr style="border-collapse:collapse;">
                                                                    <td class="es-m-txt-c" align="left" style="border-left:2px solid #e6770e;padding:0 0 0 18px;Margin:0;padding-top:10px;padding-bottom:0;color:black;font-size:18px;">

                                                                        <!-- Абзацы !-->
                                                                            <p style="line-height: 1.5;color:#333333;font-size:16px;">
                                                                                Dear User! 
                                                                                <br><br>
                                                                                You've taken the 1st place in the final prize draw of the <a href="https://1xbit.com/promotions/big-five/">BIG 5</a> tournament and got 500 mBTC, congratulations! 
                                                                                <br><br>
                                                                                Your reward has been credited to your personal account.
                                                                                <br>

                                                                            </p>
                                                                        <!-- /Абзацы !-->

                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <br>

<span class="es-button-border" style="border-style:solid;border-color:#808080;background:#E60D0D;border-width:0px;display:inline-block;border-radius:5px;width:auto;"> <a href="https://1xbit.com/office/"                                                                    class="es-button" target="_blank"                                                                    style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:roboto, 'helvetica neue', helvetica, arial, sans-serif;font-size:15px;color:#FFFFFF;border-style:solid;border-color:#E6770E;border-width:10px 40px;display:inline-block;background:#E6770E;font-weight:normal;font-style:normal;line-height:120%;width:auto;text-align:center;border-radius: 5px;"><b>CLAIM THE PRIZE</b></a> </span>

                                                        <!-- Текст после кнопки !-->
                                                            <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:16px;font-family: Tahoma, Geneva, sans-serif;line-height:150%;color:#333333;">
                                                                Thank you for being part of 1xBit, we appreciate every player!</a>
                                                            </p>
                                                        <!-- /Текст после кнопки !-->

                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
        <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
            <tbody>
                <tr style="border-collapse:collapse;">
                    <td align="center" style="padding:0;Margin:0;">
                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td align="left" style="padding:0;Margin:0;padding-top:0px;padding-left:20px;padding-right:20px;">
                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td width="560" valign="top" align="center" style="padding:0;Margin:0;">
                                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td align="center" style="padding:0;Margin:0;padding-top:0px;">
                                                                        <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td style="padding:0;Margin:0px 0px 0px 0px;border-bottom:1px solid #CCCCCC;background:none;height:1px;width:100%;margin:0px;">
                                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:16px;font-family: Tahoma, Geneva, sans-serif;line-height:150%;color:#333333;">
                                                                                            Sincerely,
                                                                                            <br> 1xBit Team
                                                                                        </p>
                                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family: Tahoma, Geneva, sans-serif;line-height:150%;color:#9b9b9b;">
                                                                                            
                                                                                            <br>

                                                                                        </p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
        <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
            <tbody>
                <tr style="border-collapse:collapse;">
                    <td align="center" style="padding:0;Margin:0;">
                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td align="left" style="padding:0;Margin:0;padding-left:20px;padding-right:20px;">
                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td width="560" valign="top" align="center" style="padding:0;Margin:0;">
                                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">

                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
        <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
            <tbody>
                <tr style="border-collapse:collapse;"></tr>
                <tr style="border-collapse:collapse;">
                    <td class="es-adaptive" align="center" style="padding:0;Margin:0;">
                        <table class="es-header-body" width="600" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td style="padding:0;Margin:0;background-image:url(http://1xbet.email/upload/files/unnamed%20%281%29.jpg);background-color:#FFFFFF;background-position:left top;background-repeat:no-repeat;" bgcolor="#ffffff" align="left">
                                        <table cellspacing="0" cellpadding="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td class="es-m-p0r" width="600" valign="top" align="center" style="padding:0;Margin:0;">
                                                        <tbody>
                                                            <tr style="border-collapse:collapse;">
                                                                <td align="left" style="padding:0;Margin:0;">
                                                                    <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family: Tahoma, Geneva, sans-serif;line-height:150%;color:#333333;">
                                                                        <br>
                                                                    </p>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                        </table>
                                        </td>
                                        </tr>
                                        </tbody>
                        </table>
                        </td>
                        </tr>
                        </tbody>
        </table>
        <table class="es-footer" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top;">
            <tbody>
                <tr style="border-collapse:collapse;">
                    <td align="center" style="padding:0;Margin:0;">
                        <table class="es-footer-body" width="600" cellspacing="0" cellpadding="0" align="center" bgcolor="#444444" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#444444;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td class="esdev-adapt-off" align="left" bgcolor="#444444" style="padding:0;Margin:0;padding-left:20px;padding-right:20px;background-color:#444444;">
                                        <table cellspacing="0" cellpadding="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td width="560" valign="top" align="center" style="padding:0;Margin:0;">
                                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td align="center" style="padding:0;Margin:0;">
                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:12px;font-family: Tahoma, Geneva, sans-serif;line-height:150%;color:#BCBABA;">
                                                                            Follow us:</p>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                <tr style="border-collapse:collapse;">
                                    <td class="esdev-adapt-off" align="left" style="padding:0;Margin:0;padding-top:10px;padding-left:20px;padding-right:20px;;padding-bottom:10px;">
                                        <table width="560" cellpadding="0" cellspacing="0" class="esdev-mso-table" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td class="esdev-mso-td" width="29.642857142857146%" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" align="left" class="es-left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td width="194" align="left" style="padding:0;Margin:0;">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="left" style="padding:0;Margin:0;"></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>

                                                    <td class="esdev-mso-td" width="6.964285714285714%" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td width="39" align="left" style="padding:0;Margin:0;">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="center" style="padding:0;Margin:0;padding-left:5px;padding-right:5px;">
                                                                                        <a target="_blank" href="https://www.instagram.com/1xbit/" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family: Tahoma, Geneva, sans-serif;font-size:14px;text-decoration:underline;color:#FFFFFF;">
                                                                                            <img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/ig_logo.png" alt="inst" style="border:2px solid white;border-radius:50%;display:block;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="40">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>

                                                            </tbody>
                                                        </table>
                                                    </td>
                                                    <td class="esdev-mso-td" width="6.964285714285714%" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td width="39" align="left" style="padding:0;Margin:0;">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="center" style="padding:0;Margin:0;padding-left:5px;padding-right:5px;">
                                                                                        <a target="_blank" href="https://www.reddit.com/r/1xBit_gambling/" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family: Tahoma, Geneva, sans-serif;font-size:14px;text-decoration:underline;color:#FFFFFF;">
                                                                                            <img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/reddit-logo.png" alt="rddt" style="border:2px solid white;border-radius:50%;display:block;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="40">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>

                                                            </tbody>
                                                        </table>
                                                    </td>
                                                    <td class="esdev-mso-td" width="6.964285714285714%" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td width="39" align="left" style="padding:0;Margin:0;">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="center" style="padding:0;Margin:0;padding-left:10px;">
                                                                                        <a target="_blank" href="https://twitter.com/1x_bit" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family: Tahoma, Geneva, sans-serif;font-size:14px;text-decoration:underline;color:#FFFFFF;">
                                                                                            <img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/tw_logo.png" alt="" style="border:2px solid white;border-radius:50%;display:block;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="40">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                    <td class="esdev-mso-td" width="6.964285714285714%" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td width="39" align="left" style="padding:0;Margin:0;">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="right" style="padding:0;Margin:0;padding-left:10px;">
                                                                                        <a target="_blank" href="https://t.me/sportsbook_1xBit" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family: Tahoma, Geneva, sans-serif;font-size:14px;text-decoration:underline;color:#FFFFFF;">
                                                                                            <img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/tg_logo.png" alt="teleg" style="border:2px solid white;border-radius:50%;display:block;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="40">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                    <td class="esdev-mso-td" width="6.964285714285714%" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td width="39" align="left" style="padding:0;Margin:0;">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="right" style="padding:0;Margin:0;padding-left:10px;">
                                                                                        <a target="_blank" href="https://www.youtube.com/c/1xBit/videos" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family: Tahoma, Geneva, sans-serif;font-size:14px;text-decoration:underline;color:#FFFFFF;">
                                                                                            <img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/yt_logo.png" alt="" style="border:2px solid white;border-radius:50%;display:block;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="40">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                                                        <td class="esdev-mso-td" width="6.964285714285714%" valign="top" style="padding:0;Margin:0;">
                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left"
                                               style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                            <tbody>
                                            <tr style="border-collapse:collapse;">
                                                <td width="39" align="left" style="padding:0;Margin:0;">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                           style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                        <tbody>
                                                        <tr style="border-collapse:collapse;">
                                                            <td align="center" style="padding:0;Margin:0;padding-left:10px;padding-right:10px;"><a target="_blank"
                                                                                                                                                 href="https://www.trustpilot.com/evaluate/1xbit.com"
                                                                                                                                                 style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family: Tahoma, Geneva, sans-serif;font-size:14px;text-decoration:underline;color:#FFFFFF;">
                                                                <img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/trustpilot-newsletter.jpg" alt="trust"
                                                                     style="border:2px solid white;border-radius:50%;display:block;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="40">
                                                            </a></td>
                                                        </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                                    <td class="esdev-mso-td" width="30.535714285714285%" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" class="es-right" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td width="171" align="left" style="padding:0;Margin:0;">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="left" style="padding:0;Margin:0;">
                                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family: Tahoma, Geneva, sans-serif;line-height:150%;color:#FFFFFF;">
                                                                                            <br>
                                                                                        </p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                <tr style="border-collapse:collapse;">
                                    <td align="left" bgcolor="#444444" style="padding:0;Margin:0;padding-top:5px;padding-left:20px;padding-right:20px;background-color:#444444;">
                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td width="560" align="center" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>

                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
        <table class="es-footer" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top;">
            <tbody>
                <tr style="border-collapse:collapse;">
                    <td align="center" style="padding:0;Margin:0;">
                        <table class="es-footer-body" width="600" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#808080;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td align="left" bgcolor="#444444" style="Margin:0;padding-top:5px;padding-bottom:20px;padding-left:20px;padding-right:20px;background-color:#444444;">
                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td width="560" valign="top" align="center" style="padding:0;Margin:0;">
                                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td align="center" style="padding:0;Margin:0;">
                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:12px;font-family: Tahoma, Geneva, sans-serif;line-height:120%;color:#FFFFFF;">
                                                                            Copyright ©
                                                                            <!--2016-2020!-->«1xBit» </p>
                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:12px;font-family: Tahoma, Geneva, sans-serif;line-height:120%;color:#FFFFFF;">
                                                                            All rights reserved and protected by law
                                                                        </p>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>

</html>

    '''  # replace with <meta charset="cp1251"> for rus language

    # preset of html parts to edit
    cur_pic = 'https://1xbitdjqrc.top//genfiles/cms/65-29/desktop/img/big5winn3.jpg'
    cur_theme = 'CHEERS FOR THE WINNER!'
    cur_message = '''Dear User! 
                                                                                <br><br>
                                                                                You've taken the 1st place in the final prize draw of the <a href="https://1xbit.com/promotions/big-five/">BIG 5</a> tournament and got 500 mBTC, congratulations! 
                                                                                <br><br>
                                                                                Your reward has been credited to your personal account.
                                                                                <br>'''
    cur_but_title = 'CLAIM THE PRIZE'
    cur_but_title2 = 'Join in NOW'
    cur_but_link = 'https://1xbit.com/office/'
    cur_but_link2 = 'https://1xbit.com/office2/'
    cur_aftertext = 'Thank you for being part of 1xBit, we appreciate every player!'
    cur_logolink = 'https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/logo_white.png'
    find_button = '''<span class="es-button-border" style="border-style:solid;border-color:#808080;background:#E60D0D;border-width:0px;display:inline-block;border-radius:5px;width:auto;"> <a href="https://1xbit.com/office/"                                                                    class="es-button" target="_blank"                                                                    style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:roboto, 'helvetica neue', helvetica, arial, sans-serif;font-size:15px;color:#FFFFFF;border-style:solid;border-color:#E6770E;border-width:10px 40px;display:inline-block;background:#E6770E;font-weight:normal;font-style:normal;line-height:120%;width:auto;text-align:center;border-radius: 5px;"><b>CLAIM THE PRIZE</b></a> </span>
'''
    add_button = '''<span class="es-button-border" style="border-style:solid;border-color:#808080;background:#E60D0D;border-width:0px;display:inline-block;border-radius:5px;width:auto;"> <a href="https://1xbit.com/office/"                                                                    class="es-button" target="_blank"                                                                    style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:roboto, 'helvetica neue', helvetica, arial, sans-serif;font-size:15px;color:#FFFFFF;border-style:solid;border-color:#E6770E;border-width:10px 40px;display:inline-block;background:#E6770E;font-weight:normal;font-style:normal;line-height:120%;width:auto;text-align:center;border-radius: 5px;"><b>CLAIM THE PRIZE</b></a> </span>
<span class="es-button-border" style="border-style:solid;border-color:#808080;background:#E60D0D;border-width:0px;display:inline;border-radius:5px;width:auto;"> <a href="https://1xbit.com/office2/"                                                                    class="es-button" target="_blank"                                                                    style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:roboto, 'helvetica neue', helvetica, arial, sans-serif;font-size:15px;color:#FFFFFF;border-style:solid;border-color:#E6770E;border-width:10px 40px;display:inline-block;background:#E6770E;font-weight:normal;font-style:normal;line-height:120%;width:auto;text-align:center;border-radius: 5px;"><b>Join in NOW</b></a> </span>
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
    mailto = '<a href="mailto:support@partners1xbit.com">support@partners1xbit.com</a>'
    try:
        new_html = new_html.replace('support@partners1xbit.com', mailto)
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

    html = '''<!DOCTYPE html>
<html style="width:100%;font-family: Tahoma, Geneva, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0;">

<head>
    <meta charset="cp1251">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <meta name="x-apple-disable-message-reformatting">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="telephone=no" name="format-detection">
    <title></title>
    <style type="text/css">
        @-ms-viewport {
            width: device-width;
        }
        
        @media only screen and (max-width: 600px) {
            p,
            ul li,
            ol li,
            a {
                font-size: 16px !important
            }
            h1 {
                font-size: 30px !important;
                text-align: center
            }
            h2 {
                font-size: 26px !important;
                text-align: center
            }
            h3 {
                font-size: 20px !important;
                text-align: center
            }
            h1 a {
                font-size: 30px !important
            }
            h2 a {
                font-size: 26px !important
            }
            h3 a {
                font-size: 20px !important
            }
            .es-menu td a {
                font-size: 13px !important
            }
            .es-header-body p,
            .es-header-body ul li,
            .es-header-body ol li,
            .es-header-body a {
                font-size: 16px !important
            }
            .es-footer-body p,
            .es-footer-body ul li,
            .es-footer-body ol li,
            .es-footer-body a {
                font-size: 16px !important
            }
            .es-infoblock p,
            .es-infoblock ul li,
            .es-infoblock ol li,
            .es-infoblock a {
                font-size: 12px !important
            }
            *[class="gmail-fix"] {
                display: none !important
            }
            .es-m-txt-c,
            .es-m-txt-c h1,
            .es-m-txt-c h2,
            .es-m-txt-c h3 {
                text-align: center !important
            }
            .es-m-txt-r,
            .es-m-txt-r h1,
            .es-m-txt-r h2,
            .es-m-txt-r h3 {
                text-align: right !important
            }
            .es-m-txt-l,
            .es-m-txt-l h1,
            .es-m-txt-l h2,
            .es-m-txt-l h3 {
                text-align: left !important
            }
            .es-m-txt-r img,
            .es-m-txt-c img,
            .es-m-txt-l img {
                display: inline !important
            }
            .es-button-border {
                display: block !important
            }
            .es-button {
                font-size: 16px !important;
                display: block !important;
                border-left-width: 0px !important;
                border-right-width: 0px !important
            }
            .es-btn-fw {
                border-width: 10px 0px !important;
                text-align: center !important
            }
            .es-adaptive table,
            .es-btn-fw,
            .es-btn-fw-brdr,
            .es-left,
            .es-right {
                width: 100% !important
            }
            .es-content table,
            .es-header table,
            .es-footer table,
            .es-content,
            .es-footer,
            .es-header {
                width: 100% !important;
                max-width: 600px !important
            }
            .es-adapt-td {
                display: block !important;
                width: 100% !important
            }
            .adapt-img {
                width: 100% !important;
                height: auto !important
            }
            .es-m-p0 {
                padding: 0px !important
            }
            .es-m-p0r {
                padding-right: 0px !important
            }
            .es-m-p0l {
                padding-left: 0px !important
            }
            .es-m-p0t {
                padding-top: 0px !important
            }
            .es-m-p0b {
                padding-bottom: 0 !important
            }
            .es-m-p20b {
                padding-bottom: 20px !important
            }
            .es-mobile-hidden,
            .es-hidden {
                display: none !important
            }
            .es-desk-hidden {
                display: table-row !important;
                width: auto !important;
                overflow: visible !important;
                float: none !important;
                max-height: inherit !important;
                line-height: inherit !important
            }
            .es-desk-menu-hidden {
                display: table-cell !important
            }
            table.es-table-not-adapt,
            .esd-block-html table {
                width: auto !important
            }
            table.es-social {
                display: inline-block !important
            }
            table.es-social td {
                display: inline-block !important
            }
        }
        
        #outlook a {
            padding: 0;
        }
        
        .ExternalClass {
            width: 100%;
        }
        
        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
            line-height: 100%;
        }
        
        .es-button {
            mso-style-priority: 100 !important;
            text-decoration: none !important;
        }
        
        a[x-apple-data-detectors] {
            color: inherit !important;
            text-decoration: none !important;
            font-size: inherit !important;
            font-family: inherit !important;
            font-weight: inherit !important;
            line-height: inherit !important;
        }
        
        .es-desk-hidden {
            display: none;
            float: left;
            overflow: hidden;
            width: 0;
            max-height: 0;
            line-height: 0;
            mso-hide: all;
        }

    </style>
</head>

<body style="width:100%;font-family: Tahoma, Geneva, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0;">
    <div class="es-wrapper-color" style="background-color:#151515;">
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top;">
            <tbody>
                <tr style="border-collapse:collapse;">
                    <td valign="top" style="padding:0;Margin:0;">
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td class="es-adaptive" align="center" style="padding:0;Margin:0;">

                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
                            <tbody>
                                <tr style="border-collapse:collapse;"></tr>
                                <tr style="border-collapse:collapse;">
                                    <td class="es-adaptive" align="center" style="padding:0;Margin:0;">
                                        <table class="es-header-body" width="600" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td style="padding:0;Margin:0;padding-left:20px;padding-right:20px;background-image:url(https://undergroundev.com/stock-img/bg-footer.jpg);background-color:#444444;background-position:left top;background-repeat:no-repeat;" bgcolor="#444444" align="left">
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td class="es-m-p0r" width="174" valign="top" align="center" style="padding:0;Margin:0;">
                                                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td class="es-m-p0l es-m-txt-c" align="left" style="padding:0;Margin:0;">
                                                                                        <a href="#logo-link#" target="_blank" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family: Tahoma, Geneva, sans-serif;font-size:14px;text-decoration:underline;color:#333333;"><img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/logo_white.png" alt="" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;padding:7%;" width="160"></a>
                                                                                    </td>
                                                                                </tr>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                        </table>
                                                        <table cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tr style="border-collapse:collapse;">
                                                                <td width="366" align="left" style="padding:0;Margin:0;">
                                                                    <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;border-left:0px solid #808080;border-right:0px solid #808080;border-top:0px solid #808080;border-bottom:0px solid #808080;" width="100%" cellspacing="0" cellpadding="0">
                                                                        <tr style="border-collapse:collapse;">
                                                                            <td style="padding:0;Margin:0;">
                                                                                <table class="es-menu" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">

                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                        </table>
                                    </td>
                                </tr>
                        </table>
                    </td>
                </tr>
                </tbody>
        </table>
        <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
            <tbody>
                <tr style="border-collapse:collapse;">
                    <td align="center" style="padding:0;Margin:0;">
                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td align="left" style="padding:0;Margin:0;">
                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td width="600" align="center" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td align="center" style="padding:0;Margin:0;">
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                <tr style="border-collapse:collapse;">
                                    <td align="left" style="padding:0;Margin:0;padding-left:20px;padding-right:20px;">
                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td width="560" valign="top" align="center" style="padding:0;Margin:0;">
                                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">

                                                                    <!-- Заголовок !-->
                                                                    <td align="left" style="padding:0;Margin:0;padding: 19px 19px">
                                                                        <h2 style="Margin-top: 20px;line-height:50%;mso-line-height-rule:exactly;font-size:20px;font-style:normal;font-weight:normal;text-align:center;">
                                                                            <b>CHEERS FOR THE WINNER!</b>
                                                                        </h2>
                                                                    </td>
                                                                    <!-- /Заголовок !-->

                                                                </tr>
                                                                <tr style="border-collapse:collapse;">

                                                                    <!-- Ссылка на картинку !-->
                                                                        <td align="left" style="padding:0;Margin:0;">
                                                                            <img src="https://1xbitdjqrc.top//genfiles/cms/65-29/desktop/img/big5winn3.jpg" style="width: 100%; margin-bottom: 2%;margin-top: 2%;" alt="" />
                                                                        </td>
                                                                    <!-- /Ссылка на картинку !-->

                                                                </tr>

                                                                <tr style="border-collapse:collapse;">
                                                                    <td class="es-m-txt-c" align="left" style="border-left:2px solid #e6770e;padding:0 0 0 18px;Margin:0;padding-top:10px;padding-bottom:0;color:black;font-size:18px;">

                                                                        <!-- Абзацы !-->
                                                                            <p style="line-height: 1.5;color:#333333;font-size:16px;">
                                                                                Dear User! 
                                                                                <br><br>
                                                                                You’ve taken the 1st place in the final prize draw of the <a href="https://1xbit.com/promotions/big-five/">BIG 5</a> tournament and got 500 mBTC, congratulations! 
                                                                                <br><br>
                                                                                Your reward has been credited to your personal account.
                                                                                <br>

                                                                            </p>
                                                                        <!-- /Абзацы !-->

                                                                    </td>
                                                                </tr>
																<tr style="border-collapse:collapse;">

                                                                    <!-- Ссылка на картинку !-->
                                                                        <td align="left" style="padding:0;Margin:0;">
                                                                            <img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/bonus/rules/ben-season-winners.jpg" style="width: 100%; margin-bottom: 2%;margin-top: 2%;" alt="" />
                                                                        </td>
                                                                    <!-- /Ссылка на картинку !-->

                                                                </tr>
																<tr style="border-collapse:collapse;">
                                                                    <td class="es-m-txt-c" align="left" style="border-left:2px solid #e6770e;padding:0 0 0 18px;Margin:0;padding-top:10px;padding-bottom:0;color:black;font-size:18px;">

                                                                        <!-- Абзацы !-->
                                                                            <p style="line-height: 1.5;color:#333333;font-size:16px;">
                                                                                Dear User! 
                                                                                <br><br>
                                                                                You’ve taken the 2st place in the final prize draw of the <a href="https://1xbit.com/promotions/bigger-five/">BIG 5</a> tournament and got 500 mBTC, congratulations! 
                                                                                <br><br>
                                                                                Your reward has been credited to your personal account.
                                                                                <br>

                                                                            </p>
                                                                        <!-- /Абзацы !-->

                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <br>

<span class="es-button-border" style="border-style:solid;border-color:#808080;background:#E60D0D;border-width:0px;display:inline-block;border-radius:5px;width:auto;"> <a href="https://1xbit.com/office/"                                                                    class="es-button" target="_blank"                                                                    style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:roboto, 'helvetica neue', helvetica, arial, sans-serif;font-size:15px;color:#FFFFFF;border-style:solid;border-color:#E6770E;border-width:10px 40px;display:inline-block;background:#E6770E;font-weight:normal;font-style:normal;line-height:120%;width:auto;text-align:center;border-radius: 5px;"><b>CLAIM THE PRIZE</b></a> </span>
                                                        <!-- Текст после кнопки !-->
                                                            <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:16px;font-family: Tahoma, Geneva, sans-serif;line-height:150%;color:#333333;">
                                                                Thank you for being part of 1xBit, we appreciate every player!</a>
                                                            </p>
                                                        <!-- /Текст после кнопки !-->

                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
        <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
            <tbody>
                <tr style="border-collapse:collapse;">
                    <td align="center" style="padding:0;Margin:0;">
                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td align="left" style="padding:0;Margin:0;padding-top:0px;padding-left:20px;padding-right:20px;">
                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td width="560" valign="top" align="center" style="padding:0;Margin:0;">
                                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td align="center" style="padding:0;Margin:0;padding-top:0px;">
                                                                        <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td style="padding:0;Margin:0px 0px 0px 0px;border-bottom:1px solid #CCCCCC;background:none;height:1px;width:100%;margin:0px;">
                                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:16px;font-family: Tahoma, Geneva, sans-serif;line-height:150%;color:#333333;">
                                                                                            Sincerely,
                                                                                            <br> 1xBit Team
                                                                                        </p>
                                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family: Tahoma, Geneva, sans-serif;line-height:150%;color:#9b9b9b;">
                                                                                            
                                                                                            <br>

                                                                                        </p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
        <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
            <tbody>
                <tr style="border-collapse:collapse;">
                    <td align="center" style="padding:0;Margin:0;">
                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td align="left" style="padding:0;Margin:0;padding-left:20px;padding-right:20px;">
                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td width="560" valign="top" align="center" style="padding:0;Margin:0;">
                                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">

                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
        <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
            <tbody>
                <tr style="border-collapse:collapse;"></tr>
                <tr style="border-collapse:collapse;">
                    <td class="es-adaptive" align="center" style="padding:0;Margin:0;">
                        <table class="es-header-body" width="600" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td style="padding:0;Margin:0;background-image:url(http://1xbet.email/upload/files/unnamed%20%281%29.jpg);background-color:#FFFFFF;background-position:left top;background-repeat:no-repeat;" bgcolor="#ffffff" align="left">
                                        <table cellspacing="0" cellpadding="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td class="es-m-p0r" width="600" valign="top" align="center" style="padding:0;Margin:0;">
                                                        <tbody>
                                                            <tr style="border-collapse:collapse;">
                                                                <td align="left" style="padding:0;Margin:0;">
                                                                    <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family: Tahoma, Geneva, sans-serif;line-height:150%;color:#333333;">
                                                                        <br>
                                                                    </p>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                        </table>
                                        </td>
                                        </tr>
                                        </tbody>
                        </table>
                        </td>
                        </tr>
                        </tbody>
        </table>
        <table class="es-footer" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top;">
            <tbody>
                <tr style="border-collapse:collapse;">
                    <td align="center" style="padding:0;Margin:0;">
                        <table class="es-footer-body" width="600" cellspacing="0" cellpadding="0" align="center" bgcolor="#444444" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#444444;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td class="esdev-adapt-off" align="left" bgcolor="#444444" style="padding:0;Margin:0;padding-left:20px;padding-right:20px;background-color:#444444;">
                                        <table cellspacing="0" cellpadding="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td width="560" valign="top" align="center" style="padding:0;Margin:0;">
                                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td align="center" style="padding:0;Margin:0;">
                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:12px;font-family: Tahoma, Geneva, sans-serif;line-height:150%;color:#BCBABA;">
                                                                            Follow us:</p>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                <tr style="border-collapse:collapse;">
                                    <td class="esdev-adapt-off" align="left" style="padding:0;Margin:0;padding-top:10px;padding-left:20px;padding-right:20px;;padding-bottom:10px;">
                                        <table width="560" cellpadding="0" cellspacing="0" class="esdev-mso-table" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td class="esdev-mso-td" width="29.642857142857146%" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" align="left" class="es-left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td width="194" align="left" style="padding:0;Margin:0;">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="left" style="padding:0;Margin:0;"></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>

                                                    <td class="esdev-mso-td" width="6.964285714285714%" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td width="39" align="left" style="padding:0;Margin:0;">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="center" style="padding:0;Margin:0;padding-left:5px;padding-right:5px;">
                                                                                        <a target="_blank" href="https://www.instagram.com/1xbit/" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family: Tahoma, Geneva, sans-serif;font-size:14px;text-decoration:underline;color:#FFFFFF;">
                                                                                            <img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/ig_logo.png" alt="inst" style="border:2px solid white;border-radius:50%;display:block;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="40">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>

                                                            </tbody>
                                                        </table>
                                                    </td>
                                                    <td class="esdev-mso-td" width="6.964285714285714%" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td width="39" align="left" style="padding:0;Margin:0;">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="center" style="padding:0;Margin:0;padding-left:5px;padding-right:5px;">
                                                                                        <a target="_blank" href="https://www.reddit.com/r/1xBit_gambling/" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family: Tahoma, Geneva, sans-serif;font-size:14px;text-decoration:underline;color:#FFFFFF;">
                                                                                            <img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/reddit-logo.png" alt="rddt" style="border:2px solid white;border-radius:50%;display:block;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="40">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>

                                                            </tbody>
                                                        </table>
                                                    </td>
                                                    <td class="esdev-mso-td" width="6.964285714285714%" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td width="39" align="left" style="padding:0;Margin:0;">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="center" style="padding:0;Margin:0;padding-left:10px;">
                                                                                        <a target="_blank" href="https://twitter.com/1x_bit" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family: Tahoma, Geneva, sans-serif;font-size:14px;text-decoration:underline;color:#FFFFFF;">
                                                                                            <img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/tw_logo.png" alt="" style="border:2px solid white;border-radius:50%;display:block;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="40">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                    <td class="esdev-mso-td" width="6.964285714285714%" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td width="39" align="left" style="padding:0;Margin:0;">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="right" style="padding:0;Margin:0;padding-left:10px;">
                                                                                        <a target="_blank" href="https://t.me/sportsbook_1xBit" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family: Tahoma, Geneva, sans-serif;font-size:14px;text-decoration:underline;color:#FFFFFF;">
                                                                                            <img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/tg_logo.png" alt="teleg" style="border:2px solid white;border-radius:50%;display:block;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="40">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                    <td class="esdev-mso-td" width="6.964285714285714%" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td width="39" align="left" style="padding:0;Margin:0;">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="right" style="padding:0;Margin:0;padding-left:10px;">
                                                                                        <a target="_blank" href="https://www.youtube.com/c/1xBit/videos" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family: Tahoma, Geneva, sans-serif;font-size:14px;text-decoration:underline;color:#FFFFFF;">
                                                                                            <img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/yt_logo.png" alt="" style="border:2px solid white;border-radius:50%;display:block;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="40">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                                                        <td class="esdev-mso-td" width="6.964285714285714%" valign="top" style="padding:0;Margin:0;">
                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left"
                                               style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                            <tbody>
                                            <tr style="border-collapse:collapse;">
                                                <td width="39" align="left" style="padding:0;Margin:0;">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                           style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                        <tbody>
                                                        <tr style="border-collapse:collapse;">
                                                            <td align="center" style="padding:0;Margin:0;padding-left:10px;padding-right:10px;"><a target="_blank"
                                                                                                                                                 href="https://www.trustpilot.com/evaluate/1xbit.com"
                                                                                                                                                 style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family: Tahoma, Geneva, sans-serif;font-size:14px;text-decoration:underline;color:#FFFFFF;">
                                                                <img src="https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/trustpilot-newsletter.jpg" alt="trust"
                                                                     style="border:2px solid white;border-radius:50%;display:block;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="40">
                                                            </a></td>
                                                        </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                                    <td class="esdev-mso-td" width="30.535714285714285%" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" class="es-right" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td width="171" align="left" style="padding:0;Margin:0;">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="left" style="padding:0;Margin:0;">
                                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family: Tahoma, Geneva, sans-serif;line-height:150%;color:#FFFFFF;">
                                                                                            <br>
                                                                                        </p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                <tr style="border-collapse:collapse;">
                                    <td align="left" bgcolor="#444444" style="padding:0;Margin:0;padding-top:5px;padding-left:20px;padding-right:20px;background-color:#444444;">
                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td width="560" align="center" valign="top" style="padding:0;Margin:0;">
                                                        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>

                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
        <table class="es-footer" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top;">
            <tbody>
                <tr style="border-collapse:collapse;">
                    <td align="center" style="padding:0;Margin:0;">
                        <table class="es-footer-body" width="600" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#808080;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td align="left" bgcolor="#444444" style="Margin:0;padding-top:5px;padding-bottom:20px;padding-left:20px;padding-right:20px;background-color:#444444;">
                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td width="560" valign="top" align="center" style="padding:0;Margin:0;">
                                                        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td align="center" style="padding:0;Margin:0;">
                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:12px;font-family: Tahoma, Geneva, sans-serif;line-height:120%;color:#FFFFFF;">
                                                                            Copyright ©
                                                                            <!--2016-2020!-->«1xBit» </p>
                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:12px;font-family: Tahoma, Geneva, sans-serif;line-height:120%;color:#FFFFFF;">
                                                                            All rights reserved and protected by law
                                                                        </p>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>

</html>
'''  # replace with <meta charset="cp1251"> for rus language

    # preset of html parts to edit
    cur_pic = 'https://1xbitdjqrc.top//genfiles/cms/65-29/desktop/img/big5winn3.jpg'
    cur_pic_2 = 'https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/bonus/rules/ben-season-winners.jpg'
    cur_theme = 'CHEERS FOR THE WINNER!'
    cur_message = '''Dear User! 
                                                                                <br><br>
                                                                                You’ve taken the 1st place in the final prize draw of the <a href="https://1xbit.com/promotions/big-five/">BIG 5</a> tournament and got 500 mBTC, congratulations! 
                                                                                <br><br>
                                                                                Your reward has been credited to your personal account.
                                                                                <br>'''
    cur_message_2 = '''Dear User! 
                                                                                <br><br>
                                                                                You’ve taken the 2st place in the final prize draw of the <a href="https://1xbit.com/promotions/bigger-five/">BIG 5</a> tournament and got 500 mBTC, congratulations! 
                                                                                <br><br>
                                                                                Your reward has been credited to your personal account.
                                                                                <br>'''
    cur_but_title = 'CLAIM THE PRIZE'
    cur_but_title2 = 'Join in NOW'
    cur_but_link = 'https://1xbit.com/office/'
    cur_but_link2 = 'https://1xbit.com/office2/'
    cur_aftertext = 'Thank you for being part of 1xBit, we appreciate every player!'
    cur_logolink = 'https://1xbitdjqrc.top/genfiles/cms/65-29/desktop/img/logo_white.png'
    find_button = '''<span class="es-button-border" style="border-style:solid;border-color:#808080;background:#E60D0D;border-width:0px;display:inline-block;border-radius:5px;width:auto;"> <a href="https://1xbit.com/office/"                                                                    class="es-button" target="_blank"                                                                    style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:roboto, 'helvetica neue', helvetica, arial, sans-serif;font-size:15px;color:#FFFFFF;border-style:solid;border-color:#E6770E;border-width:10px 40px;display:inline-block;background:#E6770E;font-weight:normal;font-style:normal;line-height:120%;width:auto;text-align:center;border-radius: 5px;"><b>CLAIM THE PRIZE</b></a> </span>
    '''
    add_button = '''<span class="es-button-border" style="border-style:solid;border-color:#808080;background:#E60D0D;border-width:0px;display:inline-block;border-radius:5px;width:auto;"> <a href="https://1xbit.com/office/"                                                                    class="es-button" target="_blank"                                                                    style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:roboto, 'helvetica neue', helvetica, arial, sans-serif;font-size:15px;color:#FFFFFF;border-style:solid;border-color:#E6770E;border-width:10px 40px;display:inline-block;background:#E6770E;font-weight:normal;font-style:normal;line-height:120%;width:auto;text-align:center;border-radius: 5px;"><b>CLAIM THE PRIZE</b></a> </span>
    <span class="es-button-border" style="border-style:solid;border-color:#808080;background:#E60D0D;border-width:0px;display:inline;border-radius:5px;width:auto;"> <a href="https://1xbit.com/office2/"                                                                    class="es-button" target="_blank"                                                                    style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:roboto, 'helvetica neue', helvetica, arial, sans-serif;font-size:15px;color:#FFFFFF;border-style:solid;border-color:#E6770E;border-width:10px 40px;display:inline-block;background:#E6770E;font-weight:normal;font-style:normal;line-height:120%;width:auto;text-align:center;border-radius: 5px;"><b>Join in NOW</b></a> </span>
    '''

    # edit preset html
    new_html = html.replace(cur_pic, pic_link)
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
    mailto = '<a href="mailto:support@partners1xbit.com">support@partners1xbit.com</a>'
    try:
        new_html = new_html.replace('support@partners1xbit.com', mailto)
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
