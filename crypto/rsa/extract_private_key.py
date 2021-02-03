from math import gcd
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

### è da sistemare firmo alla fine invece di decifrare

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


def main():
    pkeys = ["key15088.pem", "key19440.pem"]
    msg = {"key15088.pem":"msgs15088.enc", "key19440.pem":"msgs19440.enc"}

    cd = 1015155878909680562221398235963073566637283630099630019001448387633204489019244877796744804401559234413826094271477574054262756393007301763304045778966571605511981582575171708926364520591552379670494655116847883518581699106610444663


    rsa_n = {}
    rsa_e = {}

    for file in pkeys:
        rsa_pub = open("./keys/"+file, "r")
        key = RSA.importKey(rsa_pub.read())
        msg1 = open("./msgs/msgs15088.enc", "r")
        msg2 = open("./msgs/msgs19440.enc", "r")
        
        
        rsa_n[file] = key.n
        rsa_e[file] = key.e
        rsa_pub.close()

        

        n = rsa_n[file]
        e = rsa_e[file]
        p = cd
        q = n//p
        phi = (p-1)*(q-1)
        d = modinv(e, n-(p+q-1))
        
        print("_________________________________________________\n"+file)
        print("n > " + str(n))
        print("p > " + str(p))
        print("q > " + str(q))
        print("e > " + str(e))
        print("phi > " + str(phi))
        print("d > " + str(d))
        print("\n\n\n")

        private_key = RSA.construct((n, e, d))
#       private_key = RSA.construct((n, e, d, p, q))

        signer = PKCS1_v1_5.new(private_key)

        txt1 = signer.sign(msg1)
        txt2 = signer.sign(msg2)

        f = open("pkey"+file.replace("key", "").replace(".pem", "")+".pem", "wb")

        f.write(private_key.exportKey('PEM'))
        f.close()
        
        print(private_key.exportKey('PEM'))
        dec1 = private_key.decrypt(b64decode(txt1))
        dec2 = private_key.decrypt(b64decode(txt2))
        
        print("\n\n\n")
        


if __name__ == "__main__":
    main()
