import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateTicketForm, UpdateTicketForm
from .models import ticket



def ticket_details(request):
    ticket= tickets.object.get()
    context ={'ticket':ticket}
    return render(request,"ticket/ticket_details.html", context)



def create_ticket(request):
    if request.method =='POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var= form.save(commit=False)
            var.created_by= request.user
            var.tickets_status='Pending'
            var.save()
            messages.info(request, 'Ticket registerd')
            return redirect ('dashboard')
        else :
            messages.warning (request,'Error, Kindly retry')
            return redirect ("create_ticket")
    else :
        form =CreateTicketForm()
        context = {'form':form}
        return render(request,'ticket/create_ticket.html', context)



def update_ticket(request):
    ticket = ticket.objects.get()
    if request.method =='POST':
        form = UpdateTicketForm(request.POST, instance =ticket)
        if form._isvalid():
            form.save()
            messages.info(request, 'Ticket Updated')
            return redirect ('dashboard')
        else :
            messages.warning (request,'Error, Kindly retry')
            return redirect ("update_ticket")
    else :
        form = UpdateTicketForm(instance=ticket)
        context = {'form':form}
        return render(request,'ticket/update_ticket.html', context)


def all_tickets(request):
    tickets= tickets.object.filter(created_by= request.user)
    context={'tickets':tickets}
    return render(request,"ticket/all_ticket.html", context)


def ticket_queue(request):
    tickets= tickets.object.filter(tickets_status= 'Pending')
    context= {'tickets':tickets}
    return render(request,"ticket/ticket_queue.html", context)


def accept_ticket(request):
    ticket = ticket.objects.get()
    ticket.assinged_to=request.user
    ticket.ticket_status='Active'
    ticket.accepted_date= datetime.datetime.now()
    ticket.save()
    messages.info(request, 'Ticket accepted')
    return redirect('ticket_queue')


def close_ticket(request):
    ticket = ticket.objects.get()
    ticket.ticket_status='Completed'
    ticket.is_resolved= True
    ticket.closed_date= datetime.datetime.now()
    ticket.save()
    messages.info(request, 'Ticket resolved')
    return redirect('ticket_queue')



def workspace(request):
    ticket = tickets.objects.filter(assigned_to= request.user)
    context = {'ticket':ticket}
    return render(request,"ticket/workspace.html", context)

