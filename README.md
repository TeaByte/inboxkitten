# inboxkitten [![Downloads](https://static.pepy.tech/personalized-badge/inboxkitten?period=total&units=international_system&left_color=black&right_color=blue&left_text=Downloads)](https://pepy.tech/project/inboxkitten)
Simple inboxkitten python lib for https://inboxkitten.com/

## 

#### Install requirements
```
pip install inboxkitten
```

#### Example
```python
import inboxkitten as ik

# Create an inbox with name test@inboxkitten.com
email = ik.InboxKitten('test')
print(email.subjects) # Get all subjects ( list )
print(email.senders)  # Get all senders  ( list )

# You can refresh messages
email.refresh

# Get text response
# index = 0 ( mean first message )
first = email.text(index=0)
print(first)

# Searching in subjects and senders
# Returing a list of indexes
cambly = email.where_subject('Cambly')
print(email.where_sender('talent.io'))

# Save response as html file
email.save_html(first, 'first.html')

# Error handling
another_one = ik.InboxKitten('rundomthing123')
try: another_one.text(index=666)
except ik.EmailNotFound: print('No email found on that index')
```


