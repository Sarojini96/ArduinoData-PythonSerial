import serial
#finds COM port that the Arduino is on (assumes only one Arduino is connected)

ser = serial.Serial('com3', 9600) #sets up serial connection (make sure baud rate is correct - matches Arduino)

data = ser.readline()    #reads until it gets a carriage return. MAKE SURE THERE IS A CARRIAGE RETURN OR IT READS FOREVER
 #      sep = data.split()      #splits string into a list at the tabs
print (data)
file = open("records.txt", "a")
file.writelines("sensor data"+ str(data))
file.close()
