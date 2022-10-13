import csv
import pipes

creatorid=1

with open('data/Vredesbeweging.tsv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')
    for row in csv_reader:
        dmrecord=row["dmrecord"]
        uri=f'<https://cdm21069.contentdm.oclc.org/digital/collection/p21069coll13/id/{dmrecord}>'

        if row["title"]:
            title=row["title"].replace('"', r'\"');
            print(f'{uri} <https://schema.org/name> "{title}" .')

        for i in range(1,15):
            if row[f"creato {i}"]:
                creatos=row[f"creato {i}"].replace('"', r'\"').split(";");
                for creat in creatos:
                    creato=creat.strip() 
                    
                    if row[f"creato uri {i}"]:
                        curi=row[f"creato uri {i}"]
                        print(f'{uri} <https://schema.org/creator> <{curi}> .')
                        print(f'<{curi}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> .')
                        print(f'<{curi}> <http://www.w3.org/2000/01/rdf-schema#label> "{creato}" .')
                        print(f'<{curi}> <http://schema.org/name> "{creato}" .')
                    else:
                        print(f'{uri} <https://schema.org/creator> _:creator_{creatorid} .')
                        print(f'_:creator_{creatorid} <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> .')
                        print(f'_:creator_{creatorid} <http://www.w3.org/2000/01/rdf-schema#label> "{creato}" .')
                        print(f'_:creator_{creatorid} <http://schema.org/name> "{creato}" .')
                        creatorid+=1
            
        if row["subjec"]: 
            subjec=row["subjec"].replace('"', r'\"');
            print(f'{uri} <https://schema.org/about> "{subjec}" .')
            
        if row["descri"]: 
            descri=row["descri"].replace('"', r'\"').replace('\n', r'\\n');
            print(f'{uri} <https://schema.org/abstract> "{descri}" .')

        if row["losse"]: 
            losse=row["losse"].replace('"', r'\"').replace('\n', r'\\n');
            print(f'{uri} <https://schema.org/abstract> "{losse}" .')

        if row["langua"]: 
            languas=row["langua"].split(";")
            for langua in languas:
                lang=langua.strip() 
                print(f'{uri} <https://schema.org/inLanguage> _:lang_{lang} .')

        if row["publis"]: 
            publis=row["publis"].replace('"', r'\"');
            print(f'{uri} <https://schema.org/publisher> "{publis}" .')
            # TODO zou eigenlijk Organization moeten zijn
            
        if row["source"]: 
            source=row["source"].replace('"', r'\"');
            print(f'{uri} <https://schema.org/sourceOrganization> "{source}" .')
            # TODO zou eigenlijk Organization moeten zijn
            
        if row["find"]: 
            find=row["find"].replace('"', r'\"');
            print(f'{uri} <https://cdm21069.contentdm.oclc.org/digital/collection/p21069coll13/id/def/find> "{find}" .')

        if row["dmmodified"]: 
            dmmodified=row["dmmodified"].replace('"', r'\"');
            print(f'{uri} <https://cdm21069.contentdm.oclc.org/digital/collection/p21069coll13/id/def/dmmodified> "{dmmodified}" .')

        if row["date"]:
            date=row["date"].replace('"', r'\"');
            print(f'{uri} <https://schema.org/dateCreated> "{date}" .')

        if row["contri"]: 
            contri=row["contri"].replace('"', r'\"').replace('\n', r'');
            print(f'{uri} <https://schema.org/contributor> "{contri}" .')
            # TODO zou eigenlijk Organization moeten zijn
            
        if row["identi"]: 
            identi=row["identi"].replace('"', r'\"');
            print(f'{uri} <https://schema.org/identifier> "{identi}" .')
  
        if row["dmcreated"]: 
            dmcreated=row["dmcreated"].replace('"', r'\"');
            print(f'{uri} <https://cdm21069.contentdm.oclc.org/digital/collection/p21069coll13/id/def/dmcreated> "{dmcreated}" .')
 
        print(f'{uri} <https://schema.org/image> <https://cdm21069.contentdm.oclc.org/digital/api/singleitem/collection/p21069coll13/id/{dmrecord}/thumbnail> .')
        print(f'{uri} <https://schema.org/mainEntityOfPage> <https://cdm21069.contentdm.oclc.org/digital/collection/p21069coll13/id/{dmrecord}> .')
        print(f'{uri} <https://schema.org/url> <https://cdm21069.contentdm.oclc.org/digital/api/collection/p21069coll13/id/{dmrecord}/download> .')


# NB: in brondata komen enkele fouten voor:
# 1784 > Dutc;h English; French > Dutch; English; French
# 1384 > Dutch German > Dutch;German
# 1385 > Dutch German > Dutch;German

langs={'Bulgarian':'bg','Chinese':'zh','Czech':'cs','Danish':'da','Dutch':'nl','English':'en','French':'fr','German':'de',
       'Esperanto':'eo','Welsh':'cy','Japanese':'ja','Norwegian':'no','Swedish':'sv','Russian':'ru'}

for lang_key in langs:
    print(f'_:lang_{lang_key} <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Language> .')
    print(f'_:lang_{lang_key} <http://www.w3.org/2000/01/rdf-schema#label> "{lang_key}" .')
    print(f'_:lang_{lang_key} <http://schema.org/name> "{lang_key}" .')
    print(f'_:lang_{lang_key} <http://schema.org/alternateName> "{langs[lang_key]}" .')
