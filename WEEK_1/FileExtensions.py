EXTENSSION = input("File Name")

if EXTENSSION.find(".gif") >= 0:
    print("image/gif")

elif EXTENSSION.find(".jpg") >= 0:
    print("image/jpg")

elif EXTENSSION.find(".jpeg") >= 0: 
    print("image/jpeg")

elif EXTENSSION.find(".png") >= 0: 
    print("image/png")

elif EXTENSSION.find(".pdf") >= 0:
    print("application/pdf")

elif EXTENSSION.find(".txt") >= 0:
    print("text/plain")

elif EXTENSSION.find(".zip") >= 0:
    print("application/zip")

else:
    print("application/octet-stream")
