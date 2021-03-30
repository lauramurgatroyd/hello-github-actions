
def get_product(a, b):
    if (type(a) not in [int, float]) or (type(b) not in [int, float]):
        raise TypeError
    
    return a*b
