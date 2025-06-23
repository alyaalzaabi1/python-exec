from typing import Protocol, Any
from abc import ABC
import asyncio


class Event:
    def __init__(self, type: str, payload: Any):
        self.type = type
        self.payload = payload


class EventHandler(Protocol):
    async def handle(self, event: Event) -> None:
        ...


class EventSubscriber(Protocol):
    def get_event_types(self) -> list[str]
    def get_handler(self) -> EventHandler


class EventPublisher(Protocol):
    async def publish(self, event: Event) -> None
