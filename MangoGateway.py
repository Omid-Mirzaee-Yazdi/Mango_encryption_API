#!/usr/bin/python3

import requests, json

cc_url='http://mango.mirzaee.info/API'                              # Mango cloud computation url

def mangoenc(devmode=False, **arguments):                           
    # encryption function

    if (arguments['mode']=='keyless'):
        # Keyless mode encryption
        try:
            assert 2<=len(arguments)<=3                             # assert validity of number of args 
            if type(devmode) is not bool or type(arguments['text']) is not str:
                raise TypeError('please check the type of arguments(text:str, devmode:boolean(optional))')
            print('sending data to the server...')
            encryption = requests.post(cc_url+'/keylessenc.php',    # send data to compute
                            data={
                                'devmode': devmode,
                                'text': arguments['text'],
                                })
            print('sent!')
            return json.loads(encryption.text)                      # return jsoned result as a dictionary         

        except AssertionError as er:
            return "MANGO error: number of arguments must be between 2 and 3"
        except KeyError as er:
            return "MANGO error: key {} is required".format(er)
        except TypeError as er:
            return "MANGO error: invalid type: {}".format(er)
        except BaseException as er:
            return "MANGO error: {}".format(repr(er))


    elif (arguments['mode']=="ordinary"):
        # ordinary mode encryption
        try:
            assert 3<=len(arguments)<=4                             # assert validity of number of args 
            if type(devmode) is not bool or type(arguments['text']) is not str or type(arguments['initkey']) is not int:
                raise TypeError('please check the type of arguments(text:str, initkey:int, devmode:boolean(optional))')
            print('sending data to the server...')
            encryption = requests.post(cc_url+'/ordinaryenc.php',    # send data to compute
                            data={
                                'devmode': devmode,
                                'text': arguments['text'],
                                'initkey': arguments['initkey'],
                                })
            print('sent!')
            return json.loads(encryption.text)                       # return jsoned result as a dictionary         

        except AssertionError as er:
            return "MANGO error: number of arguments must be between 2 and 3"
        except KeyError as er:
            return "MANGO error: key {} is required".format(er)
        except TypeError as er:
            return "MANGO error: invalid type: {}".format(er)
        except BaseException as er:
            return "MANGO error: {}".format(repr(er))


    elif (arguments['mode']=="extreme"):
        # extreme mode encryption
        try:
            assert 4<=len(arguments)<=5                             # assert validity of number of args 
            if type(devmode) is not bool or type(arguments['text']) is not str or type(arguments['comptext']) is not str or type(arguments['initkey']) is not int:
                raise TypeError('please check the type of arguments(text:str, initkey:int, comptext:str, devmode:boolean(optional))')
            print('sending data to the server...')
            encryption = requests.post(cc_url+'/extremeenc.php',    # send data to compute
                            data={
                                'devmode': devmode,
                                'text': arguments['text'],
                                'initkey': arguments['initkey'],
                                'comptext': arguments['comptext'],
                                })
            print('sent!')
            return json.loads(encryption.text)                       # return jsoned result as a dictionary         

        except AssertionError as er:
            return "MANGO error: number of arguments must be between 2 and 3"
        except KeyError as er:
            return "MANGO error: key {} is required".format(er)
        except TypeError as er:
            return "MANGO error: invalid type: {}".format(er)
        except BaseException as er:
            return "MANGO error: {}".format(repr(er))


    elif (arguments['mode']=="illusion"):
        # illusion mode encryption
        try:
            assert 4<=len(arguments)<=5                             # assert validity of number of args 
            if type(devmode) is not bool or type(arguments['text']) is not str or type(arguments['sectext']) is not str or type(arguments['initkey']) is not int:
                raise TypeError('please check the type of arguments(text:str, initkey:int, sectext:str, devmode:boolean(optional))')
            print('sending data to the server...')
            encryption = requests.post(cc_url+'/illusionenc.php',    # send data to compute
                            data={
                                'devmode': devmode,
                                'text': arguments['text'],
                                'sectext': arguments['sectext'],
                                'initkey': arguments['initkey'],
                                })
            print('sent!')           
            return json.loads(encryption.text)                      # return jsoned result as a dictionary         

        except AssertionError as er:
            return "MANGO error: number of arguments must be between 2 and 3"
        except KeyError as er:
            return "MANGO error: key {} is required".format(er)
        except TypeError as er:
            return "MANGO error: invalid type: {}".format(er)
        except BaseException as er:
            return "MANGO error: {}".format(repr(er))


    else:
        return "MANGO error: unknown mode: {}".format(arguments['mode'])



