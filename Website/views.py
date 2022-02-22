from flask import Blueprint, render_template
# from flask_login import login_required, current_user
# from . import db
# import json

views = Blueprint('views', __name__)


@views.route('/')
# @login_required
def home():
    return "<h1>hello this is a try</h1>"


# # @views.route('/delete-note', methods=['POST'])
# # def delete_note():
# #     note = json.loads(request.data)
# #     noteId = note['noteId']
# #     note = Note.query.get(noteId)
# #     if note:
# #         if note.user_id == current_user.id:
# #             db.session.delete(note)
# #             db.session.commit()

# #     return jsonify({})