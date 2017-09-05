# insightly-python-sdk

## requirements
  Python 3.x
  requests

## Syntax
    from insightly import Insightly
    
    client = Insightly("your_api_key_here")
    
    # example of get_all() method
    contact_list = client.contacts.get_all()
    
    # example of get(id) and create(data) methods
    some_org = client.organisations.get(1111111111)
    some_org["ORGANISATION_ID"] = 0
    client.organisations.create(some_org)
    
    # example of update(data) method
    some_contact = client.contacts.get(5555555555)
    some_contact["FIRST_NAME"] = "Moe"
    client.contacts.update(some_contact)
    
    # example of delete(id) method
    client.organisations.delete(123456789)
 
## Progress
Done: contacts and organisations
Coming soon: projects, tasks, leads
 
## Reasons for creation
The SDK currently provided by Insightly/insightly-python is littered with bugs that only appear in odd edge cases- some of which I couldn't totally debug and fix even after contacting Insightly's engineering team. Therefore, I found myself having to go back to formulating the API calls myself which proved to be much more consistent. Because of this, I decided to write a new SDK that would encapsulate many common API calls.

## Changes from Insightly/insightly-python
1. New syntax inspired by charlesthk/python-mailchimp3
2. Uses Insightly API v2.2 (where possible)
3. Serves more as a thin veneer over API calls
3. PEP8 compliant
4. Not compatible with Python 2.7
5. Uses requests instead of urllib/urllib2
6. No plans for offline functionality

## Know bugs and work-arounds
Bug: For some reason I am unable to create an organisation using Insightly API v2.2
work-around: I am currently using Insightly API v2.1 to add this functionality



