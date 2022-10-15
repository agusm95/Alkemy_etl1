from venv import create
from sqlalchemy import create_engine
from procesamiento import tabla_principal, cine_principal, df

engine = create_engine('postgresql://postgres:12345@localhost:5432/alkemy')

tabla_principal.to_sql('tabla_principal', con=engine, if_exists='replace')
cine_principal.to_sql('cine_cantidades', con=engine, if_exists='replace')
df.to_sql('categorias_fuente', con=engine, if_exists='replace')