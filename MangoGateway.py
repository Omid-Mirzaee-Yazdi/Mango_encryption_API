#!/usr/bin/python3

import requests, json

def mangoenc(**arguments): #process and send data

    if (arguments['mode']=="keyless"):
        try:
            assert 2<=len(arguments)<=3  #assert validity of number of args 

            if "devmode" not in arguments.keys():
                arguments['devmode']=False

            if type(arguments['text']) is not str or type(arguments['devmode']) is not bool:
                raise TypeError('please check the type of arguments(text:str, devmode:boolean)')
                
            """
            response = requests.post('#',  #send data to cloud to compute
                            data={
                                'devmode': arguments['devmode'],
                                'text': arguments['text']
                                })
            return json.loads(r.text) #return jsoned result
            """
            return True 

        except AssertionError as er:
            return "MANGO error: number of arguments must be between 2 and 3"
        except KeyError as er:
            return "MANGO error: key {} is required".format(er)
        except TypeError as er:
            return "MANGO error: invalid type: {}".format(er)
        except BaseException as er:
            return "MANGO error: {}".format(repr(er))

        print('keyless activated')

    elif (arguments['mode']=="ordinary" and len(arguments)>=3):
        pass

    elif (arguments['mode']=="extreme" and len(arguments)>=4):
        pass

    elif (arguments['mode']=="illusion" and len(arguments)>=4):
        pass

    else:
        return "MANGO error: unknown mode: {}".format(arguments['mode'])

def mangodec():
    pass


print(mangoenc(mode="keyless",tett="2", text="5"))