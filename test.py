import random
from gtts import gTTS
import os
when = ['A few years ago','In the 20th BC', 'Once upon a time']
who = ['there lived a person named Nirala',' there was a man  named Livingstone', 'there lived a farmer']
time = ['on one fine day','on full moon night', 'in a rainy day']
residence = ['he was passing by','he was going to a picnic', 'he was walking on the roadside']
went = ['he saw a beautiful girl', 'he saw a lady','he saw a man']
happened = ['who seemed very much in panic','who seemed to be in late 20s', 'who seemed to be suspicious']
a= ['found out that','later got to know that','as he looked closely to that person found that']
b=['the person is missing from home which he read in the newspaper the same day','the person is a photographer looking for a perfect view ','the person is waiting for his friends to arrive']
mytext=(random.choice(when) + random.choice(who)  + random.choice(time)  + random.choice(residence)  + random.choice(went)  + random.choice(happened)+random.choice(a)+random.choice(b))

language= 'en'

output=gTTS(text=mytext,lang=language,slow=False)
output.save("output.mp3")
os.system("start output.mp3")
