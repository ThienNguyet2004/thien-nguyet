def Xau_doi_xung(str):
    """
    :param str: string
    :return: True if symmetrical, False if not symmetrical
    """

    if str[::-1] == str:
        return True
    return False


# Nhap du lieu
str = input("Nhap vao xau bat ky: ")
if Xau_doi_xung(str) is True:
    print("Xau tren doi xung!")
else:
    print("Xau tren khong doi xung!")