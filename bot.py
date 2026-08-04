import os
import pywikibot

# الاتصال بويكيبيديا العربية
site = pywikibot.Site("ar", "wikipedia")

# تسجيل الدخول باستخدام البيانات الموجودة في GitHub Secrets
username = os.environ.get("WIKI_USERNAME")
password = os.environ.get("WIKI_PASSWORD")

site.login(username=username, password=password)

print("تم تسجيل الدخول بنجاح")
print("الحساب المستخدم:", site.username())

# اختبار قراءة صفحة
page = pywikibot.Page(site, "ويكيبيديا")

if page.exists():
    print("تم العثور على الصفحة:")
    print(page.title())
else:
    print("الصفحة غير موجودة")
