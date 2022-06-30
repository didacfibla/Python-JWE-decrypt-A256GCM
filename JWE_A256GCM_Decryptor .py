import base64
import codecs
import json
from jose import jwe


def decodeToken(key: str, encryptedToken: bytes) -> dict:
    """
    This method decrypts and returns a dictionary of all the values of a JWE encrypted with a key of 64 characters (32 hex bytes) with the A256GCM algorithm.

    :param encryptedToken: Encrypted token in 'bytes' format
    :type encryptedToken: bytes
    :param key: Hexadecimal key of 64 characteres (32 bytes) to decrypt the JWE.
    :type key: str
    :return: Dictionary with the JWT decrypted values
    :rtype: dict
    """
    b64_key = codecs.encode(codecs.decode(key, 'hex'), 'base64').decode()
    key = base64.b64decode(b64_key).decode("utf-8")
    return json.loads(jwe.decrypt(encryptedToken, key).decode("utf-8"))


if __name__ == "__main__":

    hexKey = "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f"
    token = b'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2Iiwia2lkIjoiQ2xhdmUxIiwiYWxnIjoiZGlyIn0..xs-B6n3QA3MSSNh-ASFfRQ.iB5jfFp2D6q9AwP2Fu_voKdi805fZK4uOuTCJ2BZX_bpJX-Zjr-7IExju8sJHtuZIqokbuuzghynAICgLIL0u4eYJXgP_qoD16d0Dm3GoXiRV7X-c838tD_t0X_u0v1-.5_jrgiDUF3QVIjPBHFznlQ'

    result = decodeToken(hexKey, token)
    print(result)
    # {'sub': '98765432A', 'iss': 'AppCRUE', 'otp': '865432', 'iat': 1587376072, 'exp': 1587376132}
