def validate_values(values: dict, check: dict, exceptions: list = []) -> bool:
    """
    Checks that no 'string' values are empty.
    values: dictionary data
    exceptions: list of 'keys' allowed to be empty (basically don't check them)
    """

    for key, val in values.items():
        for k, v in check.items():
            if key == k and val == v:
                return False
        if key in exceptions:
            continue
        if isinstance(val, str) and not val.strip():
            return False
        
    return True


if __name__ == "__main__":

    value_set_1 = {'name': '', 
                   'uid': '',
                   'day': 0, 
                   'month': 'select month'}
    
    value_set_2 = {'name': 'someone', 
                   'uid': '000000',
                   'day': 1, 
                   'month': 1}
    
    unsafe_keyval = {
        "day": 0,
        "month": "select month"
    }

    print(validate_values(value_set_1, unsafe_keyval))
    print(validate_values(value_set_2, unsafe_keyval))

