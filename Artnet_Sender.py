import stupidArtnet

TARGET_IP = "1.0.0.124"  # Server IP address, put in the IP adresse you want to send to
TARGET_UNIVERSE = 1      # Universe you want to send

sender = stupidArtnet.StupidArtnet(TARGET_IP, TARGET_UNIVERSE)   
sender.start()

def send_data_to_server(data):
    sender.set(data)
    #sender.set_single_value(1, 255) # Just for testing, remove later

listen_server = stupidArtnet.StupidArtnetServer()

universe_0_listener = listen_server.register_listener(
universe=0,      #listen to universe 0
callback_function=send_data_to_server  # Function that sends data automatic when recieving Artnet
)

while True:
    sender.see_buffer()   #Shows Artnet values
    
sender.stop()
print("done")  #Just to se if program is done
