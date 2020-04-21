#SKLEARN

#GENERO VARIABLES INDEPENDIENTES
x_feactures = data_.iloc[:,40:]
df1 = data_['surface_total_in_m2']
xs = pd.concat([df1,x_feactures],axis=1)


#GENERO VARIABLE DEPENDIENTE
y = data_.price_usd_per_m2



#TRANSFORMO VARIABLES INDEPENDIENTES EN FORMATO MATRIZ
xs = xs.as_matrix()


#TRANSFORMO VARIABLE DEPENDIENTE EN FORMATO MATRIZ
y = y.as_matrix()




#IMPORTAR LIBRERIAS DE SKLEARN
from sklearn import linear_model
from sklearn.model_selection import train_test_split

#PARTICIONAR DATOS DE ENTRENAMIENTO Y TESTING
x_train, x_test, y_train, t_test = train_test_split(xs, y, test_size=0.2)


#FIT 
modelo = linear_model.LinearRegression()
modelo.fit(x_train,y_train)


#PREDECIR DATOS "Y" DE "X" TEST 
y_predict = modelo.predict(x_test)


#PENDIENTES
pendientes = modelo.coef_


#ORDENADA 
ordenada = modelo.intercept_


#R2
'EL RESULTADO DEL MODELO ES DE {}'.format(modelo.score(x_train,y_train))



'EL RESULTADO DEL MODELO ES DE {}'.format(modelo.score(x_train,y_train))