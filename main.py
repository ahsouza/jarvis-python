from fastapi import FastAPI
import uvicorn
import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel, HttpUrl
import pyttsx3
import speech_recognition as sr

app = FastAPI()

class Visitor(BaseModel):
    name: str
#    age: int
#    is_related: bool
#    is_employed: bool
#    is_delivery: bool
#    url: HttpUrl
    off_tv: bool
    off_notebook: bool
    off_video_games: bool
#   voice: str

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
#print(voices[0].id)
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', rate + 12)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# FUNCTION WITH ERROR
#def listenCommand():
    #    voice = sr.Recognizer()
    #with sr.Microphone() as source:
    #    print('Escutando comando...')
    #    voice.pause_threshold = 1
    #    audio = voice.listen(source, timeout=1, phrase_time_limit=5)
    #try:
    #    print('Recognizing...')
    #    query = voice.recognize_google(audio, language='en-in')
    #    print(f'user: {query}')
    #except Exception as e:
    #    speak('Say that again please...')
    #    return 'none'
    #return query
#listenCommand()
# FUNCTION WITH ERROR




@app.get('/')
def index():
    return {'message': 'Hello World'}

@app.post('/off')
def offAll(visitor: Visitor):
    engine.say('Olá ' + visitor.name + ', o que vamos fazer agora?')
    print(visitor.name)
    visitor.off_notebook if speak('Senhor! Estamos desligando energia fútil de sua casa!') else None
    #visitor.off_tv if speak('Desligando Televisão!') else None
    #visitor.off_video_games if speak('Desligando PS5 e Xbox One!') else None
    engine.runAndWait()
    return

@app.post('/jarvis')
async def scrapRepos(url: Visitor):
    page = requests.get(str(url.url))
    soup = BeautifulSoup(page.text, 'html.parser')

    def getTitle():
        return soup.head.find('title').text if soup.head.find('title') else None

    def getTreeLink():
        return soup.body.find('a', attrs={'class': 'd-none js-permalink-shortcut'}).get('href') \
            if soup.body.find('a', attrs={'class': 'd-none js-permalink-shortcut'}).get('href') \
            else None

    def getIdTree():
        href = soup.body.find('a', attrs={'class': 'd-none js-permalink-shortcut'}).get('href')
        result = href.split(sep="/")
        return result[-1]

    return {
        "title": getTitle(),
        "TreeLink": getTreeLink(),
        "idTree": getIdTree()
    }

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=4201)
