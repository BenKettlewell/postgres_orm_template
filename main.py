''' 
Help
'''
from Database import Database
from DatabaseSchema import User

def main ():
    
    my_database = Database()
    my_database.add_user('cool_user_jim_bob')
    new_users = [
            User(name='wendy', fullname='Wendy Williams', password='stuff'),
            User(name='otherperson', fullname='Cool Beans', password='more_stuff'),
            User(name='yay', fullname='NEVAR potatoes', password='more_stuff')
            ]
    my_database.add_all_users(new_users)
    print my_database.session.query(User).filter_by(password='stuff').first().name
    
if __name__ == "__main__":
    main()
