# 🔧 راهنمای تعمیر aswesee.art

## 📂 ساختار فایل‌ها باید اینطوری بشه:

```
aswesee/
├── index.html
├── audio/
│   ├── manifesto_with_bg.mp3
│   └── ...
└── images/
    ├── portrait.png          # برای پارتیکل‌ها (چهره)
    ├── gallery-1.webp        # I Built Myself Out of Wires
    ├── gallery-2.webp        # I Wore the Scar Like Jewelry
    ├── gallery-3.webp        # The Face I Invented
    ├── gallery-4.webp        # What Surrender Looked Like
    ├── gallery-5.webp        # When Silence Looked Back
    ├── gallery-6.webp        # While the Tears Were Still Warm
    ├── gallery-7.png         # Coloring Sorrow
    ├── gallery-8.png         # A Life Unbegun
    ├── gallery-9.png         # Inheritance of Silence
    └── gallery-10.png        # Cutting Silence
```

## 🖼️ دریافت تصاویر

### روش ۱: از imgbb دانلود کن (دستی)

۱. برو به https://imgbb.com و login کن
۲. هر تصویر رو پیدا کن و "Direct link" رو بگیر
۳. با browser دانلود کن و توی پوشه `images/` بذار

### روش ۲: از backup استفاده کن

اگه روی کامپیوترت کپی از تصاویر داری، اون‌ها رو کپی کن توی `images/`

### روش ۳: از Canva یا منبع اصلی

اگه تصاویر رو توی Canva یا جای دیگه داری، از اونجا export کن

---

## 📝 تغییرات لازم در index.html

### تغییر ۱: مسیر تصاویر گالری (خط‌های ۱۷۶ تا ۱۸۵)

**قبلی:**
```html
src="https://i.ibb.co/PZn5wGKJ/I-Built-Myself-Out-of-Wires.webp"
```

**جدید:**
```html
src="images/gallery-1.webp"
```

... و همینطور برای همه ۱۰ تصویر

### تغییر ۲: مسیر تصویر پارتیکل‌ها (خط ~۵۸۰)

**قبلی:**
```javascript
img.src ="https://i.ibb.co/W4N6XfsN/portrait.png";
```

**جدید:**
```javascript
img.src = "images/portrait.png";
```

### تغییر ۳: تابع sampleImageGrid (خط ~۶۰۰)

**قبلی:**
```javascript
sampleImageGrid("https://i.ibb.co/W4N6XfsN/portrait.png", PORTRAIT, function...
```

**جدید:**
```javascript
sampleImageGrid("images/portrait.png", PORTRAIT, function...
```

---

## 🚀 deploy روی Vercel

وقتی همه چی آماده شد:

```bash
cd "C:\Users\baghe\aswesee-repo"
npx vercel --prod
```

یا push کن به GitHub ( images/ رو هم add کن به git):

```bash
cd "C:\Users\baghe\aswesee-repo"
git add images/
git commit -m "Add local images to fix imgbb issue"
git push origin main
```

---

## ✅ چک‌لیست قبل از deploy

- [ ] تصویر portrait.png توی images/ هست (برای پارتیکل‌ها)
- [ ] ۱۰ تصویر گالری توی images/ هست
- [ ] مسیرها در index.html آپدیت شدن
- [ ] تست لوکال: فایل index.html رو توی browser باز کن ببین کار می‌کنه

---

## 🆘 اگه imgbb کلاً از کار افتاده

اگه به تصاویر دسترسی نداری، می‌تونی:

۱. از Unsplash تصاویر placeholder دانلود کنی
۲. یا اصلاً بخش gallery رو موقتاً hide کنی
۳. یا از رنگ‌های solid به جای تصاویر استفاده کنی

```javascript
// موقتاً پارتیکل‌ها رو غیرفعال کن
// در خط startMorph، comment کن
// startMorph();
```
