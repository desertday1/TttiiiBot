import pywikibot

site = pywikibot.Site("ar", "wikipedia")

site.login()

print("تم تسجيل الدخول")

page = pywikibot.Page(site, "مستخدم:TttiiiBot/اختبار")

page.text = "هذا تعديل تجريبي من بوت TttiiiBot."

page.save("اختبار البوت")
