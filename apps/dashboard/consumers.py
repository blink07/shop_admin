import json
import time

# from asgiref.sync import async_to_sync
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'shop_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print("aaaa:", self.room_group_name)
        print(self.groups)
        print("message:",message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'shop_message',   # 和下面的消息处理函数要一致
                'message': message
            }
        )
        # time.sleep(3)



    # Receive message from room group
    async def shop_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))


def send_group_msg(room_name, message):

    # 从Channels的外部发送消息给Channel
    # 用户外部接口调用
    # 推送流程：Django View -> 逻辑操作，保存数据到数据库 ->将消息发送到channel对应的group -> websocket将消息推送至接收方
    """
    from dashboard import consumers
    consumers.send_group_msg('ITNest', {'content': '这台机器硬盘故障了', 'level': 1})
    consumers.send_group_msg('ITNest', {'content': '正在安装系统', 'level': 2})
    consumers.send_group_msg('AAA', {'message': '登录成功', 'level': 2})
    :param room_name:
    :param message:
    :return:
    """
    # print("room_name, message",room_name, message)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'shop_{}'.format(room_name),  # 构造Channels组名称
        {
            "type": "shop_message",
            "message": message,
        }
    )
    # consumer = ChatConsumer()
    # consumer.channel_layer.group_send()