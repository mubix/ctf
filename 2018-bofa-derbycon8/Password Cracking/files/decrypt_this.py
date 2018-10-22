import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class AESCipher(object):

    def __init__(self, key): 
        self.blockSize = 32
        self.key = hashlib.md5(key.encode()).digest()

    def encrypt(self, raw):
        raw = self.padding(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def padding(self, x):
        return x + (self.blockSize - len(x) % self.blockSize) * chr(self.blockSize - len(x) % self.blockSize)

    @staticmethod
    def _unpad(x):
        return x[:-ord(x[len(x)-1:])]



decryptThis = "SZlG4nRNnqBv417TiC+0j3AsBAzu3Vt/UtNiOJsanXlzrysVVY3Iu51zoJSMrnaMdAcCzofj7MC6a6CJ35akd8Iin2i0Wy2ZSNhzeRILYFQ="