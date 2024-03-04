def sum_negative_positive(*args):
    negative_sum = 0
    positive_sum = 0
    for el in args:
        if el > 0:
            positive_sum += el
        elif el < 0:
            negative_sum += el
    return [positive_sum, negative_sum]


num = (int(el) for el in input().split())
positive_summ, negative_summ = sum_negative_positive(*num)
print(negative_summ)
print(positive_summ)
if abs(negative_summ) > positive_summ:
    print("The negatives are stronger than the positives")
elif positive_summ > abs(negative_summ):
    print("The positives are stronger than the negatives")
