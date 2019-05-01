"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    # print ("aaaaaa",hackbright.get_student_by_github(github))

    # if hackbright.get_student_by_github(github):

    first, last, github = hackbright.get_student_by_github(github)

        # html = render_template("student_info.html",
        #                         first = first,
        #                         last = last,
        #                         github=github)

    return render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)


@app.route('/student-search', methods=["POST"])
def get_student_form():
    """"Show form for searching for a student."""

    return render_template("student_search.html")

@app.route('/student-add-form')
def display_form():
    """show form for adding a student"""

    return render_template('add_new_student.html')




@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)
 
    return render_template('display_new_student.html', 
                            first_name=first_name,
                            last_name=last_name,
                            github=github)



# @app.route('/student-search', methods=["GET"])
# def show_new_student():

#     git_hub = request.form.get('github')
#     # added_student = get_student_by_github("github")
#     get_student_by_github("github")
#     print(added_student)

#     # html = render_template("add_new_student.html",
#     #                         last_name = added_student['last_name'],
#     #                         github=added_student['github'],
#     #                         first_name = added_student['first_name'],
#     #                         

#     html = render_template("add_new_student.html",
#                             last_name = last_name,
#                             github=github,
#                             first_name =first_name,)



#     return html







if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
