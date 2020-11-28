# Web Api Clients Scripts

Scripts de demonstração de uso de APIs

----
### Instalação
Você precisa do Python 3.8 :snake: ou superior instalado para executar os scripts

### Dependências
Para instalação das depedências você precisa executar o seguinte comando:
```
pipenv install
```
Para ativação do ambiente virtual:
```
pipenv shell
```

## Bacon Ipsum Client :bacon:
[Site](https://baconipsum.com/json-api/)
API para a geração de texto *Lorem Ipsum* usando palavras relacionadas ao Bacon

Rota | Método | Parametros | Autênticação :key:
|:---:|:---:|:---:|:---:|
| "https://baconipsum.com/api/" | **GET** | :heavy_check_mark: (Obrigatório) | :x:

##### Parametros aceitos
|Nome|Valores|Descrição|
|:---:|:---|---|
|**type**|all-meat, meat-and-filler|Tipos de carnes que aparecem no texto|
|**paras**| \<valor> | Quantidade de paragrafos gerados. Padrão é 5.|
|**sentences**| \<valor> | Quantidade de sentenças. Sobrescreve o 'paras'|
|**start-with-lorem**|1|O texto gerado começa com Lorem|
|**format**| json(padrão), html, text | Formato do texto gerado. 'text' e 'html' não são aceitos pelo script.
#### Script
```
bacon_ipsum_client.py
```

#### Método:
```python
 # Gerar resposta de acordo com os parametros passados
def get_bacon(self, params={'type': 'all-meat'}):
    ...
```
#### Exemplo de uso
```python
bacon_client = BaconIpsumClient()

bacon_client.get_bacon()
```
