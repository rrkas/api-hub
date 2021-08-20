# returns the detailed request with all attributes and values
from flask import request


def request_info(request):
    req = {}
    for d in dir(request):
        try:
            if d.startswith("_"):
                continue
            req[d] = str(getattr(request, d))
            # print(d, req[d])
        except BaseException as e:
            print(e)
    return req


# list_ex_accepted: list of example of accepted data types
# el : element got
# function returns a well formed message
def type_error_message(list_ex_accepted, el, arg=""):
    type_got = str(type(el)).split("'")[1]
    t = []
    for i in list_ex_accepted:
        t.append(str(type(i)).split("'")[1])
    return (
        f"{arg + ': ' if len(arg) > 0 else ''}expected {', '.join(t)}; got {type_got}"
    )


def get_value_form_json(key):
    if key in request.form.keys():
        return request.form.get(key)
    elif key in request.json.keys():
        return request.json[key]
    else:
        return None
