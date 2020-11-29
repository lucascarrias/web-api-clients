# Web Api Clients Scripts

Scripts de demonstração de uso de APIs

----
### Requisitos
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
---
## Bacon Ipsum Client :bacon:
[Site](https://baconipsum.com/json-api/) |
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

[bacon_ipsum_client.py](https://github.com/LucasCarrias/web-api-clients/blob/master/bacon_ipsum_client.py)


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
---
## Detect Language Client :speech_balloon:
[Site](https://detectlanguage.com/) |
API para a detecção da língua de textos

Rotas | Método | Parametros | Autênticação :key:| Descrição
|:---:|:---:|:---:|:---:|---|
| "https://ws.detectlanguage.com/0.2/detect" | **POST** | :heavy_check_mark: | :heavy_check_mark:| Detecção de linguagem
| "https://ws.detectlanguage.com/0.2/languages" | **GET** | :x: | :x: | Lista das linguas disponíveis
| "https://ws.detectlanguage.com/0.2/user/status" | **GET** | :x: | :heavy_check_mark: | Informações sobre o usuário

##### Parametros aceitos
|Nome|Valores|Descrição|
|:---:|:---|---|
|**q**|\<seu+texto>|Palavras separadas por '**+**'|
|**q[]**|\<seu+texto>|Usado quando necessário passar multíplos textos. Palavras separadas por '**+**'|

#### Script
[detect_language_client.py](https://github.com/LucasCarrias/web-api-clients/blob/master/detect_language_client.py)

#### Métodos:
```python
 # Pegar informações do usuário
def user_status(self):
    ...

# Listar linguagens disponíveis
def language_list(self):
    ...

# Detecção de língua
def detect_language(self, *content):
    ...
```
#### Exemplo de uso
```python
dl_client = DetectLanguageClient()

dl_client.detect_language("Hello+world", "Olá+mundo")
```
---