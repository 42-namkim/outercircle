#why garlic becomes cheese?
def NULL_not_found(object: any) -> int:
    o_type = type(object)
    types = {
        None: "Nothing",
        float: "Cheese",
        int: "Zero",
        str: "Empty",
        bool: "Fake"
    }
    values = (float("NaN"), 0, '', False)
    if o_type in types and object in values:
        print(types[o_type] + ": ", end = '')
        print(object, end = ' ')
        print(o_type)
        return 0
    else:
        print("Type not Found")
    return 1