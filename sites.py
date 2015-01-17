__author__ = 'bernardo'

def promoBit():
    ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
    browser = mechanize.Browser()
    browser.set_handle_robots(False)

    browser.addheaders = [('User-agent', 'Firefox')]
    start = 0
    continuar = True
    links = []

    browser.open("http://www.promobit.com.br/Offer/getPage/page/1")
    html = browser.response().get_data()
    browser.open("http://www.promobit.com.br/Offer/getPage/page/2")
    html += browser.response().get_data()
    browser.open("http://www.promobit.com.br/Offer/getPage/page/3")
    html += browser.response().get_data()

    html = html.replace("access_url small", "access_url").replace("access_url ", "access_url")
    #print html
    soup = BeautifulSoup.BeautifulSoup(html)

    divList = soup(attrs={'class': 'access_url'})
    prices = soup(attrs={'class': 'price'})

    return [divList, prices, "http://www.promobit.com.br/"]