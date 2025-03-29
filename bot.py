from playwright.async_api import async_playwright

async def buscar_processos(cpf):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto("https://pje.tjma.jus.br/pje/ConsultaPublica/listView.seam")

        # Preencher CPF
        await page.fill('input[name="fPP:cpfDocumentoParte"]', cpf)
        await page.click('input[name="fPP:searchProcessos"]')

        # Aguardar resultado
        await page.wait_for_selector('.ui-datalist-content', timeout=15000)

        # Extrair texto
        processos = await page.query_selector_all(".ui-datalist-content .rich-panel")
        resultados = []
        for processo in processos:
            texto = await processo.inner_text()
            resultados.append(texto.strip())

        await browser.close()
        return resultados
