from matplotlib import pyplot as plt 

Groups = ['Group1','Group2','Group3','Group4', 'Group5']  #значения для гистограммы 
Scores = [22, 30, 35, 35, 26]   
Scores2 = [25, 32, 30, 35, 29]   


N = 5
barWidth = .5
xloc = np.arange (N)

y_error1 = [4, 3, 4, 1, 5]  #погрешность
y_error2 = [3, 5, 2, 3, 3]


p1 = plt.bar (Groups, Scores, yerr = y_error1,      #  границы погрешностей
       ecolor = 'blue',  #  цвет линии погрешности
       capsize = 5,  width=barWidth, color = 'red')
p2 = plt.bar (Groups, Scores2, yerr = y_error2,      #  границы погрешностей
       ecolor = 'green',  #  цвет линии погрешности
       capsize = 5,  bottom=Scores, width=barWidth, color = 'green')


plt.legend((p1, p2), ['Men', 'Women']) #легедна гистограммы
plt.title('Scores by group and gender')   
plt.xlabel('Groups')   
plt.ylabel('Scores') 

plt.show() 