import csv
import mechanize
import re
import time
import BeautifulSoup
import smtplib
import email
import sites

_PRINT_ALL_ = True
_FIND_ = ["smartphone"]




def hardmob():
    ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
    browser = mechanize.Browser()
    browser.set_handle_robots(False)

    browser.addheaders = [('User-agent', 'Firefox')]
    start = 0
    continuar = True
    links = []

    browser.open("http://www.hardmob.com.br/promocoes/")
    html = browser.response().get_data()
    browser.open("http://www.hardmob.com.br/promocoes/index2.html")
    html += browser.response().get_data()
    browser.open("http://www.hardmob.com.br/promocoes/index3.html")
    html += browser.response().get_data()
    browser.open("http://www.hardmob.com.br/promocoes/index4.html")
    html += browser.response().get_data()


    #print html
    soup = BeautifulSoup.BeautifulSoup(html)
    divList = soup(attrs={'class': 'title'})
    return [divList, '']





hardmobPromos = sites.promoBit()


#promoTexts = [x.getText() for x in divList]
result = ""


if _PRINT_ALL_ == True:
    for x in xrange(0, len(hardmobPromos[0])):
        print hardmobPromos[0][x].getText() + " - " + hardmobPromos[1][x].getText()

for x in xrange(0, len(hardmobPromos[0])):
    for y in _FIND_:
        if y.lower() in hardmobPromos[0][x].getText().encode('ascii', 'ignore').lower():
            print hardmobPromos[0][x].getText().encode('ascii', 'ignore')
            result += "<a href=\"" + hardmobPromos[2] + hardmobPromos[0][x]['href'] + "\">" + hardmobPromos[0][x].getText().encode('ascii', 'ignore') + " - " + hardmobPromos[1][x].getText() + "</a><br><br>"


email.sendEmail(result)
