# AgroSat - Visão Computacional para Monitoramento de Lavouras

## Integrantes

- Fernanda Rocha Menon – RM554673
- Luiza Macena Dantas – RM556237
- Luan Ramos Garcia de Souza – RM558537
- Matheus Ricciotti – RM556930
- Matheus Bortolotto – RM555189

---

## Descrição da Solução

O AgroSat é uma solução de Visão Computacional desenvolvida em Python para auxiliar no monitoramento de lavouras e na identificação de possíveis sinais de pragas, doenças ou estresse vegetal.

O sistema processa vídeos de lavouras ou folhas utilizando OpenCV, identifica regiões verdes da vegetação e procura manchas amareladas ou marrons que podem indicar problemas na plantação.

Com base na análise visual, o sistema apresenta:

- Status da lavoura;
- Nível de risco;
- Área afetada estimada;
- Marcação visual das anomalias;
- Recomendações automáticas para o produtor rural.

---

## Problema

O agronegócio brasileiro sofre perdas significativas devido à identificação tardia de pragas, doenças e problemas ambientais.

Muitas propriedades ainda dependem de inspeções manuais, dificultando o monitoramento constante da lavoura e aumentando os riscos de prejuízos financeiros.

---

## Proposta

Utilizar Visão Computacional para analisar imagens e vídeos da lavoura, identificando sinais visuais de anomalias e gerando alertas para auxiliar a tomada de decisão do produtor.

A solução pode futuramente ser integrada com drones, sensores IoT e imagens de satélite para ampliar a capacidade de monitoramento.

---

## Bibliotecas Utilizadas

- Python
- OpenCV
- NumPy

---

## Funcionalidades

- Processamento de vídeo utilizando OpenCV;
- Segmentação de áreas verdes;
- Detecção de manchas amareladas e marrons;
- Identificação de possíveis anomalias na vegetação;
- Classificação do risco em Baixo, Médio ou Alto;
- Exibição de recomendações automáticas;
- Salvamento de prints da análise;
- Geração opcional de relatório CSV.

---

## Estrutura do Projeto

```text
AgroSat-Visao-Computacional/
│
├── src/
│   └── detector_pragas.py
│
├── docs/
│   └── roteiro_video.md
│
├── assets/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Como Executar o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/fernandamenon93/AgroSat-Visao-Computacional.git
```

```bash
cd AgroSat-Visao-Computacional
```

### 2. Criar Ambiente Virtual

```bash
python -m venv .venv
```

### 3. Ativar Ambiente Virtual

No Windows:

```bash
.venv\Scripts\activate
```

### 4. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 5. Preparar o Vídeo

O vídeo utilizado na demonstração não está armazenado no GitHub devido ao limite de tamanho de arquivos da plataforma.

Para executar o projeto:

1. Crie uma pasta chamada `assets` caso ela não exista;
2. Adicione um vídeo contendo uma folha ou lavoura;
3. Renomeie o vídeo para:

```text
lavoura_praga.mp4
```

A estrutura deverá ficar:

```text
AgroSat-Visao-Computacional/
│
├── assets/
│   └── lavoura_praga.mp4
│
├── src/
├── docs/
├── README.md
└── requirements.txt
```

### 6. Executar o Sistema

```bash
python src/detector_pragas.py --video assets/lavoura_praga.mp4
```

### 7. Gerar Relatório CSV (Opcional)

```bash
python src/detector_pragas.py --video assets/lavoura_praga.mp4 --salvar
```

---

## Controles Durante a Execução

- Pressione **Q** para encerrar o sistema;
- Pressione **S** para salvar um print da tela.

---

## Inferência Visual Utilizada

A solução utiliza técnicas de Visão Computacional baseadas em segmentação de cores no espaço HSV.

O sistema:

1. Identifica regiões verdes associadas à vegetação;
2. Procura manchas amareladas e marrons próximas dessas regiões;
3. Calcula a porcentagem estimada de área afetada;
4. Classifica automaticamente o nível de risco;
5. Exibe recomendações para o produtor rural.

---

## Aplicação Prática na Global Solution

O AgroSat está alinhado ao tema de monitoramento inteligente de lavouras.

A solução permite identificar sinais iniciais de problemas na plantação, auxiliando o produtor a agir rapidamente e reduzindo perdas agrícolas.

Em uma aplicação real, o sistema poderia ser integrado com:

- Drones;
- Sensores IoT;
- Imagens de satélite;
- Plataformas de monitoramento agrícola.

---

## Vídeo de Demonstração

Link do vídeo:

**INSERIR AQUI O LINK DO YOUTUBE (NÃO LISTADO)**

O vídeo apresenta:

- O problema abordado;
- A proposta da solução;
- O funcionamento do sistema;
- O processamento do vídeo;
- A identificação das anomalias;
- A classificação do risco;
- As recomendações geradas.
