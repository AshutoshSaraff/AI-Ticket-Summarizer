# Start Application

from ticket_processer import TicketProcessor

processor = TicketProcessor()

ticket = """
    When I try to login it gives me Error - 500
"""

summery = processor.process_ticket(ticket)

print(summery)

