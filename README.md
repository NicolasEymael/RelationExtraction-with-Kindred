# RelationExtraction-with-Kindred

Projeto para extração de relações entre entidades utilizando a lib [Kindred](https://github.com/jakelever/kindred), portanto é necessário instalar com antecedência (seguir as instruções do link). 
As execuções foram realizadas utilizando cross-validation sobre o dataset da [DBpedia em português](https://github.com/davidsbatista/Annotated-Semantic-Relationships-Datasets).

### Pré-processamento do dataset

Inicialmente é necessário transformar o dataset em formato .txt para um formato compatível com o Kindred:
```
python process_dbpedia_dataset.py
```
Assim, será criada um diretório com todas as frases do dataset. Para cada frase são criados 3 arquivos: .txt, .a1 e .a2, com a frase original, as entidades e as relações, respectivamente.

### Abordagem naive

Na primeira execução do cross-validation, os folds foram divididos sequencialmente (o primeiro fold possui as frases de 0 a x, o segundo fold de x+1 a 2x, e assim por diante).
Para dividir o dataset em folds:
```
python organize_dbpediadata_folds.py
```
Com os folds formados, já é possível executar a extração das relações:
```
python train_and_predict_all_folds.py
```
Os resultados das predições e as métricas se encontram no diretório Dataset/.
Essa abordagem demorou cerca de 3h mas os resultados foram muito instáveis (alguns folds foram ótimos e outros foram péssimos).

### Abordagem shuffled (recomendado)

Para evitar essa instabilidade dos resultados, é recomendado executar o cross-validation com os folds embaralhados:
```
python train_and_predict_shuffled.py
```
As métricas de cada iteração se encontram no diretório Results/.
Essa abordagem demorou cerca de 9h mas os resultados foram mais estáveis, todas as métricas analisadas (precision/recall/f1score) ficaram em torno de 80~85%.
