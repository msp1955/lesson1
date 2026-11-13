from pprint import pprint

dd = {'k1': "a"}
# print(dd)
dd['k2'] = "b"
# print(dd)
# print(dd.get('k3','p'))
# del dd['k1']
# print(dd)
pp = ["p8","p2","p3","p2"]
dd['k3'] = pp
pprint(dd)

dd1 = {'k1': "a" ,
       'k2': "b"}
pprint(dd1)