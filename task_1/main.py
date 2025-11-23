#Щемелёва 4 вариант
print("start code …")

books = [{"title":"Heaven Official's Blessing", "author" : "Mo Xiang Tong Xiu", "year" : "2020"},
 {"title": "Лисья Нора" , "author": "Нора Сакавич" , "year": "2013"},
 {"title": "король воронов" , "author":"Нора Сакавич" , "year":"2017"},
 {"title": "свита короля", "author": "Нора Сакавич", "year":"2018"},
 {"title": "если все кошки в мире исчезнут", "author": "Гэнки Кавамура", "year":"2012"}]

i = 1
for book in books:
    print(f" ---------------------- Книга {i} -----------------------")
    print(f"Название: {book['title']}, Автор: {book['author']}")
    print(f" ---------------------- {book['year']} ----------------------")
    print()
    i+=1


print("end code …")