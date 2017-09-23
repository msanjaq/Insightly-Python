# insightly-python-sdk

## requirements
Python 3.x

requests

## Initialization
Get your API Key from Insightly Account (User Settings > API Key)

     from insightly import Insightly
     
     client = Insightly(api_key)
     
## Examples
    from insightly import Insightly
    
    client = Insightly("your_api_key_here")
    
    # example of get_all() method
    contact_list = client.contacts.get_all()
    
    # example of get(id) and create(data) methods
    some_org = client.organisations.get(1111111111)
    some_org["ORGANISATION_ID"] = 0
    client.organisations.create(some_org)
    
    # example of create(data) methods
    new_contact = {"FIRST_NAME": Ron, "LAST_NAME": Weezly}
    client.contacts.create(new_contact)
    
    # example of update(data) method
    some_contact = client.contacts.get(5555555555)
    some_contact["FIRST_NAME"] = "Moe"
    client.contacts.update(some_contact)
    
    # example of delete(id) method
    client.organisations.delete(123456789)

## Entities and methods
Below I list all the entities and their methods that this library offers. I provide type hints for clarity. It should be noted that the 'data' argument of the create() and delete() methods is a python dictionary that represents the {"FIELD NAME": value} mappings. The code below assumes that an Insightly class has been initalized with the name "client."

### Contacts
    client.contacts.get(id: int)

    client.contacts.get_all(brief=False)

    client.contacts.create(data: {str:any})

    client.contacts.update(data: {str:any})

    client.contacts.delete(id: int)

### Organisations
    client.organisations.get(id: int)

    client.organisations.get_all(brief=False)

    client.organisations.create(data: {str:any})

    client.organisations.update(data: {str:any})

    client.organisations.delete(id: int)
    
 


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

## Known bugs and work-arounds
Bug: For some reason I am unable to create an organisation using Insightly API v2.2

work-around: I am currently using Insightly API v2.1 to add this functionality



