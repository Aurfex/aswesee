#!/usr/bin/env python3
"""
Fix imgbb links in aswesee art website
Updates image URLs to local paths
"""

import re

def fix_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Gallery images mapping
    gallery_mapping = [
        ('https://i.ibb.co/PZn5wGKJ/I-Built-Myself-Out-of-Wires.webp', 'images/gallery-1.webp'),
        ('https://i.ibb.co/xZrGddw/I-Wore-the-Scar-Like-Jewelry.webp', 'images/gallery-2.webp'),
        ('https://i.ibb.co/wrQrrHfC/the-Face-I-Invented.webp', 'images/gallery-3.webp'),
        ('https://i.ibb.co/60WMBLL0/What-Surrender-Looked-Like.webp', 'images/gallery-4.webp'),
        ('https://i.ibb.co/84zvjMfj/When-Silence-Looked-Back.webp', 'images/gallery-5.webp'),
        ('https://i.ibb.co/cKNVrQFH/While-the-Tears-Were-Still-Warm.webp', 'images/gallery-6.webp'),
        ('https://i.ibb.co/b5N73mBh/Coloring-Sorrow.png', 'images/gallery-7.png'),
        ('https://i.ibb.co/twtgSbHV/A-Life-Unbegun.png', 'images/gallery-8.png'),
        ('https://i.ibb.co/Y7NWbDs4/Inheritance-of-Silence.png', 'images/gallery-9.png'),
        ('https://i.ibb.co/fVmrnn09/Cutting-Silence.png', 'images/gallery-10.png'),
    ]
    
    # Fix gallery images
    for old_url, new_path in gallery_mapping:
        content = content.replace(old_url, new_path)
        print(f"✅ Fixed: {old_url[:40]}... → {new_path}")
    
    # Fix particle portrait image
    content = content.replace(
        'https://i.ibb.co/W4N6XfsN/portrait.png',
        'images/portrait.png'
    )
    print("✅ Fixed: portrait.png for particles")
    
    # Write back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n🎉 All image paths updated to local!")
    print("📁 Make sure to:")
    print("   1. Download your images from imgbb")
    print("   2. Rename them and put in images/ folder")
    print("   3. Deploy to Vercel or GitHub Pages")

if __name__ == '__main__':
    fix_html()
