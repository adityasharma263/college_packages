from ts.model.college_packages import College, Package, Day, Student, Course, Amenity, Image, Availability, CollegeSelectedPackage
from ts import app, db
from sqlalchemy import or_
from flask import jsonify, request, session
from ts.schema.college_package import CollegeSchema, PackageSchema, DaySchema, StudentSchema, CourseSchema, AmenitySchema, CollegeSelectedPackageSchema


@app.route('/api/v1/college', methods=['GET', 'POST'])
def college_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        package_id = request.args.get('package_id')
        args.pop('package_id', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        q = db.session.query(College).outerjoin(College.packages)
        for key in args:
            if key in College.__dict__:
                q = q.filter(getattr(College, key) == args[key])
            elif key in Package.__dict__:
                q = q.filter(getattr(Package, key) == args[key])
        if package_id:
            q = q.filter(Package.id == package_id)
        data = q.offset((int(page) - 1) * int(per_page)).limit(int(per_page)).all()
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
        print(result.data,"rrtthgfvfgrhtyhrg" )
        return jsonify({'result': {'package': result.data}, 'message': "Success", 'error': False})
    else:
        package = request.json
        days = package.get("days", None)
        amenities = package.get("amenities", None)
        availabilities = package.get("availabilities", None)
        images = package.get("images", None)
        package.pop("availabilities", None)
        package.pop("days", None)
        package.pop("images", None)
        package.pop("amenities", None)
        package_post = Package(**package)
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
        for image in images:
            image['package_id'] = package_post.id
            image_post = Image(**image)
            package_post.images.append(image_post)
            image_post.save()
        for availability in availabilities:
            availability['package_id'] = package_post.id
            availability_post = Availability(**availability)
            package_post.availabilities.append(availability_post)
            availability_post.save()
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


@app.route('/api/v1/booking', methods=['GET', 'POST'])
def booking_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = CollegeSelectedPackage.query.filter_by(**args).offset((int(page) - 1) * int(per_page)).limit(int(per_page)).all()
        result = CollegeSelectedPackageSchema(many=True).dump(data)
        return jsonify({'result': {'bookings': result.data}, 'message': "Success", 'error': False})
    else:
        print("aaaaaaaa")
        if 'post_data' in session:
            post_data = session["post_data"]
            print(post_data)
            college_id = College.query.filter_by(username=post_data['username']).first().id
            booking_post_data = request.json
            booking_post_data['college_id'] = college_id
            print(booking_post_data,"data")
            post = CollegeSelectedPackage(**booking_post_data)
            post.save()
            result = CollegeSelectedPackageSchema().dump(post)
            return jsonify({'result': {'booking': result.data}, 'message': "Success", 'error': False})