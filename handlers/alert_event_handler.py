from interfaces import Event, EventHandler, EventSubscriber

class AlertEventHandler:
    async def handle(self, event: Event) -> None:
        print(f"[Alert Handler] System alert received: {event.payload}")


class AlertSubscriber:
    def get_event_types(self) -> list[str]:
        return ["system_alert"]

    def get_handler(self) -> EventHandler:
        return AlertEventHandler()
