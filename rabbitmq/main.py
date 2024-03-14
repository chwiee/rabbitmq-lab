import pika

# Substitua 'usuario', 'senha', 'host' e 'porta' pelos seus valores reais
url = 'amqp://rmq_py:123@localhost:30000/'
params = pika.URLParameters(url)

connection = pika.BlockingConnection(params)
channel = connection.channel()

# Crie uma fila chamada 'hello'
channel.queue_declare(queue='queue1')

# Enviar uma mensagem para a fila
channel.basic_publish(exchange='',
                      routing_key='',
                      body='Olá, mundo!')

print(" [x] Enviada 'Olá, mundo!'")
connection.close()
