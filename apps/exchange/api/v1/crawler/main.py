import requests
from lxml import html


# Data Resource: http://www.tsetmc.com/
from apps.exchange.models import Exchange

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

# for index, item in enumerate(group_xpath[1:], start=3410):
#     obj = Exchange.objects.get(pk=index)
#     if item == 'N1':
#         obj.group = 'n1'
#         obj.save()
#     elif item == 'N2':
#         obj.group = 'n2'
#         obj.save()
#     else:
#         print('wrong')


# for index, item in enumerate(board_xpath[1:], start=3410):
#     obj = Exchange.objects.get(pk=index)
#     if item == 'فهرست اوليه':
#         obj.board = 'f'
#         obj.save()
#     elif item == 'تابلو فرعي':
#         obj.board = 's'
#         obj.save()
#     elif item == 'تابلو اصلي':
#         obj.board = 'm'
#         obj.save()
#     else:
#         print('wrong')
