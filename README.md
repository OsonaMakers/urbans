# urbans
Projectes d'ambit Urbà

## MQTT
El protocol MQTT (Message Queuing Telemetry Transport) és molt útil en aplicacions d'IoT (Internet de les coses) i M2M (Machine-to-Machine) a causa de la seva eficiència i escalabilitat en la transmissió de missatges entre dispositius connectats a la xarxa. Algunes de les avantatges de MQTT són:

- Lleuger: MQTT està dissenyat per ser un protocol lleuger i senzill, la qual cosa significa que es pot implementar en dispositius amb recursos limitats com ara sensors i dispositius de baixa potència.

- Eficient: MQTT utilitza un model de subscripció i publicació, la qual cosa significa que els dispositius només reben els missatges que els interessen. Això redueix l'amplada de banda necessària per a la comunicació i millora l'eficiència de la xarxa.

- Escalable: MQTT és altament escalable i pot suportar un gran nombre de dispositius connectats a la xarxa.

- Fiabilitat: MQTT utilitza un mecanisme de qualitat de servei (QoS) per garantir la entrega dels missatges. Això permet als dispositius assegurar-se que els missatges importants siguin entregats amb èxit.

En resum, MQTT és un protocol de comunicació molt útil per a la IoT i M2M a causa de la seva lleugeresa, eficiència, escalabilitat i fiabilitat.

## DEMO
![](esquema_demo.png)
### CLIENT
#### Configuració
```bash
cd mqtt_client
cp -ax .env.example .env
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 mqtt_client/app.py
```

> Omplir el arxiu .env amb les dades del broker MQTT.

### Broker && DDBB

```bash
docker compose -f "docker-compose.yml" up -d --build
```

#### Crear usuari i password mqtt

```bash
docker exec -it broker-mqtt sh
mosquitto_passwd -b /mosquitto/config/password.txt user password
```

### Eliminar usuari i password
```bash
docker exec -it broker-mqtt sh
mosquitto_passwd -D passwordfile user
```

### Securització MQTT
http://www.steves-internet-guide.com/mqtt-security-mechanisms/


## DB

Administració: [http://127.0.0.1:8081/](http://127.0.0.1:8081/)