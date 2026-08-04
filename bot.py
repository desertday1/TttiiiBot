import os
import pywikibot

site = pywikibot.Site("ar", "wikipedia")

username = os.environ.get("WIKI_USERNAME")
password = os.environ.get("WIKI_PASSWORD")

site.login()

print("تم تسجيل الدخول بنجاح")
print("الحساب المستخدم:", site.username())

page = pywikibot.Page(site, "ويكيبيديا")

if page.exists():
    print("تم العثور على الصفحة:")
    print(page.title())
else:
    print("الصفحة غير موجودة")
