from flask import Blueprint, jsonify, redirect, request
from flask_wtf.csrf import generate_csrf
from flask_login import login_required, current_user
from app.models import db, User, Video, Comment
from app.forms import comment_form

video_routes = Blueprint('video', __name__)

@video_routes.route('/allVideos')
def allVideos():
    """
    Query for all videos
    """
    videos = Video.query.all()
    return { 'videos': [video.to_dict() for video in videos] }

@video_routes.route('/singleVideo/<int:video_id>')
def singleVideo(video_id):
    """
    Query for single video using video_id passed in
    """
    video = Video.query.get(video_id)
    if not video:
        return { 'error' : 'Video not found', 'status': 404}
    
    else:
        return { 'video': video.to_dict() }
    
@video_routes.route('/createVideo', methods=['POST'])
@login_required
def createVideo():
    """
    Create video
    """
    data = request.get_json()
    user = current_user
    if(data and user):
        video = Video(
            title = data['title'],
            description = data['description'],
            video = data['video'],
            thumbnail = data['thumbnail'],
            uploader = data['uploader'],
            user_id = user.id,
        )
    
        db.session.add(video)
        db.session.commit()
    
        return { 'video': video.to_dict() }
    else:
        return { 'error': 'error with data or user is not logged in' }
    

@video_routes.route('/updateVideo/<int:video_id>', methods=['PUT'])
def updateVideo(video_id):
    """
    Update Video
    """
    

@video_routes.rote('/deleteVideo/<int:video_id>', methods=['DELETE'])
def deleteVideo(video_id):
    """
    Delete Video
    """
    