from DAN_app.config.mysqlconnection import connectToMySQL
from DAN_app.models import ninja
from collections import defaultdict
# This is my one. one dojo can have many ninjas, many ninjas belong to one dojo
class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());'
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)
        
    
    @classmethod 
    def get_one_with_user(cls, data):
        query ='SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s'
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        dojo = (cls(results[0]))

        if results[0]['ninjas.id'] == None:
            return (cls(results[0]))
        else:
            for ninja_dict in results:
                ninja_data = {
                    'id': ninja_dict['ninjas.id'],
                    'first_name': ninja_dict['first_name'],
                    'last_name': ninja_dict['last_name'],
                    'age': ninja_dict['age'],
                    'created_at': ninja_dict['ninjas.created_at'],
                    'updated_at': ninja_dict['ninjas.updated_at']
                }
                dojo.ninjas.append(ninja.Ninja.get_one_with_dojo(ninja_data))
        return dojo 

    # @classmethod
    # def get_one_with_user(cls, data):
    #     query ='SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s'
    #     results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
    #     dojo = cls(results[0])
    #     ninja_data = {
    #                 'id': ninja_dict[0]['ninjas.id'],
    #                 'first_name': ninja_dict[0]['first_name'],
    #                 'last_name': ninja_dict[0]['last_name'],
    #                 'age': ninja_dict[0]['age'],
    #                 'created_at': ninja_dict[0]['ninjas.created_at'],
    #                 'updated_at': ninja_dict[0]['ninjas.updated_at']
    #             }
    #     dojo.ni