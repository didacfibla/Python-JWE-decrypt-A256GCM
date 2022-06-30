# Python-JWE-decrypt-A256GCM
This tool uses Python to decrypt a JWE with the A256GCM algorithm.

<h1> Example </h1>

hexKey = "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f" <br>
token = b'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2Iiwia2lkIjoiQ2xhdmUxIiwiYWxnIjoiZGlyIn0..xs-B6n3QA3MSSNh-ASFfRQ.iB5jfFp2D6q9AwP2Fu_voKdi805fZK4uOuTCJ2BZX_bpJX-Zjr-7IExju8sJHtuZIqokbuuzghynAICgLIL0u4eYJXgP_qoD16d0Dm3GoXiRV7X-c838tD_t0X_u0v1-.5_jrgiDUF3QVIjPBHFznlQ'<br>
<br>
result = decodeToken(hexKey, token)<br>
print(result)<br>
\# {'sub': '98765432A', 'iss': 'AppCRUE', 'otp': '865432', 'iat': 1587376072, 'exp': 1587376132}
