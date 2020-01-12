from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        # Create a form instance from POST data.
        form = ItemForm(request.POST)
        if form.is_valid():
            # Save a new Item object from the form's data.
            form.save()
            all_items = Item.objects.all()
            return render(request, 'index.html', {'all_items':all_items})
    else: # default behaviour
        all_items = Item.objects.all()
        return render(request, 'index.html', {'all_items':all_items})

def delete(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return redirect('index')

def cross_off(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.completed = True
    item.save()
    return redirect('index')

def uncross(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.completed = False
    item.save()
    return redirect('index')

@login_required
def edit(request, item_id):
    if request.method == 'POST':
        # Create a form to edit an existing Item, but use
        # POST data to populate the form.
        item = get_object_or_404(Item, pk=item_id)
        form = ItemForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        item = get_object_or_404(Item, pk=item_id)
        return render(request, 'edit.html', {'item':item})
