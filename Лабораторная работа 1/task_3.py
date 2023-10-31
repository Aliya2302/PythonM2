# TODO Найдите количество книг, которое можно разместить на дискете
one_disc_bite = 1.44 * 1024 * 1024
pages_in_book = 100
str_one_page = 50
simbols_one_str = 25
simbols_in_book = pages_in_book * str_one_page * simbols_one_str
bite_in_book = 4 * pages_in_book * str_one_page * simbols_one_str
books = one_disc_bite // bite_in_book
print("Количество книг, помещающихся на дискету:", int(books))
