import re
from playwright.sync_api import Playwright, sync_playwright, expect

"""
username: str
password: str
slot: list of str
"""
def run(playwright: Playwright,username,password,slot) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sites.uclouvain.be/uclsport/seances/")
    page.get_by_role("button", name="login connexion").click()
    page.get_by_label("Login (Identifiant global").click()
    page.get_by_label("Login (Identifiant global").fill(username)
    page.get_by_label("Login (Identifiant global").press("Tab")
    page.get_by_label("mot de passe").fill(password)
    page.get_by_label("mot de passe").press("Enter")
    for i in range(len(slot)):
        while (i<len(slot)):
            try:
                page.locator(f"text={slot[i][0]}").wait_for(timeout=500)
                break
            except:
                page.get_by_role("button", name="chevron_right").click()
        page.get_by_role("button", name="{0} - LLN - Tennis".format(slot[i][1])).first.click()
        page.get_by_role("button", name="inscription", exact=True).click()
        page.get_by_role("button", name="confirmer").click()
    context.close()
    browser.close()

if __name__ == "__main__":
    username = ...
    password = ...
    with open('./dispo.txt', 'r') as file:
        slot = []
        for line in file:
            date = line[:10]
            hour = line[10:]
            slot.append([date,hour])
        with sync_playwright() as playwright:
            run(playwright,username,password,slot)