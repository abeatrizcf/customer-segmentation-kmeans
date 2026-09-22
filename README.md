# Documentação referente a uma análise dos clientes do banco dvdrental utilizando clusterização e K-means

## Descrição do documento:

O documento em questão busca explicitar de forma clara o processo de uma análise complementar desenvolvida que realiza uma clusterização de clientes com o uso de Machine Learning através do algoritmo K-Means.

## Objetivo da análise complementar:

Será utilizado o algoritmo de aprendizado de máquina **K-means** para realizar uma clusterização dos grupos de clientes da locadora de filmes do banco analisado a fim de alcançar decisões estratégicas e fundamentadas por dados.

## Ferramentas utilizadas:

- Python e as bibliotecas Scikit-Learn e Pandas
- SQLAlchemy
- PostgreSQL e SQL

## Etapas da Análise:

#### Escolha das features

Para realizar o objetivo proposto as seguintes features foram escolhidas:

1. Total gasto
2. Quantidade de Aluguéis
3. Ticket Médio

E o identificador: `customer_id`

#### Conexão do banco de dados `dvdrental`

Como já temos o arquivo `conexao.py` já utilizado na questão 01, a conexão com o banco foi realizada de forma facilitada.

#### ETL

Em seguida, foi realizado a verificação do banco com relação a nulos e duplicatas nas tabelas *payment* e *rental*. Notou-se nessa etapa de ETL que a tabela *payment* apresenta uma incongruência de forma que apresenta o mesmo aluguel associado a mais de um `payment_id` e mais de um `customer_id`. Esse é o `rental_id = 4591` (aparece associado a 5 clientes e pagamentos). Entretanto, na tabela *rental* ele está associado somente ao cliente 182.

Como os outros 4 registros representam uma porcentagem muito pequena no nosso banco comparado com mais de 10.000 registros. Eles serão apenas eliminados utilizando `where r.customer_id = p.customer_id` na nossa consulta que originou o dataframe utilizado no K-means.

#### Normalização

Dando continuidade, com o `StandardScaler()` os dados foram normalizados.

#### Aplicação do K-means

Foram escolhidos 3 clusters para a realização da classificação e o K-means foi aplicado.

#### Interpretação dos Clusters

Como resultado dos clusters foram obtidos 3 grupos de clientes:

| cluster | total_gasto | qtd_alugueis | ticket_medio |
| --- | --- | --- | --- |
| 0 | 128.000383 | 29.626794 | 4.320787 |
| 1 | 95.837016 | 21.010471 | 4.569994 |
| 2 | 81.638844 | 22.045226 | 3.710134 |

| Cluster | Quantidade de clientes |
| --- | --- |
| 0 | 209 |
| 1 | 191 |
| 2 | 199 |

**Características de cada grupo de clientes**

- Grupo 0: Grupo com maior valor gasto e maior quantidade de aluguéis (excelentes clientes)
- Grupo 1: Clientes que alugam filmes mais caros porém com menor frequência do que todos os outros.
- Grupo 3: Clientes que alugam pouco e valores mais baixos.

## Conclusões e observações

- Notou-se que a soma da quantidade de clientes de cada Cluster está em consonância com a quantidade demonstrada no dashboard “Insights” da questão 2.
- Também observou-se que o grupo que mais aluga não é o grupo que apresenta maior ticket médio.
- **O grupo 0**, apesar de não apresentar o maior ticket_medio, é o que mais vale a pena investir em propagandas, por exemplo, a fim de atraí-los, já que alugam mais do que todos os outros e o ticket médio é muito pouco inferior ao **grupo 1**.

## Conhecimentos demonstrados a partir da análise

- Python
- Machine Learning e K-means
- ETL
- Interpretação de Clusters, BI e KPIs
