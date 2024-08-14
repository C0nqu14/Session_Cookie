# Flask Cookie Session Example

Este é um exemplo simples de uma aplicação web usando Flask que demonstra o uso e configuração de cookies, incluindo a configuração da flags `HttpOnly` , `secure` , `samesite` para segurança adicional. A aplicação possui funcionalidades básicas de login, logout e visualização de cookies.

## Funcionalidades

- **Login**: Permite que os usuários se autentiquem e armazena o nome de usuário na sessão e em um cookie.
- **Logout**: Remove o nome de usuário da sessão e exclui o cookie associado.
- **Visualização de Cookies**: Roteiras para verificar e exibir o valor dos cookies.

## Tecnologias Usadas

- Flask: Framework web para Python.
- `itsdangerous`: Biblioteca para criptografia de dados em cookies (opcional, para segurança adicional).

## Instalação

Siga estas etapas para configurar e executar o projeto localmente:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

```
```
2. **Instale as dependências**:
```bash
pip install -r requirements.txt

```
A aplicação estará disponível em http://127.0.0.1:4444

## Rotas

- /: Página inicial. Exibe uma mensagem de boas-vindas e o nome de usuário se estiver autenticado.
- /login: Formulário de login. Envia o nome de usuário e o armazena em uma sessão e cookie.
- /logout: Faz logout do usuário, removendo o nome de usuário da sessão e excluindo o cookie.
- /setcookie: Verifica se o cookie está definido e retorna uma mensagem apropriada.
- /getcookie: Exibe o valor do cookie cookieset.

## Segurança

- Cookies: O cookie cookieset é configurado com a flag HttpOnly para evitar acesso via JavaScript. A flag secure é utilizada para garantir que o cookie seja transmitido apenas sobre HTTPS. A flag SameSite='Lax' é configurada para proteção contra CSRF (Cross-Site Request Forgery).

## Requisitos

- Python 3.x
- Flask
- itsdangerous (opcional, para criptografia de cookies)

## Arquivos

- app.py: Código principal da aplicação Flask.
- templates/: Diretório contendo os arquivos HTML para renderização.
- static/: Diretório para arquivos estáticos como CSS e JavaScript.

## Contribuições

Sinta-se à vontade para contribuir para este projeto. Se você encontrar problemas ou quiser adicionar novas funcionalidades, abra uma issue ou um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

## Contato

Se você tiver alguma dúvida ou sugestão, entre em contato com www.linkedin.com/in/joão-conquia-6a7507239

### Instruções para Uso

1. **Clone o Repositório**: Substitua a URL no comando `git clone` pelo link do seu repositório no GitHub.
2. **Ambiente Virtual**: Assegure-se de que o Python esteja instalado e que o ambiente virtual seja ativado corretamente.
3. **Dependências**: `requirements.txt` deve listar todas as bibliotecas necessárias, como Flask e `itsdangerous`. Se ainda não tiver esse arquivo, você pode criá-lo com o comando `pip freeze > requirements.txt` após instalar as dependências.

Adapte qualquer seção conforme necessário para refletir a configuração e detalhes específicos do seu projeto.
