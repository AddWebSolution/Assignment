from django.shortcuts import redirect, render
from .models import (
    UserMaster,
    ProgramMaster,
    UserProgram,
)
from django.db.models import Q
from django.contrib import messages


# Create your views here.



def home(request):
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "delete":
            try:
                UserMaster.objects.get(id=int(request.POST.get("object_id"))).delete()
                messages.success(request ,"User has been deleted")
            except:
                messages.error(request ,"User id does not exist")

            return redirect(request.path)

        user = request.POST.get("user")
        username = request.POST.get("username")

        if action == "add":
            try:
                UserMaster.objects.create_user(
                    user=user,
                    username=username,
                    password="Admin123"
                )
                messages.success(request, "User has been added!")
            except Exception as e:
                messages.error(request, f"Username already exist!")

        elif action == "update":
            try:
                data = UserMaster.objects.get(id=int(request.POST.get("object_id")))
                data.user=user
                data.username = username

                data.save()
                messages.success(request, "Account has been update!")    
            except:
                messages.error(request, "Invalid Username")    
            
        return redirect(request.path)

    query = request.GET.get("q", '')

    if query:
        user_objs = UserMaster.objects.filter(
            Q(user__icontains=query) |Q(username__icontains=query)
        )
    else:
        user_objs = UserMaster.objects.all()


    context = {
        "users": user_objs,
        "query":query
    }
    return render(request, "home/index.html", context)



def programs(request):
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "delete":
            try:
                ProgramMaster.objects.get(id=int(request.POST.get("object_id"))).delete()
                messages.success(request ,"Program has been deleted")
            except:
                messages.error(request ,"Program id does not exist")

            return redirect(request.path)


        name = request.POST.get("name")
        description = request.POST.get("description")

        if action == "add":
            try:
                ProgramMaster.objects.create(
                    name=name,
                    description=description
                )
                messages.success(request, "Program has been added!")
            except Exception as e:
                messages.error(request, f"Program can't be created!")

        elif action == "update":
            try:
                data = ProgramMaster.objects.get(id=int(request.POST.get("object_id")))
                data.name=name
                data.description = description
                data.save()
                messages.success(request, "Program has been update!")    
            except:
                messages.error(request, "Invalid Program id")    
            
        return redirect(request.path)

    query = request.GET.get("q", '')

    if query:
        prog_objs = ProgramMaster.objects.filter(name__icontains=query)
    else:
        prog_objs = ProgramMaster.objects.all()

    context = {
        "programs": prog_objs,
        "query":query,
    }
    return render(request, "home/programs.html", context)



def userPrograms(request):
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "delete":
            try:
                UserProgram.objects.get(id=int(request.POST.get("object_id"))).delete()
                messages.success(request ,"User Program has been deleted")
            except:
                messages.error(request ,"User Program id does not exist")

            return redirect(request.path)


        user = request.POST.get("user")
        program = request.POST.getlist("program")        
        access = request.POST.get("access")

        if action == "add":
            try:
                up = UserProgram.objects.create(user=UserMaster.objects.get(id=int(user)),access=access)
                
                for i in program:
                    up.program.add(ProgramMaster.objects.get(id=int(i)))

                up.save()    
                messages.success(request, "User Program has been added!")
            except Exception as e:
                print(e)
                messages.error(request, f"User Program can't be created!")

        elif action == "update":
            try:
                data = UserProgram.objects.get(id=int(request.POST.get("object_id")))
                data.user=UserMaster.objects.get(id=int(user))
                data.program.clear()
                for i in program:
                    data.program.add(ProgramMaster.objects.get(id=int(i)))
                data.access = access
                data.save()
                messages.success(request, "User Program has been update!")    
            except Exception as e:
                print(e)
                messages.error(request, "Invalid User Program id")    
            
        return redirect(request.path)

    query = request.GET.get("q", '')

    if query:
        obj_list = UserProgram.objects.filter(Q(user__user__icontains=query) | 
            Q(user__username__icontains=query))
    else:
        obj_list = UserProgram.objects.all()
    
    prog_objs = ProgramMaster.objects.all()
    user_objs = UserMaster.objects.all()

    show = {
        "programs": prog_objs,
        "users": user_objs,
        "object_list": obj_list,
        "query": query,
    }
    return render(request, "home/user-programs.html", show)