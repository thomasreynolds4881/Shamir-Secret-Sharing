def findYint(x,y):
	slope = (y[1] - y[0]) / (x[1] - x[0])
	yint = int(y[0] - slope * x[0])
	return yint

def asciiToString(num):
	chars = [num[i:i+3] for i in range(0, len(num), 3)]

	return ''.join(chr(int(i)) for i in chars)

def main():
	fi = open('pass.txt','r')
	x,y = [], []
	for i in fi:
	    row = i.split()
	    x.append(int(row[0]))
	    y.append(int(row[1]))
	fi.close()
	yint = findYint(x,y)
	pword = asciiToString(str(yint))

	print(pword)

main()
