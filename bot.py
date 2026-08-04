import pywikibot

# اسم الويكي
site = pywikibot.Site("ar", "wikipedia")

# تسجيل الدخول بالحساب
site.login()

print("تم الاتصال بويكيبيديا العربية بنجاح")

# اختبار قراءة صفحة
page = pywikibot.Page(site, "ويكيبيديا")

if page.exists():
    print("تم العثور على الصفحة:")
    print(page.title())
else:
    print("الصفحة غير موجودة")
