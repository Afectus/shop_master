


..\manage.py dumpdata --format=xml --indent 4 --natural-foreign --natural-primary -e contenttypes -o dump/auth.xml auth.User auth.Group 

..\manage.py dumpdata --format=xml node.base1c -o dump/node_base1c.xml
..\manage.py dumpdata --format=xml node.pricetype -o dump/node_pricetype.xml
..\manage.py dumpdata --format=xml node.kontragent -o dump/node_kontragent.xml
..\manage.py dumpdata --format=xml node.organization -o dump/node_organization.xml
..\manage.py dumpdata --format=xml node.shopstock -o dump/node_shopstock.xml
..\manage.py dumpdata --format=xml node.shop -o dump/node_shop.xml
..\manage.py dumpdata --format=xml node.stock -o dump/node_stock.xml
..\manage.py dumpdata --format=xml node.cashbox -o dump/node_cashbox.xml
..\manage.py dumpdata --format=xml node.hozoperation -o dump/node_hozoperation.xml
..\manage.py dumpdata --format=xml node.goodscert -o dump/node_goodscert.xml
..\manage.py dumpdata --format=xml node.tax -o dump/node_tax.xml

..\manage.py dumpdata --format=xml node.goods -o dump/node_goods.xml
..\manage.py dumpdata --format=xml node.goodsinstock -o dump/node_goodsinstock.xml
..\manage.py dumpdata --format=xml node.relgoods -o dump/node_relgoods.xml
..\manage.py dumpdata --format=xml node.pricegoods -o dump/node_pricegoods.xml
..\manage.py dumpdata --format=xml node.baseunit -o dump/node_baseunit.xml
..\manage.py dumpdata --format=xml node.properties -o dump/node_properties.xml
..\manage.py dumpdata --format=xml node.propertiesvalue -o dump/node_propertiesvalue.xml
..\manage.py dumpdata --format=xml node.discountcard -o dump/node_discountcard.xml
..\manage.py dumpdata --format=xml node.child -o dump/node_child.xml
..\manage.py dumpdata --format=xml node.buyerevent -o dump/node_buyerevent.xml
..\manage.py dumpdata --format=xml node.buyerrel -o dump/node_buyerrel.xml
..\manage.py dumpdata --format=xml node.barcodelist -o dump/node_barcodelist.xml
..\manage.py dumpdata --format=xml node.discounts -o dump/node_discounts.xml


python node_buyer.py