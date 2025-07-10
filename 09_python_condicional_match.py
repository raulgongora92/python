htpp_status = 404

if htpp_status == 200 or htpp_status == 201:
    print('Success')
elif htpp_status == 400:
    print('Bad Request')
elif htpp_status == 404:
    print('Not Found')
elif htpp_status == 500 or htpp_status == 501:
    print('Server Error')
else:
    print('Unknown Error')


match htpp_status:
    case 200 | 201:
        print('Success')
    case 400:
        print('Bad Request')
    case 404:
        print('Not Found')
    case 500 | 501:
        print('Server Error')
    case _:
        print('Unknown Error')
