def discounted(price,discount,max_discout=20):
    discounted = abs(price)
    discount = abs(discount)
    if discount > max_discout:
        discounted = discounted
    else:
        discounted = price*(1-discount/100)
    return discounted
print(discounted(100,5))
print(discounted(100,30))
print(discounted(100,30,max_discout=40))
