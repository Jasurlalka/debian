from pywebio.input import input
from pywebio.output import put_text
from requests import put

i = "instagram.com"
def main():
    user = input("Введите ссылку：")
    if i in user:
        put_text('Сайт одобрен ✔').style('color: #3e8a12; font-size: 38px; text-align: center; font-family: "Gill Sans", sans-serif;font-weight: 600; padding-top:30%' )
    else:
        put_text('Сайт не одобрен ❌').style('color: #F03A17FF; font-size: 38px; text-align: center; font-family: "Gill Sans", sans-serif;font-weight: 600; padding-top:30%' )

if __name__ == '__main__':
    main()