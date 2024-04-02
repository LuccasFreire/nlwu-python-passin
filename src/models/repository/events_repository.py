from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities import Events

class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection_handler as database:
            event = Events(
                id = eventsInfo.get("uuid"),
                title = eventsInfo.get("title"),
                detail = eventsInfo.get("detail"),
                slug = eventsInfo.get("slug"),
                maximum_attendees = eventsInfo.get("maximum_attendees"),
            )
            database.session.add(event)
            database.session.commit()

            return eventsInfo
