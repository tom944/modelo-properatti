import matplotlib.pyplot as plt

#GENERO EJE X -> SUPERFICIE TOTAL
x1 = x_test[:,0]

#GENERO EJE Y -> PRECIO M2 DE TEST
x2 = y_test

# EJE Y -> PRECIO M2 PREDICHO
x3 = y_predict


#PLOT
plt.scatter(x1,x2,label='test modelo', color='blue')
plt.scatter(x1,x3,label='prediccion modelo', color='red')
plt.title('grafico modelo')
plt.show()