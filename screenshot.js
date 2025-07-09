const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    defaultViewport: null,
    args: ['--start-maximized'],
  });

  const page = await browser.newPage();

  await page.goto('', {
    waitUntil: 'networkidle0',
    timeout: 0,
  });

  await autoScroll(page);

  await page.evaluate(() => {
    document.querySelectorAll('[style]').forEach(el => {
      el.style.opacity = '1';
      el.style.transform = 'none';
      el.style.visibility = 'visible';
      el.style.display = 'block';
    });

    const canvases = document.querySelectorAll('canvas');
    canvases.forEach(canvas => {
      canvas.style.display = 'block';
      canvas.style.opacity = '1';
    });

    document.querySelectorAll('img').forEach(img => {
      img.style.transform = 'none';
      img.style.opacity = '1';
      img.style.visibility = 'visible';
      img.style.display = 'block';
    });
  });

  // 캡처
  await page.screenshot({
    path: 'g70-fixed.png',
    fullPage: true,
  });

  console.log('캡처 완료');
  await browser.close();
})();

async function autoScroll(page) {
  await page.evaluate(async () => {
    await new Promise(resolve => {
      let totalHeight = 0;
      const distance = 100;
      const timer = setInterval(() => {
        window.scrollBy(0, distance);
        totalHeight += distance;
        if (totalHeight >= document.body.scrollHeight - window.innerHeight) {
          clearInterval(timer);
          resolve();
        }
      }, 100);
    });
  });
}
