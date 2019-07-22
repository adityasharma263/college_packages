from ts.model.college_packages import College, Package, Day, Student, Course, Amenity
from ts import app
from sqlalchemy import or_
from flask import jsonify, request
from ts.schema.college_package import CollegeSchema, PackageSchema, DaySchema, StudentSchema, CourseSchema, AmenitySchema


@app.route('/api/v1/college', methods=['GET', 'POST'])
def college_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = College.query.filter_by(**args).offset((int(page) - 1) * int(per_page)).limit(int(per_page)).all()
        result = CollegeSchema(many=True).dump(data)
        return jsonify({'result': {'college': result.data}, 'message': "Success", 'error': False})
    else:
        college = request.json
        courses = college.get("courses", None)
        college.pop("courses", None)
        college_post = College(**college)
        college_post.save()
        for course in courses:
            course['college_id'] = college_post.id
            course_post = Course(**course)
            college_post.courses.append(course_post)
            course_post.save()
        college_result = CollegeSchema().dump(college_post)
        return jsonify({'result': {'college': college_result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/college/<int:id>', methods=['PUT', 'DELETE'])
def college_id(id):
    if request.method == 'PUT':
        put = College.query.filter_by(id=id).update(request.json)
        if put:
            College.update_db()
            s = College.query.filter_by(id=id).first()
            result = CollegeSchema(many=False).dump(s)
            return jsonify({'result': result.data, "status": "Success", 'error': False})
    else:
        c = College.query.filter_by(id=id).first()
        if not c:
            return jsonify({'result': {}, 'message': "No Found", 'error': True})
        College.delete_db(c)
        return jsonify({'result': {}, 'message': "Success", 'error': False})


@app.route('/api/v1/package', methods=['GET', 'POST'])
def package_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Package.query.filter_by(**args).offset((int(page) - 1) * int(per_page)).limit(int(per_page)).all()
        result = PackageSchema(many=True).dump(data)
        return jsonify({'result': {'package': result.data}, 'message': "Success", 'error': False})
    else:
        package = request.json
        
        days = package.get("days", None)
        amenities = package.get("amenities", None)
        package.pop("days", None)
        package.pop("amenities", None)
        package_post = College(**package)
        package_post.save()
        for day in days:
            day['package_id'] = package_post.id
            day_post = Day(**day)
            package_post.days.append(day_post)
            day_post.save()
        for amenity in amenities:
            amenity['package_id'] = package_post.id
            amenity_post = Amenity(**amenity)
            package_post.amenities.append(amenity_post)
            amenity_post.save()
        result = PackageSchema().dump(package_post)
        return jsonify({'result': {'package': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/package/<int:id>', methods=['PUT', 'DELETE'])
def package_id(id):
    if request.method == 'PUT':
        put = Package.query.filter_by(id=id).update(request.json)
        if put:
            Package.update_db()
            s = Package.query.filter_by(id=id).first()
            result = PackageSchema(many=False).dump(s)
            return jsonify({'result': result.data, "status": "Success", 'error': False})
    else:
        s = Package.query.filter_by(id=id).first()
        if not s:
            return jsonify({'result': {}, 'message': "No Found", 'error': True})
        Package.delete_db(s)
        return jsonify({'result': {}, 'message': "Success", 'error': False})


@app.route('/api/v1/student', methods=['GET', 'POST'])
def student_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Student.query.filter_by(**args).offset((int(page) - 1) * int(per_page)).limit(int(per_page)).all()
        result = StudentSchema(many=True).dump(data)
        return jsonify({'result': {'student': result.data}, 'message': "Success", 'error': False})
    else:
        post = Student(**request.json)
        post.save()
        result = StudentSchema().dump(post)
        return jsonify({'result': {'student': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/student/<int:id>', methods=['PUT', 'DELETE'])
def student_id(id):
    if request.method == 'PUT':
        put = Student.query.filter_by(id=id).update(request.json)
        if put:
            Student.update_db()
            s = Student.query.filter_by(id=id).first()
            result = StudentSchema(many=False).dump(s)
            return jsonify({'result': result.data, "status": "Success", 'error': False})
    else:
        s = Student.query.filter_by(id=id).first()
        if not s:
            return jsonify({'result': {}, 'message': "No Found", 'error': True})
        Student.delete_db(s)
        return jsonify({'result': {}, 'message': "Success", 'error': False})