class Marketplace:
    def __init__(self):
        self.online_db = {
            "item_1":{
                "name": "NVIDIA RTX 3070 GPU",
                "cost": "$399",
                "count": 1
            },
            "item_2":{
                "name": "Intel 10700K CPU",
                "cost": "$350",
                "count": 1
            },
            "item_3":{
                "name": "ASUS ROG STRIX 370-E ATX Motherboard",
                "cost": "$499",
                "count": 1
            },
            "item_4":{
                "name": "32GB G-Skill 3200MHz RAM",
                "cost": "$120",
                "count": 2
            },
            "item_5":{
                "name": "Corsair 750W Power Supply",
                "cost": "$399",
                "count": 1
            },
            "item_6":{
                "name": "NZXT Full ATX Case",
                "cost": "$199",
                "count": 1
            },
            "item_7":{
                "name": "Noctua NH-U12S CPU Cooler",
                "cost": "$89",
                "count": 1
            }
        }

    def search_for_item(self, query):
        for item in self.online_db.keys():
            if query in self.online_db[item]['name']:
                return self.online_db[item]['name']
            
        return False

query = input("Search: ")
online_marketplace = Marketplace()
item_found = online_marketplace.search_for_item(query)
if item_found != False:
    print(f"Item Found: {item_found}")
else:
    print("Item not found using that search criteria")