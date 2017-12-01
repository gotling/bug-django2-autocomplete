# Bug - Django2 - Autocomplete - InlineAdmin
Show how autocomplete for relations don't work when adding a new line to inline model

## Versions

Django: 2.0rc1
Python: 3.5

## Expected behaviour

Select opening when clicked

## Actual behaviour

Nothing happens

## Screenshot

![Inline Item](/screenshot.png?raw=true "Inline Item")

## How to reproduce

1. Install dependencies

    pip install -r requirements.txt

2. Start Django server

    ./manage.py runserver

3. Open Admin in web browser

    http://127.0.0.1:8000/admin/autocomplete/item/1/change/

4. Login

    Username: djangoproject
    Password: djangoproject

5. Under *Line Items* click on select field *Category*

    Select is opened with **My Category** listed

6. Click *Add another Line item*
7. On the new row, click on select field *Category*

    Nothing is happening