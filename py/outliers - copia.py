def proceso_quitar_outliers(parametro_data):


    import pandas as pd 
    import numpy as np
    pd.set_option('chained_assignment',None)

    def quitar_outliers():

        data = pd.read_csv('properatti.csv')
        data_outliers = data

        def generar_outliers_indices_casas_supTotal():
            lista_indices=[]
            for pcia in data.state_name.unique():
                media_supTotal_casas_caba = data.loc[(data.property_type.str.contains('house'))&(data.state_name.str.contains(pcia))].groupby(['state_name','place_name','property_type'])['surface_total_in_m2'].mean().reset_index()['surface_total_in_m2'].mean()
                numero_techo = data.surface_total_in_m2.loc[(data.property_type.str.contains('house'))&(data.state_name.str.contains(pcia))&(data.surface_total_in_m2>media_supTotal_casas_caba)].sort_values().shape[0]
                numero_techo = int((numero_techo*0.1))
                techos_caba = data.surface_total_in_m2.loc[(data.property_type.str.contains('house'))&(data.state_name.str.contains(pcia))&(data.surface_total_in_m2>media_supTotal_casas_caba)].sort_values()
                indices = techos_caba.tail(numero_techo).index
                lista_indices.append(indices)

            data_outliers=data.loc[data.surface_total_in_m2==-1]  
            lista  = []

            for i in lista_indices:
                lista.append(data.loc[i])

            for i in lista:
                data_outliers = data_outliers.append(i)


            return data_outliers


        def generar_outliers_indices_ph_supTotal():
            lista_indices=[]
            for pcia in data.state_name.unique():
                media_supTotal_casas_caba = data.loc[(data.property_type.str.contains('PH'))&(data.state_name.str.contains(pcia))].groupby(['state_name','place_name','property_type'])['surface_total_in_m2'].mean().reset_index()['surface_total_in_m2'].mean()
                numero_techo = data.surface_total_in_m2.loc[(data.property_type.str.contains('PH'))&(data.state_name.str.contains(pcia))&(data.surface_total_in_m2>media_supTotal_casas_caba)].sort_values().shape[0]
                numero_techo = int((numero_techo*0.1))
                techos_caba = data.surface_total_in_m2.loc[(data.property_type.str.contains('PH'))&(data.state_name.str.contains(pcia))&(data.surface_total_in_m2>media_supTotal_casas_caba)].sort_values()
                indices = techos_caba.tail(numero_techo).index
                lista_indices.append(indices)

            data_outliers=data.loc[data.surface_total_in_m2==-1]  
            lista  = []

            for i in lista_indices:
                lista.append(data.loc[i])

            for i in lista:
                data_outliers = data_outliers.append(i)


            return data_outliers


        def generar_outliers_indices_apartment_supTotal():
            lista_indices=[]
            for pcia in data.state_name.unique():
                media_supTotal_casas_caba = data.loc[(data.property_type.str.contains('apartment'))&(data.state_name.str.contains(pcia))].groupby(['state_name','place_name','property_type'])['surface_total_in_m2'].mean().reset_index()['surface_total_in_m2'].mean()
                numero_techo = data.surface_total_in_m2.loc[(data.property_type.str.contains('apartment'))&(data.state_name.str.contains(pcia))&(data.surface_total_in_m2>media_supTotal_casas_caba)].sort_values().shape[0]
                numero_techo = int((numero_techo*0.1))
                techos_caba = data.surface_total_in_m2.loc[(data.property_type.str.contains('apartment'))&(data.state_name.str.contains(pcia))&(data.surface_total_in_m2>media_supTotal_casas_caba)].sort_values()
                indices = techos_caba.tail(numero_techo).index
                lista_indices.append(indices)

            data_outliers=data.loc[data.surface_total_in_m2==-1]  
            lista  = []

            for i in lista_indices:
                lista.append(data.loc[i])

            for i in lista:
                data_outliers = data_outliers.append(i)


            return data_outliers



        data_outliers_supTotal_casas = generar_outliers_indices_casas_supTotal()
        data_outliers_supTotal_ph = generar_outliers_indices_ph_supTotal()
        data_outliers_supTotal_apartment = generar_outliers_indices_apartment_supTotal()
        data_outliers_supTotal = data_outliers_supTotal_casas.append(data_outliers_supTotal_ph)
        data_outliers_supTotal = data_outliers_supTotal.append(data_outliers_supTotal_apartment)


        def generar_outliers_indices_casas_supCubierta():
            lista_indices=[]
            for pcia in data.state_name.unique():
                media_supTotal_casas_caba = data.loc[(data.property_type.str.contains('house'))&(data.state_name.str.contains(pcia))].groupby(['state_name','place_name','property_type'])['surface_covered_in_m2'].mean().reset_index()['surface_covered_in_m2'].mean()
                numero_techo = data.surface_covered_in_m2.loc[(data.property_type.str.contains('house'))&(data.state_name.str.contains(pcia))&(data.surface_covered_in_m2>media_supTotal_casas_caba)].sort_values().shape[0]
                numero_techo = int((numero_techo*0.1))
                techos_caba = data.surface_covered_in_m2.loc[(data.property_type.str.contains('house'))&(data.state_name.str.contains(pcia))&(data.surface_covered_in_m2>media_supTotal_casas_caba)].sort_values()
                indices = techos_caba.tail(numero_techo).index
                lista_indices.append(indices)

            data_outliers=data.loc[data.surface_covered_in_m2==-1]  
            lista  = []

            for i in lista_indices:
                lista.append(data.loc[i])

            for i in lista:
                data_outliers = data_outliers.append(i)


            return data_outliers


        def generar_outliers_indices_ph_supCubierta():
            lista_indices=[]
            for pcia in data.state_name.unique():
                media_supTotal_casas_caba = data.loc[(data.property_type.str.contains('PH'))&(data.state_name.str.contains(pcia))].groupby(['state_name','place_name','property_type'])['surface_covered_in_m2'].mean().reset_index()['surface_covered_in_m2'].mean()
                numero_techo = data.surface_covered_in_m2.loc[(data.property_type.str.contains('PH'))&(data.state_name.str.contains(pcia))&(data.surface_covered_in_m2>media_supTotal_casas_caba)].sort_values().shape[0]
                numero_techo = int((numero_techo*0.1))
                techos_caba = data.surface_covered_in_m2.loc[(data.property_type.str.contains('PH'))&(data.state_name.str.contains(pcia))&(data.surface_covered_in_m2>media_supTotal_casas_caba)].sort_values()
                indices = techos_caba.tail(numero_techo).index
                lista_indices.append(indices)

            data_outliers=data.loc[data.surface_covered_in_m2==-1]  
            lista  = []

            for i in lista_indices:
                lista.append(data.loc[i])

            for i in lista:
                data_outliers = data_outliers.append(i)


            return data_outliers


        def generar_outliers_indices_apartment_supCubierta():
            lista_indices=[]
            for pcia in data.state_name.unique():
                media_supCubierta_casas_caba = data.loc[(data.property_type.str.contains('apartment'))&(data.state_name.str.contains(pcia))].groupby(['state_name','place_name','property_type'])['surface_covered_in_m2'].mean().reset_index()['surface_covered_in_m2'].mean()
                numero_techo = data.surface_covered_in_m2.loc[(data.property_type.str.contains('apartment'))&(data.state_name.str.contains(pcia))&(data.surface_covered_in_m2>media_supCubierta_casas_caba)].sort_values().shape[0]
                numero_techo = int((numero_techo*0.1))
                techos_caba = data.surface_covered_in_m2.loc[(data.property_type.str.contains('apartment'))&(data.state_name.str.contains(pcia))&(data.surface_covered_in_m2>media_supCubierta_casas_caba)].sort_values()
                indices = techos_caba.tail(numero_techo).index
                lista_indices.append(indices)

            data_outliers=data.loc[data.surface_covered_in_m2==-1]  
            lista  = []

            for i in lista_indices:
                lista.append(data.loc[i])

            for i in lista:
                data_outliers = data_outliers.append(i)


            return data_outliers



        data_outliers_supCubierta_casas = generar_outliers_indices_casas_supCubierta()
        data_outliers_supCubierta_ph = generar_outliers_indices_ph_supCubierta()
        data_outliers_supCubierta_apartment = generar_outliers_indices_apartment_supCubierta()
        data_outliers_supCubierta = data_outliers_supCubierta_casas.append(data_outliers_supCubierta_ph)
        data_outliers_supCubierta = data_outliers_supCubierta.append(data_outliers_supCubierta_apartment)


        def generar_outliers_indices_casas_preciosAprox():
            lista_indices=[]
            for pcia in data.state_name.unique():
                media_supTotal_casas_caba = data.loc[(data.property_type.str.contains('house'))&(data.state_name.str.contains(pcia))].groupby(['state_name','place_name','property_type'])['price_aprox_usd'].mean().reset_index()['price_aprox_usd'].mean()
                numero_techo = data.price_aprox_usd.loc[(data.property_type.str.contains('house'))&(data.state_name.str.contains(pcia))&(data.price_aprox_usd>media_supTotal_casas_caba)].sort_values().shape[0]
                numero_techo = int((numero_techo*0.1))
                techos_caba = data.price_aprox_usd.loc[(data.property_type.str.contains('house'))&(data.state_name.str.contains(pcia))&(data.price_aprox_usd>media_supTotal_casas_caba)].sort_values()
                indices = techos_caba.tail(numero_techo).index
                lista_indices.append(indices)

            data_outliers=data.loc[data.price_aprox_usd==-1]  
            lista  = []

            for i in lista_indices:
                lista.append(data.loc[i])

            for i in lista:
                data_outliers = data_outliers.append(i)


            return data_outliers


        def generar_outliers_indices_ph_preciosAprox():
            lista_indices=[]
            for pcia in data.state_name.unique():
                media_supTotal_casas_caba = data.loc[(data.property_type.str.contains('PH'))&(data.state_name.str.contains(pcia))].groupby(['state_name','place_name','property_type'])['price_aprox_usd'].mean().reset_index()['price_aprox_usd'].mean()
                numero_techo = data.price_aprox_usd.loc[(data.property_type.str.contains('PH'))&(data.state_name.str.contains(pcia))&(data.price_aprox_usd>media_supTotal_casas_caba)].sort_values().shape[0]
                numero_techo = int((numero_techo*0.1))
                techos_caba = data.price_aprox_usd.loc[(data.property_type.str.contains('PH'))&(data.state_name.str.contains(pcia))&(data.price_aprox_usd>media_supTotal_casas_caba)].sort_values()
                indices = techos_caba.tail(numero_techo).index
                lista_indices.append(indices)

            data_outliers=data.loc[data.price_aprox_usd==-1]  
            lista  = []

            for i in lista_indices:
                lista.append(data.loc[i])

            for i in lista:
                data_outliers = data_outliers.append(i)


            return data_outliers


        def generar_outliers_indices_apartment_preciosAprox():
            lista_indices=[]
            for pcia in data.state_name.unique():
                media_supPrecioAprox_casas_caba = data.loc[(data.property_type.str.contains('apartment'))&(data.state_name.str.contains(pcia))].groupby(['state_name','place_name','property_type'])['price_aprox_usd'].mean().reset_index()['price_aprox_usd'].mean()
                numero_techo = data.price_aprox_usd.loc[(data.property_type.str.contains('apartment'))&(data.state_name.str.contains(pcia))&(data.price_aprox_usd>media_supPrecioAprox_casas_caba)].sort_values().shape[0]
                numero_techo = int((numero_techo*0.1))
                techos_caba = data.price_aprox_usd.loc[(data.property_type.str.contains('apartment'))&(data.state_name.str.contains(pcia))&(data.price_aprox_usd>media_supPrecioAprox_casas_caba)].sort_values()
                indices = techos_caba.tail(numero_techo).index
                lista_indices.append(indices)

            data_outliers=data.loc[data.price_aprox_usd==-1]  
            lista  = []

            for i in lista_indices:
                lista.append(data.loc[i])

            for i in lista:
                data_outliers = data_outliers.append(i)


            return data_outliers



        data_outliers_supPrecioAprox_casas = generar_outliers_indices_casas_preciosAprox()
        data_outliers_supPrecioAprox_ph = generar_outliers_indices_ph_preciosAprox()
        data_outliers_supPrecioAprox_apartment = generar_outliers_indices_apartment_preciosAprox()
        data_outliers_supPrecioAprox = data_outliers_supPrecioAprox_casas.append(data_outliers_supPrecioAprox_ph)
        data_outliers_supPrecioAprox = data_outliers_supPrecioAprox.append(data_outliers_supPrecioAprox_apartment)


        def generar_outliers_indices_casas_PrecioM2():
            lista_indices=[]
            for pcia in data.state_name.unique():
                media_supTotal_casas_caba = data.loc[(data.property_type.str.contains('house'))&(data.state_name.str.contains(pcia))].groupby(['state_name','place_name','property_type'])['price_usd_per_m2'].mean().reset_index()['price_usd_per_m2'].mean()
                numero_techo = data.price_usd_per_m2.loc[(data.property_type.str.contains('house'))&(data.state_name.str.contains(pcia))&(data.price_usd_per_m2>media_supTotal_casas_caba)].sort_values().shape[0]
                numero_techo = int((numero_techo*0.1))
                techos_caba = data.price_usd_per_m2.loc[(data.property_type.str.contains('house'))&(data.state_name.str.contains(pcia))&(data.price_usd_per_m2>media_supTotal_casas_caba)].sort_values()
                indices = techos_caba.tail(numero_techo).index
                lista_indices.append(indices)

            data_outliers=data.loc[data.price_usd_per_m2==-1]  
            lista  = []

            for i in lista_indices:
                lista.append(data.loc[i])

            for i in lista:
                data_outliers = data_outliers.append(i)


            return data_outliers


        def generar_outliers_indices_ph_PrecioM2():
            lista_indices=[]
            for pcia in data.state_name.unique():
                media_supTotal_casas_caba = data.loc[(data.property_type.str.contains('PH'))&(data.state_name.str.contains(pcia))].groupby(['state_name','place_name','property_type'])['price_usd_per_m2'].mean().reset_index()['price_usd_per_m2'].mean()
                numero_techo = data.price_usd_per_m2.loc[(data.property_type.str.contains('PH'))&(data.state_name.str.contains(pcia))&(data.price_usd_per_m2>media_supTotal_casas_caba)].sort_values().shape[0]
                numero_techo = int((numero_techo*0.1))
                techos_caba = data.price_usd_per_m2.loc[(data.property_type.str.contains('PH'))&(data.state_name.str.contains(pcia))&(data.price_usd_per_m2>media_supTotal_casas_caba)].sort_values()
                indices = techos_caba.tail(numero_techo).index
                lista_indices.append(indices)

            data_outliers=data.loc[data.price_usd_per_m2==-1]  
            lista  = []

            for i in lista_indices:
                lista.append(data.loc[i])

            for i in lista:
                data_outliers = data_outliers.append(i)


            return data_outliers


        def generar_outliers_indices_apartment_PrecioM2():
            lista_indices=[]
            for pcia in data.state_name.unique():
                media_supPrecioM2_casas_caba = data.loc[(data.property_type.str.contains('apartment'))&(data.state_name.str.contains(pcia))].groupby(['state_name','place_name','property_type'])['price_usd_per_m2'].mean().reset_index()['price_usd_per_m2'].mean()
                numero_techo = data.price_usd_per_m2.loc[(data.property_type.str.contains('apartment'))&(data.state_name.str.contains(pcia))&(data.price_usd_per_m2>media_supPrecioM2_casas_caba)].sort_values().shape[0]
                numero_techo = int((numero_techo*0.1))
                techos_caba = data.price_usd_per_m2.loc[(data.property_type.str.contains('apartment'))&(data.state_name.str.contains(pcia))&(data.price_usd_per_m2>media_supPrecioM2_casas_caba)].sort_values()
                indices = techos_caba.tail(numero_techo).index
                lista_indices.append(indices)

            data_outliers=data.loc[data.price_usd_per_m2==-1]  
            lista  = []

            for i in lista_indices:
                lista.append(data.loc[i])

            for i in lista:
                data_outliers = data_outliers.append(i)


            return data_outliers



        data_outliers_supPrecioM2_casas = generar_outliers_indices_casas_PrecioM2()
        data_outliers_supPrecioM2_ph = generar_outliers_indices_ph_PrecioM2()
        data_outliers_supPrecioM2_apartment = generar_outliers_indices_apartment_PrecioM2()
        data_outliers_supPrecioM2 = data_outliers_supPrecioM2_casas.append(data_outliers_supPrecioM2_ph)
        data_outliers_supPrecioM2 = data_outliers_supPrecioM2.append(data_outliers_supPrecioM2_apartment)

        ##PONGO EN "0" LAS FILAS OUTLINERS DE CADA CAMPO
        data_outliers_supTotal.surface_total_in_m2=0
        data_outliers_supCubierta.surface_covered_in_m2=0
        data_outliers_supPrecioAprox.price_aprox_usd=0
        data_outliers_supPrecioM2.price_usd_per_m2=0


        ##MERGEO LOS DF GENERADOS
        s_nuevaSupTotal = data.merge(data_outliers_supTotal, how='left', left_index=True, right_index=True)['surface_total_in_m2_y']
        s_nuevaSupCubierta = data.merge(data_outliers_supCubierta, how='left', left_index=True, right_index=True)['surface_covered_in_m2_y']
        s_nuevaSupCubierta = data.merge(data_outliers_supPrecioAprox, how='left', left_index=True, right_index=True)['price_aprox_usd_y']
        s_nuevaSupCubierta = data.merge(data_outliers_supPrecioM2, how='left', left_index=True, right_index=True)['price_usd_per_m2_y']

        ##ACTUALIZO LAS FILAS OUTLIERS
        data_outliers.surface_total_in_m2.update(s_nuevaSupTotal)
        data_outliers.surface_covered_in_m2.update(s_nuevaSupCubierta)
        data_outliers.price_aprox_usd.update(s_nuevaSupCubierta)
        data_outliers.price_usd_per_m2.update(s_nuevaSupCubierta)

        ##ACTUALIZO A NAN LAS FILAS OUTLIERS
        data_outliers.surface_total_in_m2.loc[data.surface_total_in_m2==0] = np.nan
        data_outliers.surface_covered_in_m2.loc[data.surface_covered_in_m2==0]=np.nan
        data_outliers.price_aprox_usd.loc[data.price_aprox_usd==0]=np.nan
        data_outliers.price_usd_per_m2.loc[data.price_usd_per_m2==0]=np.nan


        data = pd.read_csv('properatti.csv')



        return data_outliers

    
    data = parametro_data
    data_sin_outliers = quitar_outliers()
    
    return data_sin_outliers

    
    
    