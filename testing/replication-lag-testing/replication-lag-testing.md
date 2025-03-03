```yaml
cat <<EOF > producer.sh
#!/bin/bash
BROKER="my-cluster-kafka-bootstrap.strimzi.svc:9092"
TOPIC="test-topic"

echo "Starting producer..."
while true; do
    echo "message-\$(date +%s)" |  /opt/kafka/bin/kafka-console-producer.sh --broker-list \$BROKER --topic \$TOPIC
    sleep 0.1
done
EOF

cat <<EOF > consumer.sh
#!/bin/bash
BROKER="my-cluster-kafka-bootstrap.strimzi.svc:9092"
TOPIC="test-topic"
GROUP="test-group"

/opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server \$BROKER --topic \$TOPIC --group \$GROUP --from-beginning
EOF


cat <<EOF > monitor_lag.sh
#!/bin/bash
BROKER="my-cluster-kafka-bootstrap.strimzi.svc:9092"
GROUP="test-group"

while true; do
    /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server \$BROKER --group \$GROUP --describe
    sleep 2
done
EOF
```