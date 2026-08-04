import os
import pywikibot

username = os.environ["WIKI_USERNAME"]
password = os.environ["WIKI_PASSWORD"]

site = pywikibot.Site("ar", "wikipedia")

site.login(user=username, password=password)

print("تم تسجيل الدخول بنجاح")

page = pywikibot.Page(site, "مستخدم:TttiiiBot/اختبار")

page.text = "هذا تعديل تجريبي من بوت TttiiiBot.\n"

page.save("اختبار اتصال البوت وتعديلاته")

print("تم الحفظ")
