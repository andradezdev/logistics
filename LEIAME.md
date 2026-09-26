# Guia de Instalação e Configuração — CargoNext

Este documento detalha os requisitos de sistema, dependências e procedimentos passo a passo para instalação e configuração do aplicativo **CargoNext** no ecossistema **ERPZ**.

---

## 🚀 Requisitos de Ambiente

* **Framework:** v16.0 ou superior
* **ERPZ:** v16.0 ou superior
* **Python:** 3.10 ou superior (totalmente compatível com Python 3.14)
* **Node.js:** v18+, v20+ ou v24+ com Yarn
* **MariaDB:** 10.6 ou superior

---

## 📦 Procedimento de Instalação no Bench

### 1. Acessar o diretório do bench
```bash
cd ~/bench
```

### 2. Baixar o aplicativo
```bash
bench get-app https://github.com/andradezdev/logistics.git
```

### 3. Instalar o aplicativo no site desejado
```bash
bench --site [nome-do-site] install-app logistics
```

### 4. Executar a migração de metadados
```bash
bench --site [nome-do-site] migrate
```

### 5. Compilar os assets de interface
```bash
bench build --app logistics
```

### 6. Limpar o cache do sistema
```bash
bench --site [nome-do-site] clear-cache
```

---

## 🔄 Atualização

Para atualizar o aplicativo com as últimas melhorias do repositório:

```bash
cd ~/bench/apps/logistics
git pull origin develop
cd ~/bench
bench build --app logistics
bench --site [nome-do-site] migrate
bench --site [nome-do-site] clear-cache
```

Se necessário, reinicie os serviços:

```bash
sudo supervisorctl restart all
```

---

## 🗑️ Desinstalação

Para desinstalar o aplicativo de um site específico:

```bash
cd ~/bench
bench --site [nome-do-site] uninstall-app logistics
```

Para remover o aplicativo completamente do bench:

```bash
bench remove-app logistics
```
