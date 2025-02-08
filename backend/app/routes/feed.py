from flask import Blueprint, request, jsonify
from backend.app.models.post import Post, Comment
from backend.app.routes.auth import token_required
from backend.app import db
from datetime import datetime

feed_bp = Blueprint('feed', __name__)

@feed_bp.route('/posts', methods=['GET'])
@token_required
def get_posts(current_user):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    category = request.args.get('category')
    
    query = Post.query
    if category:
        query = query.filter_by(category=category)
    
    posts = query.order_by(Post.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return jsonify({
        'posts': [post.to_dict() for post in posts.items],
        'total': posts.total,
        'pages': posts.pages,
        'current_page': posts.page
    })

@feed_bp.route('/posts', methods=['POST'])
@token_required
def create_post(current_user):
    data = request.get_json()
    
    post = Post(
        content=data['content'],
        category=data['category'],
        image_url=data.get('image_url'),
        user_id=current_user.id
    )
    
    db.session.add(post)
    db.session.commit()
    
    # Award points for creating a post
    current_user.points += 5
    db.session.commit()
    
    return jsonify(post.to_dict()), 201

@feed_bp.route('/posts/<int:post_id>/like', methods=['POST'])
@token_required
def like_post(current_user, post_id):
    post = Post.query.get_or_404(post_id)
    post.likes += 1
    db.session.commit()
    return jsonify(post.to_dict())

@feed_bp.route('/posts/<int:post_id>/comments', methods=['POST'])
@token_required
def add_comment(current_user, post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    
    comment = Comment(
        content=data['content'],
        post_id=post_id,
        user_id=current_user.id
    )
    
    db.session.add(comment)
    
    # Award points for commenting
    current_user.points += 2
    db.session.commit()
    
    return jsonify(comment.to_dict()), 201

@feed_bp.route('/posts/<int:post_id>/comments', methods=['GET'])
@token_required
def get_comments(current_user, post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.desc()).all()
    return jsonify([comment.to_dict() for comment in comments])
