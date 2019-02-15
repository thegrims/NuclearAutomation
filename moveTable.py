from newportESP import ESP 
esp = ESP('COM4') # open communication with controller 

axis = str.encode('1')
stage = esp.axis(axis)   # open axis no 1

my_str_as_bytes = str.encode('1.2')
#print(type(my_str_as_bytes))

#stage.move_to(my_str_as_bytes)    # move to position 1.2 mm 
#stage.wait()          # wait until motion is finished.
