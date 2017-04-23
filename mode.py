# -*- coding: utf-8 -*-
import pyglet
from random import randint
import speech_recognition as sr

"""English command"""
class English:
    q0 = [""]
    r0 = [
        pyglet.resource.media("responses/english/i_could_not_understand_you.wav", streaming=False),
    ]

    q1 = ["who are you", "what is your name"]
    r1 = [
        pyglet.resource.media("responses/english/i'm_sally.wav", streaming=False),
        pyglet.resource.media("responses/english/my_name_is_sally.wav", streaming=False)
    ]

    q2 = ["what do you do", "what is your purpose"]
    r2 = [
        pyglet.resource.media("responses/english/i'm_speech_control.wav", streaming=False),
        pyglet.resource.media("responses/english/my_purpose_is_supervice_my_master's_house.wav", streaming=False),
        pyglet.resource.media("responses/english/my_purpose_is_to_take_care_of_my_master's_house.wav", streaming=False),
        pyglet.resource.media("responses/english/i_control_the_security_and_the_conford_of_my_master's_house.wav", streaming=False)
    ]

    q3 = ["who is your creator", "who is your master"]
    r3 = [
        pyglet.resource.media("responses/english/my_creator_is_mr_caceres.wav", streaming=False),
    ]

    q4 = ["can you count", "can you speak", "can you control"]
    r4 = [
        pyglet.resource.media("responses/english/i_can_do_that.wav", streaming=False),
        pyglet.resource.media("responses/english/yes_i_can.wav", streaming=False),
        pyglet.resource.media("responses/english/yes_i_can_do_it.wav", streaming=False)
    ]

    q5 = ["what do you control"]
    r5 = [
        pyglet.resource.media("responses/english/my_duties.wav", streaming=False),
    ]

    q6 = ["sally"]
    r6 = [
        pyglet.resource.media("responses/english/here_i'm.wav", streaming=False),
        pyglet.resource.media("responses/english/i'm_listening_you.wav", streaming=False),
        pyglet.resource.media("responses/english/tell_me.wav", streaming=False),
        pyglet.resource.media("responses/english/what_can_i_help_you_with.wav", streaming=False),
        pyglet.resource.media("responses/english/yes_sir.wav", streaming=False)
    ]

    q7 = ["turn on the lights", "turn off the lights", "turn on TV", "turn off TV", "play music", "stop music", "supervise the house", "open the doors", "close the doors",
        "open the windows", "close the windows", "shut down", "turn on the car", "turn off the car"
    ]

    r7 = [
        pyglet.resource.media("responses/english/agreed.wav", streaming=False),
        pyglet.resource.media("responses/english/excellent.wav", streaming=False),
        pyglet.resource.media("responses/english/good_idea.wav", streaming=False),
        pyglet.resource.media("responses/english/i_can_do_that.wav", streaming=False),
        pyglet.resource.media("responses/english/i'll_do_at_once.wav", streaming=False),
        pyglet.resource.media("responses/english/let_me_check.wav", streaming=False),
        pyglet.resource.media("responses/english/of_course.wav", streaming=False),
        pyglet.resource.media("responses/english/yes_sir.wav", streaming=False),
    ]
    
    player = pyglet.media.Player()

    def to_response (self, text):
        print(text)
        for q in self.q1:
            if (text == q):
                self.player.queue(self.r1[randint(0, self.r1.__len__()-1)])
                self.player.play()
                return

        for q in self.q2:
            if (text == q):
                self.player.queue(self.r2[randint(0, self.r2.__len__()-1)])
                self.player.play()
                return
        
        for q in self.q3:
            if (text == q):
                self.player.queue(self.r3[randint(0, self.r3.__len__()-1)])
                self.player.play()
                return
        
        for q in self.q4:
            if (text == q):
                self.player.queue(self.r4[randint(0, self.r4.__len__()-1)])
                self.player.play()
                return

        for q in self.q5:
            if (text == q):
                self.player.queue(self.r5[randint(0, self.r5.__len__()-1)])
                self.player.play()
                return
        
        for q in self.q6:
            if (text == q):
                self.player.queue(self.r6[randint(0, self.r6.__len__()-1)])
                self.player.play()
                return

        for q in self.q7:
            if (text == q):
                self.player.queue(self.r7[randint(0, self.r7.__len__()-1)])
                self.player.play()
                return        

        self.player.queue(self.r0[randint(0, self.r0.__len__()-1)])
        self.player.play()
        return        
        
    def to_request(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            text = ""
            print("I'm listening")
            audio = r.listen(source)
     
            try:
                text = r.recognize_google(audio)
                self.to_response (text.lower())
            except sr.UnknownValueError:
                self.to_response ("")
            except sr.RequestError as e:
                print("I Could not request results from Speech Recognition service; {0}".format(e))
                


"""Comandos de voz en español"""                
class Spanish:
    q0 = [""]
    r0 = [
        pyglet.resource.media("responses/spanish/no_puedo_entenderte.wav", streaming=False),
    ]

    q1 = [u"quién eres", u"cuál es tu nombre"]
    r1 = [
        pyglet.resource.media("responses/spanish/soy_sally.wav", streaming=False),
        pyglet.resource.media("responses/spanish/mi_nombre_es_sally.wav", streaming=False)
    ]

    q2 = [u"qué haces", u"cuál es tu propósito"]
    r2 = [
        pyglet.resource.media("responses/spanish/soy_un_programa_de_control_por_voz.wav", streaming=False),
        pyglet.resource.media("responses/spanish/mi_proposito_es_supervisar_la_casa_de_mi_amo.wav", streaming=False),
        pyglet.resource.media("responses/spanish/mi_proposito_es_cuidar_la_casa_de_mi_amo.wav", streaming=False),
        pyglet.resource.media("responses/spanish/yo_controlo_la_seguridad_y_el_confor_de_la_casa_de_mi_amo.wav", streaming=False)
    ]

    q3 = [u"quién es tu creador", u"quién es tu amo"]
    r3 = [
        pyglet.resource.media("responses/spanish/mi_creador_es_jose_luis_caceres.wav", streaming=False),
    ]

    q4 = [u"puedes contar", u"puedes hablar", u"puedes controlar"]
    r4 = [
        pyglet.resource.media("responses/spanish/puedo_hacer_eso.wav", streaming=False),
        pyglet.resource.media("responses/spanish/si_puedo_hacerlo.wav", streaming=False),
        pyglet.resource.media("responses/spanish/si_puedo.wav", streaming=False)
    ]

    q5 = [u"que controlas"]
    r5 = [
        pyglet.resource.media("responses/spanish/mis_habilidades.wav", streaming=False),
    ]

    q6 = [u"salí"]
    r6 = [
        pyglet.resource.media("responses/spanish/aqui_estoy.wav", streaming=False),
        pyglet.resource.media("responses/spanish/estoy_escuchandote.wav", streaming=False),
        pyglet.resource.media("responses/spanish/dime.wav", streaming=False),
        pyglet.resource.media("responses/spanish/en_que_puedo_ayudarte.wav", streaming=False),
        pyglet.resource.media("responses/spanish/si_señor.wav", streaming=False)
    ]

    q7 = [u"enciende las luces", u"apaga las luces", u"apaga la tv", u"enciende la tv", u"pon la música", u"para la música", u"supervisa la casa", u"abre la puerta", u"cierra la puerta",
        u"abre la ventana", u"cierra la ventana",  u"enciende el auto", u"apaga el auto"
    ]

    r7 = [
        pyglet.resource.media("responses/spanish/entendido.wav", streaming=False),
        pyglet.resource.media("responses/spanish/excelente.wav", streaming=False),
        pyglet.resource.media("responses/spanish/buena_idea.wav", streaming=False),
        pyglet.resource.media("responses/spanish/puedo_hacer_eso.wav", streaming=False),
        pyglet.resource.media("responses/spanish/lo_hare_enseguida.wav", streaming=False),
        pyglet.resource.media("responses/spanish/permiteme_revisar.wav", streaming=False),
        pyglet.resource.media("responses/spanish/de_acuerdo.wav", streaming=False),
        pyglet.resource.media("responses/spanish/si_señor.wav", streaming=False),
    ]
    
    q8 = [u"quién es karen"]
    r8 = [
        pyglet.resource.media("responses/spanish/karen.wav", streaming=False),
    ]
    
    q9 = [u"sal y apaga te",]
    r9 = [
        pyglet.resource.media("responses/spanish/si_señor.wav", streaming=False),
        pyglet.resource.media("responses/spanish/lo_hare_enseguida.wav", streaming=False),
        pyglet.resource.media("responses/spanish/entendido.wav", streaming=False),
        pyglet.resource.media("responses/spanish/te_veo_luego.wav", streaming=False)
    ]
    
    player = pyglet.media.Player()

    def to_response (self, text):
        print(text)
        for q in self.q1:
            if (text == q):
                self.player.queue(self.r1[randint(0, self.r1.__len__()-1)])
                self.player.play()
                return

        for q in self.q2:
            if (text == q):
                self.player.queue(self.r2[randint(0, self.r2.__len__()-1)])
                self.player.play()
                return
        
        for q in self.q3:
            if (text == q):
                self.player.queue(self.r3[randint(0, self.r3.__len__()-1)])
                self.player.play()
                return
        
        for q in self.q4:
            if (text == q):
                self.player.queue(self.r4[randint(0, self.r4.__len__()-1)])
                self.player.play()
                return

        for q in self.q5:
            if (text == q):
                self.player.queue(self.r5[randint(0, self.r5.__len__()-1)])
                self.player.play()
                return
        
        for q in self.q6:
            if (text == q):
                self.player.queue(self.r6[randint(0, self.r6.__len__()-1)])
                self.player.play()
                return

        for q in self.q7:
            if (text == q):
                self.player.queue(self.r7[randint(0, self.r7.__len__()-1)])
                self.player.play()
                return     
            
        for q in self.q8:
            if (text == q):
                self.player.queue(self.r7[randint(0, self.r7.__len__()-1)])
                self.player.play()
                return
            
        for q in self.q9:
            if (text == q):
                self.player.queue(self.r7[randint(0, self.r7.__len__()-1)])
                self.player.play()
                return    

        self.player.queue(self.r0[randint(0, self.r0.__len__()-1)])
        self.player.play()
        return        
        
    def to_request(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            text = ""
            print("Estoy escuchando")
            audio = r.listen(source)
     
            try:
                text = r.recognize_google(audio, language='es-ES')
                self.to_response (text.lower())
            except sr.UnknownValueError:
                self.to_response ("")
            except sr.RequestError as e:
                print("I Could not request results from Speech Recognition service; {0}".format(e))
