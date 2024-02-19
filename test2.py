import random
domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "protonmail.com", "yandex.com"]
weights = [50, 5, 16, 20, 5, 4]  # Corresponding weights for each domain

# Use random.choices() to select a domain based on the specified weights
selected_domain = random.choices(domains, weights=weights, k=1)[0]

print(selected_domain)
r= str(random.randint(1980,2010))
print(r)
print(r[2:])