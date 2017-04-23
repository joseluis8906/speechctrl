#!/usr/bin/env python
# -*- coding: utf-8 -*-
           
if __name__=="__main__":
    
    print "Lenguaje/Language"
    print "a). English\nb). Español\n"
    i = raw_input()
    if i=="a":
        from mode import English
        sally = English()
    elif i=="b":
        from mode import Spanish
        sally = Spanish()
    
    while (True):
        print "s). To speak\nq). To quit\n"
        i = raw_input()
        if i=="s":
            sally.to_request ();
        elif i=="q":
            break
        
