import pywikibot

site = pywikibot.Site("ar", "wikipedia")

page = pywikibot.Page(site, "مستخدم:TttiiiBot/اختبار")

text = "هذا تعديل تجريبي من بوت TttiiiBot.\n"

page.text = text
page.save("اختبار اتصال البوت وتعديلاته")

print("تم حفظ الصفحة بنجاح")
