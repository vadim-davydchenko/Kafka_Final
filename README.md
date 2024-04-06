### Configuring a kafka cluster using the Kraft protocol, raising a Web UI for it and writing your own consumer

**1. On each machine(final-1,final-2,final-3) configure kafka in kraft mode by changing `/opt/kafka/config/kraft/server.properties`**

```
node.id=1
listeners=PLAINTEXT://final1:9092,CONTROLLER://final1:9093
advertised.listeners=PLAINTEXT://final1:9092
listener.security.protocol.map=PLAINTEXT:PLAINTEXT,CONTROLLER:PLAINTEXT
controller.listener.names=CONTROLLER
log.dirs=/tmp/kraft-combined-logs
```

**2. Generate the uuid for the cluster on one of the machines and distribute it to the rest**

`bin/kafka-storage.sh random-uuid`

`bin/kafka-storage.sh format -t <uuid> -c config/kraft/server1.properties`

Run Kafka Server

`bin/kafka-server-start.sh config/kraft/server.properties`

**3. Сreate topic kraft-test on 3 partition with factor replication 3**

`bin/kafka-topics.sh --create --topic kraft-test --partitions 3 --replication-factor 3 --bootstrap-server final1:9092`

**4. On the second machine(final-2), run Kafka UI in the docker container using the compose file along the path `/opt/kafka/docker/ui` and pre-register the IP of all cluster machines in it**

`docker-compose up -d`

**5. On the 3rd node(final-3) in the directory `/opt/python` add script `consumer.py `so that it reads messages from all three kafka instances from the `kraft-test` topic**

`pip3 install --upgrade pip setuptools && pip3 install avro && pip3 install confluent_kafka`

`python3 consumer.py`
