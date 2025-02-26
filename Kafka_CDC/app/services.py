from app.database import PostgreSQLSession
from app.models import MyTable


def sync_data(change_event):
    session = PostgreSQLSession()
    data = change_event["payload"]["after"]

    new_entry = MyTable(
        id=data["id"],
        name=data["name"],
        value=data["value"],
        created_at=data["created_at"]
    )

    session.add(new_entry)
    session.commit()
    session.close()
