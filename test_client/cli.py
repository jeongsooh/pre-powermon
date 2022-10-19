import asyncio
# import logging
import json
import websockets

# logging.basicConfig(level=logging.INFO)
print("sample code for powermon client")

async def heartbeat_send(ws):
    print(f"Start client...")
    count = 1
    while True:
        await ws.send(json.dumps({'type':'chat', 'message':'just test, test, test, ... test'}))
        conf_data = await ws.recv()
        conf_data_json = json.loads(conf_data)
        print('Conf data # {}: {}'.format(count, conf_data_json['message']))
        count += 1
        await asyncio.sleep(10)

async def main():

    async with websockets.connect(
        'ws://127.0.0.1:8000/ws/socket-server/202021'
    ) as ws:

        print(f"Connection established..")
        await asyncio.gather(
          heartbeat_send(ws),
        #   cp.send_authorize()
        #   heartbeat_send(cp, heartbeat_interval)
        )

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except AttributeError:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
