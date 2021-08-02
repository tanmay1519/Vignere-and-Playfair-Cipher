key = input ("Enter Decryption Key \n")
ciphertext = input("Enter Cipher TExt \n")
plainText = ""
for i in range(0,len(ciphertext)) :
	charNum = (ord(ciphertext[i]) - ord(key [i%len(key)]) +26) %26
	plainText += chr (charNum+65)

print("Decrypted text is - ",plainText)