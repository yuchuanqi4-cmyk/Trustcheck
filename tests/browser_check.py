from playwright.sync_api import sync_playwright
from pathlib import Path
root=Path(__file__).resolve().parent.parent
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1200,'height':1100},device_scale_factor=1); errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 html=(root/'index.html').read_text()
 html=html.replace('<link rel="stylesheet" href="styles.css">','<style>'+ (root/'styles.css').read_text()+'</style>')
 for name in ['questions.js','logic.js','app.js']:
  html=html.replace(f'<script src="{name}"></script>','<script>'+ (root/name).read_text()+'</script>')
 page.set_content(html)
 def shot(name): page.screenshot(path=str(root/'docs'/name),full_page=True)
 def submit(choice, conf):
  page.locator(f'input[value={choice}]').check(); page.locator('#confidence').fill(str(conf));page.locator('#submit').click()
 shot('01-study.png');submit('accept',85);assert 'Appropriate acceptance' in page.locator('.feedback').inner_text();page.locator('#next').click();submit('accept',90);assert 'Over-reliance' in page.locator('.feedback').inner_text();shot('02-feedback.png');page.locator('#next').click();assert 'Check before accepting' in page.locator('.notice').inner_text();shot('03-adaptation.png');page.locator('#adaptive').uncheck();assert page.locator('#suggest').count()==0;page.locator('#adaptive').check();page.locator('#suggest').click();page.locator('#output').click();assert '[1, 2] None' in page.locator('pre').last.inner_text();shot('04-verification.png');submit('reject',80);page.locator('#next').click();submit('unsure',30);page.locator('#next').click();assert 'step-by-step' in page.locator('.notice').inner_text();submit('reject',75);page.locator('#next').click();submit('reject',70);page.locator('#next').click();assert 'Your reliance summary' in page.locator('h1').inner_text();shot('05-summary.png');assert not errors,errors
 with page.expect_download() as d: page.locator('#export').click()
 assert d.value.suggested_filename=='trustcheck-session.json'
 page.on('dialog',lambda d:d.accept());page.locator('#reset').click();assert '0 of 6' in page.locator('#progressText').inner_text();print('PASS: six-question browser flow, feedback, adaptive controls, verification, summary, export and reset; no page errors');b.close()
