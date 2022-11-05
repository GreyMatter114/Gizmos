from boltiot import Bolt #import necessary libraries
import time #conf contains Bolt device id and API key, available from Bolt cloud dashboard
import process,sys
import Ser
DEVICE_ID="BOLT6552782"
API_KEY = "a2940742-fd9f-4256-a475-83f88916d07f"
mybolt = Bolt(API_KEY,DEVICE_ID) #Create bolt object
mybolt.serialBegin(9600)
d=['HIGH','LOW']
while True:
    try:
        inp=input("Enter choice: (y/n): ")
    except:
        sys.exit()
    if(inp.lower()=='y'):
        print("Speak now: \n")
        out=Ser.main()
        o=process.main(out)
        print(d[o])
        mybolt.digitalWrite('1',d[o])
        mybolt.digitalWrite('2',d[abs(1-o)])
        time.sleep(5)
        mybolt.digitalWrite('1','LOW')
        mybolt.digitalWrite('2','LOW')
    elif(inp.lower()=='n'):
        sys.exit()
    else:
        print("Invalid Input")
    time.sleep(2)