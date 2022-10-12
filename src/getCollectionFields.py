#!/usr/bin/python

# getCollectionFields.py -- Generates a csv file of specified CONTENTdm collection field information.

import pycdm
import datetime

# Peace Movement collection
# https://cdm21069.contentdm.oclc.org/digital/collection/p21069coll13/

collection='p21069coll13'

filename = '../data/CollectionFields.' + collection + '.csv'
header = ['alias', 'field_nick', 'field_label', 'dc', 'required', 'searchable', 'vocabulary', 'hidden']
f = pycdm.CSV(filename, header=header)

coll = pycdm.Collection(collection)
alias = collection
for k, v in coll.fields.items():
    nick = v.nick
    label = v.name
    dc = v.dc
    req = v.req
    search = v.search
    vocab = v.vocab
    hidden = v.hide
    row = [alias, nick, label, dc, req, search, vocab, hidden]
    f.writerow(row)

f.close()