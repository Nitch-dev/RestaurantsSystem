
def validate_name(input):
    if len(input) >= 2:
        return True
    return False

def validate_price(input):
    try:
        if int(input) > 0:
            return True
    except:
        return False