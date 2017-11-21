#!usr/bin/python

from Scripts_store import Ask_Mode as ask, ServerMode as server, ClientMode as client
if __name__ == '__main__':
	storeobj=ask.Ask_Mode_Option()
	if storeobj==0:
		client.ClientMode(className='Python Chatting [Client Mode]').mainloop()
		pass
	elif storeobj==1:
		server.ServerMode(className='Python Chatting [Server Mode]').mainloop()
		pass
	else:
		pass