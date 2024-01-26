# Purchases-Extended

Odoo comes with a number of default applications that include 'Purchases Applications'. The RFQ module however, has some missing functionalities that need to be implemented. I will add a one-to-many relationship between an RFQ and Vendors. Create a customization in the system such that one RFQ could be assigned to several vendors at the model-level. Additionally, I will extend these features to the front-end interfaces such that it's possible for the end-user to perform such actions. In summary, i will 
-  Add the ability to assign RFQ to several vendors. Not that this implementation will require you to implement a new module that inherits from an existing module.
-  Add process for receiving bids from suppliers against the RFQ that was issued (one-to-many relation between and RFQ and Bids)
-  Add process for selecting the winning bidder and assigning them a Purchase Order.
-  Implement a purchase-request module that is used by employees to send purchase requests to the Procurement department. Note that the procurement department would use this request to prepare an RFQ specified in item 1 above.


Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,
<a href="https://www.odoo.com/app/website">Website Builder</a>,
<a href="https://www.odoo.com/app/ecommerce">eCommerce</a>,
<a href="https://www.odoo.com/app/inventory">Warehouse Management</a>,
<a href="https://www.odoo.com/app/project">Project Management</a>,
<a href="https://www.odoo.com/app/accounting">Billing &amp; Accounting</a>,
<a href="https://www.odoo.com/app/point-of-sale-shop">Point of Sale</a>,
<a href="https://www.odoo.com/app/employees">Human Resources</a>,
<a href="https://www.odoo.com/app/social-marketing">Marketing</a>,
<a href="https://www.odoo.com/app/manufacturing">Manufacturing</a>,
<a href="https://www.odoo.com/">...</a>

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.

Getting started with Odoo
-------------------------

For a standard installation please follow the <a href="https://www.odoo.com/documentation/16.0/administration/install/install.html">Setup instructions</a>
from the documentation.

To learn the software, we recommend the <a href="https://www.odoo.com/slides">Odoo eLearning</a>, or <a href="https://www.odoo.com/page/scale-up-business-game">Scale-up</a>, the <a href="https://www.odoo.com/page/scale-up-business-game">business game</a>. Developers can start with <a href="https://www.odoo.com/documentation/16.0/developer/howtos.html">the developer tutorials</a>
