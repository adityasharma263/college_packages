# -*- coding: utf-8 -*-
from ts import db
from ts.model.base import Base


class Package(Base):

    __tablename__ = 'package'

    title = db.Column(db.String, nullable=False)
    venue = db.Column(db.String, nullable=True)
    meal_plan = db.Column(db.String, nullable=True)
    trip_duration = db.Column(db.String, nullable=True)
    about_trip = db.Column(db.String, nullable=True)
    about_venue = db.Column(db.String, nullable=True)
    tour_category = db.Column(db.String, nullable=True)
    tour_domain = db.Column(db.String, nullable=True)
    mg_min_pax = db.Column(db.Integer, nullable=True)
    max_pax = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    days = db.relationship('Day', backref='package')
    images = db.relationship('Image', backref='package')
    amenities = db.relationship('Amenity', backref='package')
    availabilities = db.relationship('Availability', backref='package')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<title %r>' % self.title


class Day(Base):

    __tablename__ = 'day'

    no_of_day = db.Column(db.Integer, nullable=True)
    venue_name = db.Column(db.String, nullable=True)
    venue_image_url = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)
    timing = db.Column(db.String, nullable=True)
    package_id = db.Column(db.Integer, db.ForeignKey('package.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<no_of_day %r>' % self.no_of_day


class Availability(Base):

    __tablename__ = 'Availability'

    Availability = db.Column(db.Boolean, default=True, nullable=True)
    date = db.Column(db.DateTime, nullable=True)
    package_id = db.Column(db.Integer, db.ForeignKey('package.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<amenity %r>' % self.amenity


class Amenity(Base):

    __tablename__ = 'amenity'

    amenity = db.Column(db.String, nullable=True)
    package_id = db.Column(db.Integer, db.ForeignKey('package.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<amenity %r>' % self.amenity


class Image(Base):

    __tablename__ = 'image'

    image_url = db.Column(db.String, nullable=True)
    package_id = db.Column(db.Integer, db.ForeignKey('package.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<amenity %r>' % self.image_url


class College(Base):

    __tablename__ = 'college'

    institution_name = db.Column(db.String, nullable=True)
    college_domain = db.Column(db.String, nullable=True)
    courses = db.relationship('Course', backref='college')
    no_of_student = db.Column(db.Integer, nullable=True)
    no_of_employees = db.Column(db.Integer, nullable=True)
    coordiantor_name = db.Column(db.String, nullable=True)
    coordiantor_phone = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=True)
    username = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    bank_name = db.Column(db.String, nullable=True)
    account_holder = db.Column(db.String, nullable=True)
    ifsc_code = db.Column(db.String, nullable=True)
    account_no = db.Column(db.String, nullable=True)
    packages = db.relationship('Package', secondary='college_selected_package')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<no_of_day %r>' % self.no_of_day


class Course(Base):

    __tablename__ = 'course'

    course = db.Column(db.String, nullable=True)
    college_id = db.Column(db.Integer, db.ForeignKey('college.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<course %r>' % self.course


class CollegeSelectedPackage(Base):

    __tablename__ = 'college_selected_package'

    college_id = db.Column(db.Integer, db.ForeignKey('college.id'))
    package_id = db.Column(db.Integer, db.ForeignKey('package.id'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<college_id %r>' % self.college_id


class Student(Base):

    __tablename__ = 'student'

    name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    course = db.Column(db.String, nullable=True)
    date = db.Column(db.DateTime, nullable=True)
    college_id = db.Column(db.Integer, db.ForeignKey('college.id'), nullable=False)
    package_id = db.Column(db.Integer, db.ForeignKey('package.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<no_of_day %r>' % self.no_of_day