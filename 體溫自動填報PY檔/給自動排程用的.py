import infection as do

with open("./res/accountInformation.inf", "r") as file:
    s = file.readline().replace('\n', '').split(',')
    ok = do.upload_today(s[0], s[1])
    # print(s)

    with open("./res/record.txt", 'a') as file:
        if ok:
            file.write("OK : " + do.getToday_date() + '\n')
        else:
            file.write("FAIL : " + do.getToday_date() + '\n')
