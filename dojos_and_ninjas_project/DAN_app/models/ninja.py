from DAN_app.config.mysqlconnection import connectToMySQL
from DAN_app.models import dojo

#this is my many. many ninjas can belong to one dojo. one dojo can have many ninjas. 
class Ninja:
    # attributes

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo = None
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * from ninjas;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas 

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at ) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());'
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def get_one_with_dojo(cls, data): 
        query = 'SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data) # this always returns a list of dicts 
        ninja = (cls(results[0]))
        dojos_data = { 
            'id' : results[0]['dojos.id'], 
            'name' : results[0]['name'],
            'created_at' : results[0]['dojos.created_at'],
            'updated_at' : results[0]['dojos.updated_at'],
        } 
        ninja.dojo = dojo.Dojo(dojos_data)
        return ninja
