# CargoNext — Sistema de Gestão Logística e Comércio Exterior

[![Frappe Framework](https://img.shields.io/badge/Frappe-v16.0%2B-blue.svg)](https://frappeframework.com/)
[![ERPNext](https://img.shields.io/badge/ERPNext-v16.0%2B-blue.svg)](https://erpnext.com/)
[![Python](https://img.shields.io/badge/Python-3.14-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-AGPL--3.0-orange.svg)](license.txt)
[![Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()

O **CargoNext** é uma plataforma completa e modular de gestão logística, transporte multimodal, armazenagem (WMS) e comércio exterior (Freight Forwarding & Customs) desenvolvida nativamente para o **Frappe Framework** e **ERPNext v16**.

A solução unifica a operação de ponta a ponta: desde a cotação comercial inicial até a execução física, controle de marcos operacionais (*milestones*), desembaraço aduaneiro, consolidação de fretes internacionais (Aéreo e Marítimo), gestão de frotas rodoviárias e a apuração financeira individualizada da rentabilidade por embarque (*Job Profitability*).

---

## Sumário Executivo

1. [Visão Geral e Arquitetura](#-visão-geral-e-arquitetura)
2. [Módulos e Ferramentas Disponíveis](#-módulos-e-ferramentas-disponíveis)
   - [Torre de Controle (Control Tower)](#1-torre-de-controle-control-tower)
   - [Frete Aéreo (Air Freight)](#2-frete-aéreo-air-freight)
   - [Frete Marítimo (Sea Freight)](#3-frete-marítimo-sea-freight)
   - [Transporte Rodoviário (TMS)](#4-transporte-rodoviário-tms)
   - [Armazenagem (WMS)](#5-armazenagem-wms)
   - [Desembaraço Aduaneiro (Customs)](#6-desembaraço-aduaneiro-customs)
   - [Central de Precificação e Tarifas (Pricing Center)](#7-central-de-precificação-e-tarifas-pricing-center)
   - [Gestão Operacional de Serviços (Job Management & DRE)](#8-gestão-operacional-de-serviços-job-management--dre)
   - [Gestão de Contêineres](#9-gestão-de-contêineres)
   - [Adiantamentos e Compensação Financeira (Cash Advance & Netting)](#10-adiantamentos-e-compensação-financeira-cash-advance--netting)
   - [Sustentabilidade e Carbono](#11-sustentabilidade-e-carbono)
3. [Principais Regras do Processo e Fluxos Operacionais](#-principais-regras-do-processo-e-fluxos-operacionais)
   - [Fluxo Ponta a Ponta do Embarque](#fluxo-ponta-a-ponta-do-embarque)
   - [Cálculo de Peso Taxável e Cubagem](#cálculo-de-peso-taxável-e-cubagem)
   - [Rentabilidade em Tempo Real (DRE do Processo)](#rentabilidade-em-tempo-real-dre-do-processo)
   - [Travamento de Cobranças e Fechamento](#travamento-de-cobranças-e-fechamento)
   - [Política de Bloqueio por Limite de Crédito](#política-de-bloqueio-por-limite-de-crédito)
4. [Instalação e Configuração](#-instalação-e-configuração)
5. [Localização e Suporte a Idiomas](#-localização-e-suporte-a-idiomas)

---

## 🏛 Visão Geral e Arquitetura

O CargoNext foi projetado segundo os mais rigorosos padrões da indústria logística global (IATA, FIATA, IMO e ISO), operando de maneira acoplada aos livros fiscais e financeiros do ERPNext sem alterar o core do sistema.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        CARGONEXT LOGISTICS HUB                         │
├───────────────────────────────────┬────────────────────────────────────┤
│         TORRE DE CONTROLE         │       CENTRAL DE PRECIFICAÇÃO      │
│  KPIs Executivos, Riscos, Metas   │    Cotações, Tarifas, Câmbio       │
├─────────────────┬─────────────────┼─────────────────┬──────────────────┤
│   FRETE AÉREO   │ FRETE MARÍTIMO  │   TRANSPORTE    │   ARMAZENAGEM    │
│  MAWB/HAWB, ULD │ B/L, FCL, LCL   │  TMS, Coletas   │ WMS, Inbound/Out │
├─────────────────┴─────────────────┴─────────────────┴──────────────────┤
│                         DESEMBARAÇO ADUANEIRO                          │
│               Declarações, Licenças, Comercial Invoices                │
├────────────────────────────────────────────────────────────────────────┤
│                     JOB MANAGEMENT & FINANCIALS                        │
│   Rentabilidade (DRE), Faturas de Venda/Compra, Adiantamentos, Netting │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 📦 Módulos e Ferramentas Disponíveis

### 1. Torre de Controle (Control Tower)
Painel de inteligência executiva voltado para diretoria e gerência operacional:
* **Segmentação em 3 Eixos:**
  * **Centros de Lucro (Profit Centers):** Acompanhamento de metas de Lucro Bruto (GP Target) por filial, região e linha de negócio.
  * **Centros de Custo (Cost Centers):** Indicadores de tempos de ciclo (*Lead Times*), tempo médio de processos abertos e volume de processos manuseados.
  * **Centros de Recursos (Resource Centers):** Métricas de suporte (RH, TI, Controladoria e Finanças).
* **Funil de Oportunidades (Pipeline Listing):** Previsão de novos projetos, feiras e cargas de alto valor.
* **Matriz de Riscos Operacionais (Risk Register):** Monitoramento preventivo de sinistros, atrasos e contingências.

### 2. Frete Aéreo (Air Freight)
Gestão integral de fretes aéreos internacionais e domésticos:
* **Air Booking:** Registro da reserva de espaço junto à companhia aérea ou consolidador.
* **Air Shipment:** Execução do embarque com amarração de volumes, peso bruto e cubagem.
* **Air Consolidation:** Agrupamento de múltiplos embarques filhotes (*HAWB*) sob um mesmo conhecimento master (*MAWB*).
* **Documentos Oficiais:** Emissão de Conhecimento Aéreo Master (*MAWB*), Conhecimento Filhote (*HAWB*), Declaração de Cargas Perigosas (*Dangerous Goods Declaration - DGD*).
* **Controle de Equipamentos:** Rastreamento de *Unit Load Devices (ULD)* e paletes aéreos.

### 3. Frete Marítimo (Sea Freight)
Solução para armadores, NVOCCs e agentes de carga marítima:
* **Sea Booking:** Reserva de praça em navios porta-contêineres, graneleiros e cargas de projeto.
* **Sea Shipment:** Processo operacional de transporte marítimo com controle de portos (*POL*, *POD*, *Transshipment*).
* **Consolidação FCL e LCL:** Agrupamento de cargas soltas (*LCL - Less than Container Load*) em contêineres completos (*FCL - Full Container Load*).
* **Documentação Marítima:** Emissão e gestão de *Bill of Lading Master (B/L)* e *House Bill of Lading (HBL)*.
* **Controle de Sobrestadia:** Alertas e cálculo de *Demurrage* (no porto) e *Detention* (fora do porto).

### 4. Transporte Rodoviário (TMS)
Gestão completa de coletas, entregas e transferências rodoviárias:
* **Transport Order:** Planejamento comercial da solicitação de transporte do cliente.
* **Transport Job:** Execução operacional da viagem com alocação de frota própria ou terceirizada.
* **Janelas de Agendamento (*Pick & Drop Windows*):** Validação matemática de compatibilidade de horário entre janelas de carregamento e tempo estimado de trânsito.
* **Frota e Condutores:** Cadastro e controle de veículos de carga (*Transport Vehicle*), carretas, motoristas (*Transport Driver*) e folhas de rota (*Run Sheets*).

### 5. Armazenagem (WMS)
Operações de armazém geral, centros de distribuição e recintos alfandegados:
* **Warehouse Job:** Controle central de movimentação de mercadorias no armazém.
* **Inbound & Release Orders:** Fluxo de recebimento físico com conferência cega e ordens de expedição com picking/packing.
* **Cross-Docking Order:** Transbordo direto de mercadorias de veículos de entrada para veículos de saída sem estocagem prolongada.
* **VAS Order (Value-Added Services):** Gestão de serviços agregados como etiquetagem, montagem de kits e reembalagem.

### 6. Desembaraço Aduaneiro (Customs)
Processamento fiscal e aduaneiro de comércio exterior:
* **Declaration & Declaration Order:** Escrituração e acompanhamento de declarações de importação e exportação.
* **Documentos Vinculados:** Gestão e conferência de *Commercial Invoices*, *Packing Lists*, Certificados de Origem e Licenças de Importação/Exportação.
* **Classificação Fiscal:** Amarrações tarifárias e acompanhamento do desembaraço alfandegário.

### 7. Central de Precificação e Tarifas (Pricing Center)
Motor comercial dinâmico e flexível:
* **Sales Quote:** Elaboração de cotações comerciais detalhadas contemplando frete internacional, taxas locais, frete rodoviário e despesas de despacho.
* **Tarifas Gerais e Específicas (*Tariff*):** Tabelas de preços contratuais negociadas com armadores, companhias aéreas e clientes.
* **Taxas de Câmbio Operacionais (*Operational Exchange Rates*):** Resolução automática da taxa de câmbio aplicável na data do embarque para conversão de moedas estrangeiras (USD, EUR, etc.) para a moeda local.
* **Importação em 1 Clique:** Mecanismo `Get Charges from Quotation` para herdar automaticamente todas as linhas de tarifa da cotação aprovada para o processo operacional.

### 8. Gestão Operacional de Serviços (Job Management & DRE)
O coração financeiro do CargoNext:
* **Demonstrativo de Rentabilidade (*Job Profitability*):** Apuração em tempo real do Lucro Bruto (*Gross Profit - GP*) e Margem de Contribuição por processo.
* **Receitas e Custos:** Separação estrita entre receitas contratadas com o cliente e custos operacionais provisionados junto a fornecedores/agentes.
* **Geração Automática de Documentos Financeiros:** Criação direta de Faturas de Venda (*Sales Invoice*) e Faturas de Compra (*Purchase Invoice*) a partir das linhas de cobrança do embarque, eliminando retrabalho de digitação.
* **Subtarefas Internas (*Internal Jobs*):** Desdobramento de serviços complementares (ex: transporte de apoio ou armazenagem local) vinculados ao processo principal.

### 9. Gestão de Contêineres
* **Validação ISO 6346:** Validação algorítmica de integridade dos 11 caracteres identificadores do contêiner (sigla do proprietário + tipo + número serial + dígito verificador).
* **Depósitos e Cauções (*Container Deposit*):** Controle de valores retidos junto aos armadores e integração com contas transitórias de clientes.

### 10. Adiantamentos e Compensação Financeira (Cash Advance & Netting)
* **Adiantamentos Operacionais:** Solicitação, aprovação e prestação de contas de numerário antecipado para custeio de taxas portuárias, combustível e despesas em viagem.
* **Compensação Internacional (*Netting*):** Conciliação de saldos a pagar e a receber entre filiais e agentes internacionais parceiros com liquidação líquida periódica.

### 11. Sustentabilidade e Carbono
* **Calculadora de Pegada de Carbono:** Estimativa e relatório de emissão de CO2 equivalente com base na distância percorrida, peso da carga e modal de transporte utilizado.

---

## ⚙️ Principais Regras do Processo e Fluxos Operacionais

### Fluxo Ponta a Ponta do Embarque

```
[1. Oportunidade / Lead]
           │
           ▼
[2. Cotação de Venda (Sales Quote)]
           │
           ▼ (Aprovação Comercial)
[3. Reserva de Espaço (Air / Sea Booking)]
           │
           ▼ (Embarque Físico)
[4. Embarque Operacional (Shipment / Transport Job)] ────► [Rastreamento em Tempo Real]
           │                                         (Aeronave / Navio / Veículo)
           ▼
[5. Conferência de Marcos (Milestones) & Documentos]
           │
           ▼
[6. Faturamento (Sales Invoice) & Custeio (Purchase Invoice)]
           │
           ▼
[7. Apuração Final de Rentabilidade (Job Profitability)] ──► [Fechamento / Trava de Custos]
```

### Cálculo de Peso Taxável e Cubagem
O sistema aplica a regra internacional de peso taxável (*Chargeable Weight*), adotando o maior valor entre o peso bruto real e o peso cubado:
* **Frete Aéreo (Padrão IATA):** Relação `1 m³ = 166,67 kg` (Fator de cubagem `1:6000`).
* **Frete Marítimo LCL:** Relação `1 m³ = 1.000 kg` (Regra W/M - *Weight or Measurement*).
* **Transporte Rodoviário:** Fator configurável conforme a densidade da carga e tipo de veículo.

### Rentabilidade em Tempo Real (DRE do Processo)
Cada processo operacional possui um painel de rentabilidade (*Profitability Summary*) que confronta:
$$	ext{Receita Real Faturada} - 	ext{Custo Real Comprovado} = 	ext{Lucro Bruto (GP)}$$
$$	ext{Margem de Lucro (\%)} = \left(rac{	ext{Lucro Bruto}}{	ext{Receita Total}}ight) 	imes 100$$
Divergências entre estimativas e valores finais são destacadas visualmente para o operador antes da conclusão do processo.

### Travamento de Cobranças e Fechamento
Para evitar fraudes e lançamentos extemporâneos:
* Ao atingir o status de fechamento (`Closed` / `Completed`), o grid de cobranças e custos é bloqueado automaticamente contra edições.
* Alterações posteriores exigem a permissão de **Reabertura de Processo** (*Reopen Job*), que audita e registra o motivo e o usuário responsável.

### Política de Bloqueio por Limite de Crédito
* O CargoNext monitora em tempo real a situação financeira do cliente cadastrado no ERPNext.
* Clientes com faturas em atraso ou que excedam o limite de crédito aprovado entram em **Credit Hold**, impedindo a emissão de novos embarques ou a liberação de conhecimentos de transporte.
* Exceções emergenciais são tratadas via **Credit Hold Lift Request**, sujeitas à aprovação exclusiva do papel `Credit Manager`.

---

## 🚀 Instalação e Configuração

### Pré-requisitos
* **Frappe Framework:** v16.0 ou superior
* **ERPNext:** v16.0 ou superior
* **Python:** 3.14+
* **MariaDB:** 10.6+

### Instalação no Bench

```bash
# 1. Acessar o diretório do bench
cd ~/frappe-bench

# 2. Baixar o aplicativo
bench get-app https://github.com/andradezdev/logistics.git

# 3. Instalar o aplicativo no site desejado
bench --site [nome-do-site] install-app logistics

# 4. Executar a migração de metadados
bench --site [nome-do-site] migrate

# 5. Compilar os assets de interface
bench build --app logistics

# 6. Limpar o cache do sistema
bench --site [nome-do-site] clear-cache
```

---

## 🌐 Localização e Suporte a Idiomas

* O CargoNext suporta integralmente o **Português do Brasil (pt-BR)** através do catálogo padronizado em `translations/pt-BR.csv`.
* **Preservação de Integridade:** As traduções aplicam-se estritamente à camada de apresentação visual da interface do usuário (nomes de tela, campos, tooltips e relatórios), mantendo os esquemas de banco de dados, nomes técnicos de DocTypes, métodos Python e variáveis 100% íntegros e compatíveis com a arquitetura padrão internacional.

---

## 📄 Licença

Este projeto é distribuído sob a licença **GNU Affero General Public License v3.0 (AGPLv3)**. Consulte o arquivo `license.txt` para detalhes.
