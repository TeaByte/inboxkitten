# inboxkitten
Simple inboxkitten python lib for https://inboxkitten.com/

## Features
- Simple to use
- Email search

## Help

Install requirements
```
pip install inboxkitten
```

Example
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


