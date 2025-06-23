import asyncio
from typing import Dict, List
from interfaces import Event, EventSubscriber


class EventBus:
    def __init__(self):
        self.subscribers: Dict[str, List[EventSubscriber]] = {}

    def subscribe(self, subscriber: EventSubscriber):
        for event_type in subscriber.get_event_types():
            self.subscribers.setdefault(event_type, []).append(subscriber)

    async def dispatch(self, event: Event):
        handlers = self.subscribers.get(event.type, [])
        for sub in handlers:
            try:
                await sub.get_handler().handle(event)
            except Exception as e:
                print(f"Error handling event {event.type}: {e}")
