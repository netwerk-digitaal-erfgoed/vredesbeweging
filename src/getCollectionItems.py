#!/usr/bin/python

# getCollectionFields.py -- Generates a csv file of specified CONTENTdm collection field information.

import pycdm
import datetime

# Peace Movement collection
# https://cdm21069.contentdm.oclc.org/digital/collection/p21069coll13/

collection='p21069coll13'

fields = ['creato','subjec','descri','title','langua','publis','dmrecord','losse','source','find','dmmodified','date','contri','identi','dmcreated']
#  niet opgenomen in CSV:
# - 'rights','dmoclcno','fullrs', geen waarden
# - 'format' aantal pagina's bij sommige, meerderheid leeg
# - 'type' bij 1 Book, 1 Map, rest geen waarde
# - 'fullte', OCR tekst geeft te veel ruis

f = pycdm.CSV("../data/vredesbeweging.csv", header=fields)

vredesbeweging = pycdm.Collection(collection)
vredesbeweging.getItems()
for i in vredesbeweging.items:
    item = pycdm.item(collection, i) 
    row = []
    for p in fields:
        row.append(item.info[p])

    f.writerow(row)

f.close()