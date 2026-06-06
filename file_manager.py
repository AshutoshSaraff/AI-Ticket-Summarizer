import json
import os


class FileManager:

    def save_summary(self, ticket_data):

        if ticket_data is None:
            return

        file_name = "tickets.json"

        all_tickets = []

        if os.path.exists(file_name):

            try:

                with open(
                    file_name,
                    "r",
                    encoding="utf-8"
                ) as file:

                    all_tickets = json.load(file)

            except:

                all_tickets = []

        all_tickets.append(
            ticket_data
        )

        with open(
            file_name,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                all_tickets,
                file,
                indent=4
            )