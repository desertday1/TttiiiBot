import os
import pywikibot
from pywikibot.login import ClientLoginManager

site = pywikibot.Site("ar", "wikipedia")

username = os.environ["WIKI_USERNAME"]
password = os.environ["WIKI_PASSWORD"]

login_manager = ClientLoginManager(
    site=site,
    user=username,
    password=password
)

login_manager.login()

print("تم تسجيل الدخول بنجاح")
print("الحساب:", site.username())

page = pywikibot.Page(site, "مستخدم:TttiiiBot/اختبار")

page.text = "هذا تعديل تجريبي من بوت TttiiiBot.\n"

page.save("اختبار اتصال البوت وتعديلاته")

print("تم الحفظ بنجاح")
