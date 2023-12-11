import requests 

def get_contacts_count(url):
    response = requests.get(url)
    if response.status_code == 200:
        response_data = response.json()
        
        number_of_contacts = response_data.get('data',{}).get('total',0)

        return number_of_contacts
    

    
