
def cm2_to_m2(area_cm2):
    return area_cm2 / 10000

def m2_to_cm2(area_m2):
    return area_m2 * 10000

def compare_areas(shape1, shape2):
    area1 = shape1.area()
    area2 = shape2.area()
    
    if area1 > area2:
        return f"{shape1.__class__.__name__} is bigger than {shape2.__class__.__name__}"
    elif area2 > area1:
        return f"{shape2.__class__.__name__} is bigger than {shape1.__class__.__name__}"
    else:
        return "Both shapes have the same area"
