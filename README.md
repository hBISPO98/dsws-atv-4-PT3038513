# Formulário ​P2 📑​
Esta aplicação consiste em uma evolução do formulário web interativo desenvolvido em Flask, utilizando a extensão Flask-WTF para validação de novos campos ampliados (como sobrenome, instituição e disciplinas via SelectField), o Flask-Bootstrap para estruturação visual responsiva, a arquitetura PRG (Post-Redirect-Get) com gerenciamento de sessões e cookies, além da integração do Flask-Moment e bibliotecas de data/hora para contagem dinâmica de tempo, rastreamento de IP remoto e host da aplicação, e uma nova rota dedicada para a interface de login.

<br>

## 🚀 Resumo das Adições (Versão 1 vs. Versão 2)
**-> Expansão do Formulário (NameForm):** Adição de novos campos de coleta de dados além do nome (surname para sobrenome, institution para instituição de ensino e discipline utilizando um campo de seleção SelectField com opções pré-definidas).

**-> Captura de Informações de Rede (request):** Inclusão do rastreamento do endereço IP remoto (request.remote_addr) e do host da aplicação (request.host).

**-> Manipulação de Tempo (datetime e Flask-Moment):** Adição de relógio dinâmico, exibição de data formatada e cálculo de tempo decorrido em tempo real (fromNow()).

**-> Nova Rota e Interface de Login:** Criação de uma rota dedicada (/login) no backend e de um novo template HTML correspondente (login.html).

**-> Atualização da Barra de Navegação (base.html):** Inclusão do link dinâmico para a página de Login e ativação dos scripts do Moment.js no layout base.

<br>

## ⚙️ O que foi necessário adicionar para cada funcionalidade funcionar?
1. Novos Campos e Seleção no Formulário (hello.py e index.html)\
O que foi necessário:

* Importar a classe `SelectField` do WTForms e atualizar a classe do formulário `NameForm` adicionando os campos de sobrenome, instituição e uma lista suspensa (choices) para as disciplinas. No template index.html, foram incluídas as tags de exibição para renderizar essas novas variáveis na tela de boas-vindas.

3. Captura de IP e Host (hello.py)


O que foi necessário:

* Importar o objeto `request` do Flask `from flask import request`. Dentro da função view da rota principal (/index), foram criadas as variáveis `ip_remoto = request.remote_addr e host_aplicacao = request.host`, permitindo extrair dados do cliente e da máquina servidor para repassá-los ao template HTML.

4. Exibição de Data, Hora e Contagem Dinâmica (hello.py e base.html)
O que foi necessário:

* Importar a biblioteca nativa do Python `from datetime import datetime`.

* Importar e inicializar a extensão `Moment (moment = Moment(app))` no arquivo `hello.py`

* No template base.html, foi adicionado o bloco de scripts `{{ moment.include_moment() }}` dentro da seção `{% block scripts %}`, garantindo que a biblioteca JavaScript responsável por atualizar o tempo decorrido `(fromNow(refresh=True))` funcione corretamente no navegador.

4. Criação da Rota e Interface de Login (hello.py e login.html)
O que foi necessário:

* Criar um novo arquivo HTML chamado `login.html` herdando a estrutura do base.html.

* Adicionar uma nova rota no arquivo principal `@app.route('/login', methods=['GET', 'POST'])` associada à função `login()`, que renderiza a nova página passando os parâmetros de data e hora atuais.

* Atualizar o menu de navegação no base.html incluindo o link `<li><a href="/login">Login</a></li>` para permitir o acesso do usuário à nova tela.

## 👩🏽‍💻 Demonstração
| Interface Inicial - Atualização de Instituição e Disciplina |
| :---: |
| <img src="https://github.com/user-attachments/assets/eade9e33-827b-4388-bc67-5113a15288ab" /> |



| Tela Inicial - Atualização de Nome e Sobrenome |
| :---: |
| <img src="https://github.com/user-attachments/assets/ec994f87-33c3-4c33-9b38-796a840bdc63" /> |



| Interface de Login - Autenticação |
| :---: |
| <img src="https://github.com/user-attachments/assets/510093ba-fc8d-439e-b969-ac5011b6f6e7" /> |
