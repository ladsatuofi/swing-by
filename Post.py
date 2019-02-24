class Post:
    def __init__(self, description, date, contributor, num_upvotes, num_downvotes):
        self.date = date
        self.description = description
        self.contributor = contributor
        self.num_upvotes = num_upvotes
        self.num_downvotes = num_downvotes