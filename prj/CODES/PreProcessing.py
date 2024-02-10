# Importações necessárias
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score

# Importar a função prepare_data do script data_preparation
from data_preparation import prepare_data

# Modelos de Machine Learning
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier

# Definição da função para realizar busca em grade e avaliação
def perform_grid_search_and_evaluate(model, param_grid, X_train, y_train, X_test, y_test, model_name):
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    
    print(f"\n{model_name} - Melhores Parâmetros: ", grid_search.best_params_)
    print(f"{model_name} - Melhor score de validação cruzada (acurácia): ", grid_search.best_score_)
    
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    print(f"\n{model_name} - Avaliação no conjunto de teste:")
    print(classification_report(y_test, y_pred))
    print("Accuracy:", accuracy_score(y_test, y_pred))
    
    # Salvar o melhor modelo
    joblib.dump(best_model, f'{model_name}_best_model.joblib')

# Caminho para o arquivo de dados e especificações
file_path = 'caminho/para/spotify_dataset.csv'
target_column = 'Quadrante'
numeric_features = [
    'Acousticness', 'Danceability', 'Energy', 'Instrumentalness',
    'Key', 'Liveness', 'Loudness', 'Speechiness', 'Tempo', 'Valence',
    'Mode', 'Time Signature'
]

# Preparar os dados
X_train, X_test, y_train, y_test, preprocessor, label_encoder = prepare_data(
    file_path=file_path,
    target_column=target_column,
    numeric_features=numeric_features
)

# Configurações dos modelos e grades de hiperparâmetros (Exemplo simplificado)
models_param_grid = {
    "KNN": (KNeighborsClassifier(), {
        'n_neighbors': [5, 7],
        'weights': ['uniform'],
        'metric': ['euclidean']
    }),
    # Adicione configurações para outros modelos conforme necessário
}

# Realizar busca em grade e avaliar para cada modelo
for model_name, (model, param_grid) in models_param_grid.items():
    perform_grid_search_and_evaluate(model, param_grid, X_train, y_train, X_test, y_test, model_name)
