import redis
import json
from time import sleep
from random import randint

if __name__ == '__main__':
    r = redis.Redis(host='queue', port=6379, db=0)
    print('aguardando mensagens...')
    while True:
        mensagem = json.loads(r.blpop('sender')[1])
        # simulando o envio do email....
        print('Mandando a mensagem:', mensagem['assunto'])
        sleep(randint(5, 15))
        print('Mensagem', mensagem['assunto'], 'enviada')