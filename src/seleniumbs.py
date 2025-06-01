from seleniumbase import SB

with SB(test=True, uc=True) as sb:
    sb.open("https://www.baidu.com/")
    sb.type('[id="kw"]', "github\n")

    #sb.click('[class*="tts-b-hl"]')
    #sb.click('[href*="http://www.baidu.com/link?url=s5Bbx9UULYera-TnDJiWJ0T44IheSPmSUnMBIi8KTSGeH3kXezwVN-TOU4-8MvSs"]')
    sb.click('a[href*="http://www.baidu.com/link?url=s5Bbx9UULYera-TnDJiWJ0T44IheSPmSUnMBIi8KTSGeH3kXezwVN-TOU4-8MvSs"]')
    #sb.uc_gui_click_captcha()
    sb.save_screenshot_to_logs()  # ./latest_logs/
    print(sb)
    print(sb.get_page_title())