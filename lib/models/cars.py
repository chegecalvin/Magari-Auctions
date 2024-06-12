from models.__init__ import CURSOR,CONN

class Car:
    all={}

    def __init__(self,manufacture_yr,make,price,id=None):
        self.id=id
        self.manufacture_yr=manufacture_yr
        self.make=make
        self.price=price

    def get_manufacture_yr(self):
        return self._manufacture_yr

    def set_manufacture_yr(self,manufacture_yr):
        if isinstance(manufacture_yr,int) and (2000<=len(manufacture_yr)<=2024) :
            self._manufacture_yr=manufacture_yr
        else:
            raise Exception("Year of manufacture must be a valid year between 2000 and 2024")
    manufacture_yr=property(get_manufacture_yr,set_manufacture_yr)

    def get_make(self):
        return self._make    
    
    def set_make(self,make):
        if isinstance(make,str):
            self._make=make
        else:
            raise Exception("Input a valid make")
    make=property(get_make,set_make)

    def get_price(self):
        return self._price
    
    def set_price(self,price):
        if isinstance(price,int) and len(price)> 0:
            self._price=price
        else:
            raise Exception("Price must be a value greater than 0")
    price=property()

    @classmethod
    def create_table(cls):
        sql= """
           CREATE TABLE IF NOT EXISTS cars(
           id INTEGER PRIMARY KEY,
           make TEXT,
           manufacture_yr INTEGER
           price INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql= """
           INSERT INTO cars (make,manufacture_yr,price)
           VALUES(?,?)
        """
        CURSOR.execute(sql,(self.make,self.manufacture_yr,self.price))
        CONN.commit()
        self.id=CURSOR.lastrowid
        type(self).all[self.id]=self

    @classmethod
    def add_car(cls,make,manufacture_yr,price):
        car=cls(make,manufacture_yr,price)
        car.save()
        return car
    
    def delete_car(self):
        sql= """
           DELETE FROM cars
           WHERE id=?
        """
        CURSOR.execute(sql,(self.id))
        CONN.commit()
        del type(self).all[self.id]
        self.id=None

    @classmethod
    def instance(cls,row):
        car=cls.all.get(row[0])
        if car:
            car.make=row[1]
            car.maufacture_yr=row[2]
            car.price=row[3]
        else:
            car=cls(row[1],row[2],row[3])
            car.id=row[0]
            cls.all[car.id]=car
        return car
    
    @classmethod
    def get_all_cars(cls):
        sql= """
           SELECT * FROM cars
        """
        all_rows=CURSOR.execute(sql).fetchall()
        return [cls.instance(row) for row in all_rows]
    
    @classmethod
    def get_by_id(cls,id):
        sql= """
           SELECT * FROM cars
           WHERE id=?
        """
        row=CURSOR.execute(sql,(id,)).fetchone
        return cls.instance(row) if row else None
    
    def participants(self):
        from lib.models.participant import Participant
        sql= """
           SELECT * FROM participants
           WHERE car_id=?
        """
        CURSOR.execute(sql,(self.id,),)
        all_rows=CURSOR.fetchall()
        return [Participant.instance(row) for row in all_rows ]


