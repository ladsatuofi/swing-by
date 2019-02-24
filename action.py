class Action:
    def __init__(self, event, num_upvotes, num_downvotes):
        self.event = event
        self.num_upvotes = num_upvotes
        self.num_downvotes = num_downvotes
    def upvote(event):
        event.num_upvotes += 1
    def downvote(event):
        event.num_downvotes += 1
    def post_event(self, description, date, time, location):
        self.description = description
        self.date = date
        self.time = time
        self.location = location