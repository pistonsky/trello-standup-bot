# trello-standup-bot

Simple bot that gets you ready for standup.

Sample output:
```
[55 minutes] Calendar widget. Localizations.
[16 minutes] API. Currency conversion doesn't work.
[38 minutes] Metrics report.
[2 hours 2 minutes] API. Currency conversion doesn't work in cache method.
[33 minutes] Calendar Widget. Bug #34.
[11 minutes] Calendar: Cannot read property 'city_code' of undefined
[14 minutes] Klit. OnlineTours
[1 hour 39 minutes] Stats. Clicktripz fraud report.
[4 minutes] Calendar widget. "KOP" bug.

TOTAL: 7 hours
```


# Installation

Assuming you have python3 already installed,

* Clone this repository and change to it
```
git clone git@github.com:pistonsky/trello-standup-bot.git
cd trello-standup-bot
```

* Install virtualenv
```
pip install virtualenv
```

* Create Python virtual environment for project
```
virtualenv env
```

* Activate virtual environment
```
source env/bin/activate
```

* Install project requirements
```
pip install -r requirements.txt
```

* Create settings.py from example
```
cp settings.py.example settings.py
```

* Run the bot
```
python bot.py
```
