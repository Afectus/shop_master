#!/bin/bash


../manage.py dumpdata --format=xml --indent 4 --natural-foreign --natural-primary -e contenttypes -o dump/auth.xml auth.User auth.Group 

../manage.py dumpdata --format=xml --indent 4 node.base1c -o dump/node_base1c.xml
../manage.py dumpdata --format=xml --indent 4 node.pricetype -o dump/node_pricetype.xml
../manage.py dumpdata --format=xml --indent 4 node.kontragent -o dump/node_kontragent.xml
../manage.py dumpdata --format=xml --indent 4 node.organization -o dump/node_organization.xml
../manage.py dumpdata --format=xml --indent 4 node.shopstock -o dump/node_shopstock.xml
../manage.py dumpdata --format=xml --indent 4 node.shop -o dump/node_shop.xml
../manage.py dumpdata --format=xml --indent 4 node.stock -o dump/node_stock.xml
../manage.py dumpdata --format=xml --indent 4 node.cashbox -o dump/node_cashbox.xml
../manage.py dumpdata --format=xml --indent 4 node.hozoperation -o dump/node_hozoperation.xml
../manage.py dumpdata --format=xml --indent 4 node.goodscert -o dump/node_goodscert.xml
../manage.py dumpdata --format=xml --indent 4 node.tax -o dump/node_tax.xml

../manage.py dumpdata --format=xml --indent 4 node.goods -o dump/node_qinstock.xml
../manage.py dumpdata --format=xml --indent 4 node.goodsmotivationratiosum -o dump/node_goodsmotivationratiosum.xml



../manage.py dumpdata --format=xml --indent 4 node.goods -o dump/node_goods.xml
../manage.py dumpdata --format=xml --indent 4 node.goodsinstock -o dump/node_goodsinstock.xml
../manage.py dumpdata --format=xml --indent 4 node.relgoods -o dump/node_relgoods.xml
../manage.py dumpdata --format=xml --indent 4 node.pricegoods -o dump/node_pricegoods.xml
../manage.py dumpdata --format=xml --indent 4 node.baseunit -o dump/node_baseunit.xml
../manage.py dumpdata --format=xml --indent 4 node.properties -o dump/node_properties.xml
../manage.py dumpdata --format=xml --indent 4 node.propertiesvalue -o dump/node_propertiesvalue.xml
../manage.py dumpdata --format=xml --indent 4 node.discountcard -o dump/node_discountcard.xml
../manage.py dumpdata --format=xml --indent 4 node.child -o dump/node_child.xml
../manage.py dumpdata --format=xml --indent 4 node.buyerevent -o dump/node_buyerevent.xml
../manage.py dumpdata --format=xml --indent 4 node.buyerrel -o dump/node_buyerrel.xml
../manage.py dumpdata --format=xml --indent 4 node.barcodelist -o dump/node_barcodelist.xml
../manage.py dumpdata --format=xml --indent 4 node.discounts -o dump/node_discounts.xml

python node_buyer.py