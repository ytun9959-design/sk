# .so ဖိုင်ထဲမှ RuijieBypass class ကို လှမ်းခေါ်ခြင်း
from yourgod import RuijieBypass

if __name__ == "__main__":
    # Class ကို Object ဆောက်သည် (Object ဆောက်တာနဲ့ လိုင်စင်က အော်တိုစစ်မှာပါ)
    app = RuijieBypass()
    
    # app.run_menu() မသုံးတော့ဘဲ Banner ပြပြီး Option 1 (Login လုပ်ငန်းစဉ်) ကို တန်း run စေခြင်း
    app.print_banner()
    app.do_login()
