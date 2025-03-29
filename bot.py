from playwright.async_api import async_playwright

async def buscar_processos(cpf: str) -> str:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://pje.tjma.jus.br/pje/ConsultaPublica/listView.seam")

        # 🔽 AQUI É ONDE VOCÊ DEVE ADICIONAR O WAIT
        await page.wait_for_selector('input[name="fPP:cpfDocumentoParte"]', timeout=60000)

        # 🔽 Só depois disso você faz o fill
        await page.fill('input[name="fPP:cpfDocumentoParte"]', cpf)

        # o restante continua igual...
        await page.click('input[type="submit"]')  # botão "Pesquisar"
        await page.wait_for_timeout(5000)

        # pegar resultado (isso aqui pode variar conforme seu código)
        conteudo = await page.content()
        await browser.close()
        return conteudo
