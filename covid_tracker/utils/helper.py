    
def serializer_error_message(errors):
    error_list = []
    for key, val in errors.items():
        if type(val) == list:
            if isinstance(val[0], dict):
                inner_errors = [serializer_error_message(item) for item in val]
                error_list += [error for error in inner_errors if error != '']
            else:
                error = "{} - {}".format(key, "".join(val))
                error_list.append(error)
    
    return ",".join(error_list)
