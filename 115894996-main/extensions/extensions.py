filename = input("File name: ")
updated_filename =filename.lower()

if '.gif' in updated_filename:
    print("image/gif")

elif '.jpg' in updated_filename:
    print("image/jpeg")

elif '.jpeg' in updated_filename:
    print("image/jpeg")

elif '.png' in updated_filename:
    print("image/png")

elif '.pdf' in updated_filename:
    print("application/pdf")

elif '.txt' in updated_filename:
    print("text/plain")

elif '.zip' in updated_filename:
    print("application/zip")

else:
    print("application/octet-stream")

