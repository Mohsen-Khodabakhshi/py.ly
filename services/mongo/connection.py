from motor.motor_asyncio import AsyncIOMotorClient


class MongoConnection:
    def __init__(
        self, host: str, port: int, user: str, password: str
    ) -> None:
        self.client = AsyncIOMotorClient(
            f"mongodb://{user}:{password}@{host}:{port}"
        )

    def __new__(cls, *args):
        if not hasattr(cls, "instance"):
            cls.instance = super(MongoConnection, cls).__new__(cls)
        return cls.instance

    def get_client(self) -> AsyncIOMotorClient:
        """just will return self.client (DB connection)

        Returns:
            AsyncIOMotorClient: client that connected to DB
        """
        return self.client
