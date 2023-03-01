import stupidArtnet
import time

TARGET_IP = "1.0.0.124"  # Server IP address
TARGET_UNIVERSE = 1


sender = stupidArtnet.StupidArtnet(TARGET_IP, TARGET_UNIVERSE)
sender.start()

def send_data_to_server(data):
    sender.set(data)
    sender.show()
    #sender.set_single_value(1, 255) # Just for testing, remove later

x = 1

listen_server = stupidArtnet.StupidArtnetServer()

universe_0_listener = listen_server.register_listener(
universe=0,
callback_function=send_data_to_server  # Funksjon som kjøres automatisk når det mottas ArtNet
)

while True:
    sender.see_buffer()
    
sender.stop()
print("done")