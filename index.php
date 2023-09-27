<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://code.jquery.com/jquery-1.9.1.js"></script>
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link rel="icon" href="View/icon.svg" type="image/svg+xml">
    <link rel="stylesheet" href="View/style.css">
    <script src="main.js"></script>
    <title>ChatBot</title>
</head>

<body>

    <div id="box">
        <h1>ChatBot</h1>
        <hr>
        <div id="chat">
            <div id="chat-area"></div>
            <p id="resposta">Olá! Eu sou o sistema MAAM. Por favor, digite sua pergunta ou 'Tchau' para encerrar a nossa conversa.</p>
            <br>
            <input type=" text" id="pergunta" placeholder="Digite sua pergunta...">
            <button id="perguntar" title="Enviar">
                <i class="ph ph-play"></i>
            </button>
        </div>
    </div>

</body>

</html>
