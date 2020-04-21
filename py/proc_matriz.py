import unidecode as uni
import pandas as pd 
import numpy as np
pd.set_option('chained_assignment',None)


def ejecutar_programa(salida):
    ##DEFINO FUNCIONES LOCALES DEL PROGRAMA
    def f_ambiente (x) :
        if x.contains("ambiente") :
            return 1
        else :
            return 0


    def obtengo_ambiente(x): 
        v_1 = x.lower()             # texto en minuscula
        v_2 = v_1.find('amb')     # posicion "amb"
        if v_2<0:
            return -1
        else:
            v_3 = v_2-2                     # posicion -2 OBTENGO NUMERO DE AMBIENTES
            v_4 = v_2-1                     # posicion -1 OBTENGO NUMERO DE AMBIENTES
            v_5 = v_1[v_3:v_4]
            return v_5
        
    def obtengo_dormitorio(x): 
        v_1 = x.lower()             # texto en minuscula
        v_2 = v_1.find('dorm')     # posicion "dormitorio"
        if v_2<0:
            return -1
        else:
            v_3 = v_2-2                     # posicion -2 OBTENGO NUMERO DE AMBIENTES
            v_4 = v_2-1                     # posicion -1 OBTENGO NUMERO DE AMBIENTES
            v_5 = v_1[v_3:v_4]
            return v_5
    
    def obtengo_depto(x): 
        v_1 = x.lower()             # texto en minuscula
        v_2 = v_1.find('dep')     # posicion "amb"
        if v_2<0:
            return -1
        else:
            v_3 = v_2-2                     # posicion -2 OBTENGO NUMERO DE AMBIENTES
            v_4 = v_2-1                     # posicion -1 OBTENGO NUMERO DE AMBIENTES
            v_5 = v_1[v_3:v_4]
            return v_5
    
    def devolver_un_ambiente (x):
        if x :
            return 1
    
    
    def inferir_error_superficies_mayores_cu():
        df_errores = []
        df_indices = []
        for i in data.state_name.unique():
            tam_total = pd.DataFrame(data[(data.surface_covered_in_m2>data.surface_covered_in_m2[data.state_name.str.contains(i)].mean())].sort_values('surface_covered_in_m2'))
            cantidad_error = tam_total.shape[0]*0.002
            cantidad_error = pd.Series(cantidad_error).astype(int)[0]
            indices_error = tam_total.tail(cantidad_error).index
            indices = data.loc[indices_error].index.values
            data.surface_covered_in_m2.loc[indices] = -1
    
    def inferir_error_superficies_menores_cu():
        df_errores = []
        df_indices = []
        for i in data.state_name.unique():
            tam_total = pd.DataFrame(data[(data.surface_covered_in_m2<data.surface_covered_in_m2[data.state_name.str.contains(i)].mean())].sort_values('surface_covered_in_m2'))
            cantidad_error = tam_total.shape[0]*0.018
            cantidad_error = pd.Series(cantidad_error).astype(int)[0]
            indices_error = tam_total.head(cantidad_error).index
            indices = data.loc[indices_error].index.values
            data.surface_covered_in_m2.loc[indices] = -2
    
    
    def inferir_error_superficies_mayores_total():
        df_errores = []
        df_indices = []
        for i in data.state_name.unique():
            tam_total = pd.DataFrame(data[(data.surface_total_in_m2>data.surface_total_in_m2[data.state_name.str.contains(i)].mean())].sort_values('surface_total_in_m2'))
            cantidad_error = tam_total.shape[0]*0.003
            cantidad_error = pd.Series(cantidad_error).astype(int)[0]
            indices_error = tam_total.tail(cantidad_error).index
            indices = data.loc[indices_error].index.values
            data.surface_total_in_m2.loc[indices] = -1
    
    def inferir_error_superficies_menores_total():
        df_errores = []
        df_indices = []
        for i in data.state_name.unique():
            tam_total = pd.DataFrame(data[(data.surface_total_in_m2<data.surface_total_in_m2[data.state_name.str.contains(i)].mean())].sort_values('surface_total_in_m2'))
            cantidad_error = tam_total.shape[0]*0.022
            cantidad_error = pd.Series(cantidad_error).astype(int)[0]
            indices_error = tam_total.head(cantidad_error).index
            indices = data.loc[indices_error].index.values
            data.surface_total_in_m2.loc[indices] = -2

    def inferir_error_precios_mayores_usd():    
        
        df_errores = []
        df_indices = []
    
        for i in data.state_name.unique():
            tam_total = pd.DataFrame(data[(data.price_aprox_usd>data.price_aprox_usd[data.state_name.str.contains(i)].mean())].sort_values('price_aprox_usd'))
            cantidad_error = tam_total.shape[0]*0.0015
            cantidad_error = pd.Series(cantidad_error).astype(int)[0]
            indices_error = tam_total.tail(cantidad_error).index
            indices = data.loc[indices_error].index.values
            data.price_aprox_usd.loc[indices] = -1
    
    
    def inferir_error_precios_menores_usd():    
        
        df_errores = []
        df_indices = []
    
        for i in data.state_name.unique():
            tam_total = pd.DataFrame(data[(data.price_aprox_usd<data.price_aprox_usd[data.state_name.str.contains(i)].mean())].sort_values('price_aprox_usd'))
            cantidad_error = tam_total.shape[0]*0.018
            cantidad_error = pd.Series(cantidad_error).astype(int)[0]
            indices_error = tam_total.head(cantidad_error).index
            indices = data.loc[indices_error].index.values
            data.price_aprox_usd.loc[indices] = -2
    
    
    def imputacion_automatica_ambientes(limite):

        data['imputar_ambientes'] = np.nan
        
        for i in range(1,limite): 
        
            #GENERAR GRUPOS DE SUPERFICIES
            data['categorias_sup_cubierta_por_m2'] = pd.qcut(data[data.surface_covered_in_m2>10].nueva_surface_total_in_m2,i)
            #CALCULAR MEDIAS CANTIDAD_AMBIENTES 
            dfImputacionesAmbientes = pd.DataFrame(data[data.ambientes_ceros!=0].groupby(['state_name','place_name','categorias_sup_cubierta_por_m2'])['ambientes_ceros'].mean())
            serie_imputaciones_ambientes = data.merge(dfImputacionesAmbientes,how='left',left_on=['state_name','place_name','categorias_sup_cubierta_por_m2'],right_on=['state_name','place_name','categorias_sup_cubierta_por_m2'])['ambientes_ceros_y']   
            data.imputar_ambientes.update(serie_imputaciones_ambientes)
            
        return data.imputar_ambientes
    
    
        
    def imputacion_automatica_superficies_cu(limite):

        data['imputando_superficies_cubiertas'] = np.nan
        
        for i in range(1,limite): 
        
            #GENERAR GRUPOS DE AMBIENTES EN PESOS
            data['ambientes_imputados_ceros'] = data.ambientes_imputados.fillna(0).astype(float)
            data['categorias_ambientes'] = pd.qcut(data[data.ambientes_imputados_ceros>=1].ambientes_imputados_ceros,i)
            #CALCULAR MEDIAS SUPERFICIES CUBIERTAS
            df_superficies_imput = pd.DataFrame(data[data.ambientes_imputados_ceros>=1].groupby(['state_name','place_name','property_type','categorias_ambientes'])['nueva_surface_total_in_m2'].mean())
            imputar_serie = data.merge(df_superficies_imput,how='left',left_on=['state_name','place_name','property_type','categorias_ambientes'],right_on=['state_name','place_name','property_type','categorias_ambientes'])['nueva_surface_total_in_m2_y']
            data.imputando_superficies_cubiertas.update(imputar_serie)

        return data.imputando_superficies_cubiertas
    
    
    def imputacion_automatica_sup_jardines(limite):
        
        data['imputando_superficie_jardines'] = np.nan
        
        for i in range(1,limite):
            
            data['categoria_superficie_total'] = pd.qcut(data.surface_total[(data.surface_total>=1)&(data.superficies_jardines.notnull())],i)
    
            ##SUPERFICIES JARDINES IMPUTACION
            df_sup_jardines = pd.DataFrame(data[(data.surface_total>=1)&(data.superficies_jardines.notnull())].groupby(['state_name','place_name','property_type','categoria_superficie_total'])['superficies_jardines'].mean())
            serie_imputar_sup_jardines = data.merge(df_sup_jardines,how='left',left_on=['state_name','place_name','property_type','categoria_superficie_total'], right_on=['state_name','place_name','property_type','categoria_superficie_total'])['superficies_jardines_y']
            data.imputando_superficie_jardines.update(serie_imputar_sup_jardines)
            
        return data.imputando_superficie_jardines
    
    
    
    def imputacion_automatica_sup_terraza(limite):
        
        data['imputando_superficie_terraza'] = np.nan
           
        for i in range(1,limite):
        
            data['categoria_superficie_total'] = pd.qcut(data.surface_total[(data.surface_total>=1)&(data.superficie_terraza.notnull())],i)
            
            ##SUPERFICIES TERRAZAS IMPUTACION
            df_sup_terrazas = pd.DataFrame(data[(data.surface_total>=1)&(data.superficie_terraza.notnull())].groupby(['state_name','place_name','property_type','categoria_superficie_total'])['superficie_terraza'].mean())
            serie_imputar_sup_jardines = data.merge(df_sup_terrazas, how='left', left_on=['state_name','place_name','property_type','categoria_superficie_total'], right_on=['state_name','place_name','property_type','categoria_superficie_total'])['superficie_terraza_y']
            data.imputando_superficie_terraza.update(serie_imputar_sup_jardines)
        
        return data.imputando_superficie_terraza
    
    
    
    def imputacion_automatica_sup_terraza_jardines(limite):
            
        data['imputando_superficie_terraza_jardines'] = np.nan
        
        for i in range (1,limite):
            
            data['categoria_superficie_total'] = pd.qcut(data.surface_total[(data.surface_total>=1)&(data.superficie_terraza_jardin.notnull())],i)

            ##SUPERFICIES TERRAZAS/JARDINES IMPUTACION
            df_sup_terrazas_jardines_terraza = pd.DataFrame(data[(data.surface_total>=1)&(data.superficie_terraza_jardin.notnull())].groupby(['state_name','place_name','property_type','categoria_superficie_total'])['superficie_terraza_jardin'].mean())
            serie_imputar_sup_jardines_terraza = data.merge(df_sup_terrazas_jardines_terraza, how='left',left_on=['state_name','place_name','property_type','categoria_superficie_total'], right_on=['state_name','place_name','property_type','categoria_superficie_total'])['superficie_terraza_jardin_y']
            data.imputando_superficie_terraza_jardines.update(serie_imputar_sup_jardines_terraza)
        
        return data.imputando_superficie_terraza_jardines
    
    
    def imputacion_automatica_sup_total(limite):
        
        data['imputando_superficie_total'] = np.nan
        
        for i in range(1,limite):
        
            ##IMPUTAR SUPERFICIES TOTALES CON JARDINES
            data['categorias_jardines'] = pd.qcut(data[data.superficie_jardin_imputada.notnull()].superficie_jardin_imputada,i)
            df_jardines = pd.DataFrame(data.groupby(['state_name','place_name','property_type','categorias_jardines'])['surface_total'].mean())
            serie_sup_total_jardines = data.merge(df_jardines,how='left',left_on=['state_name','place_name','property_type','categorias_jardines'],right_on=['state_name','place_name','property_type','categorias_jardines'])['surface_total_y']
            
            data.imputando_superficie_total.update(serie_sup_total_jardines)
            
            ##IMPUTAR SUPERFICIES TOTALES CON TERRAZAS
            data['categorias_terraza'] = pd.qcut(data[data.superficie_terraza_imputada.notnull()].superficie_terraza_imputada,10)
            df_terraza = pd.DataFrame(data.groupby(['state_name','place_name','property_type','categorias_terraza'])['surface_total'].mean())
            serie_sup_total_terrazas = data.merge(df_terraza, how='left',left_on=['state_name','place_name','property_type','categorias_terraza'],right_on=['state_name','place_name','property_type','categorias_terraza'])['surface_total_y']
            
            data.imputando_superficie_total.update(serie_sup_total_terrazas)
            
            
            ##IMPUTAR SUPERFICIES TOTALES CON JARDINES/TERRAZAS
            data['categorias_terraza_jardines'] = pd.qcut(data[data.sup_terraza_jardin_imputada.notnull()].sup_terraza_jardin_imputada,10)
            df_terraza_jardin = pd.DataFrame(data.groupby(['state_name','place_name','property_type','categorias_terraza_jardines'])['surface_total'].mean())
            serie_sup_total_terrazas_jardines = data.merge(df_terraza_jardin, how='left',left_on=['state_name','place_name','property_type','categorias_terraza_jardines'],right_on=['state_name','place_name','property_type','categorias_terraza_jardines'])['surface_total_y']
            
            data.imputando_superficie_total.update(serie_sup_total_terrazas_jardines)
            
            
        return data.imputando_superficie_total
    
    
    def imputacion_automatica_precios_usd(limite):

        data['imputar_precios_usd'] = np.nan
        
        for i in range(1,limite): 
                
            data['categorias_superficie_terraza'] = pd.qcut(data.superficie_terraza,i)
            ##IMPUTAR PRECIOS DE SUPERFICIES CON TERRAZA
            df_terraza = pd.DataFrame(data[data.categorias_superficie_terraza.notnull()].groupby(['state_name','place_name','property_type','categoria_superficie_cubierta_imputada','categorias_superficie_terraza'])['price_aprox_usd'].mean()) 
            data['imputar_precios_terraza'] = data.merge(df_terraza, how='left', left_on=['state_name','place_name','property_type','categoria_superficie_cubierta_imputada','categorias_superficie_terraza'],right_on=['state_name','place_name','property_type','categoria_superficie_cubierta_imputada','categorias_superficie_terraza'])['price_aprox_usd_y']
            data.imputar_precios_usd.update(data.imputar_precios_terraza)

            data['categorias_superficie_jardines']  = pd.qcut(data.superficies_jardines,i)
            ##IMPUTAR PRECIOS DE SUPERFICIES CON JARDINES
            df_jardin = pd.DataFrame(data[data.categorias_superficie_jardines.notnull()].groupby(['state_name','place_name','property_type','categoria_superficie_cubierta_imputada','categorias_superficie_jardines'])['price_aprox_usd'].mean())
            data['imputar_precios_jardines'] = data.merge(df_jardin,how='left',left_on=['state_name','place_name','property_type','categoria_superficie_cubierta_imputada','categorias_superficie_jardines'], right_on=['state_name','place_name','property_type','categoria_superficie_cubierta_imputada','categorias_superficie_jardines'])['price_aprox_usd_y']
            data.imputar_precios_usd.update(data.imputar_precios_jardines)

            data['categorias_superficie_terraza_jardin'] = pd.qcut(data.superficie_terraza_jardin,i)
            ##IMPUTAR PRECIOS DE SUPERFICIES CON TERRAZAS Y JARDINES 
            df_terraza_jardin = pd.DataFrame(data[data.categorias_superficie_terraza_jardin.notnull()].groupby(['state_name','place_name','property_type','categoria_superficie_cubierta_imputada','categorias_superficie_terraza_jardin'])['price_aprox_usd'].mean())
            data['imputar_precios_terraza_jardin'] = data.merge(df_terraza_jardin, how='left', left_on=['state_name','place_name','property_type','categoria_superficie_cubierta_imputada','categorias_superficie_terraza_jardin'], right_on=['state_name','place_name','property_type','categoria_superficie_cubierta_imputada','categorias_superficie_terraza_jardin'])['price_aprox_usd_y']
            data.imputar_precios_usd.update(data.imputar_precios_terraza_jardin)

        return data.imputar_precios_usd
    
    def imputacion_automatica_precios_usd_sup_total(limite):
        
        data['imputar_precios_usd'] = np.nan
        
        for i in range(1,limite):
            
            data['categorias_superficie_total_m2'] = pd.qcut(data.surface_total,i)
            df_precio_sup_total = pd.DataFrame(data.groupby(['state_name','place_name','property_type','categorias_superficie_total_m2'])['price_aprox_usd'].mean())
            serie_imputada_precio_sup_total = data.merge(df_precio_sup_total,how='left',left_on=['state_name','place_name','property_type','categorias_superficie_total_m2'], right_on=['state_name','place_name','property_type','categorias_superficie_total_m2'])['price_aprox_usd_y']            
            data.imputar_precios_usd.update(serie_imputada_precio_sup_total)            
        
        return data.imputar_precios_usd
    
    #LEER ARCHIVO
    data = pd.read_csv('/home/DS-DH/DigitalHouse/desafio/properatti.csv')
    #data = data[data['Unnamed: 0']!=11]
    
    #QUITO LAS FILAS REPETIDAS DEL CAMPO DESCRIPCION
    data = data.drop_duplicates(subset=['description'], keep='first')
    
    #QUITO LAS FILAS CON SUPERFICIE CUBIERTA MENOR A 16
    data = data[(data.surface_covered_in_m2>16)|(data.surface_covered_in_m2.isnull())]
    
    #QUITO LAS FILAS CON SUPERFICIE TOTAL MENOR A 16
    data = data[(data.surface_total_in_m2>16)|(data.surface_total_in_m2.isnull())]
    
    #QUITO LAS FILAS CON SUPERFICIES CUBIERTAS MENOR 50 DE CASAS 
    data = data[(~((data.surface_covered_in_m2<50)&(data.property_type.str.contains('house'))))]
    
    #QUITO LAS FILAS CON SUPERFICIE TOTAL MENOR 50 DE CASAS 
    data = data[(~((data.surface_total_in_m2<50)&(data.property_type.str.contains('house'))))]
  
    #PONGO NULOS LOS VALORES DE SUPERFICIE CUBIERTA CUANDO SUPERFICIE_CUBIERTA>SUPERFICIE_TOTAL
    data.surface_covered_in_m2[data.surface_covered_in_m2>data.surface_total_in_m2] = np.nan 
    
    ##INFERIMOS EL ERROR 
    #inferir_error_superficies_mayores_cu()
    #inferir_error_superficies_menores_cu()
    #inferir_error_superficies_mayores_total()
    #inferir_error_superficies_menores_total()
    #inferir_error_precios_mayores_usd()    
    #inferir_error_precios_menores_usd()    
    
    ##DESISTIMO EL ERROR QUITANDO LAS FILAS CALCULADAS EN EL PASO ANTERI
    #data = data[(data.surface_covered_in_m2>0)|(data.surface_covered_in_m2.isnull())]
    #data = data[(data.surface_total_in_m2>0)|(data.surface_total_in_m2.isnull())]
    #data = data[(data.price_aprox_usd>0)|(data.price_aprox_usd.isnull())]
    
    
    
    #REEMPLAZAR STRING |    
    replace_place = data.place_with_parent_names.str.replace("|",",").str[1:-1].str.split(',')
  
    
    ##AGREGO COLUMNA DE PAIS
    data["pais_2"] = replace_place[:].str[0].str.lower()
    ##AGREGO COLUMNA DE LOCALIDAD
    data["localidad_2"] = replace_place[:].str[1].str.lower()
    ##AGREGO COLUMNA DE BARRIO
    data["barrio_2"] = replace_place[:].str[2].str.lower()
    ##AGREGO COLUMNA BARRIO EXTRA
    data["barrio_2b"] = replace_place[:].str[3].str.lower()
    

    
    ##REEMPLAZO COLUMNAS DESCRIPCION Y TITULO (MINUSCULAS Y ACENTOS)
    data.description = data.description.astype(str).apply(uni.unidecode).str.lower()
    data.title = data.title.astype(str).apply(uni.unidecode).str.lower()
    
    
    ##OBTENGOS JARDINES, TERRAZAS 
    booleanos_jardines =(data.description.str.contains('parquizado'))|(data.description.str.contains('patio'))|(data.description.str.contains('jardin')) 
    booleanos_terraza = (data.description.str.contains('terraza'))|(data.description.str.contains('quincho')) 
    
    
    ##CALCULO SUPERFICIES DE JARDINES (SIN TERRAZA) 
    
    serie_jardines = (booleanos_jardines) & (~booleanos_terraza) & (data.surface_covered_in_m2.notnull()) & (data.surface_total_in_m2.notnull())
    data['superficie_jardin_patio'] = data.surface_total_in_m2[serie_jardines]-data.surface_covered_in_m2[serie_jardines]
    serie_superficie_jardines = pd.DataFrame(data.superficie_jardin_patio[(data.superficie_jardin_patio.notnull()) & (data.superficie_jardin_patio > 0)])
    data['superficies_jardines'] = data.merge(serie_superficie_jardines,how='left',left_on=['Unnamed: 0'],right_index=True)['superficie_jardin_patio_y']

        
    ##CALCULO SUPERFICIES DE TERRAZAS (SIN JARDINES)
    serie_terraza = (booleanos_terraza) & (~booleanos_jardines) & (data.surface_covered_in_m2.notnull()) & (data.surface_total_in_m2.notnull())
    superficie_terraza_indices = pd.DataFrame(data.surface_total_in_m2[serie_terraza]-data.surface_covered_in_m2[serie_terraza],columns=['terraza_y'])    
    columna_superficie_terraza = data.merge(superficie_terraza_indices[superficie_terraza_indices.terraza_y>0],how='left', left_on=['Unnamed: 0'],right_index=True)['terraza_y']
    data['superficie_terraza'] = columna_superficie_terraza
    
    
    ##CALCULO SUPERFICIES DE TERRAZAS CON JARDINES
    serie_terraza_jardin = (booleanos_terraza) & (booleanos_jardines) & (data.surface_covered_in_m2.notnull()) & (data.surface_total_in_m2.notnull())
    superficie_terraza_jardin_indices = pd.DataFrame(data.surface_total_in_m2[serie_terraza_jardin]-data.surface_covered_in_m2[serie_terraza_jardin],columns=['terraza_jardin_y'])
    columna_superficie_terraza_jardin = data.merge(superficie_terraza_jardin_indices[superficie_terraza_jardin_indices.terraza_jardin_y>0],how='left', left_on=['Unnamed: 0'], right_index=True)['terraza_jardin_y']
    data['superficie_terraza_jardin'] = columna_superficie_terraza_jardin
    
        
    ##CONTIENE AMBIENTES EN CAMPO DESCRIPCION 
    un_ambiente = data[data.rooms<=7].description.str.contains("ambiente ") | data.description.str.contains("amb.","amb ") & data.description.str.contains("1 amb")
    dos_o_mas_ambientes = data.description.str.contains("ambientes") | data.description.str.contains("2 amb")
    data["un_ambiente"]=un_ambiente
        

    
    cant_ambientes_old_desc = data[data.rooms<=7].description.astype(str).apply(obtengo_ambiente)
    cant_ambientes_old_title = data[data.rooms<=7].title.astype(str).apply(obtengo_ambiente)
    cant_ambientes_desc = cant_ambientes_old_desc.str.extract(r'(\d+)')
    cant_ambientes_title = cant_ambientes_old_title.str.extract(r'(\d+)')
    
    data['cantidad_ambientes_desc'] = cant_ambientes_desc
    data['cantidad_ambientes_title'] = cant_ambientes_title
    
    data['un_ambiente'] = data.un_ambiente
    data['monoambiente'] = data[data.rooms<=7].description.str.contains('monoambiente') | data.description.str.contains('mono ambiente') | data.title.str.contains('monoambiente') | data.title.str.contains('mono ambiente')  

    
    data['ambientes'] = data.rooms[data.rooms.fillna(100).astype(int)<6].astype(int)
    
    var_un_ambiente = data.un_ambiente.apply(devolver_un_ambiente)
    var_monoambiente = data.monoambiente.apply(devolver_un_ambiente)
    #data.cantidad_ambientes_title.update(data.cantidad_ambientes_desc)
    data.ambientes.update(data.cantidad_ambientes_title)
    data.ambientes.update(data.cantidad_ambientes_desc)
    
    
    
    data['var_un_ambiente'] = var_un_ambiente
    data['var_monoambiente'] = var_monoambiente
    data.var_un_ambiente.update(data.ambientes)
    data.var_monoambiente.update(data.var_un_ambiente)
    
    
    data['nuevos_ambientes'] = data.var_monoambiente 
    
    data['ambientes_ceros'] = data.nuevos_ambientes.fillna(0).astype(int) 
    #data['grupos_ambientes'] = pd.cut(data.ambientes_ceros,[0,4!=0])
    
    
    ##GUARDO COLUMNA TITLE
    data['surface_total'] = data.surface_total_in_m2
    
    data.surface_total_in_m2.update(data.surface_covered_in_m2)
    data['nueva_surface_total_in_m2'] = data.surface_total_in_m2 
        

    ##IMPUTAR AMBIENTES
    data['ambientes_imputados'] = imputacion_automatica_ambientes(20)
    data.ambientes_imputados.update(data.nuevos_ambientes)
    
        
    #IMPUTAR FALTANTES CANTIDAD_AMBIENTES CON SUPERFICIES CUBIERTAS
    data['superficie_cubierta_imputada'] = np.nan
    imputar_serie = imputacion_automatica_superficies_cu(5)
    data.superficie_cubierta_imputada.update(imputar_serie)

    data.superficie_cubierta_imputada.update(data.nueva_surface_total_in_m2)
    data.superficie_cubierta_imputada[(data.superficie_cubierta_imputada<50)&(data.property_type.str.contains('house'))] = np.nan
    
    ##IMPUTAR SUPERFICIE JARDIN
    data['superficie_jardin_imputada'] = imputacion_automatica_sup_jardines(10)
    data.superficie_jardin_imputada.update(data.superficies_jardines)
    
    ##IMPUTAR SUPERFICIE TERRAZA
    data['superficie_terraza_imputada'] = imputacion_automatica_sup_terraza(10)
    data.superficie_terraza_imputada.update(data.superficie_terraza)
    
    ##IMPUTAR SUPERFICIE JARDIN/TERRAZA
    data['sup_terraza_jardin_imputada'] = imputacion_automatica_sup_terraza_jardines(10)
    data.sup_terraza_jardin_imputada.update(data.superficie_terraza_jardin)
    
    
    ##IMPUTAR SUPERFICIE TOTAL DE JARDINES TERRAZAS 
    data['superficie_total_imputada'] = imputacion_automatica_sup_total(20)
    data.superficie_total_imputada.update(data.surface_total)
    
    
    
    ##CUANDO LA SUPERFICIE TOTAL < SUPERFICIE CUBIERTA REEMPLAZO CON SUPERFICIE CUBIERTA + JARDIN/TERRAZA
    data['superficie_jardin_imputada_ceros'] = data.superficie_jardin_imputada.fillna(0)
    data['superficie_terraza_imputada_ceros'] = data.superficie_terraza_imputada.fillna(0)
    data['sup_terraza_jardin_imputada_ceros'] = data.sup_terraza_jardin_imputada.fillna(0)
    data.superficie_total_imputada[data.superficie_total_imputada<data.superficie_cubierta_imputada] = data.superficie_cubierta_imputada + data.superficie_jardin_imputada_ceros + data.superficie_terraza_imputada_ceros + data.sup_terraza_jardin_imputada_ceros
    
    
    
    ##IMPUTAR PRECIOS USD
    data['precios_usd_imputados'] = np.nan
    data['categoria_superficie_cubierta_imputada'] = pd.qcut(data[data.superficie_cubierta_imputada>=10].superficie_cubierta_imputada,5)
    
    
    
    #ACTUALIZO POR SUPERFICIE TOTAL
    serie_imputada_sup_total_precios = imputacion_automatica_precios_usd_sup_total(20)
    data.precios_usd_imputados.update(serie_imputada_sup_total_precios)
    
    #ACTUALIZO POR SUPERFICIE CUBIERTA (JARDINES; TERRAZAS; JARDINES Y TERRAZAS)
    serie_imputada_precios = imputacion_automatica_precios_usd(20)
    data.precios_usd_imputados.update(serie_imputada_precios)
    
    #ACTUALIZO POR COLUMNA PRICE_APROX_USD
    data.precios_usd_imputados.update(data.price_aprox_usd)
    
    
    if salida == 1:
        return data
    
    
    
    #GENERAR MATRIZ
    matriz = pd.DataFrame({ 'id':data['Unnamed: 0'],
                            'tipo':data['operation'],
                            'propiedad':data.property_type,
                            'id_localizacion':data.geonames_id,
                            'pais':data.country_name.astype(str).apply(uni.unidecode).str.lower(),
                            'localidad':data.state_name.astype(str).apply(uni.unidecode).str.lower(),
                            'barrio':data.place_name.astype(str).apply(uni.unidecode).str.lower(),
                            'barrio_2b':data.barrio_2b.astype(str).apply(uni.unidecode).str.lower(),
                            'latitud':data.lat,
                            'longitud':data.lon,
                            'moneda':data.currency.str.lower(),
                            'ambientes':data.ambientes_imputados,
                            'ambientes_ceros':data.ambientes_imputados.fillna(0),
                            'nuevos_ambientes' : data.nuevos_ambientes,
                            'superficie_total':data.superficie_total_imputada,
                            'superficie_cubierta_m2':data.superficie_cubierta_imputada,
                            'precio_aprox_usd':data.precios_usd_imputados       
                   } )
    
    if salida == 0: 
        return matriz
  