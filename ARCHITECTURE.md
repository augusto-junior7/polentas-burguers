# Project Architecture

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
├── ARCHITECTURE.md
├── main.py
└── README.md
```
