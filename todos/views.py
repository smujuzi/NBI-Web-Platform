from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import NBI
from .resources import NBIResource
from TodoProject import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import NBIForm
from account.models import Account



# Create your views here.


def edit(request, todo_id):

    print('todo_id: ', todo_id)
    todo = NBI.objects.get(id=todo_id)
    print('todo: ', todo)
    context = {'edit': todo}
    print('Edit Function')
    return render(request, 'todos/edit.html', context)


def change(request, todo_id):
    print('Change Function')
    print('The beginning')

    print('todo_id: ', todo_id)
    todo = NBI.objects.get(id=todo_id)
    print('todo: ', todo)
    context = {'edit': todo}

    edit.no = request.POST['no']
    edit.mda = request.POST['mda']
    edit.mda_site = request.POST['mda_site']
    edit.location = request.POST['location']
    edit.district = request.POST['district']
    edit.period_of_nbi_extension = request.POST['period_of_nbi_extension']
    edit.status = request.POST['status']
    edit.internet = request.POST['internet']
    edit.leased_mda = request.POST['leased_mda']
    edit.leased_ifms = request.POST['leased_ifms']
    edit.dark_fibre = request.POST['dark_fibre']
    edit.fy_period_of_connectivity = request.POST['fy_period_of_connectivity']
    edit.date_of_connection_internet_bandwidth = request.POST['date_of_connection_internet_bandwidth']
    edit.date_of_connection_ifms = request.POST['date_of_connection_ifms']
    edit.date_of_connection_leased_lines = request.POST['date_of_connection_leased_lines']
    edit.date_of_connection_dark_fibre = request.POST['date_of_connection_dark_fibre']
    edit.internet_capacity = request.POST['internet_capacity']
    edit.leased_mda_capacity = request.POST['leased_mda_capacity']
    edit.leased_ifms_capacity = request.POST['leased_ifms_capacity']
    edit.dark_fibre_quantity = request.POST['dark_fibre_quantity']
    edit.fibre_done = request.POST['fibre_done']
    edit.odf_installed = request.POST['odf_installed']
    edit.latitude = request.POST['latitude']
    edit.longitude = request.POST['longitude']
    edit.comments = request.POST['comments']

    nbi_info = NBI(no=edit.no, mda=edit.mda, mda_site=edit.mda_site, location=edit.location, district=edit.district,
                   period_of_nbi_extension=edit.period_of_nbi_extension,
                   status=edit.status, internet=edit.internet, leased_mda=edit.leased_mda, leased_ifms=edit.leased_ifms,
                   dark_fibre=edit.dark_fibre, fy_period_of_connectivity=edit.fy_period_of_connectivity,
                   date_of_connection_internet_bandwidth=edit.date_of_connection_internet_bandwidth,
                   date_of_connection_ifms=edit.date_of_connection_ifms,
                   date_of_connection_leased_lines=edit.date_of_connection_leased_lines,
                   date_of_connection_dark_fibre=edit.date_of_connection_dark_fibre, internet_capacity=edit.internet_capacity,
                   leased_mda_capacity=edit.leased_mda_capacity, leased_ifms_capacity=edit.leased_ifms_capacity,
                   dark_fibre_quantity=edit.dark_fibre_quantity, fibre_done=edit.fibre_done, odf_installed=edit.odf_installed,
                   latitude=edit.latitude, longitude=edit.longitude, comments=edit.comments)

    nbi_info.save()
    print('At the END')
    #return redirect('/records/')
    return render(request, 'todos/table.html',context)


def createOrder(request):
    form = NBIForm()
    if request.method == 'POST':
        form = NBIForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/records/')

    context = {'form': form}
    return render(request, 'todos/order_form.html', context)


def updateOrder(request, pk):

    order = NBI.objects.get(id=pk)
    form = NBIForm(instance=order)


    if request.method == 'POST':
        form = NBIForm(request.POST,instance=order)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/records/')

    context = {'form': form}
    print(form)

    return render(request, 'todos/order_form.html', context)


def deleteOrder(request, pk):
    order = NBI.objects.get(id=pk)

    if request.method == "POST":
        order.delete()
        return redirect('/records/')
    context = {'item': order}

    return render(request, 'todos/delete.html', context)


def home_screen_view(request):
    accounts = Account.objects.all()

    context = {'accounts': accounts}
    print('accounts: ', accounts)
    return render(request, 'todos/cover.html', context)

def users_view(request):
    accounts = Account.objects.all()

    context = {'accounts': accounts}
    print('accounts: ', accounts)
    return render(request, 'todos/manage_users.html', context)


