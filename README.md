# README

  1. Install stuff

```
sudo pip install -r requirement.txt
```

  1. Put `E@v` txt files in `input` directory
  2. Put `J@v` txt file in `input_cred` directory
  3. Put `E@v` txt file in `input_email` directory  
  4. Execute the app

```
.\app.py
```

#### Notes

  * Converting last/first name using a naive approach. Takking the name field, splitting out the spaces and grabbing the first and last.
  * Looks like approximately 15% of the database have single names (unable to convert to first and last name) --- based on 10,000 records
  * Exporting available names is the following SQL
