from faker import Faker

fake = Faker()
Faker.seed(0)

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
        "vatId": "Corperation-vatId",
    },
     "administrator": {
        "email": "provider-email@gmail.com",
        "givenName": "Corperation-admin-givenName",
        "familyName": "Corperation-admin-familyName",
        "displayName": "Corperation-admin-displayName",
        "telephone": "Corperation-admin-telephone",
        "jobTitle": "Cporperation-admin-jobTitle",
    },
}


def create_provider():
    providers = []
    for _ in range(2):
        PROVIDER = {
        "corporation": {
            "email": fake.email(),
            "name": fake.name(),
            "description": fake.text(),
            "legalName": fake.company(),
            "duns": fake.aba(),
            "telephone": fake.phone_number(),
            "url": fake.url(),
            "taxId": fake.aba(),
            "vatId": fake.aba(),
        },
        "administrator": {
            "email": fake.email(),
            "givenName": fake.first_name(),
            "familyName": fake.last_name(),
            "displayName": fake.first_name(),
            "telephone": fake.phone_number(),
            "jobTitle": fake.job(),
        }
        }
        providers.append(PROVIDER)
    print(providers)
    
    

if __name__ == "__main__":
    create_provider()