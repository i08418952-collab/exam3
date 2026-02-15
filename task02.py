class Seat:
    def __init__(self, number: int):
        self.number = number
        self.is_taken = False


class Ticket:
    def __init__(self, seat: Seat, owner: str):
        if not isinstance(seat, Seat):
            raise ValueError("seat Seat obyekt bolishi kerak")
        if not owner or not owner.strip():
            raise ValueError("owner bosh bolmasligi kerak")
        self.seat = seat
        self.owner = owner


class CinemaSession:
    def __init__(self, movie_title: str, total_seats: int):
        if not movie_title or not movie_title.strip():
            raise ValueError("movie_title bosh bolmasligi kerak")
        if not isinstance(total_seats, int) or total_seats <= 0:
            raise ValueError("total_seats 0 dan katta bolishi kerak")

        self.movie_title = movie_title
        self.total_seats = total_seats
        self.seats = [Seat(i) for i in range(1, total_seats + 1)]
        self.bookings = []

    def available_seats(self) -> list[int]:
        return [seat.number for seat in self.seats if not seat.is_taken]

    def book_seat(self, seat_number: int, user: str) -> Ticket:
        if not isinstance(seat_number, int) or not (1 <= seat_number <= self.total_seats):
            raise ValueError("Bunday orin mavjud emas")

        seat = self.seats[seat_number - 1]
        if seat.is_taken:
            raise RuntimeError("Orin allaqachon olingan")

        seat.is_taken = True
        ticket = Ticket(seat, user)
        self.bookings.append(ticket)
        return ticket

    def __str__(self):
        return f"CinemaSession: {self.movie_title} ({self.total_seats} seats)"



if __name__ == "__main__":
    session = CinemaSession("Avatar 2", 5)

    print(session.available_seats())  # [1, 2, 3, 4, 5]

    ticket1 = session.book_seat(3, "Ali")
    print(ticket1.owner)         # Ali
    print(ticket1.seat.number)   # 3
    print(ticket1.seat.is_taken) # True

    print(session.available_seats())  # [1, 2, 4, 5]

    ticket2 = session.book_seat(1, "Vali")
    print(session.available_seats())  # [2, 4, 5]

    try:
        session.book_seat(3, "Sardor")
    except RuntimeError:
        print("Xato: O'rin allaqachon olingan!")

    print(session)

    print(f"Jami bron: {len(session.bookings)}")
    for ticket in session.bookings:
        print(f"O'rin {ticket.seat.number}: {ticket.owner}")
