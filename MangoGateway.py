#!/usr/bin/python3

import requests, json

cc_url='http://mango.mirzaee.info/API'                              # Mango cloud computation url

def mangoenc(devmode=False, **arguments):                           # process and send data
    
    if (arguments['mode']=='keyless'):
        # Keyless mode
        try:

            assert 2<=len(arguments)<=3                             # assert validity of number of args 
            if type(devmode) is not bool or type(arguments['text']) is not str:
                raise TypeError('please check the type of arguments(text:str, devmode:boolean)')
            encreption = requests.post(cc_url+'/keylessenc.php',    # send data to compute
                            data={
                                'devmode': devmode,
                                'text': arguments['text']
                                })
            return encreption.text                                   # return jsoned result as a dictionary         

        except AssertionError as er:
            return "MANGO error: number of arguments must be between 2 and 3"
        except KeyError as er:
            return "MANGO error: key {} is required".format(er)
        except TypeError as er:
            return "MANGO error: invalid type: {}".format(er)
        except BaseException as er:
            return "MANGO error: {}".format(repr(er))


    elif (arguments['mode']=="ordinary"):
        # ordinary mode
        pass

    elif (arguments['mode']=="extreme"):
        # extreme mode
        pass

    elif (arguments['mode']=="illusion"):
        pass


    else:
        return "MANGO error: unknown mode: {}".format(arguments['mode'])


def mangodec():
    pass



print(mangoenc(mode="keyless", text="5"))