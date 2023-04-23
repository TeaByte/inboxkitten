import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
class EmailNotFound(TypeError): pass

class InboxKitten:
    def __init__(self, email, setup=True): 
        self.email = email
        self._keys, self._storages = [], []
        self.senders, self.subjects = [], []
        if setup: self.refresh

    @property
    def refresh(self):
        if '@' in self.email: self.email = self.email.split('@')[0]
        
        response = requests.get(
            'https://inboxkitten.com/api/v1/mail/list',
            params={'recipient': self.email}, headers=headers
        )

        for mail in response.json():
            data, info = mail['storage'], mail['message']['headers']
            self._keys.append(str(data['key']))
            self._storages.append(str(data['region']))
            self.senders.append(str(info['from']))
            self.subjects.append(str(info['subject']))
        return True

    def text(self, index: int):
        index = int(index)
        try:
            return requests.get(
                f'https://inboxkitten.com/api/v1/mail/getHtml?mailKey=storage-{self._storages[index]}-{self._keys[index]}', 
                headers=headers
            ).text
        except IndexError: 
            raise EmailNotFound("Selected index is out of range")
        
    def where_subject(self, condition: str):
        indexes = []
        condition = str(condition).lower() 
        for index, subject in enumerate(self.subjects):
            if condition in str(subject).lower():
                indexes.append(int(index))
        return indexes
    
    def where_sender(self, condition: str):
        indexes = []
        condition = str(condition).lower() 
        for index, sender in enumerate(self.senders):
            if condition in str(sender).lower():
                indexes.append(int(index))
        return indexes 
    
    def save_html(self, email_object, filename: str):
        with open(filename, 'w', encoding='utf-8', errors='ignore') as html_file: 
            html_file.write(email_object)
        return True