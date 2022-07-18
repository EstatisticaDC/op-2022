import pandas as pd

minha_planilha = pd.read_excel('C:\ewila\Desktop\SASI OP 2022\BASE SASI OFICIAL.xlsx')
planilha_base = pd.read_excel('C:\ewila\Desktop\SASI OP 2022\dados_cartao_total_concatenado.xlsx')

novos_registros = planilha_base.loc[~planilha_base['id_sasi'].isin(minha_planilha['id_sasi'])].reset_index(drop=True)

minha_planilha = pd.concat([minha_planilha, novos_registros]).sort_values(by=['id_sasi'])
print('comecou a salvar')

#ordena por id
minha_planilha = minha_planilha.sort_values(by=['id_sasi'])
planilha_base = planilha_base.sort_values(by=['id_sasi'])

#atualiza status e contagem
minha_planilha.sort_values(by=['id_sasi'])['status_valecard']  = planilha_base.sort_values(by=['id_sasi'])['status_valecard']
minha_planilha.sort_values(by=['id_sasi'])['contagem_ativados']= planilha_base.sort_values(by=['id_sasi'])['contagem_ativados']

minha_planilha.sort_values(by=['id_sasi']).to_excel("C:\ewila\Desktop\SASI OP 2022\BASE SASI OFICIAL.xlsx" , index=False)

print("finalizado com sucesso :)")