# Project Architecture

```
polentas-burguers/
│
├── controller/
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
│   └── is_not_instance.py
│
├── model/
│   ├── __init__.py
│   ├── menu.py
│   ├── order.py
│   ├── person.py
│
├── utils/
│   └── cpf_checker.py
│
├── view/
│   ├── __init__.py
│   ├── abstract_view.py
│   ├── client_view.py
│   ├── employee_view.py
│   ├── menu_view.py
│   ├── order_view.py
│   └── system_view.py
│
└── main.py
```
