# # from dataclasses import dataclass
# # from typing import NamedTuple
# # from collections import namedtuple
# from typing import List, Optional
import json

# # @dataclass(frozen=True)
# # class Name:
# #     first_name: str
# #     surname: str

# # class Money(NamedTuple):
# #     currency: str
# #     value: int
    
    
# # Line = namedtuple('Line', ['sku', 'qty'])

# # class Person:
# #     def __init__(self, name: Name):
# #         self.name = name

# # def test_equality():
# #     print("*******************Value Object base test*************")
# #     print(Money('gbp', 10) == Money('gbp', 10))
# #     print(Name('Harry', 'Percival') != Name('Bob', 'Gregory'))
# #     print(Line('RED-CHAIR', 5) == Line('RED-CHAIR', 5))
    

# # result = ord('m')    

# # print(f'**********ord of m is {result}**********')
# # def test_barry_is_harry():
# #     print("*******************Entity base test*************")
# #     harry = Person(Name("Harry", "Percival"))
# #     barry = harry

# #     barry.name = Name("Barry", "Percival")

# #     print(harry is barry and barry is harry)
    
# # if __name__ == "__main__":
# #     test_equality()
# #     test_barry_is_harry()


# # authentifyer_user_id = "emmanuel"
# # credential_id = "prayo"
# # conditions = []
# # if authentifyer_user_id is not None:
# #     conditions.append("authentifyer_user_id='{}'".format(authentifyer_user_id))
# # if credential_id is not None:
# #     conditions.append("credential_id='{}'".format(credential_id))
# #         # if presentation_id is not None:
# #         #     conditions.append("presentation_id='{}'".format(presentation_id))
# #         # if provider_id is not None:
# #         #     conditions.append("provider_id='{}'".format(provider_id))
# #         # if status is not None:
# #         #     conditions.append("status IN ('{}')".format(status))

# # condition_str = "TRUE" if not conditions else " AND ".join(conditions)
# # if not conditions:
# #     print("**************Conditions is empty************")
# # else:
# #     print("**************Conditions is NOT empty************")
# #     print(conditions)
# # print(condition_str)


# # def my_func(param: List[int]) -> int:
# #     params = [a for a in param]
# #     print(f"param is pointing to the object: {param}")
# #     print(f"params is pointing to the object: {params}")
# #     return params

# # print(my_func(5))


# type = 'value'

# def my_fnc(type: Optional[str] = None):
#     type_str = "TRUE" if not type else "type ILIKE '%{}%'".format(type)
    
#     return type_str


# print(my_fnc(type))


CREATE_PROVIDER = {
  "corporation": {
    "email": "corporation@gmail.com",
    "name": "Corperation-name",
    "description": "Corperation-description",
    "legalName": "Corperation-legalName",
    "duns": "Corperation-duns",
    "telephone": "Corperation-telephone",
    "url": "Corperation-url",
    "taxId": "Corperation-taxId",
    "vatId": "Corperation-vatId"
  },
  "administrator": {
    "email": "Corperation-admin-email",
    "givenName": "Corperation-admin-givenName",
    "familyName": "Corperation-admin-familyName",
    "displayName": "Corperation-admin-displayName",
    "telephone": "Corperation-admin-telephone",
    "jobTitle": "Cporperation-admin-jobTitle"
  }
}

print(json.dumps(CREATE_PROVIDER))