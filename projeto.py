import streamlit as st
import pandas as pd
from PIL import Image

def function():
        
    st.set_page_config(layout='wide')

    st.title('Dashboard do Projeto - Black Friday Sales')
    st.write('')
    st.write('''O objetivo do projeto é entender o comportamento (valor) de compra do cliente em relação a vários produtos de diversas categorias.
                O conjunto de dados contém diversas características, tanto dos clientes quanto dos produtos, que influenciam no valor das compras.''')
    st.write('')
    st.write('Com isso, pretende-se mensurar o valor da compra de um cliente com base em um determinado conjunto de características.')
    st.write('')

    with st.expander("Ver dataset original"):
        st.subheader('Dataset original')
        data = pd.read_csv('black_friday_sales.csv')
        df = pd.DataFrame(data)
        st.write(df)

        st.subheader('Entendendo as variáveis:')
        st.markdown('''
                        - ***User_ID:*** identificação do cliente
                        - ***Product_ID:*** identificação do produto
                        - ***Gender:*** sexo do cliente (F/M)
                        - ***Age:*** faixa etária do cliente
                        - ***Occupation:*** ocupação do cliente
                        - ***City_Category:*** categoria da cidade do cliente (A, B, C)
                        - ***Stay_In_Current_City_Years:*** tempo, em anos, de permanência do cliente na cidade atual
                        - ***Marital_Status:*** estado civil do cliente (0 - solteiro, 1 - casado)
                        - ***Product_Category_1:*** categoria principal do produto
                        - ***Product_Category_2:*** categoria secundária do produto
                        - ***Product_Category_3:*** categoria terciária do produto
                        - ***Purchase:*** valor da compra (variável alvo)
                    ''')

    with st.expander("Ver análise exploratória"):
        st.header('Análise Exploratória dos dados', divider='grey')
        st.write('')
        st.write('''Iniciamos o projeto tratando os dados ausentes:''')
        st.write('')
            
        col1, col2 = st.columns(2)
        
        with col1:
            img = Image.open('ausentes.png')
            st.image(img, caption='Visualizando os dados ausentes')
        
        with col2:
            img = Image.open('ausentes2.png')
            st.image(img, caption='Verificando se os dados ausentes foram deletados')
            
        st.write('')
        st.write('O gráfico à direita, em branco, mostra que todos os valores nulos foram eliminados do dataset.')
        st.write('Em seguida, foi feita a análise da variável alvo:')

        st.subheader('Gráfico de Distribuição da variável alvo - Purchase')
        img = Image.open('distribuicao_purchase.png')
        st.image(img, caption='Distribuição de Purchase')
        st.write('A média maior que a mediana indica uma assimetria à direita na curva representativa dos dados.')
        st.write('')
            
        st.subheader('Boxplot da variável alvo - Purchase')
        img = Image.open('boxplot_purchase.png')
        st.image(img, caption='Boxplot de Purchase')

        st.subheader('Estatísticas Descritivas de Purchase')
        img = Image.open('descr_purchase.png')
        st.image(img, caption='Descrição de Purchase')
    
        st.write('')
        st.write('Os gráficos refletem que os dados seguem uma distribuição quase normal. Também podem ser observados alguns outliers em valores acima de, aproximadamente, 20.000, como representado no boxplot, justificando a assimetria da curva representativa dos dados.')
        st.write('O desvio padrão relativamente alto em relação à média sugere que os valores são dispersos, e a presença de outliers pode ser uma razão para essa dispersão. Os quartis também ajudam a entender como os valores estão distribuídos ao longo do intervalo de dados:')
        st.markdown('''
                        - 25% das compras tem um valor igual ou inferior a $ 5.823,00;
                        - 50% das compras tem um valor igual ou inferior a $ 8.047,00;
                        - 75% das compras tem um valor igual ou inferior a $ 12.054,00
                    ''')
        st.write('A diferença entre o terceiro e o primeiro quartil (IQR) é de aproximadamente 6,231, um IQR relativamente grande também sugere uma dispersão considerável nos dados. A grande diferença entre o terceiro quartil (75%) e o valor máximo (max) reforça a existência de outliers no lado superior da distribuição, indicando observações com valores muito acima da média.')
        st.write('')
            
        st.subheader('Analisando outliers das variáveis numéricas')
        st.write('')
        img = Image.open('outliers.png')
        st.image(img, caption='Outliers')
        st.write('''
                    Verificamos a existência de outliers nas colunas Product_Category_1 e Purchase, mas como a porcentagem de outliers 
                    é baixa, então, como temos uma quantidade razoável de dados, optamos por deletar esses registros para que os mesmos não influenciem no estudo.
                ''')
        st.write('')
            
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        col5, col6 = st.columns(2)
        col7, col8 = st.columns(2)
        
        with col1:
                st.subheader('Gender x Purchase')
                img = Image.open('gender_purchase.png')
                st.image(img, caption='Gender x Purchase')
                st.write('Em média, homens gastam mais que mulheres.')

        with col2:
                st.subheader('Age x Purchase')
                img = Image.open('age_purchase.png')
                st.image(img, caption='Age x Purchase')
                st.write('''Os maiores consumidores são homens na faixa etária de 26 a 35 anos.
                            Os menores de idade são quem menos consome.''')

        with col3:
                st.subheader('Occupation x Purchase')
                img = Image.open('occ_purchase.png')
                st.image(img, caption='Occupation x Purchase')
                st.write('O total gasto em compras varia bastante em relação à profissão do cliente.')

        with col4:
                st.subheader('City_Category x Purchase')
                img = Image.open('city_purchase.png')
                st.image(img, caption='City_Category x Purchase')
                st.write('''Clientes de cidades da categoria B são os que mais consomem.
                            Isso pode ser influenciado por diversos fatores, como: tamanho da população, nível de renda, demografia, acesso a lojas, necessidades e preferências do consumidor, entre outros.''')

        with col5:
                st.subheader('Stay_In_Current_City_Years x Purchase')
                img = Image.open('years_purchase.png')
                st.image(img, caption='Years in city x Purchase')
                st.write('''Pessoas que vivem há mais de um ano na cidade compram e gastam menos.
                            O maior consumo é de pessoas entre 1 e 2 anos na cidade.''')

        with col6:
                st.subheader('Marital_Status x Purchase')
                img = Image.open('ms_purchase.png')
                st.image(img, caption='Marital Status x Purchase')
                st.write('Solteiros consomem mais do que os casados.')

        with col7:
                st.subheader('Product_Category_1 x Purchase')
                img = Image.open('categories_purchase_1.png')
                st.image(img, caption='Category_1 x Purchase')
                st.write('Os produtos com mais vendas são os produtos que tem a categoria 5 como categoria principal.')

        with col8:
                st.subheader('Product_Category_1 x Purchase')
                img = Image.open('categories_purchase_2.png')
                st.image(img, caption='Category_1 x Purchase')
                st.write('Já os produtos da Categoria 10 promovem compras com o maior valor médio total.')

    with st.expander('Ver pré-processamento dos dados'):
        st.header('Pré-processamento dos dados', divider='grey')
        st.write('')
        st.write('''Na fase de pré-processamento, foram removidas do dataframe as colunas User_ID e Product_ID, por serem variáveis apenas com fins de identificação do cliente e do produto.
                    Também foi removida a coluna Occupation. 
                    Foi realizada a codificação das variáveis Gender, Age, City_Category, Stay_In_Current_City_Years e Product_Category_1, pois são variáveis que possuem dados categóricos e devem ser transformados em valores numéricos antes de serem usadas em um modelo de regressão linear.
                ''')
        st.write('O resultado final foi o dataframe abaixo:')
        st.write('')
        new_data = pd.read_csv('encoded_df.csv')
        new_df = pd.DataFrame(new_data)
        st.write(new_df)
        
    with st.expander('Ver resultados do modelo'):
        st.header('Regressão Linear - Resultados', divider='grey')
        st.write('')
        st.write('Após a aplicação do modelo de Regressão Linear, estes foram alguns dos resultados:')
        st.write('')
            
        col1, col2 = st.columns(2)
        
        with col1:
            img = Image.open('regressao.png')
            st.image(img, caption='Valores Reais x Previsões do modelo')
        
        with col2:
            img = Image.open('regplot.png')
            st.image(img, caption='Resultados do modelo')

    with st.expander('Ver métricas do modelo'):
        st.header('Regressão Linear - Métricas de Avaliação', divider='grey')
        st.write('')
        st.write('Após a aplicação do modelo de Regressão Linear, foram calculadas as seguintes métricas de avaliação:')
        st.write('')
        metrics_data = pd.read_csv('metrics.csv')
        metrics_df = pd.DataFrame(metrics_data)
        st.write(metrics_df)
        st.write('''
                    Considerando essas métricas, um modelo ideal teria valores de MSE, RMSE e MAE próximos de zero, o que indicaria que as previsões do modelo são muito próximas dos valores reais.
                    Porém, os resultados obtidos e as métricas calculadas sugerem que o modelo de regressão linear possui um desempenho razoável, porém com um erro considerável nas previsões em relação aos valores reais.
                    Assim, chegamos à conclusão de que a regressão modelar pode não ser o melhor modelo a ser aplicado ao conjuntos de dados em questão para prever o valor da compra.
                    É importante aplicar outros modelos mais complexos que consigam prever valores mais próximos dos reais e que atinjam métricas mais satisfatórias.
                ''')

if __name__ == "__main__":
        function()
