from ts.model.college_packages import College, Course, Student, Day, Amenity
from ts.model.college_packages import Package

from ts import ma


class AmenitySchema(ma.ModelSchema):
    class Meta:
        model = Amenity
        exclude = ('updated_at', 'created_at')


class DaySchema(ma.ModelSchema):
    class Meta:
        model = Day
        exclude = ('updated_at', 'created_at')


class PackageSchema(ma.ModelSchema):
    days = ma.Nested(DaySchema, many=True)
    Amenity = ma.Nested(AmenitySchema, many=True)

    class Meta:
        model = Package
        exclude = ('updated_at', 'created_at')


class CourseSchema(ma.ModelSchema):
    class Meta:
        model = Course
        exclude = ('updated_at', 'created_at')


class CollegeSchema(ma.ModelSchema):
    packages = ma.Nested(PackageSchema, many=True)
    courses = ma.Nested(CourseSchema, many=True)

    class Meta:
        model = College
        exclude = ('updated_at', 'created_at')


class StudentSchema(ma.ModelSchema):
    college = ma.Nested(PackageSchema, many=False)

    class Meta:
        model = Student
        exclude = ('updated_at', 'created_at')