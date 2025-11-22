# Polenta's Burguers

Um projeto criado para a disciplina **DSOO I — Desenvolvimento de Sistemas Orientados a Objetos I** no curso de **Sistemas de Informação** da **UFSC**. O objetivo principal é aplicar conceitos de orientação a objetos, arquitetura MVC, persistência (local) e interface gráfica no desenvolvimento de um sistema Python.

---

## Sobre

O _Polenta's Burguers_ simula um sistema básico de gerenciamento de pedidos, clientes e funcionários, além de relatórios, de uma hamburgueria fictícia. Meu amigo e eu estávamos em ligação pelo Discord no momento de escolher o nome do projeto. Ele tem um gato, chamado Polenta. Pedi a ele uma ideia de nome para a hamburgueria, e ele respondeu "Polenta Hamburguers", e daí surgiu o queridíssimo.

---

## Tecnologias Utilizadas

-   **Python 3.12**
-   **FreeSimpleGUI**

---

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/augusto-junior7/polentas-burguers.git
    ```
2. Entre no diretório do projeto:
    ```bash
    cd polentas-burguers
    ```
3. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

---

## Execução

Basta rodar o arquivo principal (caso já exista no projeto):

```bash
python main.py
```

---

## Estrutura do Projeto

```
polentas-burguers/
│
├── controllers/
│   ├── __init__.py
│   ├── client_controller.py
│   ├── employee_controller.py
│   ├── menu_controller.py
│   ├── order_controller.py
│   └── system_controller.py
│
├── daos/
│   ├── __init__.py
│   ├── clients_dao.py
│   ├── dao.py
│   ├── employees_dao.py
│   ├── menu_dao.py
│   └── orders_dao.py
│
├── data/
│   ├── clients.pkl
│   ├── employees.pkl
│   ├── menu.pkl
│   └── orders.pkl
│
├── exceptions/
│   ├── __init__.py
│   ├── entity_not_found.py
│   ├── invalid_cpf.py
│   ├── invalid_email.py
│   ├── invalid_phone.py
│   └── is_not_instance.py
│
├── models/
│   ├── __init__.py
│   ├── burger.py
│   ├── client.py
│   ├── drink.py
│   ├── employee.py
│   ├── menu.py
│   ├── menu_item.py
│   ├── order.py
│   ├── order_item.py
│   └── user.py
│
├── utils/
│   ├── cpf_checker.py
│   ├── email_checker.py
│   └── phone_checker.py
│
├── views/
│   ├── __init__.py
│   ├── abstract_view.py
│   ├── client_view.py
│   ├── employee_view.py
│   ├── menu_view.py
│   ├── order_view.py
│   └── system_view.py
│
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

---

## Licença

MIT License

Copyright (c) 2025 **Augusto Roberto Tavares Júnior**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## Autor

[**Augusto Roberto Tavares Júnior**](https://github.com/augusto-junior7)
