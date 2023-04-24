from django.shortcuts import render , HttpResponse,redirect
from home.models import  AudioFile , UserLikedAudio
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import AudioFile, UserLikedAudio
from django.db.models import Case , When 

def homepage(request) :
    if request.user.is_anonymous :
        print(request.user.is_anonymous)
        return redirect("/login")
    audio = AudioFile.objects.all()
    return render(request, 'afterlogin.html', {'audio_files': audio})


def guest(request) :
    return(request ,'')

def signup(request) :
    if request.method=="POST" :
        name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        return redirect("login")
    return render(request ,'signup.html')

def login(request) :
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect("homepage")
        else :
            return render(request ,'login1.html')
    
    return render(request ,'login1.html')



@login_required
def logoutuser(request):
    logout(request)
    return redirect("/login") 

    


def uploader(request):

    if request.method == 'POST':
        type = request.POST['audio_or_video']
        if type == "audio":
            audio_video_file = request.FILES['audio_or_video_file']
            image_file = request.FILES['image']
            podcast_name = request.POST['podcast_name']
            podcast_speaker = request.POST['speaker']
            podcast_des = request.POST['description']

            # Save the audio file to the server
            fs = FileSystemStorage()
            image_path = f'audio_pod/{podcast_name}/{image_file.name}'
            audio_file_path = f'audio_pod/{podcast_name}/{audio_video_file.name}'
            image_filename = fs.save(image_path, image_file)
            a_file = fs.save(audio_file_path, audio_video_file)

            # Save the audio file info to the database
            audio = AudioFile(podcastname=podcast_name, podcast_des=podcast_des, podcast_speaker=podcast_speaker ,file2='',file=a_file, file1=image_filename if image_file else '')
            audio.save()
            messages.success(request, "podcast has been uploaded successfully")
        else:
            audio_video_file = request.FILES['audio_or_video_file']
            image_file = request.FILES['image']
            podcast_name = request.POST['podcast_name']
            podcast_speaker = request.POST['speaker']
            podcast_des = request.POST['description']

            # Save the video file to the server
            fs = FileSystemStorage()
            image_path = f'video_pod/{podcast_name}/{image_file.name}'
            video_file_path = f'video_pod/{podcast_name}/{audio_video_file.name}'
            image_filename = fs.save(image_path, image_file)
            v_file = fs.save(video_file_path, audio_video_file)

            # Save the video file info to the database
            video = AudioFile(podcastname=podcast_name, podcast_des=podcast_des, podcast_speaker=podcast_speaker ,file2=v_file, file='', file1=image_filename if image_file else '')
            video.save()
            messages.success(request, "podcast has been uploaded successfully")

    return render(request, 'uploader.html')


def audio_list(request):
    audio_files = AudioFile.objects.filter(file__icontains='audio_pod/')
    return render(request, 'index.html', {'audio_files': audio_files})


def video_list(request):
    video_files = AudioFile.objects.filter(file__icontains='video_pod/')
    return render(request, 'index2.html', {'video_files': video_files})



def like_audio_file(request):
    if request.method == 'POST':
        user = request.user
        audio_file_id = request.POST.get('idid')
        if audio_file_id is not None:
            try:
                audio_file_id = int(audio_file_id)
                watch = UserLikedAudio.objects.filter(user=user)
                for i in watch :
                    if audio_file_id==i.audio :
                        print("___________________________")
                        print(audio_file_id)
                        print(i.audio)
                        print("___________________________")
                else :        
                    userlikedaudio=UserLikedAudio(user=user,audio=audio_file_id)
                    userlikedaudio.save()
            except ValueError:
                # Handle the case where audio_file_id is not a valid integer
                pass
        
        audio = AudioFile.objects.all()
        return render(request, 'afterlogin.html', {'audio_files': audio})


    # if request.method == 'POST':
    #     user = request.user
    #     audio_file_id = request.POST['idid']
    #     watch = UserLikedAudio.objects.filter(user=user)
    #     for i in watch :
    #         if audio_file_id==i.audio :
    #             print("___________________________")
    #             print(audio_file_id)
    #             print(i.audio)
    #             print("___________________________")
    #     else :        
    #         userlikedaudio=UserLikedAudio(user=user,audio=audio_file_id)
    #         userlikedaudio.save()
    #     audio = AudioFile.objects.all()
    #     return render(request, 'afterlogin.html', {'audio_files': audio})
    wl=UserLikedAudio.objects.filter(user=request.user)
    ids=[]
    for i in wl :
        ids.append(i.audio)

    preserved = Case(*[When(pk=pk ,then=pos) for pos,pk in enumerate(ids)])
    #song = AudioFile.objects.filter(podcast_id__in=ids).order_by(preserved)
    song = AudioFile.objects.all()

    return render(request , "likedlist.html" , {'song': song})
        