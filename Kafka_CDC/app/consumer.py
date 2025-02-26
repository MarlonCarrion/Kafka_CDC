from kafka import KafkaConsumer, TopicPartition


def main():
    try:
        consumer = KafkaConsumer(
            bootstrap_servers=['kafka:9092'],
            auto_offset_reset='earliest',  # Lee desde el inicio si es un consumidor nuevo
            enable_auto_commit=False,  # Confirma automáticamente la lectura de los mensajes
            group_id=None  # Grupo de consumidores
        )
        topic = 'dbserver1.public.estudiantes'
        partitions = consumer.partitions_for_topic(topic)
        if partitions is not None:
            topic_partitions = [TopicPartition(topic, p) for p in partitions]
            consumer.assign(topic_partitions)
            consumer.seek_to_beginning()  # Ensure starting from the beginning

        print(f"Esperando mensajes en el tópico {topic}.")

        for msg in consumer:
            print(f"Mensaje recibido: {msg.value.decode('utf-8')}")

    except Exception as e:
        print(f"Error en el consumidor: {e}")


if __name__ == '__main__':
    main()
