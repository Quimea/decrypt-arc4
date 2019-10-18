from Crypto.Cipher import ARC4
import codecs
from base64 import b64encode, b64decode

key = raw_input("input key(if key is unknown, put ` as key: ")
msg = raw_input("input encrypted base64 message: ")

if key = "`" {
print("the encrypted message: %s" %  msg)
for i in range(256):
  cipher = ARC4.new((bytes([i])))
  msg = cipher.decrypt(b64decode(msg))
  print("The secret message is: %s" % msg)
 } else {
cipher = ARC4.new(key)
msg = cipher.decrypt(b64decode(msg))
}
