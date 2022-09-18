import pandas as pd
df = pd.read_csv("pratica/pokemon_data.csv") # lê o arquivo que nesse caso está no formato csv

print(df.head(3)) # filtra para que mostre apenas as linhas começando de cima

print(df.columns) # Mostra apenas os identificadores das colunas

print(df['Name']) # printa uma coluna inteira com base no identificador

print(df['Name'][0:5]) # você pode escolher de qual linha até qual linha será printada com o [] logo apos o identificador

print(df[['Name', 'Type 1', 'Type 2', 'HP']] [0:5]) # Você pode selecionar diversas colunas colocando uma lista dentro de outra lista
                                                    # e dá pra usar o limitador de linhas também
print(df.iloc[1]) # Seleciona qual LINHA será printada, vai mostrar todos os valores que estão naquela linha
                       # Também é possível usar o limitador mas não demonstrei aqui. Caso queira limitar 
                       # é só fazer como nos dois exemplos acima

print(df.iloc[2,3]) # Aqui é possível selecionar a linha E a coluna que você deseja, é bem util, lembrando que o primeiro valor é a 
                    # linha e o segundo é a coluna

#for index, row in df.iterrows(): # É possível usar esse loop de diversas formas, dá pra printar o index e a coluna de sua escolha, como
    #print(index, row['Name'])    # Como no exemplo eu printei a coluna "Name" mas da pra printar todas as outras colunas


print(df.loc[df['Type 1'] == 'Poison']) # Filtra as linhas para um determinado valor de uma coluna
print(df.loc[df['Type 1'] == "Poison"][df['Type 2'] == "Fighting"]) # Dá pra filtrar mais ainda com outras tabelas
df.describe() # Mostra em nível detalhado as informações sobre seus dados (min, max, std, etc...)





