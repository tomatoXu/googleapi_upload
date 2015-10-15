# separator used by search.py, categories.py, ...
SEPARATOR = ";"

LANG            = "en_US" # can be en_US, fr_FR, ...
#ANDROID_ID      = "3A9F6D7C0E7729AA"
ANDROID_ID      = "20014289e714f20c"
GOOGLE_LOGIN    = "tomatoXu94@gmail.com"
GOOGLE_PASSWORD = "wc3leswciest"
AUTH_TOKEN      = None # "yyyyyyyyy"


# force the user to edit this file
if any([each == None for each in [ANDROID_ID, GOOGLE_LOGIN, GOOGLE_PASSWORD]]):
    raise Exception("config.py not updated")

