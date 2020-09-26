import requests
from lxml import html


# Data Resource: http://www.tsetmc.com/
URL = "http://www.tsetmc.com/Loader.aspx?ParTree=111C1417"

page = requests.get(URL)
text_page = html.fromstring(page.text)
symbol_code_xpath = text_page.xpath('//*/td[1]/text()')
group_xpath = text_page.xpath('//*/td[2]/text()')
group_industry_xpath = text_page.xpath('//*/td[3]/text()')
board_xpath = text_page.xpath('//*/td[4]/text()')
latin_symbol_xpath = text_page.xpath('//*/td[5]/text()')
latin_name_xpath = text_page.xpath('//*/td[6]/text()')
persian_symbol_xpath = text_page.xpath('//*/td[7]/a/text()')
persian_name_xpath = text_page.xpath('//*/td[8]/a/text()')


for i in persian_name_xpath[1:]:
    print(i)


# print('n1' if i == 'N1' else 'N2')