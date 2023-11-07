#running your function alone does nothing.... should i check if object is empty?
#str.capitalize
def all_thing_is_obj(object: any) -> int:
    types = {list: "List"
            , tuple: "Tuple"
            , set: "Set"
            , dict: "Dict"
            , str: " is in the kitchen"
            }
    for t in types:
        if isinstance(object, t):
                if t == str:
                    print(object + types[t], end='')
                else:
                    print(types[t], end='')
                print(" : ", end='')
                print(type(object))
                break
    if type(object) not in types:
        print("Type not found")
    return 42