import time

from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright,shirota,dolgota):
    firefox = playwright.firefox
    browser = firefox.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://zoon.ru/ekb/restaurants/?search_query_form=1&center%5B%5D="+str(shirota)+"&center%5B%5D="+str(dolgota)+"&zoom=16")
    time.sleep(2)
    texts = page.locator('.minicard-item__title').get_by_role("link").all()
    links = [i.get_attribute("href") for i in texts]
    restNames = []
    menus=[]
    result = {}
    maxRests = 3
    if len(texts)<maxRests:
        maxRests=len(texts)
    for y in range(0,maxRests):
        restNames.append(texts[y].all_inner_texts()[0])

    for k in range(0, len(restNames)):
        for link in page.locator(".z-placeholder__image").all():
            try:
                if link.get_attribute("alt")==restNames[k]:
                    restNames[k]=restNames[k]+"|"+link.get_attribute("src")
            except:
                restNames[k] = restNames[k] + "|None"
        # print(u)
        # print([i.get_attribute("alt") for i in page.locator(".z-placeholder__image").all()])
        # print(page.locator(".z-placeholder__image").all().get_by_alt_text(u).get_attribute("src"))
    contextt = browser.new_context()
    contextt.route("**/*", lambda route: route.abort()
        if route.request.resource_type == "image"
        or route.request.resource_type == "stylesheet"
        or route.request.resource_type == "svg"
        else route.continue_())
    pagee = contextt.new_page()
    for i in range(0, maxRests):
        pagee.goto(links[i])
        try:
            try:
                pagee.get_by_role("button").get_by_text("Показать еще").click(timeout=1500)
                pagee.get_by_role("button").get_by_text("Показать еще").click(timeout=1500)
            except:
                print("маленькое меню")
            menu =pagee.locator(".price-dish-content").all_inner_texts()
            for j in range(0, len(menu)):
                menu[j]=menu[j].split("\n")
            menus.append(menu)
        except:
            menus.append(["меню отсутствует"])
    browser.close()

    for k in range(0,len(restNames)):
        result[restNames[k]]=menus[k]
    return result

def parse(shirota,dolgota):
    with sync_playwright() as playwright:
        return run(playwright, shirota,dolgota)
