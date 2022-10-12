# Vredesbeweging collectie / Peace Movement collection
Code en data voor proof-of-concetp PICA Verbonden Erfgoed project van de Vredespaleis bibliotheek.
Focus op de ContentDM collectie https://cdm21069.contentdm.oclc.org/digital/collection/p21069coll13/

# Gebruikte software
- [RMLMapper](https://github.com/RMLio/rmlmapper-java) executes RML rules to generate high quality Linked Data from multiple originally (semi-)structured data sources
- [Pycdm](https://github.com/saverkamp/pycdm) is a simple Python 2.7 library (tip: use (virtualenv)[https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b]) for working with your CONTENTdm item and collection metadata as Python objects.
- [dmwebservices](https://help.oclc.org/Metadata_Services/CONTENTdm/Advanced_website_customization/API_Reference/CONTENTdm_API/CONTENTdm_Server_API_Functions_-_dmwebservices) is a simple wrapper around the CONTENTdm Server API functions
- [OpenRefine](https://openrefine.org/) (previously Google Refine) is a powerful tool for working with messy data: cleaning it; transforming it from one format into another; and extending it with web services and external data.


# Stap 1

Opvragen van de metadata van betreffende collectie via [getCollectionFields.py](https://github.com/netwerk-digitaal-erfgoed/vredesbeweging/blob/main/src/getCollectionFields.py):

```
python src/getCollectionFields.py
```

Resultaat (inclusief de DC mapping) is [CollectionFields.p21069coll13.csv](https://github.com/netwerk-digitaal-erfgoed/vredesbeweging/blob/main/data/CollectionFields.p21069coll13.csv)

# Stap 2

Alle items uit de collectie ophalen via [getCollectionItems.py](https://github.com/netwerk-digitaal-erfgoed/vredesbeweging/blob/main/src/getCollectionItems.py):

```
python src/getCollectionItems.py
```

Resultaat in CSV bestand [vredebeweging.csv](https://github.com/netwerk-digitaal-erfgoed/vredesbeweging/blob/main/data/vredesbeweging.csv)

Dit bestand is in OpenRefine bekeken en enkele kolommen zijn geïndentificeerd als altijd leeg, zeer weinig waarde of te veel ruis (de ge-OCR-de tekst). Deze kolommen zijn in getCollectionItems.py uitgezonderd, waarna het CSV bestand opnieuw is aangemaakt.

# Stap 3

Conversie op basis van contentdm.ttl RML van de CSV naar N-triples:

```
docker run --rm -v $(pwd):/data rmlmapper -m etc/contentdm.ttl > data/vredesbeweging.nt
```

De mapping maakt een @id op basis van de het dmrecord veld. De meeste velden zijn gemapped naar de Dublin Core variant. Enkele contentDM specifieke velden zijn onvertaald.

Lege waarden zijn uit het bestand gefilterd (moet waarschijnlijk netter via RML kunnen...):

```
grep -v '> "".' data/vredesbeweging.nt > data/vredesbeweging2.nt
```

# Stap 4

De N-triples uit [vredesbeweging2.nt](https://github.com/netwerk-digitaal-erfgoed/vredesbeweging/blob/main/data/vredesbeweging2.nt) zijn geupload in naar Triply:
https://data.netwerkdigitaalerfgoed.nl/Peace-Palace-Library/Peace-Movement-collection/

# TODO 

Velden die zich lenen voor reconciliatie: 
- dct:creator (echter, veld kan meerdere creators bevatten, dus eerst opsplitsen/opschonen)
