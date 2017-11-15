# -*- coding: UTF-8 -*-

from math import ceil

class Pagination(object):

    def __init__(self, page, per_page, total_count):
        self.page = page  # запрос страницы
        self.per_page = per_page  # кол-во постов на странице
        self.total_count = total_count  # всего постов

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        # Создание окружения страниц с левой и правой стороны от текущей.
        last = 0
        for num in range(1, self.pages + 1):
            if num <= left_edge or (num > self.page - left_current - 1 and \
                num < self.page + right_current) or num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num



# ss = Pagination(5, 5, 300)
# print(ss.pages)
#
# print(ss.has_next)
# print(ss.has_prev)
#
# for b in ss.iter_pages():
#     print(b)
