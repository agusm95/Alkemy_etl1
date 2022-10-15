from operator import index
from matplotlib.pyplot import margins
import pandas as pd
from sqlalchemy import values

"""Creacion de las tablas"""

bibliotecas_df = pd.read_csv(r'bibliotecas\2021-noviembre\bibliotecas-03-11-2021.csv')
museos_df = pd.read_csv(r'museos\2021-noviembre\museos-03-11-2021.csv')
salas_de_cine_df = pd.read_csv(r'salas_de_cine\2021-noviembre\salas_de_cine-03-11-2021.csv')

tabla_principal = pd.DataFrame(columns=['cod_localidad', 'id_provincia', 'id_departamento', 'categoría', 'provincia', 'localidad', 'nombre', 'domicilio', 'código_postal', 'número_de_teléfono', 'mail', 'web'])

# Descartamos columnas
bibliotecas_df_2 = bibliotecas_df.drop(['Observacion', 'Subcategoria', 'Información adicional','Cod_tel','Departamento','Piso', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Tipo_gestion', 'año_inicio', 'Año_actualizacion'], axis=1)
museos_df_2 = museos_df.drop(['Observaciones', 'subcategoria', 'Info_adicional','piso','cod_area', 'Latitud', 'Longitud', 'TipoLatitudLongitud','jurisdiccion', 'año_inauguracion', 'actualizacion'], axis=1)
salas_de_cine_df_2 = salas_de_cine_df.drop(['Observaciones', 'Información adicional','Departamento','Piso', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'tipo_gestion', 'año_actualizacion'], axis=1)

#Renombramos nombres de las columnas
bibliotecas_df_2 = bibliotecas_df.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia', 'Localidad':'localidad', 'Nombre':'nombre', 'Domicilio':'domicilio', 'CP':'código_postal', 'Teléfono':'número_de_teléfono', 'Mail':'mail', 'Web':'web'})
museos_df_2 = museos_df.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'categoria':'categoría','fuente':'Fuente', 'Domicilio':'domicilio', 'CP':'código_postal', 'telefono':'número_de_teléfono', 'Mail':'mail', 'Web':'web'})
salas_de_cine_df_2 = salas_de_cine_df.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoría', 'Dirección':'domicilio', 'CP':'código_postal', 'Teléfono':'número_de_teléfono', 'Mail':'mail', 'Web':'web'})


#data = pd.concat([museos_data, salas_de_cine_df, bibliotecas_df] , join='inner', ignore_index=True)

tabla_principal = tabla_principal.append(bibliotecas_df_2)
tabla_principal = tabla_principal.append(museos_df_2)
tabla_principal = tabla_principal.append(salas_de_cine_df_2)

""" Procesar la información de cines para poder crear una tabla que contenga:
o Provincia
o Cantidad de pantallas
o Cantidad de butacas
o Cantidad de espacios INCAA"""

cine_principal = salas_de_cine_df[['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]
cine_principal['espacio_INCAA'] = cine_principal['espacio_INCAA'].replace('SI', 'si').replace('si', 1)
cine_principal['espacio_INCAA'] = cine_principal['espacio_INCAA'].fillna(0)
cine_principal['espacio_INCAA'] = cine_principal['espacio_INCAA'].astype("int")
cine_principal = cine_principal.groupby('Provincia').sum()

cine_principal

""" Ingresamos los datos de la fecha en los dataframe"""

museos_data = museos_df.rename(columns={'fuente':'Fuente', 'categoria':'Categoría', 'provincia':'Provincia', 'nombre':'Nombre'}) 
data = museos_data.append(salas_de_cine_df).append(bibliotecas_df)
#data = pd.concat([museos_data, salas_de_cine_df, bibliotecas_df] , join='inner', ignore_index=True)

data_nueva = data.drop(['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Observaciones', 'subcategoria', 'localidad', 'direccion', 'piso', 'CP', 'cod_area', 'telefono', 'Mail', 'Web', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'jurisdiccion', 'año_inauguracion', 'actualizacion', 'Departamento', 'Localidad', 'Dirección', 'Piso', 'Teléfono', 'Información adicional', 'tipo_gestion', 'Pantallas', 'Butacas', 'espacio_INCAA', 'año_actualizacion', 'Observacion', 'Subcategoria', 'Domicilio', 'Cod_tel', 'Tipo_gestion', 'año_inicio', 'Año_actualizacion'], axis=1)

df = data_nueva.pivot_table(values= 'Nombre', index=['Fuente','Categoría'], columns=['Provincia'], aggfunc='count', margins=True)