#
# def home_screen_view(request):
#     context = {'header': NBI.objects.all()}
#     return render(request, 'todos/cover.html', context)


def list_todo_items(request):
    context = {'todo_list': NBI.objects.all()}
    return render(request, 'todos/table.html', context)


def list_todo_items_user(request):
    context = {'todo_list': NBI.objects.all()}
    return render(request, 'todos/table_user.html', context)


def insert_todo_item(request: HttpRequest):
    no = request.POST['no']
    mda = request.POST['mda']
    mda_site = request.POST['mda_site']
    location = request.POST['location']
    district = request.POST['district']
    period_of_nbi_extension = request.POST['period_of_nbi_extension']
    status = request.POST['status']
    internet = request.POST['internet']
    leased_mda = request.POST['leased_mda']
    leased_ifms = request.POST['leased_ifms']
    dark_fibre = request.POST['dark_fibre']
    fy_period_of_connectivity = request.POST['fy_period_of_connectivity']
    date_of_connection_internet_bandwidth = request.POST['date_of_connection_internet_bandwidth']
    date_of_connection_ifms = request.POST['date_of_connection_ifms']
    date_of_connection_leased_lines = request.POST['date_of_connection_leased_lines']
    date_of_connection_dark_fibre = request.POST['date_of_connection_dark_fibre']
    internet_capacity = request.POST['internet_capacity']
    leased_mda_capacity = request.POST['leased_mda_capacity']
    leased_ifms_capacity = request.POST['leased_ifms_capacity']
    dark_fibre_quantity = request.POST['dark_fibre_quantity']
    fibre_done = request.POST['fibre_done']
    odf_installed = request.POST['odf_installed']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    comments = request.POST['comments']

    nbi_info = NBI(no=no, mda=mda, mda_site=mda_site, location=location, district=district,
                   period_of_nbi_extension=period_of_nbi_extension,
                   status=status, internet=internet, leased_mda=leased_mda, leased_ifms=leased_ifms,
                   dark_fibre=dark_fibre, fy_period_of_connectivity=fy_period_of_connectivity,
                   date_of_connection_internet_bandwidth=date_of_connection_internet_bandwidth,
                   date_of_connection_ifms=date_of_connection_ifms,
                   date_of_connection_leased_lines=date_of_connection_leased_lines,
                   date_of_connection_dark_fibre=date_of_connection_dark_fibre, internet_capacity=internet_capacity,
                   leased_mda_capacity=leased_mda_capacity, leased_ifms_capacity=leased_ifms_capacity,
                   dark_fibre_quantity=dark_fibre_quantity, fibre_done=fibre_done, odf_installed=odf_installed,
                   latitude=latitude, longitude=longitude, comments=comments)
    nbi_info.save()

    return redirect('/todos/list/')


def delete_todo_item(request, todo_id):
    print('todo_id: ', todo_id)
    todo_to_delete = NBI.objects.get(id=todo_id)
    print('todo_to_delete: ', todo_to_delete)
    todo_to_delete.delete()
    return redirect('/todos/list/')


def add_record(request):
    context = {'add_record': NBI.objects.all()}
    return render(request, 'todos/add_record.html', context)


def charts(request):
    context = dict()
    context['internet'] = NBI.objects.filter(internet="YES").count()
    print("The value of internet is = ", context['internet'])

    context['leased_mda'] = NBI.objects.filter(leased_mda="YES").count()
    print('The value of leased_mda is = ', context['leased_mda'])

    context['leased_ifms'] = NBI.objects.filter(leased_ifms="YES").count()
    print('The value of leased_ifms is = ', context['leased_ifms'])

    context['dark_fibre'] = NBI.objects.filter(dark_fibre="YES").count()
    print('The value of dark_fibre is = ', context['dark_fibre'])

    context['internet_capacity_5'] = NBI.objects.filter(internet_capacity="5").count()
    print('The value of internet_capacity_5 is = ', context['internet_capacity_5'])

    context['internet_capacity_b'] = NBI.objects.filter(internet_capacity="YES").count()
    print('The value of internet_capacity_b is = ', context['internet_capacity_b'])

    context['internet_capacity_10'] = NBI.objects.filter(internet_capacity="10").count()
    print('The value of internet_capacity_10 is = ', context['internet_capacity_10'])

    context['map'] = NBI.objects.all()
    print('The value of maps is = ', context['map'])
    print('Default_map function')

    context['total'] = NBI.objects.all().count()
    print('Total number of sites = ', context['total'])
    print('Default_map function')
    return render(request, 'todos/charts.html', context, )


def export(request):
    nbi_resource = NBIResource()
    dataset = nbi_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="nbi.csv"'
    return response


