# 🧩 Identificador de Categoria de Gadgets

Este projeto foi desenvolvido como parte de um desafio da DIO (Digital Innovation One).  
O objetivo é criar uma função simples, clara e reutilizável que identifique a categoria de um gadget analisando somente a **primeira letra do código** informado pelo usuário.

---

## 📘 Sobre o desafio

O código do gadget sempre começa com uma letra, que representa sua categoria:

| Letra | Categoria  |
|-------|------------|
| **T** | tablet     |
| **P** | phone      |
| **N** | notebook   |
| outra | unknown    |

Se a primeira letra não corresponder a nenhuma das categorias conhecidas, o retorno deve ser **"unknown"**.

---

## 🚀 Tecnologias utilizadas

- **Python 3**
- Estruturas condicionais (`if`)
- Funções
- Manipulação básica de strings

---

## 🧠 Lógica da Solução

1. A função recebe uma string representando o código do gadget.  
2. Verifica a **primeira letra** usando `startswith()`.  
3. Retorna a categoria correspondente:  
   - `"tablet"` para códigos que começam com **T**  
   - `"phone"` para códigos que começam com **P**  
   - `"notebook"` para códigos que começam com **N**  
4. Caso nenhuma condição seja atendida → retorna `"unknown"`.

---

## 📥 Exemplo de Entrada e Saída

| Entrada   | Saída     |
|-----------|-----------|
| `T12345X` | tablet    |
| `P45YTS`  | phone     |
| `N9087L`  | notebook  |
| `R22K9W`  | unknown   |

---

## 💻 Como executar

No terminal, execute:

```bash
python nome_do_arquivo.py
