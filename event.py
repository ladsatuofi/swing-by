class Event:
    def __init__(self, description, date, poster, num_upvotes, num_downvotes):
        self.date = date
        self.description = description
        self.poster = poster
        self.num_upvotes = num_upvotes
        self.num_downvotes = num_downvotes