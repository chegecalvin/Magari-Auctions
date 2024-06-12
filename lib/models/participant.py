from models.__init__ import CURSOR, CONN
from models.cars import Car

class Participant:
    all={}

    def __init__(self,name,age,location,car_id,id=None):
        self.name=name
        self.age=age
        self.location=location
        self.car_id=car_id

    def get_name(self):
        return self._name
    
    def set_name(self,name):
        if isinstance(name,str):
            self._name=name
        else:
            raise Exception("Input a valid name")
    name=property(get_name,set_name)

    def get_age(self):
        return self._age
    
    def set_age(self,age):
        if isinstance(age,int) and len(age) > 0:
            self._age=age
        else:
            raise Exception("Input a valid age")
    age=property(get_age,set_age)

    def get_location(self):
        return self._location
    
    def set_location(self,location):
        if isinstance(location,str):
            self._location=location
        else:
            raise Exception("Input a valid location")
    location=property(get_location,set_location)

    def get_car_id(self):
        return self._car_id
    
    def set_car_id(self,car_id):
        if isinstance(car_id,int) and Car.get_by_id(car_id):
            self._car_id=car_id
        else:
            raise Exception("Invalid Id")
    car_id=property(get_car_id,set_car_id)

    @classmethod
    def create_table(cls):
        sql= """
           CREATE TABLE IF NOT EXISTS participants(
           id INTEGER PRIMARY KEY,
           name TEXT,
           age INTEGER,
           location TEXT,
           car_id INTEGER,
           FOREIGN KEY (car_id) REFERENCES cars(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql= """
           INSERT INTO participants(name,age,location,car_id)
           VALUES(?,?,?)
        """
        CURSOR.execute(sql,(self.name,self.age,self.location,self.car_id))
        CONN.commit()
        self.id=CURSOR.lastrowid
        type(self).all[self.id]=self

    @classmethod
    def add_participant(cls,name,age,location,car_id):
        participant=cls(name,age,location,car_id)
        participant.save()
        return participant
    
    def remove_participant(self):
        sql= """
           DELETE from participants
           WHERE id=?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id=None

    @classmethod
    def instance(cls,row):
        participant=cls.all.get(row[0])
        if participant:
            participant.name=row[1]
            participant.age=row[2]
            participant.location=row[3]
            participant.car_id=row[4]
        else:
            participant=cls(row[1],row[2],row[3],row[4])
            participant.id=row[0]
            cls.all[participant.id]=participant
        return participant
    
    @classmethod
    def get_all_participants(cls):
        sql= """
           SELECT * FROM participants
        """
        all_rows=CURSOR.execute(sql).fetchall()
        return [cls.instance(row) for row in all_rows]
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM participants
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance(row) if row else None
    
    @classmethod
    def get_by_id(cls,id):
        sql= """
           SELECT * FROM participants
           WHERE id=?
        """
        row=CURSOR.execute(sql,(id,)).fetchone
        return cls.instance(row) if row else None
    