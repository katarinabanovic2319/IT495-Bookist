# IT495-Bookist
Bookist je aplikacija za ljubitelje knjiga.
# Instalacija
Klonirati repozitorijum komandom

`git clone https://github.com/katarinabanovic2319/IT495-Bookist.git`

Pokrenuti komandu za instalaciju zahteva

`pip install -r requirements.txt`

Zatim pokrenuti sledeću komandu

python setup.py install

Kreirati bazu sledećim komandama

```
python manage.py makemigrations
python manage.py migrate
```

Kreirati administratora komandom

`python manage.py createsuperuser`

# Pokretanje aplikacije

Pokrenuti aplikaciju komandom

`python manage.py runserver`

Pristupiti localhostu na URL-u localhost:8000/
