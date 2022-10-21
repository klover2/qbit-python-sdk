import hashlib
import hmac


# hmac-sha256
def encryptHmacSHA256(secret: str, **params):
    message = join_str(**params)
    encryption = hmac.new(bytes(secret, encoding='UTF-8'), bytes(message, encoding='UTF-8'), hashlib.sha256)
    return encryption.hexdigest()


def join_str(**origin):
    keys = list(origin.keys())
    keys.sort()
    content = []
    for key in keys:
        val = origin[key]
        if val is None:
            val = ''
        content.append(key + '=' + str(val))
    return '&'.join(content)
