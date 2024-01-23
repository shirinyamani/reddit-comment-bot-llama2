# reddit-comment-bot-llama2 🦙

![bot](https://miro.medium.com/v2/resize:fit:1400/1*_tFFL4D1331iE_L8J9Oh1A.jpeg)

## What is this?
This bot will find specific comments which contain a keyword `trigger_phrase` and reply to them with a `reply`. For `reply` comment it is connected to llama2 model which will generate a reply based on the `trigger_phrase` word. 

## Make sure to:
1. Install all the dependencies using:
```python
pip install -r requirements.txt
```
2. Create a reddit app and get the `client_id` and `client_secret` from [here](https://www.reddit.com/prefs/apps/)

3. Install `llama2` model from [ollama repo](https://github.com/jmorganca/ollama)


## How to run?
1. Clone the repo
```python
git clone
2. Run the bot in the directory where you cloned the repo
```python
python main.py
```
