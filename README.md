# 🤖 ChatBot
Atividade Final de Python - Construir um ChatBot para atendimento ao cliente

## 👨🏽‍💻**Introdução:**

`Bem-vindo à documentação do sistema de chatbot, criado em Python com adições de JavaScript, HTML, CSS e PHP,
desenvolvido por Maria Machado como parte da atividade final da UC15 (Implementação de Inteligência Artificial) do curso Técnico em Desenvolvimento de Sistemas - Senac 22/23.
Nesta documentação, apresentarei uma visão geral, tecnologias utilizadas, cada etapa para acessar este projeto, seus objetivos e seu funcionamento final.` <br>
               
---

## ✨ Visão Geral:

O sistema "ChatBot" foi criado para demonstrar e testar conhecimentos em Python, servindo como uma introdução à construção de chatbots.
Ele utiliza processamento de linguagem natural para responder a perguntas e puxar reações do chatbot com base nas palavras-chave identificadas nas perguntas dos usuários.

---

## 🎯 Tecnologias utilizadas:

- Python
  - Flask
  - NLTK
- PHP
- HTML
- JavaScript

---

## 💻 Como Acessar o Projeto:

Para acessar e utilizar o ChatBot, siga as instruções abaixo:

- Certifique-se de ter o XAMPP instalado e o Apache iniciado em seu computador;
  
- Clone este projeto em uma pasta dentro do diretório "htdocs" do XAMPP;

  ```
   git clone https://github.com/MaaMachado/chatbot.git
   ```

- Abra o projeto no Visual Studio Code;
  
- Descomente o seguinte comando para fazer o download de um recurso específico necessário para o sistema funcionar:

  ```
   nltk.download('punkt')
   ```
  
- Abra um terminal no VSCode e instale as bibliotecas necessárias com os seguintes comandos:

  ```
   pip install flask
   ```
  ```
   pip install nltk
   ```
  
- Execute o seguinte comando para iniciar o sistema:

   ```
   python chatbot.py
   ```

- Depois de seguir todas essas etapas, acesse o 'index.php' do projeto em seu navegador:

  ```
   http://localhost/chatbot/index.php
   ```
  
- Agora você pode prosseguir no sistema e testar as respostas do chatbot com perguntas como 'Olá', 'Tudo bem?', 'Qual é o seu nome?', 'Qual é a sua função?', 'Tchau' ou outras variantes de perguntas.

---

## 🏆 Objetivos:

- Demonstrar conhecimentos em Python e processamento de linguagem natural.
- Servir como uma introdução à construção de chatbots e à integração de respostas com base em palavras-chave.
- Fornecer uma experiência de aprendizado prática em processamento de texto e interação com o usuário.
- Mostrar como criar uma interface web simples para interagir com um chatbot.
- Oferecer a oportunidade de expandir o chatbot com respostas personalizadas e funcionalidades adicionais.
- Facilitar o acesso e o teste do chatbot no ambiente local, utilizando o XAMPP e o servidor Apache.

---

## 🖥 Funcionamento do Sitema:


Quando um usuário digita uma pergunta no campus disponibilizaddo e clica no botão "Enviar", a pergunta é processada pelo chatbot.
Com base nas palavras-chave identificadas, o chatbot seleciona uma resposta adequada a partir de um conjunto predefinido de respostas.

---
