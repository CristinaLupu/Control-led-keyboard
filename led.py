import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
try:
	while(True):
		key=raw_input('O on, F off')
		if(key=='O'):
			print('O pressed')
			GPIO.output(12,1)
		elif(key=='F'):
			print('F pressed')
			GPIO.output(12,0)
		else:
			print('incorrect')

except KeyboardInterrupt:
	print('ctrl-c')
	GPIO.cleanup()

