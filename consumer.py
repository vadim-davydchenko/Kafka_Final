from confluent_kafka import Consumer

c = Consumer({
'bootstrap.servers': 'final1:9092,final2:9092,final3:9092',
'group.id': 'kraft-test',
'auto.offset.reset': 'earliest'
})
c.subscribe(['kraft-test'])
for i in range(15):
    msg = c.poll(1.0)
    if msg is None:
        print(1)
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))
c.close()
