from django.shortcuts import render,HttpResponse

from django.http import JsonResponse

# Create your views here.




# ALLOWED_TYPES = ['jpg', 'jpeg', 'png', 'gif',"pdf"]


# from django.views.decorators.csrf import csrf_exempt, csrf_protect
# @csrf_protect

# @csrf_exempt

from .models import Upload



from django.core.files.storage import FileSystemStorage




def home(request):


    return render(request,'home.html')
    # return HttpResponse("Conline Here")


def submission(request):


    return render(request,'submission.html')
    # return HttpResponse("Conline Here")



def child(request):


    return render(request,'child.html')
    # return HttpResponse("Conline Here")



def upload(request):

    if request.method == "POST":

        # filetype = request.POST.get('type')
        filetype=str(request.GET['type'])

        # print(filetype)


        ALLOWED_TYPES=[]
        file_loc="unkown/"

        if filetype=="pdf":
            ALLOWED_TYPES.append("pdf")
            file_loc="pdf/"
            
        else:
            return JsonResponse({"message": "Invalid Query Type"},status=422)
            

        fileobj = request.FILES


        file_name=str(fileobj['file']).lower()

        spliter=file_name.split(".")

        if(spliter[-1] in ALLOWED_TYPES):



            # uploadobj=Upload.objects.create(upload_file=file)
            # uploadobj.save()
            file_path=file_loc+file_name
            # print(file_name)


            fs = FileSystemStorage() 
            savefile = fs.save(file_path, fileobj['file']) 
            # the fileurl variable now contains the url to the file. This can be used to serve the file when needed. 
            fileurl = fs.url(savefile)

            urlsplitter=fileurl.split("/")

            newfilename=urlsplitter[-1]

            # print(fileurl)

            msg="File uploaded "+fileurl
            print(msg)


            return JsonResponse({"message": msg,"filename":newfilename,"filepath":fileurl},status=200)





        else:
            msg="Invalid File Type "+file_name
            print(msg)
            return JsonResponse({"message": msg},status=422)
            

        
        

    return render(request, 'upload.html')
    