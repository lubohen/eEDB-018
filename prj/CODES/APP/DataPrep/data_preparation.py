import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import joblib

def prepare_data(file_path, target_column, numeric_features, test_size=0.2, random_state=42, scaler_path='preprocessor.joblib', label_encoder_path='label_encoder.joblib'):
    """
    Carrega e prepara os dados para modelagem.

    Args:
        file_path (str): Caminho para o arquivo CSV dos dados.
        target_column (str): Nome da coluna alvo.
        numeric_features (list of str): Lista de nomes das colunas numéricas.
        test_size (float, optional): Proporção do conjunto de teste. Padrão é 0.2.
        random_state (int, optional): Semente para a geração de números aleatórios. Padrão é 42.
        scaler_path (str, optional): Caminho para salvar o objeto de pré-processamento. Padrão é 'preprocessor.joblib'.
        label_encoder_path (str, optional): Caminho para salvar o codificador de rótulos. Padrão é 'label_encoder.joblib'.

    Returns:
        tuple: Tupla contendo os conjuntos de dados processados (X_train, X_test, y_train, y_test), além do pré-processador e o codificador de rótulos.
    """
    # Carregar dados
    df = pd.read_csv(file_path)

    # Separar em features e target
    X = df[numeric_features]
    y = df[target_column]

    # Codificar a variável alvo categórica
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # Dividir os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=test_size, random_state=random_state)

    # Construir o pré-processador para features numéricas
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),  # Preencher valores ausentes
        ('scaler', StandardScaler())                   # Normalizar dados numéricos
    ])

    # Aplicar transformações nas colunas numéricas
    preprocessor = ColumnTransformer(transformers=[
        ('num', numeric_transformer, numeric_features)
    ])

    # Pré-processar os dados de treinamento e teste
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    # Salvar o pré-processador e o label encoder
    joblib.dump(preprocessor, scaler_path)
    joblib.dump(label_encoder, label_encoder_path)

    return X_train_processed, X_test_processed, y_train, y_test, preprocessor, label_encoder

# Exemplo de uso
if __name__ == "__main__":
    file_path = 'spotify_dataset.csv'
    target_column = 'Quadrante'
    numeric_features = [
    'Acousticness', 'Danceability', 'Energy', 'Instrumentalness', 
    'Key', 'Liveness', 'Loudness', 'Speechiness', 'Tempo', 'Valence', 
    'Mode', 'Time Signature'
]

    scaler_path = 'preprocessor.joblib'
    label_encoder_path = 'label_encoder.joblib'

    # Preparar os dados
    X_train, X_test, y_train, y_test, preprocessor, label_encoder = prepare_data(
        file_path=file_path,
        target_column=target_column,
        numeric_features=numeric_features,
        scaler_path=scaler_path,
        label_encoder_path=label_encoder_path
    )

    # Agora, X_train, X_test, y_train, e y_test estão prontos para serem usados em qualquer modelo de ML.