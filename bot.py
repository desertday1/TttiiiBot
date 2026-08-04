import pywikibot
from pywikibot.login import LoginManager
import os

login_manager = LoginManager(
    password=os.environ["WIKI_PASSWORD"],
    username=os.environ["WIKI_USERNAME"],
    site=site
)

login_manager.login()

print("تم تسجيل الدخول")
print(site.username())

page = pywikibot.Page(site, "مستخدم:TttiiiBot/اختبار")

page.text = "هذا تعديل تجريبي من بوت TttiiiBot."

page.save("اختبار البوت")
