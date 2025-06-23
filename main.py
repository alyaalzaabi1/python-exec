import asyncio
from interfaces import Event
from dispatcher import EventBus
from handlers.user_event_handler import UserSubscriber
from handlers.alert_event_handler import AlertSubscriber

async def main():
    bus = EventBus()
    bus.subscribe(UserSubscriber())
    bus.subscribe(AlertSubscriber())

    await bus.dispatch(Event("user_action", {"username": "alya", "action": "login"}))
    await bus.dispatch(Event("system_alert", {"level": "warning", "msg": "CPU usage high"}))

asyncio.run(main())
