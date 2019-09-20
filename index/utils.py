# ily bagoum
b64alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"

def b64todigit(b64):
    output = 0
    for b64it in b64:
        output *= 64
        output += b64alphabet.index(b64it)
    return output
