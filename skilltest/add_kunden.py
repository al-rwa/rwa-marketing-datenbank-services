import random
import sqlite3

from faker import Faker


def exec_sqlquery(qry:str):
    connection = sqlite3.connect('./skilltest/db.sqlite3')
    cursor = connection.cursor()
    
    cursor.execute(qry)
    connection.commit()
    
    return cursor.fetchall()
    
    
    
    
def insert_fake_kunden(amount:int):
    mandant_choices = [1,2,3,4,5]
    herkunft_choices = [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3]
    dsgvo_choices = [1,2,3,4,5,6,7]




    for i in range(amount):
        fake = Faker("de-AT")
            
        # kundeid
        mandant = random.choice(mandant_choices)
        herkunft = random.choice(herkunft_choices)
        titel = ''
        vorname = fake.first_name()
        nachname = fake.last_name()
        name = vorname + ' ' + nachname
        geburtsdatum = str(fake.date_of_birth())
        kdkdnr = str(fake.random_int())
        dsgvo = random.choice(dsgvo_choices)
        strasse = fake.street_address()
        plz =  str(random.randrange(100,999)*10)
        ort = fake.city()
        email = fake.free_email()
        telefon = str(fake.phone_number())
        telefon_mobil = str(fake.phone_number())


        qry = """
        insert into kuKunden (mandant_id,herkunft_id,titel,name,vorname,nachname,geburtsdatum,kdkdnr,dsgvo_id,strasse,plz,ort,email,telefon,telefon_mobil)
        values ( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' )
        """ % ( mandant, herkunft, titel, name, vorname, nachname, geburtsdatum, kdkdnr, dsgvo, strasse, plz, ort, email, telefon, telefon_mobil )
    
        # print(qry)
        exec_sqlquery(qry)
    
def main():
    insert_fake_kunden(1000)
    
if __name__ == "__main__":
    main()