def mangodec(devmode=False, **arguments):                                        
     # decryption function

    if (arguments['mode']=='keyless'):
        # Keyless mode decryption
        try:
            assert 2<=len(arguments)<=3                             # assert validity of number of args 
            if type(devmode) is not bool or type(arguments['text']) is not str:
                raise TypeError('please check the type of arguments(text:str, devmode:boolean(optional))')
            print('sending data to the server...')
            decryption = requests.post(cc_url+'/keylessdec.php',    # send data to compute
                            data={
                                'devmode': devmode,
                                'text': arguments['text'],
                                })
            print('sent!')
            return json.loads(decryption.text)                       # return jsoned result as a dictionary         

        except AssertionError as er:
            return "MANGO error: number of arguments must be between 2 and 3"
        except KeyError as er:
            return "MANGO error: key {} is required".format(er)
        except TypeError as er:
            return "MANGO error: invalid type: {}".format(er)
        except BaseException as er:
            return "MANGO error: {}".format(repr(er))

            
    elif (arguments['mode']=="ordinary"):
        # ordinary mode decryption
        try:
            assert 3<=len(arguments)<=4                             # assert validity of number of args 
            if type(devmode) is not bool or type(arguments['text']) is not str or type(arguments['deckey']) is not str:
                raise TypeError('please check the type of arguments(text:str, deckey:str, devmode:boolean(optional))')
            print('sending data to the server...')
            decryption = requests.post(cc_url+'/ordinarydec.php',    # send data to compute
                            data={
                                'devmode': devmode,
                                'text': arguments['text'],
                                'deckey': arguments['deckey'],
                                })
            print('sent!')
            return json.loads(decryption.text)                        # return jsoned result as a dictionary         

        except AssertionError as er:
            return "MANGO error: number of arguments must be between 2 and 3"
        except KeyError as er:
            return "MANGO error: key {} is required".format(er)
        except TypeError as er:
            return "MANGO error: invalid type: {}".format(er)
        except BaseException as er:
            return "MANGO error: {}".format(repr(er))


    elif (arguments['mode']=="extreme"):
        # extreme mode decryption
        try:
            assert 3<=len(arguments)<4                             # assert validity of number of args 
            if type(devmode) is not bool or type(arguments['text']) is not str or type(arguments['deckey']) is not str:
                raise TypeError('please check the type of arguments(text:str, deckey:str, devmode:boolean(optional))')
            print('sending data to the server...')
            decryption = requests.post(cc_url+'/extremedec.php',    # send data to compute
                            data={
                                'devmode': devmode,
                                'text': arguments['text'],
                                'deckey': arguments['deckey'],
                                })
            print('sent!')
            return json.loads(decryption.text)                      # return jsoned result as a dictionary         

        except AssertionError as er:
            return "MANGO error: number of arguments must be between 2 and 3"
        except KeyError as er:
            return "MANGO error: key {} is required".format(er)
        except TypeError as er:
            return "MANGO error: invalid type: {}".format(er)
        except BaseException as er:
            return "MANGO error: {}".format(repr(er))

    elif (arguments['mode']=="illusion"):
         # illusion mode decryption
        try:
            assert 3<=len(arguments)<=4                             # assert validity of number of args 
            if type(devmode) is not bool or type(arguments['text']) is not str or type(arguments['deckey']) is not str:
                raise TypeError('please check the type of arguments(text:str, deckey:str, devmode:boolean(optional))')
            print('sending data to the server...')
            decryption = requests.post(cc_url+'/illusiondec.php',    # send data to compute
                            data={
                                'devmode': devmode,
                                'text': arguments['text'],
                                'deckey': arguments['deckey'],
                                })
            print('sent!')
            return json.loads(decryption.text)                      # return jsoned result as a dictionary         

        except AssertionError as er:
            return "MANGO error: number of arguments must be between 2 and 3"
        except KeyError as er:
            return "MANGO error: key {} is required".format(er)
        except TypeError as er:
            return "MANGO error: invalid type: {}".format(er)
        except BaseException as er:
            return "MANGO error: {}".format(repr(er))
    else:
        return "MANGO error: unknown mode: {}".format(arguments['mode'])
