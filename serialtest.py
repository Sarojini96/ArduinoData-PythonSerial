import serial

#sets up serial connection (make sure baud rate is correct - matches Arduino)
ser = serial.Serial('com3', 9600) 

while(True):
 #reads until it gets a carriage return. MAKE SURE THERE IS A CARRIAGE RETURN OR IT READS FOREVER
 data = ser.readline()
 #splits string into a list at the tabs
 #sep = data.split() 
 print (data)
 
 #create a text document and update the arduino data 
 file = open("records.txt", "a")
 file.writelines("sensor data"+ str(data))
 file.close()
