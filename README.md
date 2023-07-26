# Predição da temperatura média horária da cidade de São João del-Rei

Geração de modelo preditivo utilizando predição recursiva em séries temporais (recursive forecasting), atingindo um erro absoluto médio (MAE) de 1.04 e um valor de 1.36 na raiz do erro quadrático médio (RMSE).

O modelo desenvolvido consegue predizer temperaturas com um erro de cerca de ±1.04°C e sem muitos erros atípicos (outliers), o que pode ser observado pela proximidade dos erros MAE e RMSE. 


## Dados

Os dados utilizados nesse projeto foram obtidos através do site do Instituto Nacional de Metereologia ([INMET](https://portal.inmet.gov.br/)) e representam as medições da temperatura média horária para a cidade de SJDR.

O conjunto de treino conta com 10 anos de medições, no intervalo entre 01 de janeiro de 2013 e 31 de dezembro de 2022; e o conjunto de dados utilizados para teste apresenta as medições dos 10 primeiros dias de 2023, de 01 de janeiro de 2023 a 10 de janeiro de 2023.

### Análise Exploratória

As análises exploratórias dos dados indicam que a cidade possui uma temperatura amena, que frequentemente se encontra entre 16°C e 24°C, possuindo média (e moda) de ±19.8°C, mas que pode chegar a menos de 5°C ou mais de 35°C nos dias de frio ou calor mais extremos, respectivamente.

Um ponto muito importante para o trabalho foi a observação e correção dos 4.38% de dados faltantes na base de testes.

Esses dados foram corrigidos utilizando um método de imputação iterativa e, a partir das imagens abaixo, é possível observar que a imputação desses dados faltantes não alterou a característica dos dados.

Uma outra observação que pode ser realizada pelas imagens, tanto pela média horária quanto pela média mensal, é de que as estações do ano na cidade são muito bem definidas.

![](/img/media_horaria.png)
![](/img/media_mensal.png)


## Modelo desenvolvido

O modelo gerado foi desenvolvido utilizando a [Skforecast](https://skforecast.org/0.9.1/index.html), uma biblioteca que utiliza a API do [scikit-learn](https://scikit-learn.org/stable/) e realiza predições em séries temporais.

Os erros obtidos pelo modelo fora de 1.04 pontos para o MAE e 1.36 pontos para o RMSE.

Nesse caso, como os valores dos dados representam a temperatura em graus Celsius(°C), o erro absoluto médio (MAE) representa, diretamente, a média do erro das previsões em °C.

Como os valores dos erros MAE e RMSE estão próximos, isso indica que são poucas as previsões realizadas nas quais o erro é alto (outliers).

Na próxima imagem são exibidas as predições do modelo quando aplicado ao conjunto de dados de testes.

Em conclusão, o modelo consegue predizer a temperatura média horária para a cidade de SJDR com um erro de cerca de ±1.04°C e sem muitos erros atípicos.

![](/img/forecast.png)
