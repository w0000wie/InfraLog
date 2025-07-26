from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageReplyForm, MessageForm # o MessageReplyForm si lo prefieres

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-created_at')
    return render(request, 'messages_app/inbox.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messages_app/send_message.html', {'form': form})

@login_required
def view_message(request, pk):
    message = get_object_or_404(Message, id=pk, recipient=request.user)

    if request.method == 'POST':
        form = MessageReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.sender = request.user
            reply.recipient = message.sender
            reply.save()
            return redirect('inbox')
    else:
        form = MessageReplyForm()

    return render(request, 'messages_app/view_message.html', {
        'message': message,
        'form': form,
    })


@login_required
def message_detail(request, pk):
    original_message = get_object_or_404(Message, pk=pk, recipient=request.user)

    if request.method == 'POST':
        form = MessageReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.sender = request.user 
            reply.recipient = original_message.sender  
            reply.subject = f"RE: {original_message.subject}"  
            reply.save()
            return redirect('inbox')  
    else:
        form = MessageReplyForm()

    return render(request, 'messages_app/message_detail.html', {
        'message': original_message,
        'form': form
    })