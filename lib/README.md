# README

  1. Install stuff

```
sudo pip install -r requirement.txt
```

  1. Put txt files in `input` directory
  2. Execute the app

```
.\app.py
```

#### Notes

  * Converting last/first name using a naive approach. Takking the name field, splitting out the spaces and grabbing the first and last.
  * Looks like approximately 15% of the database have single names (unable to convert to first and last name) --- based on 10,000 records
  * Exporting available names is the following SQL

`
select id, name_first, name_last from user where name_first is not null;
`
