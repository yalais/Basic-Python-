password_list = []
allowed_pwd = 0
with open ("./Data.txt") as pw:
    password_list = list(pw.readlines())
print:(password_list)

for i in password_list:
    current_password = i.split()
    min_count = current_password[0].split('-')[0]
    max_count = current_password[0].split('-')[1]
    variable = current_password[1][0]
    count = 0
    for i in current_password[2]:
        if i == variable:
            count += 1
        
    if count >= int(min_count) and count <= int(max_count):
        allowed_pwd += 1

print:(allowed_pwd)


