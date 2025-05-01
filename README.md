# Furichat-Bot 🇧🇷🎮

Um chatbot do Telegram para manter você atualizado sobre tudo da FÚRIA! 🔥

## Funcionalidades

* `/help` ou `/start`: Exibe as instruções e comandos disponíveis.
* `/next_game`: Informa sobre os próximos jogos da FÚRIA.
* `/score`: Mostra os placares ao vivo dos jogos atuais da FÚRIA.
* `/line`: Lista os jogadores da line principal da FÚRIA.

## Pré-requisitos

Antes de começar, você precisará ter:

* **Python 3.6 ou superior** instalado no seu sistema. Você pode verificar sua versão do Python executando `python --version` ou `python3 --version` no terminal.
* **Pip** (Python package installer) instalado. Geralmente vem com a instalação do Python.
* **Conta no Telegram** para interagir com o bot.
* **Token do Bot do Telegram:** Você precisa criar um bot no Telegram através do BotFather e obter o token de acesso.
* **Token da API PandaScore:** Você precisa obter um token de acesso da API PandaScore para acessar os dados de partidas e times.

## Configuração

1.  **Clone o repositório:**

    ```bash
    git clone [https://docs.github.com/articles/referencing-and-citing-content](https://docs.github.com/articles/referencing-and-citing-content)
    cd furichat-bot
    ```

2.  **Crie o arquivo `.env`:**

    Na raiz do projeto, crie um arquivo chamado `.env` e adicione suas credenciais da seguinte forma:

    ```dotenv
    TELEGRAM_TOKEN=SEU_TOKEN_DO_TELEGRAM
    PANDASCORE_TOKEN=SEU_TOKEN_DA_PANDASCORE
    WEBHOOK_URL=https://furichat-bot.onrender.com
    ```
    o WEBHOOK_URL é também o link do servidor online

    Substitua `SEU_TOKEN_DO_TELEGRAM` pelo token que você obteve do BotFather e `SEU_TOKEN_DA_PANDASCORE` pelo token da API PandaScore.

3.  **Instale as dependências:**

    Certifique-se de ter um arquivo `requirements.txt` na raiz do seu projeto listando as dependências. Se não tiver, crie um com o seguinte conteúdo:

    ```
    telebot
    python-dotenv
    requests
    flask
    ```

    Em seguida, execute o seguinte comando no terminal para instalar as bibliotecas necessárias:

    ```bash
    pip install -r requirements.txt
    ```
    ou
    ```bash
    python3 -m pip install -r requirements.txt
    ```

## Como Rodar o Projeto Localmente

Para executar o chatbot no seu computador:

1.  **Navegue até o diretório do projeto** no seu terminal (se você ainda não estiver lá):

    ```bash
    cd furichat-bot
    ```

2.  **Execute o script principal:**

    ```bash
    python main.py
    ```
    ou
    ```bash
    python3 main.py
    ```

    O bot começará a rodar e ficará aguardando por interações no Telegram. Você pode então procurar pelo seu bot no Telegram e começar a usar os comandos.

## Autor

Lucas Gonçalves Venancio
