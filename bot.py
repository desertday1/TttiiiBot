import pywikibot
from pywikibot import pagegenerators

def fix_moved_pages():
    # الاتصال بويكيبيديا العربية
    site = pywikibot.Site("ar", "wikipedia")
    
    # التأكد من تسجيل الدخول
    if not site.logged_in():
        site.login()
    print(f"تم تسجيل الدخول بنجاح كـ: {site.username()}")

    # جلب آخر 20 عملية نقل من سجل النقل (Move Log)
    print("جاري فحص سجل النقل لآخر المقالات المنقولة...")
    move_events = site.logevents(logtype="move", total=20)

    for event in move_events:
        try:
            # الصفحة القديمة (التي تم نقلها وتحولت لصفحة تحويل)
            old_page = event.page()
            # الصفحة الجديدة (الاسم الجديد للمقالة)
            new_page = event.target_page()
            
            print(f"\nفحص النقل: [{old_page.title()}] -> [{new_page.title()}]")

            # التأكد أن الصفحة القديمة أصبحت صفحة تحويل فعلاً
            if old_page.isRedirectPage():
                # جلب كل الصفحات التي تحتوي على رابط للاسم القديم
                backlinks = list(old_page.backlinks(namespaces=0)) # نطاق المقالات فقط
                
                if not backlinks:
                    print("-> لا توجد صفحات مرتبطة بالاسم القديم لتعديلها.")
                    continue

                for referring_page in backlinks:
                    print(f"   -> جاري تحديث الرابط في صفحة: {referring_page.title()}")
                    
                    # قراءة نص الصفحة التي تحتوي الرابط القديم
                    text = referring_page.text
                    
                    # استبدال الرابط القديم بالجديد (بأشكال الوصلات المختلفة في الويكي)
                    old_title = old_page.title()
                    new_title = new_page.title()
                    
                    # استبدال بسيط وآمن للوصلات الموسوعية
                    updated_text = text.replace(f"[[{old_title}]]", f"[[{new_title}]]")
                    updated_text = updated_text.replace(f"[[{old_title}|", f"[[{new_title}|")

                    if updated_text != text:
                        referring_page.text = updated_text
                        # حفظ الصفحة مع خلاصة تعديل توضح ما فعله البوت
                        summary = f"بوت: تحديث وصلة مقالة منقولة من [[{old_title}]] إلى [[{new_title}]]"
                        referring_page.save(summary=summary, minor=True, botflag=True)
                        print(f"   [✓] تم التحديث والحفظ!")
                    else:
                        print("   [!] الرابط موجود بشكل معقد أو مدمج، تم تخطيه تلقائياً للأمان.")
        except Exception as e:
            print(f"خطأ أثناء معالجة هذا السجل: {e}")
            continue

if __name__ == "__main__":
    fix_moved_pages()
