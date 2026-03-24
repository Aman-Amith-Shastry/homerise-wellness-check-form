import firebase_admin
import urllib.parse
from firebase_admin import credentials, firestore
from datetime import datetime, timezone

#initialize firebase
cred = credentials.Certificate("serviceAccountKey.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

subcollection_sites = db.collection("sites")
sites = list(subcollection_sites.stream())

for site in sites:
    # print("site_id:", site.id)
    site_dict = site.to_dict()
    site_id = site.id
    doc_ref = db.collection("sites").document(site_id)
    residents_ref = doc_ref.collection("residents")
    residents_ref = residents_ref.stream()
    residents = list(residents_ref)
    site_name = site_dict["name"] # need to edit to proper name

    print(
            
            f"Site ID {site_id}: "
            f"Site Name {site_name}: "
           
        )

    for resident in residents:
        # print(resident)
        resident_dict = resident.to_dict()
        
        resident_id = resident.id

        name = resident_dict["name"]


        print(
            
            f"Resident ID {resident_id}: "
            f"Resident Name {name}: "
           
        )

        

        site_name = site_dict["name"] # need to edit to proper name
        site_name = site_name.lower()
        site_name = site_name.replace(" ", "")

        
        name = urllib.parse.quote(name)


       

            





