# Importar bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

# Carregar o dataset (caso o dataset já esteja em df, pule esta linha)
df = pd.read_csv('dataset_idade_faixa_etaria.csv')

# Verificar as classes únicas de 'Faixa_Etaria'
classes_faixa_etaria = df['Faixa_Etaria'].unique()
print(f'Classes em Faixa_Etaria: {classes_faixa_etaria}')

# Definir a feature (Idade) e o target (Faixa_Etaria)
X = df[['Idade']]  # Feature (variável de entrada)
y = df['Faixa_Etaria']  # Target (variável de saída)

# Dividir o dataset em conjunto de treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo KNN e ajustar (treinar) com os dados de treino
knn = KNeighborsClassifier(n_neighbors=3)  # Usar 3 vizinhos mais próximos
knn.fit(X_train, y_train)

# Listar as classes (rótulos) aprendidas pelo modelo
classes_aprendidas = knn.classes_
print(f'Classes aprendidas pelo modelo KNN: {classes_aprendidas}')

# Fazer previsões no conjunto de teste
y_pred = knn.predict(X_test)

# Avaliar a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo KNN: {accuracy * 100:.2f}%')

# Fazer uma previsão com uma nova idade (exemplo: idade = 25)
nova_idade = [[25]]
faixa_predita = knn.predict(nova_idade)
print(f'Faixa etária prevista para idade 25: {faixa_predita[0]}')

joblib.dump(knn, 'modelo_knn_faixa_etaria.pkl')

print("Modelo KNN salvo com sucesso!")
