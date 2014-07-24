def is_list(value):
    if type(value) in (list, tuple): return True
    return False

def list_str(value):
    if not is_list(value): return str(value)
    return [list_str(v) for v in value]