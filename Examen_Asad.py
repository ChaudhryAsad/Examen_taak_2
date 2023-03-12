import requests
import re
import yaml

url = "https://api.domainsdb.info/v1/domains/search?domain=syntra.be"

response = requests.get(url)
data = response.json()["domains"][0]

# extracteer jaar, maand en dag van de create_date
m = re.match(r'^(\d{4})-(\d{2})-(\d{2})', data["create_date"])
year, month, day = m.groups()

# extracteer de provider van de nameservers
provider = re.match(r'^ns\d?.(.+).\w+$', data["NS"][0]).group(1)

# verzamel de gewenste gegevens in een dictionary
output = {
    "created": {
        "jaar": year,
        "maand": month,
        "dag": day
    },
    "ip": data["A"][0],
    "land": data["country"],
    "provider": provider
}

# output de gegevens als YAML
print(yaml.dump(output))
