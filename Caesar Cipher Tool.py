def encrypt(text, shift):
  result = ""
  for char in text:
    if char.isalpha():
      shift_amount = shift % 26
      if char.isupper():
        result += chr((ord(char) - 65 + shift_amount) % 26 + 65)
      else:
        result += chr((ord(char) - 97 + shift_amount) % 26 + 97)
    else:
      result += char
  return result

def decrypt(text, shift):
  return encrypt(text, -shift)

message = "My Name is Ayush"
shift_value = 3

encrypted = encrypt(message, shift_value)
print("Original:", message)
print("Encrypted :", encrypted)

decrypted = decrypt(encrypted, shift_value)
print("Decrypted :", decrypted)

