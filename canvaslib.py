def format_url(uri):
    return 'https://courseworks2.columbia.edu/api/v1{}'.format(uri)


def auth_header(token):
    return {
            'Authorization': 'Bearer {}'.format(token),
    }


class GradesheetEntry(object):
    def __init__(self, user_id, grade=None, comment=None):
        self.user_id = user_id

        # poor man's type checking
        if grade is not None:
            float(grade)
        if comment is not None:
            pass
            # comment.decode('utf-8') # this used to check for invalid characters in python2

        self.grade = grade
        self.comment = comment


def update_grades(course_id, assignment_id, gradesheet):
    uri = '/courses/{}/assignments/{}/submissions/update_grades'.format(
            course_id, assignment_id)

    data = {}
    for e in gradesheet:
        if e.grade is not None:
            data['grade_data[sis_user_id:%s][posted_grade]' % e.user_id] = e.grade
        if e.comment is not None:
            data['grade_data[sis_user_id:%s][text_comment]' % e.user_id] = e.comment

    return uri, data
