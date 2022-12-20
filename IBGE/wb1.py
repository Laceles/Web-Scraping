# -*- coding: utf-8 -*-


import requests
import pandas as pd
def municipio(x):
    codigo = x
    districts=requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/35/municipios").json()
    districts_df=[municipios['nome'] for municipios in districts]
    districts_id=[municipios['id'] for municipios in districts]
    data_sp=pd.DataFrame.from_dict({'ID':districts_id,'Municipios':districts_df})
    return data_sp.iloc[codigo,:]