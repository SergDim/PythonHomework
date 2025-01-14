

import inspect

def introspection_info(obj):
    atribyte_list = []
    method_list = []
    object_data = inspect.getmembers(obj)
    for name, value in object_data:
        if inspect.ismethodwrapper(value) or inspect.isroutine(value) or inspect.isbuiltin(value):
            method_list.append(name)
        elif inspect.ismodule(name):
            pass
        else:
            atribyte_list.append(name)
    module = inspect.getmodule(obj)
    if module != None:
        module_name = module.__name__
    else:
        module_name = __name__
    return {'type': obj.__class__.__name__, 'attributes': atribyte_list, 'methods': method_list, 'module': module_name}


mu_number = 42
number_info = introspection_info(mu_number)
print(number_info)