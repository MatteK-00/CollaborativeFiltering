
with open('FullData_2/LOG_K_Varianti.csv','r') as SM:
	ListByK_3 = [[],[],[],[]]
	for line in SM:
		t = line
		temp = t.split(",")
		ListByK_3[int(temp[4])-1].append((int(temp[2]),int(temp[3]),int(temp[0]),int(temp[1])))


with open('FullData_2/K_varianti_plot','w') as WR:

	var = ['mark=*, pink','mark=*, red','mark=*, blue','mark=*, green','mark=*, orange','mark=*, yellow','mark=*, gray','mark=*, black',
	'mark=o, pink','mark=o, red','mark=o, blue','mark=o, green','mark=o, orange','mark=o, yellow','mark=o, gray','mark=o, black']


	for k_3 in range(0,len(ListByK_3)):

		WR.write('\\begin{figure}[H] \n')
		WR.write('\\begin{tikzpicture} \n')
		WR.write('\\begin{axis}[scale=1.8,xlabel=$k_2$,ylabel=\\% TP, legend pos=outer north east] \n')


		k_1 = 1
		WR.write('\n')
		WR.write('% K_3 = '+ str(k_3 + 1) + '\n')
		WR.write('%    K_1 = ' + str(k_1) + '\n')
		WR.write('\\addplot[smooth,'+ var[k_1] +'] plot coordinates { ')
		for i in ListByK_3[k_3]:
			if i[0] == k_1:
				WR.write('('+str(i[1])+','+str(i[2]*100/float((943-i[3])*(k_3+1))) +')')
			else:
				WR.write('}; \n')
				k_1 += 1
				WR.write('%    K_1 = ' + str(k_1) + '\n')
				WR.write('\\addplot[smooth,'+ var[k_1] +'] plot coordinates { ')
				WR.write('('+str(i[1])+','+str(i[2]*100/float((943-i[3])*(k_3+1))) +')')


		WR.write('}; \n')
		WR.write(' \\legend{$K_1$ = 1,$K_1$ = 2,$K_1$ = 3,$K_1$ = 4,$K_1$ = 5,$K_1$ = 6,$K_1$ = 7,$K_1$ = 8,$K_1$ = 9,$K_1$ = 10,$K_1$ = 11,$K_1$ = 12,$K_1$ = 13,$K_1$ = 14,$K_1$ = 15,} \n')
		WR.write('\\end{axis} \n')
		WR.write('\\end{tikzpicture} \n')
		WR.write('\\label{fig:4} \n')
		WR.write('\\caption{TP al variare della dimensione del vicinato $k_1$ su $k_3$ = '+ str(k_3 + 1) + ' estrazioni per utente e $30\%$ di test set con '+ str(ListByK_3[k_3][3]) +' righe scartate.} \n')
		WR.write('\\end{figure} \n')
		WR.write('\n')
		WR.write('\n')		
		WR.write('\n')


