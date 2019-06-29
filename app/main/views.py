from flask import render_template, request, redirect,url_for,abort
from . import main
from ..models import Pitch,User, Comment
from .forms import PitchForm, UpdateProfile, CommentsForm
from flask_login import login_required, current_user
from .. import db,photos
import markdown2 

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "1 min in an elevator with an investor to sell your idea"

    return render_template('index.html',title = title)


@main.route('/categories/')
def categories():

    '''
    View categories page function that returns the categories details page and its data
    '''

    pitches = Pitch.get_pitches('categories')

    return render_template('categories.html', pitches = pitches)

@main.route('/business/')
def business():

    '''
    View categories page function that returns the business category details page and its data
    '''

    pitchBusiness = Pitch.query.filter_by(pitch_category ="Business").all()

    return render_template('business.html', pitchBusiness = pitchBusiness)

@main.route('/software/')
def software():

    '''
    View categories page function that returns the software category details page and its data
    '''

    pitchSoft = Pitch.query.filter_by(pitch_category ="Software").all()

    return render_template('software.html', pitchSoft = pitchSoft)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    new_pitch = None

    if form.validate_on_submit():
        category = form.category.data
        title = form.title.data
        pitch = form.pitch.data
        
        new_pitch = Pitch(category = category, pitch = pitch, title = title, user = current_user)

        new_pitch.save_pitch()

        return redirect(url_for('.index'))

    return render_template('new_pitch.html', pitch_form = form, new_pitch=new_pitch)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/pitch/<int:id>')
def single_pitch(id):
    pitch = Pitch.query.get(id)
    if pitch is None:
        abort(404)
    format_pitch = markdown2.markdown(pitch.pitch,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('pitch.html',pitch = pitch,format_pitch=format_pitch)


@main.route("/pitch/new/comment/<int:id>",methods=["GET","POST"])
@login_required
def comment(id):
    
    pitch = Pitch.query.get(id)
    commentForm = CommentsForm()

    if id is None:
        abort(404)

    if comment_form.validate_on_submit():
        comments = commentForm.comment.data
        new_comment = Comment(comments = comments, pitch_id = id, user = current_user)

        new_comment.save_comment()
        return redirect(url_for('.comment',id=id))

    all_comments = Comment.query.filter_by(pitch_id=id).all()

    return render_template("new_comment.html",pitch = pitch, id=id,comment_form = commentForm, all_comments = all_comments)