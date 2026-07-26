<h1 align="center">🎓 Mentor SI</h1>

<p align="center">
Plataforma gamificada para apoiar estudantes de Sistemas de Informação no aprendizado de programação, utilizando Python, SQLite e Inteligência Artificial.
</p>

<p align="center">
  <img src="assets/banner.png" width="100%">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![Git](https://img.shields.io/badge/Git-Version%20Control-red?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-success)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

## 📚 Sobre o projeto

O Mentor SI é uma plataforma gamificada desenvolvida em Python para auxiliar estudantes de Sistemas de Informação no aprendizado de programação.

O projeto combina conceitos de gamificação, persistência de dados com SQLite e Inteligência Artificial para incentivar o estudo contínuo e acompanhar a evolução do aluno.

Entre os principais recursos da plataforma estão:

- ⭐ Sistema de XP
- 🏆 Sistema de Conquistas
- 🔥 Sistema de Streak
- 📝 Quiz de Python
- 📊 Dashboard
- 📈 Estatísticas
- 📜 Histórico
- 🤖 Recomendações de estudo
- 💾 Persistência em SQLite

## ✨ Funcionalidades

- 👤 Cadastro de usuário
- ⭐ Sistema de XP
- 🔥 Sistema de Streak
- 🏆 Sistema de Conquistas
- 📝 Quiz de Python
- 📚 Plano de Estudos
- 📊 Dashboard
- 📈 Estatísticas
- 📜 Histórico
- 📉 Desempenho
- 🤖 Recomendações de estudo
- 💾 Persistência em SQLite

## 🛠 Tecnologias

- Python 3.13
- python-dotenv
- SQLite
- Google Gemini API
- Git
- GitHub
- Visual Studio Code

## 📂 Estrutura do Projeto

```text
Mentor-SI/

assets/
database/
models/
notebooks/
prompts/
services/
tests/
ui/
utils/

chatbot.py
config.py
README.md
```

## 📋 Requisitos

- Python 3.13 ou superior
- SQLite (já incluído no Python)
- VS Code (opcional)

## 🚀 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/ricardonogueiraneres/Mentor-SI.git
```

2. Entre na pasta do projeto:

```bash
cd Mentor-SI
```

3. Execute o programa:

```bash
python chatbot.py
```

4. Configure o arquivo `.env`

```env
GEMINI_API_KEY=sua_chave_aqui
```

Ao iniciar o sistema você poderá:

- cadastrar seu perfil;
- responder quizzes;
- ganhar XP;
- desbloquear conquistas;
- acompanhar seu desempenho;
- visualizar seu dashboard;
- criar planos de estudo.

## 🏛 Arquitetura

O Mentor SI foi desenvolvido utilizando uma arquitetura modular para facilitar manutenção, testes e evolução do sistema.

```text
Interface (CLI)
        │
        ▼
     Services
        │
        ▼
    Database
        │
        ▼
      SQLite
```

## 🚀 Roadmap

### ✅ Versão 7.x

- Arquitetura em camadas
- Dashboard Service
- Quiz Service
- Config centralizado
- Multiusuário
- SQLite
- README profissional

### 🔄 Próximas versões

- Interface gráfica
- Flashcards
- Dashboard Web
- API REST
- Aplicativo Mobile
- IA mais integrada
- Testes automatizados
- Sistema de desafios

## 🧠 Evolução da Arquitetura

Durante o desenvolvimento, o Mentor SI passou por diversas refatorações para melhorar a organização e a manutenção do código.

Principais melhorias:

- Separação em camadas (`services`, `database`, `ui`, `models`)
- Centralização das configurações em `config.py`
- Refatoração do Dashboard para `dashboard_service.py`
- Refatoração do Quiz para `quiz_service.py`
- Uso do Git com commits por sprint
- Estrutura preparada para crescimento futuro

## 🚀 Evolução do Projeto

O Mentor SI iniciou como um projeto simples em Python e evoluiu gradualmente para uma arquitetura modular.

Principais melhorias implementadas:

- ✔ Sistema Multiusuário
- ✔ SQLite
- ✔ Dashboard
- ✔ Sistema de XP
- ✔ Sistema de Conquistas
- ✔ Refatoração para Services
- ✔ Configurações centralizadas
- ✔ Versionamento com Git

## 📄 Licença

Este projeto está licenciado sob a licença MIT.

Foi desenvolvido para fins de estudo, prática e construção de portfólio.

## 👨‍💻 Autor

**Ricardo Adriano Nogueira Neres**

🎓 Estudante de Sistemas de Informação

💻 Desenvolvedor Python | Inteligência Artificial | Automação

📍 Brasília - DF

🔗 GitHub:
https://github.com/ricardonogueiraneres

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório.