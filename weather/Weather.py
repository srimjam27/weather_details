import gtts
import playsound3
import requests
import json
import playsound3 as ps
import gtts as gs

while True:
    city = input("ENTER THE NAME OF THE CITY : or $$$ to exit ")

    if city == "$$$":
        print("THANKYOU FOR USING ME")
        break
    req = f"http://api.weatherapi.com/v1/current.json?key=ead5bb7b984f47aa9df90517241105&q={city}"

    r = requests.get(req)
    wdic = json.loads(r.text)
    say = f"The current temperature in {city} in degree celsius is : {wdic["current"]["temp_c"]}"
    print(say)
    saymp = gtts.gTTS(text=say, lang="en")
    saymp.save("play.mp3")
    play = playsound3.playsound("play.mp3")
