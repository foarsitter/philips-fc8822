# Remote
Most of the buttons don't need explanations, but some do:

KEY_1, KEY_2, KEY_3 and KEY_4 are the time control buttons, 

KEY_F* are the cleaning path algorithm's

KEY_KP* are for the brushes on the front. 

# Flask webapp
The webapp directory contains a Flask webapp with the remote. 

Run the app with
```
python3 app.py
```

## Screenshot
![alt text](https://github.com/foarsitter/philips-fc8822/blob/master/webapp_screenshot.PNG)


## Security (or the absence of it)
There is HTTP basis auth for the one and only endpoint. Copy the `.env.dist` to `.env` and fill in the values.