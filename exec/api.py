import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

cradentials = ServiceAccountCredentials.from_json_keyfile_name('exec/sheetProjekt-32bb973be610.json', scope)

#i didnt add credentials file to github becouse is private for me

risation = gspread.authorize(cradentials)

worksheet = risation.open('fakeid').sheet1


def inputid(name, surname, pes, email):
    worksheet.append_row([name, surname, pes, email])
    print("fakeID has been added to sheet")


def showids():
    sheets = worksheet.get_all_records()
    j = 1
    for i in sheets:
        print(j, i)
        j += 1


def  delid(row):
    worksheet.delete_row(row + 1)
    print("successful removal of id")
