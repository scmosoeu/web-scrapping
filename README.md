# web-scrapping

## Key take aways so far...

Within your virtual environment  <br> 
`
pip install ipython
`

Inside the **scrapy.cfg** below the [settings]
insert: <br>
`
shell = ipython
`

For data processing, there are two options: <br>
1. Serializer (inserted in **items.py**)
2. Pipelines

After creating Pipelines, uncomment the ITEM_PIPELINE section in settings.py

Saving data:
Create FEEDS in the settings.py file to create an output file format

custom_settings insider your spider can be used to overwrite settings

pip install mysql mysql-connector-python

