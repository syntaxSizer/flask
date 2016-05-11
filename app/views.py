
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, \
    login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/TMT')
def TMT():
    print' Hi!'
    return render_template('/TMT',title='TMT',user=user
<!-- extends from base layout -->
st=post)
{% extends "base.html" %}

{% block content %}
<!-- js script that renders openID -->
  <script type="text/javascript">
    function set_openid(openid, pr)
    {
        u = openid.search('<username>');
        if (u != -1) {
            // openid requires username
            user = prompt('Enter your ' + pr + ' username:');
            openid = openid.substr(0, u) + user;
        }
        form = document.forms['login'];
        form.elements['openid'].value = openid;
    }
</script>
 </script>
    <h1>Sign In</h1>
    <form action="" method="post" name="login">
        {{ form.hidden_tag() }}
        <p>
            Please enter your OpenID, or select one of the providers below:<br>
            {{ form.openid(size=80) }}
            {% for error in form.openid.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}<br>
            |{% for pr in providers %}
                <a href="javascript:set_openid('{{ pr.url }}', '{{ pr.name }}');">{{ pr.name }}</a> |
            {% endfor %}
        </p>
        <p>{{ form.remember_me }} Remember Me</p>
        <p><input type="submit" value="Sign In"></p>
    </form>
{% endblock %}
