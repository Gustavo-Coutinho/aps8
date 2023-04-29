# Hotel Environment Management System

Este trabalho semestral tem como objetivo desenvolver uma aplicação baseada em Web Services para a gestão ambiental de um hotel, minimizando o desperdício de água e energia nos quartos e implementando melhorias de procedimentos alinhadas à ISO 14.000.

## Serviços Implementados

A aplicação consiste em um sistema que integra os seguintes serviços:

1. **Serviço de Monitoramento de Presença**: Detecta a presença de hóspedes e funcionários no quarto e envia essas informações para o sistema central.
2. **Serviço de Controle de Termostato**: Ajusta a temperatura do ar condicionado ou aquecedor do quarto de acordo com a presença e preferências dos hóspedes.
3. **Serviço de Controle de Chuveiro Inteligente**: Regula o fluxo e a temperatura da água do chuveiro de acordo com a presença e preferências dos hóspedes, e monitora o consumo de água.
4. **Serviço de Controle de Tomadas Programáveis**: Liga ou desliga as tomadas elétricas do quarto de acordo com a presença e preferências dos hóspedes.

## Tecnologias Utilizadas

- Linguagem de programação: Python
- Web framework: Flask
- Formatos de dados: JSON

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

hotel_environment_management/
    app.py
    webservices/
    init.py
    routes.py
    presence_monitor.py
    thermostat_control.py
    smart_shower_control.py
    programmable_outlet_control.py


## Como Executar

1. Instale as dependências do projeto:

pip install -r requirements.txt


2. Execute o arquivo `app.py`:

python app.py

O servidor Flask será iniciado em `http://localhost:5000/`.

## Testes

Foram realizados testes unitários, de integração e de aceitação para garantir que os serviços implementados atendam aos requisitos especificados. Utilizamos ferramentas como Postman e SoapUI para testar os serviços.

## Documentação

A documentação do projeto detalha os objetivos, motivações, decisões tomadas e os resultados obtidos em cada etapa do trabalho. A documentação também explica o funcionamento da aplicação e como ela contribui para a gestão ambiental da organização escolhida.

## Contribuidores
