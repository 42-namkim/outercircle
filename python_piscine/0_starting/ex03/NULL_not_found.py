#why garlic becomes cheese?
def NULL_not_found(object: any) -> int:
    o_type = type(object)
    types = {
        float: "Cheese",
        int: "Zero",
        str: "Empty",
        bool: "Fake"
    }
    values = (0, '', False, None)
    if o_type in types and object in values \
            or o_type == float and object != object:
        print(f'{types[o_type]}: {object} {o_type}' if object != '' \
            else f'{types[o_type]}: {o_type}')
        return 0
    elif object is None:
        print(f'Nothing: {object} {o_type}')
        return 0
    else:
        print("Type not Found")
    return 1