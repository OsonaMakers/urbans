from src.MQTTClient import MQTTClient

if __name__ == '__main__':
    client = MQTTClient()
    client.connect()
    client.subscribeToAllTopics()
    # client.subscribe('**/**')
    # client.publish('**/**', '***F')
    client.loop_forever()
