# AgroSat - Visão Computacional para Monitoramento de Lavouras

## Integrantes

* Fernanda Rocha Menon – RM554673
* Luiza Macena Dantas – RM556237
* Luan Ramos Garcia de Souza – RM558537
* Matheus Ricciotti – RM556930
* Matheus Bortolotto – RM555189
* Monica Paula Rocha – RM (adicionar RM)

---

## Descrição da Solução

O **AgroSat** é uma solução de Visão Computacional desenvolvida em Python para apoiar o monitoramento de lavouras e a identificação de possíveis sinais de pragas, doenças ou estresse na plantação.

Dentro do contexto da Global Solution, o projeto simula uma ferramenta que poderia ser utilizada por produtores rurais para analisar imagens capturadas por webcam, vídeo, drone ou câmeras de campo. O sistema processa o vídeo em tempo real, identifica regiões verdes associadas à vegetação e detecta manchas amareladas ou marrons que podem representar anomalias visuais relacionadas a pragas ou doenças.

A aplicação exibe na tela:

* Status da lavoura;
* Nível de risco;
* Percentual estimado de área afetada;
* Marcação visual das anomalias encontradas;
* Recomendação automática para o produtor.

---

## Problema

O agronegócio brasileiro enfrenta perdas significativas quando pragas, doenças ou períodos de seca são identificados tardiamente. Muitas propriedades ainda dependem de inspeções manuais, tornando o monitoramento lento e aumentando os riscos de prejuízo na produção.

---

## Proposta

Utilizar técnicas de Visão Computacional para analisar imagens da lavoura em tempo real e emitir alertas quando sinais de risco forem identificados.

A solução foi idealizada para futuramente ser integrada com:

* Satélites;
* Drones;
* Sensores IoT;
* Plataformas de monitoramento agrícola.

---

## Bibliotecas Utilizadas

* Python
* OpenCV
* NumPy

---

## Funcionalidades

* Captura de vídeo em tempo real via webcam;
* Processamento de vídeos gravados;
* Modo demonstração com vídeo sintético;
* Segmentação de áreas verdes da imagem;
* Detecção de manchas amarelas e marrons;
* Classificação de risco (baixo, médio ou alto);
* Exibição de recomendações na tela;
* Salvamento de prints;
* Geração opcional de relatório CSV.

---

## Estrutura do Projeto

```text
AgroSat-Visao-Computacional/
├── src/
│   └── detector_pragas.py
├── assets/
├── docs/
│   └── roteiro_video.md
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Como Executar

### 1. Clonar o Repositório

```bash
git clone https://github.com/fernandamenon93/AgroSat-Visao-Computacional.git
cd AgroSat-Visao-Computacional
```

### 2. Criar Ambiente Virtual

```bash
python -m venv .venv
```

### 3. Ativar Ambiente Virtual

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 5. Executar com Webcam

```bash
python src/detector_pragas.py
```

### 6. Executar com Vídeo

```bash
python src/detector_pragas.py --video assets/lavoura_praga.mp4
```

### 7. Executar Modo Demonstração

```bash
python src/detector_pragas.py --demo
```

### 8. Gerar Relatório CSV

```bash
python src/detector_pragas.py --salvar
```

Ou:

```bash
python src/detector_pragas.py --video assets/lavoura_praga.mp4 --salvar
```

---

## Controles Durante a Execução

* Pressione **Q** para encerrar o sistema;
* Pressione **S** para salvar um print da tela.

---

## Inferência Visual Utilizada

A inferência visual foi desenvolvida utilizando OpenCV e segmentação de cores no espaço HSV.

O sistema:

1. Identifica áreas verdes da imagem, representando vegetação;
2. Procura manchas amarelas e marrons associadas a possíveis anomalias;
3. Calcula a porcentagem da área afetada;
4. Classifica o risco em baixo, médio ou alto;
5. Exibe recomendações automaticamente ao usuário.

---

## Aplicação Prática na Global Solution

O AgroSat foi desenvolvido para auxiliar no monitoramento inteligente de lavouras, permitindo identificar visualmente sinais iniciais de pragas, doenças ou estresse vegetal.

Em um cenário real, essa solução poderia ser integrada com drones, satélites e câmeras instaladas no campo, contribuindo para decisões mais rápidas e redução de perdas na produção agrícola.

---

## Objetivos de Desenvolvimento Sustentável (ODS)

O projeto está alinhado com:

* ODS 2 – Fome Zero e Agricultura Sustentável;
* ODS 9 – Indústria, Inovação e Infraestrutura;
* ODS 13 – Ação Contra a Mudança Global do Clima.

---

## Vídeo de Demonstração

O vídeo apresenta:

1. O problema enfrentado pelo agronegócio;
2. A proposta da solução AgroSat;
3. A execução do sistema;
4. A inferência visual funcionando em tempo real;
5. A classificação de risco e recomendações automáticas.

Link do vídeo: inserir link do YouTube (não listado).

---

## Repositório GitHub

Inserir link do repositório público:

```text
https://github.com/SEU-USUARIO/AgroSat-Visao-Computacional
```
    
