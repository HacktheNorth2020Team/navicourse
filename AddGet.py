

def AddUser(session, u_id, nm):
    new_user = Users(user_id=u_id,
                     name=nm)
    session.add(new_user)

def GetUser(session, u_id):
    users = session.query.filter_by(user_id=u_id).first()
    return list(map(lambda user: {'user_id': user.user_id,
                                  'name': user.name},
                    users))

def AddRating(session, u_id, c_id, rt):
    new_rating = Ratings(user_id=u_id,
                         course_id=c_id,
                         rating=rt)
    session.add(new_rating)

def GetRating(session, u_id, c_id):
    ratings = session.query.filter_by(user_id=u_id) \
                           .filter_by(course_id=c_id).first()
    return list(map(lambda rating: {'user_id': rating.user_id,
                                    'course_id': rating.course_id,
                                    'rating': rating.rating},
                    ratings))

def AddCourseInProgress(session, u_id, c_id):
    newCIP = CoursesInProgress(user_id=u_id,
                               course_id=c_id)
    session.add(newCIP)

def GetCourseInProgress(session, u_id):
    CIPs = session.query.filter_by(user_id=u_id).all()
    return list(map(lambda CIP: {'user_id': CIP.user_id,
                                 'course_id': CIP.course_id},
                    CIPS))
