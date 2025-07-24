from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import redirect
from django.utils.html import format_html
from unfold.admin import ModelAdmin

from ..models.order import OrderModel


# === BOShQaDAN YAZILGAN FUNKSIYaLAR ===

def product_images(obj):
    images = []
    image = obj.image
    if image:
        images.append(f'''
            <img src="{image.url}" width="50" height="70"
            style="margin: 4px; border-radius: 8px;" />
        ''')

    if not images:
        return "-"

    return format_html(
        '<div style="display: flex; flex-wrap: wrap; gap: 4px; max-width: 250px;">{}</div>',
        format_html(''.join(images))
    )

product_images.short_description = "Rasmlar"


def colored_id(obj):
    return format_html(
        '<span style="font-weight: bold; color: #3b82f6;">#{}<span>', obj.id
    )

colored_id.short_description = "ID"




