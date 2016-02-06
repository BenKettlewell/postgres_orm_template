from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from DatabaseSchema import *

Session = sessionmaker()
'''
    Session must be bound to an engine when one is declared
    Instance variables of session are used to query the database 
    and commit changes
    '''

class Database:
    """
    Abstracts I/O for nwatcher database
    """
    def __init__(self):
        '''
        Initializes a connection with the database
        Makes sure the database matches our schema (doesn't do migrations yet) 2/5/16
        Defines any missing tables
        Starts a session
        '''
        engine = self.create_engine()
        self.initialize_schema(engine)
        Session.configure(bind=engine)
        self.session = Session()

    def create_engine(self, database_type=None):
        '''
        The engine is what sends SQL requests to the database api (DBAPI)
        The connection string is hard-coded right now. If the database later
        contains sensitive info we need to find a way to secure the password
        '''
        # Set echo to True to see SQL in output
        if database_type == 'sqllite':
            return create_engine('sqlite:///:memory:', echo=False) 
        return  create_engine("postgresql://your_username:you_password@localhost:5432/your_database", echo=False)

    def initialize_schema(self, engine):
        '''
        Base finds class definitions with type Base and loads them into the 
          database if they do not exist (does not migrate database changes)
        .metadata creates a SQL structure definition of each table
          which you can see in the program output if the database engine echo 
          option is set to True
        .create_all does what you'd expect
        '''
        Base.metadata.create_all(engine)
    
    def add_user(self, customer_name):
        User.addresses = relationship("Address", order_by=Address.id, back_populates="user")
        new_customer_entry = User(name=customer_name, fullname='Ed Jones', password='edpassword')
        self.session.add(new_customer_entry)
        self.session.commit()
    
    def add_all_users(self, list_of_users):
        '''
        ex list_of_users:
            [
            User(name='wendy', fullname='Wendy Williams', password='stuff'),
            User(name='otherperson', fullname='Cool Beans', password='more_stuff'),
            User(name='yay', fullname='NEVAR potatoes', password='more_stuff')
            ]
        '''
        self.session.add_all(list_of_users)
        self.session.commit()
