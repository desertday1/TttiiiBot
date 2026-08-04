import pywikibot

site = pywikibot.Site("ar", "wikipedia")

print("الحساب المستخدم:", site.username())

page = pywikibot.Page(site, "ويكيبيديا")

if page.exists():
    print("تم العثور على الصفحة:")
    print(page.title())
else:
    print("الصفحة غير موجودة")
