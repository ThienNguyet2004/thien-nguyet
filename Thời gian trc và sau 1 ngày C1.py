from datetime import datetime, timedelta

# Nhập ngày, tháng, năm 
day = int(input())
month = int(input())
year = int(input())

# Tạo đối tượng datetime từ ngày, tháng, năm
date = datetime(year, month, day)

# Tìm ngày hôm trước
yesterday = date - timedelta(days=1)

# Tìm ngày hôm sau
tomorrow = date + timedelta(days=1)

# In kết quả ra màn hình
print(yesterday.strftime("%d/%m/%Y"))
print(tomorrow.strftime("%d/%m/%Y"))