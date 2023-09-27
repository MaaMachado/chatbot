<?php
$api_url = 'http://localhost:5000/chatbot'; // Substitua pela URL da sua API Python

$pergunta = $_POST["pergunta"];

$data = json_encode(['question' => $pergunta]);

$ch = curl_init(($api_url));
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json', 'Content-Length: ' . strlen($data)]);

$response = curl_exec($ch);
curl_close($ch);

$resultado = json_decode($response, true);
$chatbot_resposta = $resultado['response'];

echo json_encode($chatbot_resposta);

?>