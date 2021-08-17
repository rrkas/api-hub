def request_info(request):
    req = {
        "values": request.values,
        "path": request.path,
        "root_path": request.root_path,
        "method": request.method,
        "host": request.host,
        "is_json": request.is_json,
        "content-type": request.content_type,
        "json": request.json,
    }
    req = {}
    for d in dir(request):
        try:
            if d.startswith("_"):
                continue
            req[d] = str(getattr(request, d))
            print(d, req[d])
        except BaseException as e:
            print(e)
            print("error:", d)
    print(req)
    return req


def type_error_message(list_ex_accepted, el):
    type_got = str(type(el)).split("'")[1]
    t = []
    for i in list_ex_accepted:
        t.append(str(type(i)).split("'")[1])
    return f"expected {', '.join(t)}; got {type_got}"
