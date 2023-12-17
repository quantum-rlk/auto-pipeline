
def echo(_msg:str) -> int:
    if _msg == 'calling pipeline job .....':
        print('\n')
        print(_msg)
        return 1
    return 0

echo('calling pipeline job .....')
