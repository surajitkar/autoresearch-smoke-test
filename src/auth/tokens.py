def refresh_token(token):
    if token.is_expired():
        return generate_new_token()
    return token
