from PIL import Image  
  
t=0
i=0
while(i<10):
    if(t==0):
        im = Image.open(r"C:\Users\anuttam\Desktop\IMG20171217150312.jpg")  
        im.show()
        t=1
        i=i+1 
    else:
        im = Image.open(r"C:\Users\anuttam\Desktop\IMG20171217150311.jpg")
        im.show()
        t=0
        i=i+1