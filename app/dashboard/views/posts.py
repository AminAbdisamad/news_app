from flask import render_template, flash, redirect, url_for
from app.dashboard.models.post import Post
from app.dashboard.forms.post_form import PostForm
from app.dashboard.routes import dashboard

# GET ALL THE POSTS


@dashboard.route('/posts/')
def posts():
    posts = Post.query.all()
    return render_template("posts/posts.html", posts=posts)


# CREATE A NEW POST
@dashboard.route('/create-post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        print(form.title.data, form.category.data, form.description.data)
        post = Post(title=form.title.data, description=form.description.data,
                    category=form.category.data, source=form.source.data)
        post.save()
        flash("Post Created Successfully", "is-success")
        return redirect(url_for("dashboard.posts"))

    # categories = Category.query.all()
    # if request.method == 'POST':
    #     if request.form:
    #         title = request.form.get("title")
    #         description = request.form.get("description")
    #         category = request.form.get("category")
    #         source = request.form.get("source")
    #         post = Post(title=title, description=description,
    #                     category=category, source=source)
    #         post.save()
    #         flash("Post Created Successfully", "is-success")
    #         return redirect(url_for("dashboard.posts"))
    return render_template('posts/create_post.html', form=form)


# DELETE A POST
@dashboard.route("/posts/delete/<id>")
def delete_post(id):
    # Get post with the id
    post = Post.query.get_or_404(id)
    # Check if the user has permission to delete
    if post:
        post.delete()
        flash(f"{post.title} deleted successfully", "is-success")
        return redirect(url_for('dashboard.posts'))
    return render_template("posts/delete_post.html", post=post)
