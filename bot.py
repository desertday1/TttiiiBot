import os
import pywikibot
from pywikibot.login import ClientLoginManager

site = pywikibot.Site("ar", "wikipedia")

username = os.environ.get("WIKI_USERNAME")
password = os.environ.get("WIKI_PASSWORD")

login_manager = ClientLoginManager(site=site, user=username)
login_manager.password = password
login_manager.login()

print("تم تسجيل الدخول بنجاح")
print("الحساب المستخدم:", site.username())

page = pywikibot.Page(site, "ويكيبيديا")

print(page.title())
