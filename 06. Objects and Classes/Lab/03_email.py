class Email:
    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
line = input()

while line != "Stop":
    info = line.split(" ")
    sender = info[0]
    receiver = info[1]
    content = info[2]
    email = Email(sender, receiver, content)
    emails.append(email)

    line = input()

# send_emails_index = list(map(lambda x: int(x), input().split(", ")))
send_emails_index = [emails[int(x)].send() for x in input().split(", ")]

# for x in send_emails_index:
#     emails[x].send()
for email in emails:
    print(email.get_info())
