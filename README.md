![Capa](./media/images/Carmen-Portinho.png)

# <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="25px;"/> Site para abrigo de animais
Projeto final realizado no Bootcamp Back-end Python e Django da [WomakersCode](https://womakerscode.org/) pela Squad Carmen Portinho.

## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px;"/> Índice <a name="retornar-ao-índice"></a>
- [Estrutura e Requisitos](#estruturas-e-requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Exemplos](#exemplos)
- [Integrantes](#integrantes)
- [Deploy](#deploy)



## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px;"/> Estruturas e Requisitos 

#### 1. Especificações Técnicas
- Ambiente de Desenvolvimento: Ambiente virtual Django local;
- Controle de Versão com Git;
- Design Responsivo;
- Banco de Dados;
- Modelos Django: Modelos Django que representem os animais, seus registros, históricos de adoção, além de informações sobre os voluntários.

#### 2. Funcionalidades do Abrigo
- Página Inicial: Exibir todos os animais disponíveis para adoção;
- Páginas de Detalhes: Visualização individual dos animais, incluindo informações como nome, espécie, idade, raça, histórico de saúde e imagens;
- Gestão de Adoções: Os interessados podem solicitar a adoção de um animal e os responsáveis pelo abrigo podem aprovar ou recusar as solicitações;
- Barra de Pesquisa: Barra de pesquisa que permita aos usuários procurar animais disponíveis para adoção.

[![Retornar ao índice](https://img.shields.io/badge/Retornar%20ao%20%C3%ADndice-Verde%20Escuro?color=%23006400&style=flat&labelColor=%23006400&logo=github)](#retornar-ao-índice)


## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px;"/> Instalação

Antes de começar, será necessário ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org/). 
Além disto é bom ter uma IDE, sugerimos o [VS Code](https://code.visualstudio.com/).

```bash
# Clonar o repositório
git clone https://github.com/Renatarafaelaalves/ProjetoFinalSquadCarmenPortinho

# Criar ambiente virtual
python -m venv myvenv

# Ativar ambiente virtual
.\myvenv\Scripts\activate

# Instalar as dependências
pip install -r requirements.txt

# Criar arquivo de banco de dados SQLite 
python manage.py migrate
```

[![Retornar ao índice](https://img.shields.io/badge/Retornar%20ao%20%C3%ADndice-Verde%20Escuro?color=%23006400&style=flat&labelColor=%23006400&logo=github)](#retornar-ao-índice)

## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px;"/> Como Usar

Sugestão para visualizar o banco de dados: Extensão `SQLite Viewer` do VSCode

``` bash
# Para criar um SuperUser e ter acesso ao /admin
python manage.py createsuperuser

# Rodar aplicação
python manage.py runserver
```


[![Retornar ao índice](https://img.shields.io/badge/Retornar%20ao%20%C3%ADndice-Verde%20Escuro?color=%23006400&style=flat&labelColor=%23006400&logo=github)](#retornar-ao-índice)

## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px;"/> Funcionalidades

#### 📌 Home
> Página inicial com alguns dados e links para a aplicação

![Página Inicial](./media/images/Pagina-Inicial.png)

#### 📌 Animais

> Listar animais disponíveis para adoção

![Animais](./media/images/Animais.png)

> Dentro dessa página é possível ver detalhes de cada animal clicando em cima das informações dele

![Ver animal](./media/images/Ver-animal.png)

> Busque seu amigo - Filtra os animais de acordo com a espécie

![Filtro](./media/images/filtro.png)

#### 📌 Adoção

> Para solicitar a adoção de animais disponíveis

![Adoção](./media/images/Adotar.png)


#### 📌 Voluntários

> Para se cadastrar como voluntário do abrigo

![Voluntários](./media/images/Voluntarios.png)


#### 📌 Conheça o projeto

> Redireciona para esse repositório

![Footer](./media/images/Footer.png)

#### 📌 Administrativo

> Área para acesso da parte administrativa, para cadastro de animais, de funcionários, de voluntários, bem como aprovação ou reprovação de adoção

![Administrativo](./media/images/Admin.png)


[![Retornar ao índice](https://img.shields.io/badge/Retornar%20ao%20%C3%ADndice-Verde%20Escuro?color=%23006400&style=flat&labelColor=%23006400&logo=github)](#retornar-ao-índice)

## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px;"/> Deploy

É possível acessar nossa aplicação através do link:
[Clique aqui](https://squadcarmenportinho.pythonanywhere.com/)

## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px;"/> Integrantes

<div style="align-itens:center">
<table>
    <td align="center">
        <a href="https://github.com/alynebrasil"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/37218646?v=4" width="100px;" alt="Imagem Alyne"/><br /><sub><b>Alyne Brasil</b></sub></a><br /><a href="https://github.com/alynebrasil">👩‍💻</a>
    </td>
    <td align="center">
        <a href="https://github.com/anamariagds"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/23744957?v=4" width="100px;" alt="Imagem Ana Maria"/><br /><sub><b>Ana Maria Gomes</b></sub></a><br /><a href="https://github.com/anamariagds">👩‍💻</a>
    </td>
    </td>
    <td align="center">
        <a href="https://github.com/danisoaresl"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/84364512?v=4" width="100px;" alt="Imagem Daniele"/><br /><sub><b>Daniele Soares</b></sub></a><br /><a href="https://github.com/danisoaresl">👩‍💻</a>
    </td>
    <td align="center">
        <a href="https://github.com/gabiapp"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/108434852?v=4" width="100px;" alt="Imagem Gessyca"/><br /><sub><b>Gabriela Nunez</b></sub></a><br /><a href="https://github.com/gabiapp">👩‍💻</a>
    </td>
    <td align="center">
        <a href="https://github.com/GessycaBorges"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/124705468?v=4" width="100px;" alt="Imagem Gessyca"/><br /><sub><b>Gessyca Borges</b></sub></a><br /><a href="https://github.com/GessycaBorges">👩‍💻</a>
    </td>
    <td align="center">
        <a href="https://github.com/OrcFofa"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/104779345?v=4" width="100px;" alt="Imagem Laura"/><br /><sub><b>Laura Santos</b></sub></a><br /><a href="https://github.com/OrcFofa">👩‍💻</a>
    </td>
    <td align="center">
        <a href="https://github.com/Renatarafaelaalves"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/141291179?v=4" width="100px;" alt="Imagem Renata"/><br /><sub><b>Renata Rafaela Alves</b></sub></a><br /><a href="https://github.com/Renatarafaelaalves">👩‍💻</a>
    </td>
</table>