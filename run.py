import csv
import mechanize
import re
import time
import BeautifulSoup
import smtplib
import inemail
import sites

_PRINT_ALL_ = True
_FIND_ = ["smartphone"]







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


#inemail.sendEmail(result)
