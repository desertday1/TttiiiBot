import pywikibot

site = pywikibot.Site("ar", "wikipedia")

site.login()

print("تم تسجيل الدخول بنجاح")
print("الحساب:", site.username())

page = pywikibot.Page(site, "مستخدم:TttiiiBot/اختبار")

page.text = "هذا تعديل تجريبي من بوت TttiiiBot.\n"

page.save("اختبار اتصال البوت وتعديلاته")

print("تم الحفظ بنجاح")
