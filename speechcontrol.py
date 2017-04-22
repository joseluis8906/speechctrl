#!/usr/bin/env python

import speech_recognition as sr
import pyglet
from random import randint


player = pyglet.media.Player()

q0 = [""]
r0 = [
    pyglet.resource.media("responses/i_could_not_understand_you.wav", streaming=False),
]

q1 = ["who are you", "what is your name"]
r1 = [
    pyglet.resource.media("responses/i'm_sally.wav", streaming=False),
    pyglet.resource.media("responses/my_name_is_sally.wav", streaming=False)
]

q2 = ["what do you do", "what is your purpose"]
r2 = [
    pyglet.resource.media("responses/i'm_speech_control.wav", streaming=False),
    pyglet.resource.media("responses/my_purpose_is_supervice_my_master's_house.wav", streaming=False),
    pyglet.resource.media("responses/my_purpose_is_to_take_care_of_my_master's_house.wav", streaming=False),
    pyglet.resource.media("responses/i_control_the_security_and_the_conford_of_my_master's_house.wav", streaming=False)
]

q3 = ["who is your creator", "who is your master"]
r3 = [
    pyglet.resource.media("responses/my_creator_is_mr_caceres.wav", streaming=False),
]

q4 = ["can you count", "can you speak", "can you control"]
r4 = [
    pyglet.resource.media("responses/i_can_do_that.wav", streaming=False),
    pyglet.resource.media("responses/yes_i_can.wav", streaming=False),
    pyglet.resource.media("responses/yes_i_can_do_it.wav", streaming=False)
]

q5 = ["what do you control"]
r5 = [
    pyglet.resource.media("responses/my_duties.wav", streaming=False),
]

q6 = ["Sally"]
r6 = [
    pyglet.resource.media("responses/here_i'm.wav", streaming=False),
    pyglet.resource.media("responses/i'm_listening_you.wav", streaming=False),
    pyglet.resource.media("responses/tell_me.wav", streaming=False),
    pyglet.resource.media("responses/what_can_i_help_you_with.wav", streaming=False),
    pyglet.resource.media("responses/yes_sir.wav", streaming=False)
]

q7 = ["turn on the lights", "turn off the lights", "turn on TV", "turn off TV", "play music", "stop music", "supervise the house", "open the doors", "close the doors",
      "open the windows", "close the windows", "shut down", "turn on the car", "turn off the car"
]

r7 = [
    pyglet.resource.media("responses/agreed.wav", streaming=False),
    pyglet.resource.media("responses/excellent.wav", streaming=False),
    pyglet.resource.media("responses/good_idea.wav", streaming=False),
    pyglet.resource.media("responses/i_can_do_that.wav", streaming=False),
    pyglet.resource.media("responses/i'll_do_at_once.wav", streaming=False),
    pyglet.resource.media("responses/let_me_check.wav", streaming=False),
    pyglet.resource.media("responses/of_course.wav", streaming=False),
    pyglet.resource.media("responses/yes_sir.wav", streaming=False),
]


def to_response (text):
    print(text)
    for q in q1:
        if (text == q):
            player.queue(r1[randint(0, r1.__len__()-1)])
            player.play()
            return

    for q in q2:
        if (text == q):
            player.queue(r2[randint(0, r2.__len__()-1)])
            player.play()
            return
        
    for q in q3:
        if (text == q):
            player.queue(r3[randint(0, r3.__len__()-1)])
            player.play()
            return
        
    for q in q4:
        if (text == q):
            player.queue(r4[randint(0, r4.__len__()-1)])
            player.play()
            return

    for q in q5:
        if (text == q):
            player.queue(r5[randint(0, r5.__len__()-1)])
            player.play()
            return
        
    for q in q6:
        if (text == q):
            player.queue(r6[randint(0, r6.__len__()-1)])
            player.play()
            return

    for q in q7:
        if (text == q):
            player.queue(r7[randint(0, r7.__len__()-1)])
            player.play()
            return        

    player.queue(r0[randint(0, r0.__len__()-1)])
    player.play()
    return        
        
def to_request():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        text = ""
        print("I'm listening")
        audio = r.listen(source)
     
        try:
            text = r.recognize_google(audio)
            to_response (text)
        except sr.UnknownValueError:
            to_response ("")
        except sr.RequestError as e:
            print("I Could not request results from Speech Recognition service; {0}".format(e))

            
if __name__=="__main__":
    while (True):
        print "s). To speak\nq). To quit\n"
        i = raw_input()
        if i=="s":
            to_request ();
        elif i=="q":
            break
        
