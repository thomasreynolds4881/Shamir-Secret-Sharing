import random

def encryptWord(word):
	numlist = []
	for i in range(len(word)):
		numlist.append(str(ord(word[i])).zfill(3))
	num = int("".join(numlist))
	return num

def createPoints(pwd, pts):
	yint = pwd
	gradient = random.randint(100,1000)
	xvals = []
	yvals = []
	for i in range(pts):
		n = random.randint(1000,10000)
		xvals.append(n)
		yvals.append(((n) * gradient) + pwd)

	return xvals, yvals

def main():
	pword = input("Enter a password to encrypt: ")
	pword = encryptWord(pword)
	numpoints = int(input("How many points to generate? "))
	if numpoints < 2:
		numpoints = 2
	xpts, ypts = createPoints(pword, numpoints)

	fi = open("pass.txt","w")
	for i in range(len(xpts)):
		fi.write(str(xpts[i]))
		fi.write(' ')
		fi.write(str(ypts[i]))
		fi.write('\n')
	fi.close()
	print("Sent to file (pass.txt)")
main()