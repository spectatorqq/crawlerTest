import requests
from lxml import etree

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/77.0.3865.120 '
#                   'Safari/537.36',
#
# }
# for i in range(5):
#     res = requests.get(url='https://www.574aw.com/shuku/'+str(i)+'.html', headers=headers)
#     res = res.text
#     ele = etree.HTML(res)
#     books_name = ele.xpath('//*[@id="container"]/div/div[2]/div/h2/a/text()')
#     books_url = ele.xpath('//*[@id="container"]/div/div[2]/div/h2/a/@href')
#     # print(books_url)
#     # print(books_name)
#     for book_name, book_url in zip(books_name, books_url):
#         print(book_name)
#         res = requests.get(url=book_url, headers=headers)
#         res = res.text
#         ele = etree.HTML(res)
#         chapters_name = ele.xpath('//*[@id="booklistBox"]/li/a/text()')
#         chapters_url = ele.xpath('//*[@id="booklistBox"]/li/a/@href')
#         for chapter_name, chapter_url in zip(chapters_name, chapters_url):
#
#             res = requests.get(url=chapter_url, headers=headers)
#             res = res.text
#             ele = etree.HTML(res)
#             content = ele.xpath('//div[@id="chapter_content"]/text()')
#             context = chapter_name+'\n'
#             for con in content:
#                 con = con.rstrip()
#                 context += con + '\n'
#             context += '\n'
#             with open(book_name+'.txt', mode='a+', encoding='utf8') as f:
#                 f.write(context)
#             print(chapter_name)


class BookTool:

    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/77.0.3865.120 '
                          'Safari/537.36',
        }

    def crawl_quanshu(self):
        res = requests.get(url='https://www.574aw.com/shuku/', headers=self.headers)
        res = res.text
        ele = etree.HTML(res)
        books_name = ele.xpath('//*[@id="container"]/div/div[2]/div/h2/a/text()')
        books_url = ele.xpath('//*[@id="container"]/div/div[2]/div/h2/a/@href')
        self.get_chapters(books_name, books_url)

    def get_chapters(self, books_name, books_url):
        for book_name, book_url in zip(books_name, books_url):
            print(book_name)
            res = requests.get(url=book_url, headers=self.headers)
            res = res.text
            ele = etree.HTML(res)
            chapters_name = ele.xpath('//*[@id="booklistBox"]/li/a/text()')
            chapters_url = ele.xpath('//*[@id="booklistBox"]/li/a/@href')
            self.get_content(chapters_name, chapters_url, book_name)

    def get_content(self, chapters_name, chapters_url, book_name):
        for chapter_name, chapter_url in zip(chapters_name, chapters_url):
            res = requests.get(url=chapter_url, headers=self.headers)
            res = res.text
            ele = etree.HTML(res)
            content = ele.xpath('//div[@id="chapter_content"]/text()')
            self.down_book(content, chapter_name, book_name)

    def down_book(self, content, chapter_name, book_name):
        context = chapter_name + '\n'
        for con in content:
            con = con.rstrip()
            context += con + '\n'
        context += '\n'
        with open(book_name + '.txt', mode='a+', encoding='utf8') as f:
            f.write(context)
        print(chapter_name)


if __name__ == '__main__':
    book_tool = BookTool()
    book_tool.crawl_quanshu()
