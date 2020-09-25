# Pyramid-Word
Rest API is used to check whether a word is a pyramid word or not.

## Problem Statement 

**Write a web service that takes in a string and returns a boolean to indicate whether a word is a pyramid word. A word is a ‘pyramid’ word if you can arrange the letters in increasing frequency, starting with 1 and continuing without gaps and without duplicates.**

*Examples: banana is a pyramid word because you have 1 'b', 2 'n's, and 3 'a's. bandana is not a pyramid word because you have 1 'b' and 1 'd'.*


## Requirements
 - Python >= 3.5.6
 - See [requirements.txt](requirements.txt) for python package requirements.
 
 
## Running the application

 Assuming that Python >= 3.5.6 (preferably 3.7.6) is installed
 
 - Install the python packages required to run the application using:
 
```bash
$ python -m pip install -r requirements.txt -U
```

- Run the api using:

```bash
$ python test_app.py
```

## REST API Endpoints

 - **`http://localhost:8000/is_pyramid_word?word=<word_to_be_checked>`** - **`GET`** - it will check wheather it is a pyramid or not based on the user input.
 
 
 ## Examples
 
 - http://localhost:8000/is_pyramid_word?word=banana - It will return "true" as it is a pyramid.
 
 - http://localhost:8000/is_pyramid_word?word=bandana - it will return "false" as it is not a pyramid.
 
