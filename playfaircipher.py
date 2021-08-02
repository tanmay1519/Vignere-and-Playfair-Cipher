
matrix = []
keyword = input ("\nEnter keyword\n- ")
used = []
asciiNum=65
def make_matrix () :
	global asciiNum,matrix,keyword,used
	for i in range (0,5):
		app_line = []
		for j in range (0,5):
			if keyword != "" :
				char_key = keyword[0]
				if char_key not in used :
					if char_key=='I' :
						char_key=['I',"J"]
						used.append('I')
						used.append('J')
					else :
						used.append(char_key)
					app_line.append(char_key)
				else :
					while keyword[0]  in used :
						keyword=keyword[1:]
					app_line.append(keyword[0])
					used.append(keyword[0])
				keyword=keyword[1:]
			else :
				while chr(asciiNum) in used :
					asciiNum+=1
				to_append = chr(asciiNum)
				if chr(asciiNum) == 'I' :
					used.append('I')
					used.append('J')
					to_append=['I','J']
				used.append(chr(asciiNum))
				app_line.append(to_append)
				asciiNum+=1
		matrix.append(app_line)

make_matrix()

def printMatrix(matrix) :
	for i in matrix :
		print(i)

printMatrix(matrix)
def giveRowCol (matrix,key) :

	for i in range (0,len(matrix)) :
		for j in range (0,len(matrix[i])):
			if type(matrix[i][j])==str :
				if matrix[i][j]==key :
					return i,j
			elif type(matrix[i][j])==list  :
			
				if matrix[i][j][0]==key or matrix[i][j][1] ==key :
					return i,j

def decryption  (ciphertext) :
	decrypted_text = ""
	for i in range (0,int(len(ciphertext)/2)):
			key1=ciphertext[i*2]
			key2=ciphertext[i*2+1]
			key1_row,key1_col=giveRowCol(matrix,key1)
			key2_row,key2_col=giveRowCol(matrix,key2)
			plain_key_1=""
			plain_key_2=""
			if (key1_row==key2_row) :
				plain_key_1=matrix[key1_row][(key1_col+4)%5]
				plain_key_2=matrix[key1_row][(key2_col+4)%5]

			elif  (key1_col==key2_col) :
				plain_key_1 =matrix[(key1_row+4)%5][key1_col]
				plain_key_2 =matrix[(key2_row+4)%5][key2_col]
			else :
				plain_key_1=matrix[key1_row][key2_col]
				plain_key_2=matrix[key2_row][key1_col]
			if type(plain_key_1) == list :
				plain_key_1 = plain_key_1[0]

			if type(plain_key_2) == list :
				plain_key_2 = plain_key_2[0]

			decrypted_text = decrypted_text + plain_key_1+plain_key_2
	return decrypted_text
ciphertext = input ("\nEnter ciphertext \n- ")
upper_text = ciphertext.upper()
plainText=decryption(upper_text)

print(f"\n\nCipherText - {ciphertext} \n\nDecrypted Text - {plainText[:-1]}")

