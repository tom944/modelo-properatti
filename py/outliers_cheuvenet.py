def outliers(p_data):


    data_modificada = p_data

    # GENERO CULUMNA DE MEDIAS AGRUPANDO POR PCIA, BARRIO, TIPO DE PROPIEDAD
    data_modificada ['media_supTotal'] = data_modificada.groupby(['state_name','place_name','property_type'])['surface_total_in_m2'].transform('mean')
    data_modificada ['media_supCubierta'] = data_modificada.groupby(['state_name','place_name','property_type'])['surface_covered_in_m2'].transform('mean')
    data_modificada ['media_PrecioM2'] = data_modificada.groupby(['state_name','place_name','property_type'])['price_usd_per_m2'].transform('mean')
    data_modificada ['media_PrecioAproxUSD'] = data_modificada.groupby(['state_name','place_name','property_type'])['price_aprox_usd'].transform('mean')


    #GENERO COLUMNA DE STD AGRUPANDO POR PCIA, BARRIO, TIPO DE PROPIEDAD
    data_modificada ['std_supTotal'] = data_modificada.groupby(['state_name','place_name','property_type'])['surface_total_in_m2'].transform('std')
    data_modificada ['std_supCubierta'] = data_modificada.groupby(['state_name','place_name','property_type'])['surface_covered_in_m2'].transform('std')
    data_modificada ['std_PrecioM2'] = data_modificada.groupby(['state_name','place_name','property_type'])['price_usd_per_m2'].transform('std')
    data_modificada ['std_PrecioAproxUSD'] = data_modificada.groupby(['state_name','place_name','property_type'])['price_aprox_usd'].transform('std')


    #GENERO COLUMNA CON LA FORMULA DE CHEUVENET PARA EL CALCULO DE OUTLIERS
    data_modificada ['supTotal_criterio_cheuvenet'] = (abs(data_modificada.surface_total_in_m2-data_modificada.media_supTotal))/(data_modificada.std_supTotal)
    data_modificada ['supCubierta_criterio_cheuvenet'] = (abs(data_modificada.surface_covered_in_m2-data_modificada.media_supCubierta))/(data_modificada.std_supCubierta)
    data_modificada ['priceM2_criterio_cheuvenet'] = (abs(data_modificada.price_usd_per_m2-data_modificada.media_PrecioM2))/(data_modificada.std_PrecioM2)
    data_modificada ['priceAprox_criterio_cheuvenet'] = (abs(data_modificada.price_aprox_usd-data_modificada.media_PrecioAproxUSD))/(data_modificada.std_PrecioAproxUSD)

    
    
    #  % OUTLIERS SUPERFICIES TOTALES
    data_modificada.loc[data_modificada.supTotal_criterio_cheuvenet>2].shape[0]/data_modificada.shape[0]    
    data_modificada.surface_total_in_m2.loc[data_modificada.supTotal_criterio_cheuvenet>2] = np.nan
    
    
    #  % OUTLIERS SUPERFICIES CUBIERTAS
    data_modificada.loc[data_modificada.supCubierta_criterio_cheuvenet>2].shape[0]/data_modificada.shape[0] 
    data_modificada.surface_covered_in_m2.loc[data_modificada.supCubierta_criterio_cheuvenet>2] = np.nan
    
    
    #  % OUTLIERS DE PRECIOS APROX USD
    data_modificada.price_aprox_usd.loc[data_modificada.priceAprox_criterio_cheuvenet>2].shape[0]/data_modificada.shape[0]   
    data_modificada.price_aprox_usd.loc[data_modificada.priceAprox_criterio_cheuvenet>2] = np.nan
    
    #  % OUTLIERS DE PRECIOS POR M2
    data_modificada.loc[data_modificada.priceM2_criterio_cheuvenet>2].shape[0]/data_modificada.shape[0]
    data_modificada.price_usd_per_m2.loc[data_modificada.priceM2_criterio_cheuvenet>2] = np.nan
    
    
    
    return data_modificada 