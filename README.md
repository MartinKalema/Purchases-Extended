<img align="center" alt="Coding" width="300" src="./odoo_logo.svg">

## Purchases-Extended  ![Static Badge](https://img.shields.io/badge/purchases_extended-v1.0-blue?style=for-the-badge)  ![GitHub contributors](https://img.shields.io/github/contributors/MartinKalema/purchases-extended?style=for-the-badge&logo=github) ![Static Badge](https://img.shields.io/badge/Odoo_version-v17.0-neon?style=for-the-badge)

Odoo comes with a number of default applications that include 'Purchases Applications'. The RFQ module however, has some missing functionalities that need to be implemented. I will add a one-to-many relationship between an RFQ and Vendors. Create a customization in the system such that one RFQ could be assigned to several vendors at the model-level. Additionally, I will extend these features to the front-end interfaces such that it's possible for the end-user to perform such actions. In summary, i will 
-  Add the ability to assign RFQ to several vendors. Not that this implementation will require you to implement a new module that inherits from an existing module.
-  Add process for receiving bids from suppliers against the RFQ that was issued (one-to-many relation between and RFQ and Bids)
-  Add process for selecting the winning bidder and assigning them a Purchase Order.
-  Implement a purchase-request module that is used by employees to send purchase requests to the Procurement department. Note that the procurement department would use this request to prepare an RFQ specified in item 1 above.

## Structure
```
├── controllers
│   ├── controllers.py
│   └── __init__.py
├── demo
│   └── demo.xml
├── __init__.py
├── __manifest__.py
├── models
│   ├── __init__.py
│   └── models.py
├── security
│   └── ir.model.access.csv
└── views
    ├── templates.xml
    └── views.xml
```
## Install this project
Add this to your custom addons folder using this bash command 
  ```bash
  git clone https://github.com/MartinKalema/purchases-extended.git
  ```

