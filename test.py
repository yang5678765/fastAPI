import requests

def fetch_api(url, data):
    response = requests.post(url, json=data)
    return response.status_code, response.json()


def main():
    code, res_body = fetch_api('http://127.0.0.1:8000/create_account', {'username':'allDigit', 'password':'12345678'})
    print('allDigit', code, res_body)


    code, res_body = fetch_api('http://127.0.0.1:8000/create_account', {'username':'allUpper', 'password':'ABCDEFGH'})
    print('allUpper', code, res_body)


    code, res_body = fetch_api('http://127.0.0.1:8000/create_account', {'username':'allLower', 'password':'abcdefgh'})
    print('allLower', code, res_body)


    code, res_body = fetch_api('http://127.0.0.1:8000/create_account', {'username':'upperLower', 'password':'efghABCD'})
    print('upperLower', code, res_body)

    code, res_body = fetch_api('http://127.0.0.1:8000/create_account', {'username':'upperdigit', 'password':'5678ABCD'})
    print('upperdigit', code, res_body)


    code, res_body = fetch_api('http://127.0.0.1:8000/create_account', {'username':'lowerdigit', 'password':'efgh1234'})
    print('lowerdigit', code, res_body)


    code, res_body = fetch_api('http://127.0.0.1:8000/create_account', {'username':'allmixed', 'password':'efgh123ABCD'})
    print('allmixed', code, res_body)

    
    code, res_body = fetch_api('http://127.0.0.1:8000/create_account', {'username':'allmixed', 'password':'q12eqr2eEW'})
    print('allmixed', code, res_body)
    

if __name__=='__main__':
    main()