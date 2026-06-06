# Business Logic
from ai_client import AIClient
from file_manager import FileManager

class TicketProcessor:

    def __init__(self):

        self.ai_client = AIClient()

        self.file_manager = FileManager()

    def process_ticket(self, ticket):

        ticket_data = self.ai_client.generate_summary(
            ticket
        )

        if ticket_data is None:

            return "AI Request Failed"
        
        self.file_manager.save_summary(
            ticket_data
        )

        return ticket_data