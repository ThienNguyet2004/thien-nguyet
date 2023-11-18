s=input("nhap ho ten:")
i=s.find(" ")
ho=s[:i]
print(f"ho:{ho}")
j=s.rfind(" ")
ten=s[(j+1):]
print(f"ten:{ten}")
dem=s[(i+1):j]
print(f"dem:{dem}")