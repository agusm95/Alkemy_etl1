import requests
import os

bibliotecas_id = '1udwn61l_FZsFsEuU8CMVkvU2SpwPW3Krt1OML3cYMYk'
bibliotecas = requests.get(f"https://docs.google.com/spreadsheets/d/{bibliotecas_id}/export?format=csv", allow_redirects= True)
os.makedirs('bibliotecas/2021-noviembre')
open('bibliotecas/2021-noviembre/bibliotecas-03-11-2021.csv', 'wb').write(bibliotecas.content)

museos_id = '1PS2_yAvNVEuSY0gI8Nky73TQMcx_G1i18lm--jOGfAA'
museos = requests.get(f"https://docs.google.com/spreadsheets/d/{museos_id}/export?format=csv", allow_redirects= True)
os.makedirs('museos/2021-noviembre')
open('museos/2021-noviembre/museos-03-11-2021.csv', 'wb').write(museos.content)


salas_de_cine_id = '1o8QeMOKWm4VeZ9VecgnL8BWaOlX5kdCDkXoAph37sQM'
salas_de_cine = requests.get(f"https://docs.google.com/spreadsheets/d/{salas_de_cine_id}/export?format=csv", allow_redirects= True)
os.makedirs('salas_de_cine/2021-noviembre')
open('salas_de_cine/2021-noviembre/salas_de_cine-03-11-2021.csv', 'wb').write(salas_de_cine.content)





