import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

cradentials = ServiceAccountCredentials.from_json_keyfile_name('exec/sheetProjekt-32bb973be610.json', scope)

risation = gspread.authorize(cradentials)

worksheet = risation.open('fakeid').sheet1


def inputid(name, surname, pes, email):
    worksheet.append_row([name, surname, pes, email])
    print("fakeID has been added to sheet")
    # worksheet.delete_row(3)
    # print(worksheet.get_all_records())