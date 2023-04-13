

import pyCryptoRSA


print("[*]Generate keys...")
private_key, public_key = pyCryptoRSA.generate_RSA(bits=2048)

public_key_loc = "public_key"
private_key_loc = "private_key"

try:
    with open(public_key_loc, 'wb') as f:
        f.write(public_key)

    with open(private_key_loc, 'wb') as f:
        f.write(private_key)

    print("[+]Generated keys very well")

except Exception as e :
    print("[Err] Key Genrater has err: {}".format(e))
    
message = b"I love my job!"
package = pyCryptoRSA.encrypt_RSA(public_key_loc, message)


decode = pyCryptoRSA.decrypt_RSA(private_key_loc, package)
print(decode)
