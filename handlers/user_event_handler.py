from interfaces import Event, EventHandler, EventSubscriber

class UserEventHandler:
    async def handle(self, event: Event) -> None:
        print(f"[User Handler] User action: {event.payload}")


class UserSubscriber:
    def get_event_types(self) -> list[str]:
        return ["user_action"]

    def get_handler(self) -> EventHandler:
        return UserEventHandler()
