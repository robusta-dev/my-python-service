class Dal:

    def __init__(self, db_conn_str: str):
        self.db_client = Client(db_conn_str)

    def insert_service(self, service: Service):