def default_map(request):
    context = {'map': NBI.objects.all()}
    print(context)
    print('Default_map function')
    return render(request, 'todos/default.html', context)


# FRONT END DEVELOPMENT


def checkout(request):
    context = {'add_record': NBI.objects.all()}
    return render(request, 'todos/checkout_example.html', context)


def dashboard_map(request):
    context = dict()
    context['internet'] = NBI.objects.filter(internet="YES").count()
    print("The value of internet is = ", context['internet'])

    context['leased_mda'] = NBI.objects.filter(leased_mda="YES").count()
    print('The value of leased_mda is = ', context['leased_mda'])

    context['leased_ifms'] = NBI.objects.filter(leased_ifms="YES").count()
    print('The value of leased_ifms is = ', context['leased_ifms'])

    context['dark_fibre'] = NBI.objects.filter(dark_fibre="YES").count()
    print('The value of dark_fibre is = ', context['dark_fibre'])

    context['internet_capacity_5'] = NBI.objects.filter(internet_capacity="5").count()
    print('The value of internet_capacity_5 is = ', context['internet_capacity_5'])

    context['internet_capacity_b'] = NBI.objects.filter(internet_capacity="YES").count()
    print('The value of internet_capacity_b is = ', context['internet_capacity_b'])

    context['internet_capacity_10'] = NBI.objects.filter(internet_capacity="10").count()
    print('The value of internet_capacity_10 is = ', context['internet_capacity_10'])

    context['map'] = NBI.objects.all()
    print('The value of maps is = ', context['map'])
    print('Default_map function')

    context['total'] = NBI.objects.all().count()
    print('Total number of sites = ', context['total'])
    print('DASHBOOOOAAARRRDDD')
    return render(request, 'todos/dashboard_example_map.html', context)


def dashboard_chart(request):
    context = dict()
    context['internet'] = NBI.objects.filter(internet="YES").count()
    print("The value of internet is = ", context['internet'])

    context['leased_mda'] = NBI.objects.filter(leased_mda="YES").count()
    print('The value of leased_mda is = ', context['leased_mda'])

    context['leased_ifms'] = NBI.objects.filter(leased_ifms="YES").count()
    print('The value of leased_ifms is = ', context['leased_ifms'])

    context['dark_fibre'] = NBI.objects.filter(dark_fibre="YES").count()
    print('The value of dark_fibre is = ', context['dark_fibre'])

    context['internet_capacity_5'] = NBI.objects.filter(internet_capacity="5").count()
    print('The value of internet_capacity_5 is = ', context['internet_capacity_5'])

    context['internet_capacity_b'] = NBI.objects.filter(internet_capacity="YES").count()
    print('The value of internet_capacity_b is = ', context['internet_capacity_b'])

    context['internet_capacity_10'] = NBI.objects.filter(internet_capacity="10").count()
    print('The value of internet_capacity_10 is = ', context['internet_capacity_10'])

    context['map'] = NBI.objects.all()
    print('The value of maps is = ', context['map'])
    print('Default_map function')

    context['total'] = NBI.objects.all().count()
    print('Total number of sites = ', context['total'])
    return render(request, 'todos/dashboard_example_chart.html', context)


def dashboard(request):
    context = dict()
    context['internet'] = NBI.objects.filter(internet="YES").count()
    print("The value of internet is = ", context['internet'])

    context['leased_mda'] = NBI.objects.filter(leased_mda="YES").count()
    print('The value of leased_mda is = ', context['leased_mda'])

    context['leased_ifms'] = NBI.objects.filter(leased_ifms="YES").count()
    print('The value of leased_ifms is = ', context['leased_ifms'])

    context['dark_fibre'] = NBI.objects.filter(dark_fibre="YES").count()
    print('The value of dark_fibre is = ', context['dark_fibre'])

    context['internet_capacity_5'] = NBI.objects.filter(internet_capacity="5").count()
    print('The value of internet_capacity_5 is = ', context['internet_capacity_5'])

    context['internet_capacity_b'] = NBI.objects.filter(internet_capacity="YES").count()
    print('The value of internet_capacity_b is = ', context['internet_capacity_b'])

    context['internet_capacity_10'] = NBI.objects.filter(internet_capacity="10").count()
    print('The value of internet_capacity_10 is = ', context['internet_capacity_10'])

    context['map'] = NBI.objects.all()
    print('The value of maps is = ', context['map'])
    print('Default_map function')

    context['total'] = NBI.objects.all().count()
    print('Total number of sites = ', context['total'])
    print('Dashboard')
    return render(request, 'todos/dashboard_example.html', context)

# FRONT END DEVELOPMENT
