class News:
    def __init__(self, id, type):

        self.id = id
        self.deleted = "models.BooleanField()"
        self.type = type
        self.by = "models.CharField()"
        self.time = "models.DateTimeField()"
        self.text = "models.TextField()"
        self.dead = "models.TextField()"
        self.parent = "models.TextField()"
        self.poll = "models.TextField()"
        self.kids = "models.TextField()"
        self.url = "models.TextField()"
        self.score = "models.TextField()"
        self.title = "models.TextField()"
        self.parts = "models.TextField()"
        self.descendants = "models.TextField()"

    def return_dict(self):
        types = {
            "story": {
                "by": self.by,
                "descendants": self.descendants,
                "id": self.id,
                "kids": self.kids,
                "score": self.score,
                "time": self.time,
                "title": self.title,
                "type": self.type,
                "url": self.url,
            },
            'comments': {
                "by": self.by,
                "id": self.id,
                "kids": self.kids,
                "parent": self.parent,
                "text": self.text,
                "time": self.time,
                "type": self.type
            },
            "job": {
                "by": self.by,
                "id": self.id,
                "score": self.score,
                "text": self.text,
                "time": self.time,
                "title": self.title,
                "type": self.type,
                "url": self.url
            },
            "poll": {
                "by": self.by,
                "descendants": self.descendants,
                "id": self.id,
                "kids": self.kids,
                "parts": self.parts,
                "score": self.score,
                "text": self.text,
                "time": self.time,
                "title": self.title,
                "type": self.type
            },
            "pollopt": {
                "by": self.by,
                "id": self.id,
                "poll": self.poll,
                "score": self.score,
                "text": self.text,
                "time": self.time,
                "type": self.type
            }
        }

        return types

    def __str__(self):
        return 'The object id: {}, and type is: {}'.format(self.return_dict()[self.type]['id'], self.return_dict()[self.type]['type'])


first_news = News(1, 'story')

second_news = News(2, 'poll')

print(first_news)
print(second_news)
