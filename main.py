from progressbar33 import ProgressBar
from time import sleep
from os import system
from requets import get
from random import randint

class RandomMAC():
	def get():
		mac = [ 0x00, 0x16, 0x3e,
		randint(0x00, 0x7f),
        randint(0x00, 0xff),
        randint(0x00, 0xff) ]
		return ':'.join(map(lambda x: "%02x" % x, mac))


class BruteforceMAC():
	def enter():
		tmp_mac = RandomMAC.get()
		system("sudo ifconfig en0 ether {0}".format(tmp_mac))
		with open('macs.log', 'w') as macs_log:
			macs_log.writelines(tmp_mac)
		return tmp_mac


	def check(tmp_mac):
		r = get("http://blog.alexdless.ru/")
		count_str = "alexdless - Atom"
		if count_str in r.text():
			with open('success.log', 'w') as success:
				success.writelines(tmp_mac)



value = int(input('value = '))
pbar = ProgressBar(maxval=value)
pbar.start()


for i in range(value):
	tmp_mac = BruteforceMAC.enter()
	BruteforceMAC.check(tmp_mac)
	pbar.update(i)

pbar.finish()
