# mi_app/firebase.py
import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate(r'C:\Users\Imer\Documents\GitHub\Project-Umbra\mi_proyecto\mi_proyecto\umbra-bd86a-firebase-adminsdk-fbsvc-899ddfce5b.json')


firebase_admin.initialize_app(cred)
