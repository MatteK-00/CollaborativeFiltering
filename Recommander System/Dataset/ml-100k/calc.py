import numpy as np
import csv



def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

with open('datixmedia','r') as SM:
	tp = [[],[]]
	fp = [[],[]]
	prec = [[],[]]
	count = 1
	for line in csv.reader(SM, dialect="excel"):

		#if len(line) is not 0:


		if line[0] == '*':
			print line[1]
		elif is_number(line[0]) and int(line[0]) == 1:
			tp[0].append(int(line[1]))
			fp[0].append(int(line[2]))
			prec[0].append(float(line[3]))
		elif is_number(line[0]) and int(line[0]) == 2:
			tp[1].append(int(line[1]))
			fp[1].append(int(line[2]))
			prec[1].append(float(line[3]))
		elif line[0] == '-':
			if not(tp[0] == []):
				tp1 = np.array(tp[0])
				fp1 = np.array(fp[0])
				prec1 = np.array(prec[0])

				#print 'Eq: 1 ' + str(np.mean(tp1)) + ' ' + str(np.mean(fp1)) + ' ' + str(np.mean(prec1))
				print str(100-(count*5)) +'	&'+ str(count*5) +'& 1	& ' +str(np.mean(tp1))+ '& ' + str(np.mean(fp1)) + '	& ' + str(np.mean(prec1))+ '//'

			if not(tp[1] == []):
				tp2 = np.array(tp[1])
				fp2 = np.array(fp[1])
				prec2 = np.array(prec[1])

				#print 'Eq: 2 ' + str(np.mean(tp2)) + ' ' + str(np.mean(fp2)) + ' ' + str(np.mean(prec2))
				print (str(100-count*5) +'	&'+ str(count*5) +'& 2	& ' +str(np.mean(tp2))+ '& ' + str(np.mean(fp2)) + '	& ' +str(np.mean(prec2))+ '	//')

			tp = [[],[]]
			fp = [[],[]]
			prec = [[],[]]
			count +=1
			if count == 5:
				count = 1

			print ''




			
