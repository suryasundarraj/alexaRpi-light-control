#Import the Modules Required
import RPi.GPIO as GPIO
import time
from pubnub import Pubnub

# Initialize the Pubnub Keys 
g_pub_key = "pub-c-913ab39c-d613-44b3-8622-2e56b8f5ea6d"
g_sub_key = "sub-c-8ad89b4e-a95e-11e5-a65d-02ee2ddab7fe"

LIGHT = 18
'''****************************************************************************************
Function Name 	:	init
Description		:	Initalize the pubnub keys and Starts Subscribing 
Parameters 		:	None
****************************************************************************************'''
def init():
	#Pubnub Initialization
	global pubnub
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(LIGHT,GPIO.OUT)
	GPIO.output(LIGHT, False) 
	pubnub = Pubnub(publish_key=g_pub_key,subscribe_key=g_sub_key)
	pubnub.subscribe(channels='alexaTrigger', callback=callback, error=callback, reconnect=reconnect, disconnect=disconnect)

'''****************************************************************************************
Function Name 	:	alexaControl
Description		:	Alexa Control, commands received and action performed  
Parameters 		:	controlCommand
****************************************************************************************'''
def alexaControl(controlCommand):
	if(controlCommand.has_key("trigger")):
		if(controlCommand["trigger"] == "light" and controlCommand["status"] == 1):
			GPIO.output(LIGHT, True) 
			print "light on successfully"
		else:
			GPIO.output(LIGHT, False) 
			print "light off"
	else:
		pass


'''****************************************************************************************
Function Name 	:	callback
Description		:	Waits for the message from the alexaTrigger channel
Parameters 		:	message - Sensor Status sent from the hardware
					channel - channel for the callback
****************************************************************************************'''
def callback(message, channel):
	if(message.has_key("requester")):
		alexaControl(message)
	else:
		pass

'''****************************************************************************************
Function Name 	:	error
Description		:	If error in the channel, prints the error
Parameters 		:	message - error message
****************************************************************************************'''
def error(message):
    print("ERROR : " + str(message))

'''****************************************************************************************
Function Name 	:	reconnect
Description		:	Responds if server connects with pubnub
Parameters 		:	message
****************************************************************************************'''
def reconnect(message):
    print("RECONNECTED")

'''****************************************************************************************
Function Name 	:	disconnect
Description		:	Responds if server disconnects from pubnub
Parameters 		:	message
****************************************************************************************'''
def disconnect(message):
    print("DISCONNECTED")

'''****************************************************************************************
Function Name 	:	__main__
Description		:	Conditional Stanza where the Script starts to run
Parameters 		:	None
****************************************************************************************'''
if __name__ == '__main__':
	#Initialize the Script
	init()

#End of the Script 
##*****************************************************************************************************##