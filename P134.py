'''8-12
def sandwiches(*shicais):
        for shicai in shicais:
            print(f"The sandwiches is {shicai} sandwiches.")
sandwiches('a')
sandwiches('a','b')
sandwiches('a','b','c')
'''

'''8-14'''
def make_car(zhizaoshang,xinghao,**kwargs):
    kwargs['制造商']=zhizaoshang
    kwargs['型号'] = xinghao
    return kwargs

car = make_car('subaru','outback',color='blue',two_package=True)
print(car)