from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import redirect
from django.utils.html import format_html
from unfold.admin import ModelAdmin

from ..models.order import OrderModel
from django.urls import reverse




def order_images(obj):
    images = []
    for item in obj.order_item.all():
        if item.book.image:
            images.append(f'''
                <img src="{item.book.image.url}" width="50" height="70"
                style="margin: 4px; border-radius: 8px;" />
            ''')

    if not images:
        return "-"

    return format_html(
        '<div style="display: flex; flex-wrap: wrap; gap: 4px; max-width: 250px;">{}</div>',
        format_html(''.join(images))
    )

order_images.short_description = "Rasmlar"


def colored_id(obj):
    return format_html(
        '<span style="font-weight: bold; color: #3b82f6;">#{}<span>', obj.id
    )

colored_id.short_description = "ID"


def colored_status(obj):
    color = {
        'pending': 'orange',
        'processing': 'blue',
        'ready': 'green',
        'cancelled': 'red',
    }.get(obj.status, 'gray')

    return format_html(
        '<span style="color: {}; font-weight: 600;">{}</span>',
        color,
        obj.status.capitalize()
    )

colored_status.short_description = 'Holat'



def mark_ready_button(obj):
    if obj.status != 'ready':
        url = reverse("mark_ready", args=[obj.id])
        return format_html(
            '''
            <a href="{}"
                style="
                    color: #46FF50;
                    font-weight: bold;
                    background-color: #1d2230;
                    padding: 6px 14px;
                    border-radius: 6px;
                    text-decoration: none;
                    transition: background-color 0.2s ease;
                    display: inline-block;
                "
                onmouseover="this.style.backgroundColor='#2a2f40';"
                onmouseout="this.style.backgroundColor='#1d2230';"
            >
                Tayyor deb belgilash
            </a>
            ''',
            url
        )
    return "-"







def get_custom_urls(admin_class):
    return [
        path(
            '<int:order_id>/mark-ready/',
            admin_class.admin_site.admin_view(lambda request, order_id: mark_ready(request, order_id, admin_class)),
            name='order-mark-ready',
        ),
    ]


def mark_ready(request, order_id, admin_class):
    order = OrderModel.objects.get(pk=order_id)
    if order.status != 'ready':
        order.status = 'ready'
        order.save()
        admin_class.send_notification(order)
        admin_class.message_user(request, f"Buyurtma #{order.id} tayyor bo‘ldi va xabar yuborildi.", messages.SUCCESS)
    else:
        admin_class.message_user(request, f"Buyurtma #{order.id} allaqachon tayyor.", messages.WARNING)
    return redirect(f"../../{order_id}/change/")



