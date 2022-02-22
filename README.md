# Batalha Naval Online

Jogo de Batalha Naval feito com python, que utiliza de sockets para implementar uma comunicação cliente-servidor e conta com uma interface gráfica.
<br></br>
## Como executar

### Requisitos

1. Biblioteca python chamada pygame, que pode ser instalada utilizado o pip:

```
pip install -U pygame --user
```

### Execução

1. Primeiro, é preciso executar o servidor e seu respectivo socket, que irá gerenciar as conexões dos clientes e fazer o jogo acontecer transmitindo informações pela rede.

```
cd src/server
python3 server.py
```

2. Em seguida, é necessário iniciar os clientes que serão os jogadores. Portanto, é necessário executar em duas abas diferentes do terminal o arquivo render que vai renderizar a interface gráfica do jogo e conectar o cliente.

```
cd src/client
python3 render.py
```

Ao clicar em start, o cliente fará a conexão com o servidor, o jogo inicia quando dois clientes estiverem conectados. Para mais informações de como jogar, leia o arquivo Relatório.pdf
