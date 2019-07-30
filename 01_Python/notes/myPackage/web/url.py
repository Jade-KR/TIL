def my_url(itemPerPage=10, **api):
    if api.get('key') == None and api.get('targetDt') == None:
        print('필수 요청변수가 누락되었습니다.')
        return
    if itemPerPage > 10:
        print('1~10까지의 값을 넣어주세요')
        return
    
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    base_url += f'itemPerPage={itemPerPage}&'
    for key, value in api.items():
        base_url += f'{key}={value}&'
    return(base_url)
