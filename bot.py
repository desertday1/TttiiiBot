import pywikibot

site = pywikibot.Site("ar", "wikipedia")

print("الحساب المستخدم:", site.username())

page = pywikibot.Page(site, "مستخدم:TttiiiBot/اختبار")

page.text = "هذا اختبار تعديل من بوت TttiiiBot."

page.save("اختبار تعديل البوت")

print("تم التعديل بنجاح")
