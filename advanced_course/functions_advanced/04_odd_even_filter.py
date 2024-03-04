def even_odd_filter(**kwargs):
    if "odd" in kwargs:
        odd_list = []
        for el in kwargs["odd"]:
            if el % 2 != 0:
                odd_list.append(el)
        kwargs["odd"] = odd_list
    if "even" in kwargs:
        even_list = []
        for el in kwargs["even"]:
            if el % 2 == 0:
                even_list.append(el)
            kwargs["even"] = even_list
    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
