def validate_discount(code, expiry):
    if expiry < today():
        raise ValueError('Expired')
    return True
