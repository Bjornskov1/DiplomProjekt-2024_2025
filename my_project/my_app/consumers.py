from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MeetingRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"room_{self.room_name}"

        print(f"Connecting to WebSocket group: {self.room_group_name}")  # Debug

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def meeting_update(self, event):
        message = event['message']

        # Send message til WebSocket
        await self.send(text_data=message)