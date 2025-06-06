# scripts/upload_all_images_to_cloudinary.py

import os
import django
import cloudinary.uploader
import cloudinary

import sys

# Ajoute la racine du projet au path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Initialisation Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_platform.settings')
django.setup()

from shop.models import Product, Category
from django.conf import settings

# Dossiers locaux
product_image_path = os.path.join(settings.BASE_DIR, 'media/products')
category_image_path = os.path.join(settings.BASE_DIR, 'media/category_images')

def is_already_on_cloudinary(image_field):
    return image_field and image_field.url.startswith("http")

def upload_image_and_get_url(file_path, folder):
    result = cloudinary.uploader.upload(file_path, folder=folder)
    return result['secure_url']

def upload_product_images():
    print("📦 Uploading product images...")
    for product in Product.objects.all():
        if is_already_on_cloudinary(product.image):
            print(f"✅ Skipping (already on Cloudinary): {product.name}")
            continue

        filename_candidates = [
            f"{product.name}.jpg", f"{product.name}.jpeg",
            f"{product.name}.png", f"{product.name}.webp"
        ]

        for filename in filename_candidates:
            local_file = os.path.join(product_image_path, filename)
            if os.path.exists(local_file):
                try:
                    print(f"⬆️ Uploading: {filename}")
                    url = upload_image_and_get_url(local_file, "products/")
                    product.image = url
                    product.save()
                    print(f"✔️ Uploaded: {product.name} → {url}")
                    break
                except Exception as e:
                    print(f"❌ Error uploading {product.name}: {e}")
            else:
                continue
        else:
            print(f"⚠️ No local image found for product: {product.name}")

def upload_category_images():
    print("\n📁 Uploading category images...")
    for category in Category.objects.all():
        if is_already_on_cloudinary(category.image):
            print(f"✅ Skipping (already on Cloudinary): {category.name}")
            continue

        filename_candidates = [
            f"{category.name}.jpg", f"{category.name}.jpeg",
            f"{category.name}.png", f"{category.name}.webp"
        ]

        for filename in filename_candidates:
            local_file = os.path.join(category_image_path, filename)
            if os.path.exists(local_file):
                try:
                    print(f"⬆️ Uploading: {filename}")
                    url = upload_image_and_get_url(local_file, "categories/")
                    category.image = url
                    category.save()
                    print(f"✔️ Uploaded: {category.name} → {url}")
                    break
                except Exception as e:
                    print(f"❌ Error uploading {category.name}: {e}")
            else:
                continue
        else:
            print(f"⚠️ No local image found for category: {category.name}")

if __name__ == "__main__":
    upload_product_images()
    upload_category_images()
