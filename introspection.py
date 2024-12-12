import inspect

def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': dir(obj),
        'methods': [attr for attr in dir(obj) if callable(getattr(obj, attr))],
        'module': inspect.getmodule(obj)

    }
    return info

number_info = introspection_info(42)
print(number_info)