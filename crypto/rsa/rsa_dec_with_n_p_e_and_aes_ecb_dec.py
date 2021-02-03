from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
import sys,base64

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def pad_even(x):
        return ('', '0')[len(x)%2] + x


def CipherB2n(c):
    c2 = base64.b64decode(c)
    return int.from_bytes(c2, 'big')

def CipherN2b(m):
    hex_m=hex(m)[2:]
    if hex_m[-1] == 'L' :
        hex_m=hex_m[:-1]
    return bytes.fromhex(hex_m).decode('ascii')

def main():
    
    n = 0
    e = 0
    with open("pubkey.pem", "r") as pkey_f:
        pkey = RSA.importKey(pkey_f.read())
        n = pkey.n
        e = pkey.e
    
   
    # n is small so we can try to facroize it (YAFU)
    # YAFU OUTPUT-> 10410080216253956216713537817182443360779235033823514652866757961082890116671874771565125457104853470727423173827404139905383330210096904014560996952285911 cubed
    p = 10410080216253956216713537817182443360779235033823514652866757961082890116671874771565125457104853470727423173827404139905383330210096904014560996952285911
    
    # calc d of RSA

    q = n//p

    phi = pow(p,2) * (p-1)
    d = inverse(e,phi)
    
    # read enc message (key of AES)
    with open("key") as f:
        aes_key = f.read()
    aes_key = bytes_to_long(bytes.fromhex(aes_key))

    print("aes key -> "+str(aes_key))

    # decrypt message (AES KEY)
    aes_key_decrypt = long_to_bytes(pow(aes_key, d, n))
    print("AES key decripted ->" + str(aes_key_decrypt))

    # create cypher for AES
    cipher = AES.new(aes_key_decrypt, AES.MODE_ECB)
    ## important read byte <------
    with open("flag.txt.aes", "rb") as f:
        flag = cipher.decrypt( f.read().strip())
    print(str(flag))



if __name__ == "__main__":
    main()
