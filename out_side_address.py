import urllib.request
import notification
import time 

def check_address():
	try: return urllib.request.urlopen('https://ident.me').read().decode('utf8')
	except Exception:
		time.sleep(60)
		return "0.0.0.0"
	
def notify(external_ip):
	return notification.schedule("Your external IP address has changed. Your current IP address is: %s" % external_ip,5,'digital:PhaserUp7',)

external_ip = check_address()

while True:
	if external_ip == check_address():
		time.sleep(30)
		continue
	elif external_ip != check_address():
		notify(external_ip)
		external_ip = check_address()
		
	

#external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

#print(external_ip)

#notification.schedule()

#notification.schedule("Your external IP adrress has changes. Your current IP address is: %s" % external_ip,5,'digital:PhaserUp7',)


